# Unsloth — Google Colab UI Walkthrough

A walkthrough of the Unsloth fine-tuning notebook as run inside Google Colab — what each part of the notebook UI does, in the order you actually click/run through it.

## 1. Runtime Setup

- **Runtime → Change runtime type → T4 GPU** (or better, if available). Unsloth needs a CUDA GPU; without one the install cell will fail or fall back to CPU (unusably slow for training).
- Colab's top-right status pill shows RAM/Disk/GPU usage once the runtime connects — worth watching during training so you notice VRAM pressure before an out-of-memory crash.

## 2. Install Cell

The first code cell installs `unsloth` (and pinned dependency versions for `torch`, `transformers`, `trl`, `peft`, `bitsandbytes`). This is a **Run** (▶) on a single cell — Colab shows a spinner, then a green check when it finishes. This step alone can take a couple of minutes on a fresh runtime.

## 3. Model Selection (Form Cell)

Unsloth's official notebooks use Colab's **form UI** — a code cell annotated with `#@param`, which Colab renders as an actual form (text box / dropdown) instead of raw code. Typical fields:

- `model_name` — dropdown/text field for the base model, e.g. `unsloth/Llama-3.2-3B-Instruct`, `unsloth/Qwen2.5-7B-Instruct`, `unsloth/gemma-2-9b`. Unsloth hosts pre-quantized versions of common models so the download is smaller and faster.
- `max_seq_length` — context length for training (e.g. 2048).
- `load_in_4bit` — checkbox toggle; loads the base model in 4-bit (QLoRA-style) to cut VRAM usage drastically, at the cost of a small amount of precision.
- `dtype` — usually left as `None` so Unsloth auto-detects the best type for the GPU.

Running this cell calls `FastLanguageModel.from_pretrained(...)` under the hood and downloads the model from Hugging Face.

## 4. LoRA Configuration (Form Cell)

A second form cell exposes the PEFT/LoRA hyperparameters as fields rather than requiring you to edit code directly:

- `r` (rank) — e.g. 16; controls the size of the trainable adapter matrices.
- `lora_alpha` — scaling factor, often set equal to `r`.
- `target_modules` — which layers get adapters (commonly `q_proj, k_proj, v_proj, o_proj, gate_proj, up_proj, down_proj`).
- `use_gradient_checkpointing` — toggle for `"unsloth"` mode, which trades a bit of speed for a large VRAM reduction.

Running this cell wraps the base model with `FastLanguageModel.get_peft_model(...)`, turning it into a LoRA-trainable model.

## 5. Dataset Cell

Loads a dataset (from Hugging Face Hub or an uploaded file via Colab's file-upload widget in the left sidebar) and applies a chat/instruction template so raw examples are formatted the way the base model expects (e.g. Llama-3 chat template, Alpaca-style prompt, etc.). This is usually where you point at your own `.jsonl`/`.csv` if fine-tuning on custom data.

## 6. Training Cell (the "Run" step)

Configures `SFTTrainer` from TRL with training arguments exposed as form fields:

- `per_device_train_batch_size`
- `gradient_accumulation_steps`
- `max_steps` or `num_train_epochs`
- `learning_rate`
- `output_dir`

Pressing ▶ on this cell starts the actual training loop. Colab streams a live progress bar with step number and loss, updating in place — this is the closest thing to a "pretraining/fine-tuning in progress" view in the UI. Colab's RAM/GPU usage graph (hover over the status pill) is useful here to confirm you're not close to OOM.

## 7. Inference / Test Cell

After training, a cell reloads the model in inference mode (`FastLanguageModel.for_inference(model)`) and runs a sample prompt through it, printing the generated output directly below the cell — the quickest sanity check that fine-tuning actually changed behavior.

## 8. Save / Export Cell

Final form cell offers export options as checkboxes:

- Save LoRA adapter only (small, just the trained deltas)
- Save merged 16-bit model (base + adapter combined)
- Export to **GGUF** (for local inference via llama.cpp/Ollama), often with a quantization-level dropdown (Q4_K_M, Q8_0, etc.)

Running it pushes the output either to Colab's local disk (downloadable via the file browser sidebar) or directly to the Hugging Face Hub if a token/repo name was supplied earlier.

## Key UI/UX Notes

- Every "parameter" the notebook exposes is really just a Colab form wrapping a Python variable — nothing exotic, but it's what makes the notebook usable without reading the underlying code.
- Cells must be run **top to bottom** in order; skipping the model-load or LoRA cells and jumping straight to training will error out.
- Colab disconnects idle runtimes, so a long training run needs the tab kept active (or Colab Pro for background execution).
