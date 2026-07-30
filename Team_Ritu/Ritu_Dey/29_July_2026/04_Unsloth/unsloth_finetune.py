# %% [markdown]
# # Unsloth Fine-Tuning — Colab Script
# Each `# %%` block below is one Colab cell (open this file in VS Code / Jupyter
# with the Jupytext extension, or paste each block into its own Colab cell).
# Runtime: Colab -> Runtime -> Change runtime type -> T4 GPU (or better).

# %% [markdown]
# ## Cell 1 — Install

# %%
# !pip install "unsloth[colab-new] @ git+https://github.com/unslothai/unsloth.git"
# !pip install --no-deps trl peft accelerate bitsandbytes

# %% [markdown]
# ## Cell 2 — Load base model (4-bit)
# Colab form fields (edit the values directly here, or as #@param cells in Colab)

# %%
from unsloth import FastLanguageModel
import torch

model_name = "unsloth/Llama-3.2-3B-Instruct"  # @param {type:"string"}
max_seq_length = 2048                          # @param {type:"integer"}
load_in_4bit = True                            # @param {type:"boolean"}
dtype = None  # auto-detect best dtype for the current GPU

model, tokenizer = FastLanguageModel.from_pretrained(
    model_name=model_name,
    max_seq_length=max_seq_length,
    dtype=dtype,
    load_in_4bit=load_in_4bit,
)

# %% [markdown]
# ## Cell 3 — Wrap with LoRA adapters

# %%
r = 16              # @param {type:"integer"}
lora_alpha = 16      # @param {type:"integer"}
lora_dropout = 0     # @param {type:"number"}

model = FastLanguageModel.get_peft_model(
    model,
    r=r,
    target_modules=[
        "q_proj", "k_proj", "v_proj", "o_proj",
        "gate_proj", "up_proj", "down_proj",
    ],
    lora_alpha=lora_alpha,
    lora_dropout=lora_dropout,
    bias="none",
    use_gradient_checkpointing="unsloth",  # big VRAM saving
    random_state=3407,
)

# %% [markdown]
# ## Cell 4 — Load & format dataset
# Swap the dataset name / loading logic for your own `.jsonl` / `.csv` as needed.

# %%
from datasets import load_dataset

dataset_name = "yahma/alpaca-cleaned"  # @param {type:"string"}
dataset = load_dataset(dataset_name, split="train")

PROMPT_TEMPLATE = """Below is an instruction that describes a task, paired with an input that provides further context. Write a response that appropriately completes the request.

### Instruction:
{}

### Input:
{}

### Response:
{}"""

EOS_TOKEN = tokenizer.eos_token


def format_example(examples):
    instructions = examples["instruction"]
    inputs = examples["input"]
    outputs = examples["output"]
    texts = [
        PROMPT_TEMPLATE.format(instr, inp, out) + EOS_TOKEN
        for instr, inp, out in zip(instructions, inputs, outputs)
    ]
    return {"text": texts}


dataset = dataset.map(format_example, batched=True)

# %% [markdown]
# ## Cell 5 — Train

# %%
from trl import SFTTrainer
from transformers import TrainingArguments

per_device_train_batch_size = 2     # @param {type:"integer"}
gradient_accumulation_steps = 4     # @param {type:"integer"}
max_steps = 60                      # @param {type:"integer"}
learning_rate = 2e-4                # @param {type:"number"}

trainer = SFTTrainer(
    model=model,
    tokenizer=tokenizer,
    train_dataset=dataset,
    dataset_text_field="text",
    max_seq_length=max_seq_length,
    args=TrainingArguments(
        per_device_train_batch_size=per_device_train_batch_size,
        gradient_accumulation_steps=gradient_accumulation_steps,
        warmup_steps=5,
        max_steps=max_steps,
        learning_rate=learning_rate,
        fp16=not torch.cuda.is_bf16_supported(),
        bf16=torch.cuda.is_bf16_supported(),
        logging_steps=1,
        optim="adamw_8bit",
        weight_decay=0.01,
        lr_scheduler_type="linear",
        seed=3407,
        output_dir="outputs",
    ),
)

trainer_stats = trainer.train()
print(trainer_stats)

# %% [markdown]
# ## Cell 6 — Inference check (before/after sanity test)

# %%
FastLanguageModel.for_inference(model)

test_prompt = PROMPT_TEMPLATE.format(
    "Explain the difference between an API key and an OAuth token.", "", ""
)
inputs = tokenizer([test_prompt], return_tensors="pt").to("cuda")
outputs = model.generate(**inputs, max_new_tokens=128, use_cache=True)
print(tokenizer.batch_decode(outputs, skip_special_tokens=True)[0])

# %% [markdown]
# ## Cell 7 — Save / export
# Pick one or more export targets.

# %%
save_lora_only = True     # @param {type:"boolean"}
save_merged_16bit = False # @param {type:"boolean"}
export_gguf = False       # @param {type:"boolean"}
gguf_quant = "q4_k_m"     # @param {type:"string"}

if save_lora_only:
    model.save_pretrained("lora_adapter")
    tokenizer.save_pretrained("lora_adapter")

if save_merged_16bit:
    model.save_pretrained_merged(
        "merged_model", tokenizer, save_method="merged_16bit"
    )

if export_gguf:
    model.save_pretrained_gguf(
        "gguf_model", tokenizer, quantization_method=gguf_quant
    )
