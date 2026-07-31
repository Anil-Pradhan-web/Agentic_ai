# Model File Formats — Brief

## GGUF
GPT-Generated Unified Format. Binary format from llama.cpp for efficient local LLM inference (CPU/GPU). Bundles weights + tokenizer + config in one file. Supports quantization (4/5/8-bit) for smaller size, faster inference. Used by llama.cpp, Ollama, LM Studio.

## Other Formats

| Format | Use Case |
|---|---|
| **safetensors** | Hugging Face's safe, fast storage; default for most releases |
| **PyTorch (.pt/.bin)** | Native training checkpoints; pickle-based |
| **ONNX** | Cross-framework portability/deployment |
| **TensorFlow (.h5/SavedModel)** | TF/Keras native |
| **GGML** | GGUF's deprecated predecessor |
| **GPTQ/AWQ/EXL2** | GPU-optimized quantization |
| **MLX** | Apple Silicon optimized |
| **CoreML** | iOS/macOS on-device |
| **TensorRT** | NVIDIA compiled inference engine |

**Rule of thumb:** GGUF for local/CPU inference → GPTQ/AWQ for GPU-only quantized inference → safetensors/PyTorch for training & full precision.
