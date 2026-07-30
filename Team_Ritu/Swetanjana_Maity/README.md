# 🤖 Swetanjana Maity — Agentic AI Learning Journal

> *"From raw tokens to fine-tuned intelligence — one model at a time."*

Welcome to my personal learning space within **Team Ritu's Agentic AI program**. This repository is a live record of my journey through the cutting edge of AI — covering model architectures, fine-tuning strategies, local inference, and everything in between.

---

## 👩‍💻 About Me

| | |
|---|---|
| **Name** | Swetanjana Maity |
| **Team** | Team Ritu |
| **Program** | Agentic AI (SOA) |
| **Focus Areas** | LLM Fine-Tuning · Model Quantization · GGUF Inference · AI Research |

---

## 🗺️ Learning Roadmap

```
Phase 1 ──────────────────────────────────────────────────── Phase N
   │                                                              │
   ▼                                                              ▼
Model Landscape         Fine-Tuning             Deployment
   │                       │                        │
   ├─ Closed Source        ├─ LoRA / QLoRA          ├─ GGUF Format
   ├─ Open Weight          ├─ Unsloth Engine         ├─ Ollama / LM Studio
   └─ True Open Source     └─ Dataset Extraction     └─ Hybrid CPU+GPU
```

---

## 📅 Daily Learning Log

| Date | Day | Topic | Key Outcome |
| :--- | :---: | :--- | :--- |
| 2026-07-27 | Day 01 | Unsloth & GGUF Fine-Tuning Workflow | Built end-to-end fine-tuning pipeline on Google Colab; exported model to GGUF |

---

## 🧠 Key Concepts Mastered

### 🔓 Model Licensing Paradigms

| Type | Access | Dataset | License |
|---|---|---|---|
| **Closed Source** | API only | Hidden | Proprietary |
| **Open Weight** | Downloadable weights | Hidden | Custom (may restrict commercial use) |
| **True Open Source** | Weights + Code + Data | Open | Apache 2.0 / MIT |

> 💡 *Examples: GPT-4o (Closed) · LLaMA 3.3 (Open Weight) · OLMo by Allen AI (True OSS)*

---

### ⚙️ Fine-Tuning Toolkit Showdown

| Framework | Speed | VRAM Savings | Best For |
|---|---|---|---|
| **Hugging Face TRL** | 1× baseline | Standard | Standard pipelines, HF ecosystem |
| **Unsloth** | **2×–5× faster** | **Up to 80% less** | Solo devs, budget builds, Colab |
| **Axolotl + DeepSpeed** | 1.5×–2.5× | High (FSDP/ZeRO-3) | Enterprise multi-GPU clusters |

> 🏆 *My pick for individual use:* **Unsloth** — runs 8B models on a free Colab T4!

---

### 📦 Model Serialization Formats

```
Model Formats at a Glance:

  Raw / FP16           GPU-Quantized        Local / Edge
  ┌──────────────┐     ┌──────────────┐     ┌──────────────┐
  │ Safetensors  │     │ AWQ          │     │ GGUF ◄ STAR  │
  │ PyTorch .bin │     │ GPTQ         │     │ ONNX         │
  │ (Baseline)   │     │ EXL2         │     │ (Hybrid CPU) │
  └──────────────┘     └──────────────┘     └──────────────┘
```

**GGUF** — the local inference king:
- ✅ Single-file packaging (weights + tokenizer + metadata)
- ✅ Hybrid CPU + GPU layer offloading
- ✅ `mmap` fast loading — instant startup
- ✅ Advanced quantization: `Q4_K_M`, `Q5_K_M`, `IQ3_XS`
- ✅ Powers Ollama, LM Studio, llama.cpp, Jan.ai

---

### 📊 LLM vs. SLM — The Trade-off

| Dimension | Large (LLM) | Small (SLM) |
|---|---|---|
| **Parameters** | 70B – 1T+ | 1B – 9B |
| **Hardware** | Multi-GPU Cloud | Laptop / Mobile NPU |
| **Cost per 1M tokens** | $0.50 – $15 | $0.01 – $0.10 |
| **Inference Latency** | 1s – 5s | < 50ms – 200ms |
| **Data Privacy** | Vendor-dependent | 100% on-premise |

> 🔑 *The winning strategy: **SLM-first routing** — handle 80% of tasks locally, escalate complex queries to LLMs.*

---

## 📂 Repository Structure

```
Swetanjana_Maity/
│
├── 📁 27thJuly/
│   ├── ans.md                  ← Deep-dive: Licensing, Frameworks, GGUF & LLM vs SLM
│   └── unsloth_workflow.ipynb  ← Hands-on: Unsloth fine-tuning skeleton notebook
│
├── 📁 28thJuly task/
│   └── SKILL.md                ← ASCII art toolchain skill documentation
│
└── 📄 README.md                ← You are here!
```

---

## 🛠️ Tech Stack Encountered

![Python](https://img.shields.io/badge/Python-3776AB?style=flat-square&logo=python&logoColor=white)
![Jupyter](https://img.shields.io/badge/Jupyter-F37626?style=flat-square&logo=jupyter&logoColor=white)
![HuggingFace](https://img.shields.io/badge/HuggingFace-FFD21E?style=flat-square&logo=huggingface&logoColor=black)
![Google Colab](https://img.shields.io/badge/Google%20Colab-F9AB00?style=flat-square&logo=googlecolab&logoColor=black)

**Libraries & Tools:**
`Unsloth` · `Transformers` · `TRL` · `PEFT` · `llama.cpp` · `GGUF` · `LoRA` · `QLoRA`

---

## 🚀 What's Next

- [ ] Run the `unsloth_workflow.ipynb` on a real dataset
- [ ] Deploy a GGUF model locally with Ollama
- [ ] Experiment with DPO (Direct Preference Optimization)
- [ ] Build a multi-agent pipeline using an SLM router

---

<div align="center">

*Built with curiosity, caffeine, and a lot of GPU hours ☕🔥*

**Team Ritu · Agentic AI Program · 2026**

</div>
