# Model File Formats & GGUF

Large Language Models (LLMs) are stored in different **model file formats**, each optimized for specific tasks such as **training, fine-tuning, deployment, or inference**. The choice of format depends on the framework, hardware, and intended use. Among these, **GGUF** has become the preferred format for running quantized LLMs locally.

---

## Common Model File Formats

| Format                 | Purpose                        | Training | Inference | Common Extension   |
| ---------------------- | ------------------------------ | -------- | --------- | ------------------ |
| **PyTorch Checkpoint** | Model training & fine-tuning   | ✅ Yes    | ✅ Yes     | `.pt`, `.pth`      |
| **SafeTensors**        | Secure model weight storage    | ✅ Yes    | ✅ Yes     | `.safetensors`     |
| **ONNX**               | Cross-platform inference       | Limited  | ✅ Yes     | `.onnx`            |
| **TensorRT**           | Optimized NVIDIA GPU inference | ❌ No     | ✅ Yes     | `.engine`, `.plan` |
| **GGUF**               | Quantized local inference      | ❌ No     | ✅ Yes     | `.gguf`            |

---

## What is GGUF?

**GGUF (GPT-Generated Unified Format)** is a binary file format developed for **efficient local inference** of LLMs. It is the successor to the older GGML format and is widely supported by tools such as **llama.cpp**, **Ollama**, **LM Studio**, and **Jan**.

Unlike traditional model formats, GGUF stores both the **model weights** and **metadata** (e.g., tokenizer, architecture, quantization settings) in a single file.

### Key Features

* Optimized for CPU inference with optional GPU acceleration.
* Supports quantized models (e.g., Q4, Q5, Q8) to reduce memory usage.
* Single-file format containing weights and metadata.
* Easy to distribute and deploy locally.
* Ideal for offline AI applications.

---

## Comparison

| Feature      | PyTorch        | SafeTensors          | ONNX               | TensorRT    | GGUF                 |
| ------------ | -------------- | -------------------- | ------------------ | ----------- | -------------------- |
| Training     | ✅              | ✅                    | Limited            | ❌           | ❌                    |
| Fine-tuning  | ✅              | ✅                    | Limited            | ❌           | ❌                    |
| Inference    | ✅              | ✅                    | ✅                  | ✅           | ✅                    |
| Quantization | External tools | External tools       | Supported          | Supported   | Native               |
| Best Use     | Training       | Secure model sharing | Portable inference | NVIDIA GPUs | Local LLM deployment |

---

## Recommendation

* **PyTorch** – Best for model development, training, and fine-tuning.
* **SafeTensors** – Best for securely storing and sharing pretrained models.
* **ONNX** – Best for portable inference across different platforms.
* **TensorRT** – Best for high-performance inference on NVIDIA GPUs.
* **GGUF** – Best for running quantized LLMs locally with tools like Ollama and llama.cpp.

---


Different model formats serve different purposes throughout the AI lifecycle. **PyTorch** and **SafeTensors** are commonly used for training and fine-tuning, **ONNX** and **TensorRT** focus on optimized inference, while **GGUF** is the preferred format for efficient, quantized local deployment of LLMs due to its portability, compact size, and broad support across local AI tools.
