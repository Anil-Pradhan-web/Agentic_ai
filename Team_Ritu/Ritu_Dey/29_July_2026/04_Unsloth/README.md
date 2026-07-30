# Unsloth Fine-Tuning — Colab Code

[`unsloth_finetune.py`](unsloth_finetune.py) is the actual runnable workflow, written as Colab-style cells (each `# %%` block = one cell — paste blocks individually into Colab, or open the file directly with the Jupytext extension in VS Code).

## What it does, cell by cell

| Cell | Purpose |
|---|---|
| 1 — Install | Installs `unsloth` and pinned deps (`trl`, `peft`, `accelerate`, `bitsandbytes`) |
| 2 — Load base model | Loads `unsloth/Llama-3.2-3B-Instruct` in 4-bit via `FastLanguageModel.from_pretrained` |
| 3 — LoRA wrap | Adds trainable LoRA adapters via `FastLanguageModel.get_peft_model` (rank 16, gradient checkpointing in `"unsloth"` mode for lower VRAM) |
| 4 — Dataset | Loads `yahma/alpaca-cleaned` and formats each example into the instruction/input/response prompt template |
| 5 — Train | Runs `SFTTrainer` (from TRL) with 8-bit AdamW, linear LR schedule, fp16/bf16 auto-selected based on GPU support |
| 6 — Inference check | Switches the model to inference mode and runs one test prompt to sanity-check the fine-tune actually changed behavior |
| 7 — Save/export | Saves the LoRA adapter, and optionally a merged 16-bit model or a quantized GGUF export for local inference (Ollama/llama.cpp) |

## Run it (Colab)

1. New Colab notebook → Runtime → Change runtime type → **T4 GPU**.
2. Paste each `# %%` block from `unsloth_finetune.py` into its own cell, top to bottom.
3. Run Cell 1 (install) first — this alone can take a couple of minutes on a fresh runtime.
4. Run cells 2–7 in order. Skipping the model-load or LoRA cells before training will error out.
5. To fine-tune on your own data instead of `yahma/alpaca-cleaned`, swap the `dataset_name` in Cell 4 (or replace `load_dataset(...)` with your own `.jsonl`/`.csv` loader) and keep the same `instruction` / `input` / `output` field names, or adjust `format_example` to match your schema.

## Swappable parameters

All the `# @param` lines are the values Colab renders as form fields (dropdowns/text boxes) — edit them directly in the script, or use Colab's form UI if pasted cell-by-cell:

- `model_name` — any Unsloth-hosted 4-bit base model (Llama, Qwen, Gemma, Mistral, …)
- `r`, `lora_alpha`, `lora_dropout` — LoRA capacity/regularization
- `per_device_train_batch_size`, `gradient_accumulation_steps`, `max_steps`, `learning_rate` — training run size/duration
- `save_lora_only` / `save_merged_16bit` / `export_gguf` — pick one or more export formats at the end

## Notes

- This is **fine-tuning** (LoRA on an already-pretrained base model), not pretraining from scratch — pretraining an LLM from random weights needs far more compute than a Colab session provides.
- 4-bit loading + LoRA + `"unsloth"` gradient checkpointing is what makes fine-tuning a 3B–8B model realistic on a single free-tier T4 GPU.
