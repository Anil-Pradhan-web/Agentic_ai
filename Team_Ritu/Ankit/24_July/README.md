# Day 02 - 24 July 2026

# Agentic AI Daily Learning Report

**Name:** Ankit Kumar  
**Team:** Team_Ritu  
**Date:** 24 July 2026

---

# Objective

The objective of today's learning was to understand different model access types, compare Large Language Models (LLMs) and Small Language Models (SLMs), explore popular model training and fine-tuning tools, and learn about the GGUF model format used for local AI deployment.

---

# Task 1: Difference Between Closed Source, Open Weight, and Open Source Open Weight Models

## Closed Source Models

Closed Source models do not provide access to their model weights, training data, or source code. Users interact with these models through cloud APIs managed by the provider.

### Features

- Accessible through APIs only
- No access to model weights
- Cannot modify or retrain the model
- Managed entirely by the provider

### Advantages

- High performance
- Easy integration
- No infrastructure required
- Regular updates

### Limitations

- Data is processed on third-party servers
- API usage cost
- Vendor lock-in
- No customization

### Examples

- GPT-4o
- Claude 3.5 Sonnet
- Gemini 1.5 Pro

---

## Open Weight Models

Open Weight models provide downloadable model weights, allowing users to run and fine-tune models locally. However, the original training code and datasets may not be publicly available.

### Features

- Downloadable model weights
- Local execution
- Fine-tuning supported
- Offline deployment

### Advantages

- Better privacy
- No API cost
- Domain-specific customization
- Offline capable

### Limitations

- Requires GPU hardware
- Self-managed deployment
- Manual updates

### Examples

- Llama 3
- Qwen3
- Gemma
- Falcon

---

## Open Source Open Weight Models

These models provide both the model weights and source code, allowing complete transparency and customization.

### Features

- Open weights
- Open source training code
- Community driven
- Fully customizable

### Advantages

- Full control
- Research reproducibility
- Community contributions
- No vendor dependency

### Limitations

- High hardware requirements
- Deployment complexity
- Quality varies between projects

### Examples

- OLMo
- Falcon
- Mistral 7B (Apache 2.0)

---

# Comparison

| Feature | Closed Source | Open Weight | Open Source Open Weight |
|----------|--------------|-------------|-------------------------|
| Model Weights | ❌ | ✅ | ✅ |
| Source Code | ❌ | Partial | ✅ |
| Fine-Tuning | ❌ | ✅ | ✅ |
| Local Deployment | ❌ | ✅ | ✅ |
| Privacy | Low | High | High |
| API Cost | Yes | No | No |

---

# Task 2: Top 3 Tools for Model Training and Fine-Tuning

## 1. Hugging Face Transformers

### Description

The most widely used framework for loading, training, and fine-tuning transformer-based models.

### Advantages

- Large collection of pretrained models
- Excellent documentation
- Supports LoRA and QLoRA
- Strong community support

---

## 2. Unsloth

### Description

A fast and memory-efficient framework for fine-tuning LLMs on consumer GPUs.

### Advantages

- Faster training
- Lower VRAM usage
- Easy LoRA and QLoRA support
- Beginner-friendly

---

## 3. Axolotl

### Description

A powerful fine-tuning framework designed for supervised instruction tuning.

### Advantages

- Easy configuration
- Supports multiple LLMs
- Production-ready

---

## Recommendation

For learning Agentic AI, I recommend:

1. Hugging Face Transformers
2. Unsloth
3. Axolotl

Among these, **Unsloth** is my preferred choice because it reduces GPU memory usage while providing fast fine-tuning, making it ideal for students and developers with limited hardware.

---

# Task 3: Why LLMs Cannot Be Trained Easily

Large Language Models (LLMs) contain billions or even trillions of parameters.

Examples:

| Model | Parameters |
|--------|-----------:|
| Llama 3 8B | 8 Billion |
| Qwen3 8B | 8 Billion |
| GPT-4 | Estimated Hundreds of Billions+ |

Training an LLM requires:

- Massive datasets
- High-end GPU clusters
- Weeks or months of computation
- Millions of dollars

Because of these requirements, individuals generally **do not train LLMs from scratch**.

Instead, developers use techniques such as:

- Fine-Tuning
- LoRA
- QLoRA
- PEFT

These approaches adapt an existing pretrained model instead of rebuilding it from the beginning.

---

# Task 4: Difference Between LLM and SLM

## Large Language Models (LLMs)

LLMs contain billions of parameters and are designed for highly complex reasoning, coding, and language understanding tasks.

Examples:

- GPT-4o
- Claude
- Gemini
- Llama 3 70B

---

## Small Language Models (SLMs)

SLMs contain significantly fewer parameters and are optimized for faster inference and deployment on devices with limited resources.

Examples:

- Phi-3 Mini
- TinyLlama
- Gemma 2B
- Qwen 2.5 3B

---

## Comparison

| Feature | LLM | SLM |
|----------|-----|-----|
| Parameters | Billions | Millions to Few Billions |
| Speed | Moderate | Fast |
| Memory Usage | High | Low |
| Cost | High | Low |
| Hardware | GPU Cluster | Laptop or Small GPU |
| Accuracy | Higher | Moderate |
| Offline Deployment | Difficult | Easy |

---

# Task 5: What is GGUF?

## Definition

GGUF (GPT-Generated Unified Format) is a model file format designed for efficient local inference.

It is commonly used with:

- Ollama
- llama.cpp
- LM Studio
- Jan AI

---

## Advantages

- Faster model loading
- Smaller file size
- Supports quantized models
- Optimized for CPU and low-memory systems

---

## Example

Instead of downloading a standard model, users can download a quantized GGUF version such as:

```
llama3-8b.Q4_K_M.gguf
```

This version consumes less memory while maintaining good inference performance.

---

# Key Learnings

- Learned the difference between Closed Source, Open Weight, and Open Source Open Weight models.
- Explored the top frameworks used for model training and fine-tuning.
- Understood why training Large Language Models from scratch is impractical for individual developers.
- Compared Large Language Models with Small Language Models.
- Learned about the GGUF file format and its importance in running models locally using Ollama and llama.cpp.

---

# Conclusion

Today's session provided a solid understanding of AI model accessibility, deployment options, training methodologies, and local inference techniques. These concepts form the foundation for future work in Agentic AI, local LLM deployment, and efficient fine-tuning of open-weight models.