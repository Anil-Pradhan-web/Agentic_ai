# Unsloth Fine-Tuning Run — Write-Up

> Documents a fine-tuning run following the Colab UI walkthrough in [`Unsloth_Colab_UI_Walkthrough.md`](Unsloth_Colab_UI_Walkthrough.md). Numbers below are placeholders from a template run — swap in the real values (loss curve, timings, sample outputs) once you re-run it and want this filled in with actual results.

## Objective

Fine-tune a small instruct model with LoRA using Unsloth, on a single Colab GPU, to specialize it for a narrow instruction-following task rather than general-purpose chat.

## Setup

| Item | Value |
|---|---|
| Base model | `unsloth/Llama-3.2-3B-Instruct` (4-bit) |
| Environment | Google Colab, T4 GPU |
| Fine-tuning method | LoRA (via Unsloth `FastLanguageModel`) |
| Sequence length | 2048 |

## LoRA Configuration

| Parameter | Value |
|---|---:|
| Rank (r) | 16 |
| Alpha | 16 |
| Target modules | q_proj, k_proj, v_proj, o_proj, gate_proj, up_proj, down_proj |
| Gradient checkpointing | "unsloth" mode (memory-optimized) |
| Dropout | 0 |

## Dataset

- Instruction/response pairs formatted with the model's chat template.
- Split: train / small held-out validation set for spot-checking generalization.
- Size: small enough to iterate quickly on a free-tier Colab GPU (a few thousand examples is a reasonable starting point for LoRA on a 3B model).

## Training Configuration

| Parameter | Value |
|---|---:|
| Batch size (per device) | 2 |
| Gradient accumulation | 4 (effective batch size 8) |
| Learning rate | 2e-4 |
| Epochs / max steps | 3 epochs (or capped at a fixed max_steps for a quick run) |
| Optimizer | AdamW (8-bit) |

## What "Pretraining" vs "Fine-Tuning" Meant Here

Note for clarity: this run is **fine-tuning** (LoRA on top of an already-pretrained base model), not pretraining from scratch. True pretraining an LLM from random weights requires massive compute (thousands of GPU-hours) that isn't feasible in a Colab session. What the notebook UI calls "training" in this context is adapting an existing pretrained model to a new task/dataset — which is the realistic, achievable version of "training a model" for a student/individual setup.

## Results (fill in after running)

| Step | Training Loss |
|---:|---:|
| — | — |
| — | — |
| — | — |

- **Training time:** _[fill in]_
- **Peak VRAM usage:** _[fill in]_ (Unsloth's 4-bit + gradient checkpointing typically keeps this well under the T4's 16GB)

## Inference Check (before vs after)

**Prompt:** _[example prompt from your task domain]_

- **Base model output (before fine-tuning):** _[generic/off-target response]_
- **Fine-tuned model output (after):** _[response reflecting the target behavior/format]_

## Export

- LoRA adapter saved separately (small file, portable — can be re-applied to the base model later).
- Optional: merged model exported to GGUF for local inference via Ollama/llama.cpp, avoiding any dependency on Colab or a hosted API afterward.

## Takeaways

- LoRA + 4-bit loading + Unsloth's optimized kernels make fine-tuning a 3B–8B model realistic on a single free-tier Colab GPU, which would not be possible with a full-parameter fine-tune.
- The Colab form-cell UI (see the walkthrough doc) keeps the whole run reproducible without needing to touch the underlying Python beyond the exposed parameters.
- Real gains from fine-tuning are easiest to judge with a small, consistent set of before/after prompts — track those every run so quality changes are visible, not just the loss number.
