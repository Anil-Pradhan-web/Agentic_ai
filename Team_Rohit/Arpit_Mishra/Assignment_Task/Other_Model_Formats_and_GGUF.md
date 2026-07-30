# Other AI Model Formats and GGUF

## Introduction

AI models are distributed in different file formats depending on the framework, optimization techniques, and deployment environment.

---

## Common Model Formats

| Format | Used By | Purpose |
|---------|----------|----------|
| GGUF | llama.cpp | Local inference |
| Safetensors | Hugging Face | Secure model storage |
| PyTorch (.pt/.pth) | PyTorch | Training and inference |
| TensorFlow (.ckpt/.pb) | TensorFlow | Model training |
| ONNX | Multiple frameworks | Cross-platform deployment |
| TensorRT Engine | NVIDIA | GPU optimization |
| Core ML | Apple | iOS deployment |
| TFLite | TensorFlow Lite | Mobile devices |

---

## What is GGUF?

GGUF (GPT-Generated Unified Format) is a modern model format developed for **llama.cpp** to efficiently run large language models on consumer hardware.

### Features

- Faster loading
- Quantization support
- Metadata storage
- CPU optimized
- Supports GPU acceleration
- Lower memory usage

---

## Advantages

- Small file size
- Runs on laptops
- Faster inference
- Easy deployment
- Compatible with llama.cpp and Ollama

---

## Limitations

- Primarily for inference rather than training
- Not universally supported across all frameworks

---

## When to Use GGUF

- Running LLMs locally
- Offline AI applications
- Limited hardware environments
- Privacy-focused deployments

---

## Conclusion

GGUF has become one of the most popular formats for running open-weight language models locally due to its efficient storage, fast inference, and broad support in tools such as llama.cpp and Ollama. Other formats like Safetensors, ONNX, and TensorRT remain important for training, interoperability, and optimized deployment.