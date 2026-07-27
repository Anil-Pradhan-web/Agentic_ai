24/07/2026

TASKS:-

1. Difference Between Closed Source, Open Source, and Open Weight Models

•  Closed Source Models:

o  What they are: Proprietary models accessible only via API or web interface. The
code, architecture, training data, and model weights are kept secret by the
company.

o  Pros: Top-tier performance, zero infrastructure setup, continuous server-side

updates.

o  Cons: Vendor lock-in, data privacy risks, ongoing usage fees per token, no custom

weight modification.

o  Examples: GPT-4o (OpenAI), Claude 3.5 Sonnet (Anthropic), Gemini 1.5 Pro

(Google).

•  Open Weight Models:

o  What they are: Models where the trained weights are freely downloadable,
allowing you to run, host, or fine-tune them on your own infrastructure.
However, the exact datasets or full training code might not be fully released.

o  Pros: Total data privacy, fine-tuning capability, no per-token API cost when hosted

locally.

o  Cons: Requires substantial hardware/GPUs to host and run effectively.

o  Examples: Meta’s Llama 3.1, Mistral 7B, Google’s Gemma 2.

•  Open Source Models:

o  What they are: Fully transparent models where the weights, source code, data
processing scripts, and training datasets are released under an open-source
license.

o  Pros: Full inspectability, end-to-end customization, zero reliance on external

entities.

o  Cons: High resource barrier to pre-train from scratch.

o  Examples: OLMo (Allen Institute for AI), Pythia (EleutherAI).

2. Top 3 Tools for Model Training and Fine-Tuning

1.  Unsloth:

o  Overview: A lightweight, high-speed library engineered specifically for ultra-fast

and memory-efficient fine-tuning (LoRA / QLoRA).

o  Key Strength: Reduces VRAM usage by up to 80% and increases training speed by

2x–5x without dropping accuracy. Ideal for single-GPU setups.

2.  Axolotl:

o  Overview: A flexible, config-driven framework built on Hugging Face and PyTorch

that lets you fine-tune models using simple YAML configuration files.

o  Key Strength: Great support for multi-GPU training, various dataset formats, and

modern optimizations like FlashAttention-2 and DeepSpeed.

3.  Hugging Face TRL (Transformer Reinforcement Learning):

o  Overview: A full-stack library providing tools for Supervised Fine-Tuning (SFT),

Direct Preference Optimization (DPO), and Reinforcement Learning with Human
Feedback (RLHF).

o  Key Strength: Seamless integration with the broader Hugging Face ecosystem

and standard enterprise ML pipelines.

Recommendation

•  For individual developers or standard single-GPU setups (e.g., T4 / RTX 3090 / A10G):
Unsloth is the recommended choice because it minimizes memory overhead and
drastically cuts down fine-tuning time.

•  For structured enterprise projects or multi-GPU distributed training: Axolotl or Hugging

Face TRL provides standard flexibility and configuration management.

