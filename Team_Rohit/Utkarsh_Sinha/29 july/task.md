# Model Formats & GGUF Deep Dive — 29 July 2026

## 1. Overview of Common AI Model Formats
Machine learning models are distributed in various file formats depending on the target runtime environment (training vs. inference, CPU vs. GPU, cloud vs. edge).

| Format | File Extension | Key Characteristics & Primary Use Cases |
| :--- | :--- | :--- |
| **PyTorch Checkpoint** | `.pt` / `.bin` | Raw PyTorch tensor dictionary. Uses Python `pickle` (inherent security risk). Standard during initial training phase. |
| **Safetensors** | `.safetensors` | Modern, zero-copy, secure tensor format developed by Hugging Face. Fast memory-mapped (`mmap`) loading, no executable code. Standard for model weight distribution on Hugging Face. |
| **GGUF** | `.gguf` | Single-file binary format optimized for CPU & GPU local inference via `llama.cpp` and Ollama. Packages model metadata, vocabulary, and quantized weights together. |
| **EXL2** | `.exl2` | ExLlamaV2 format designed for high-speed quantized inference on NVIDIA GPUs. Supports variable fractional bitrates (e.g., 3.5-bit, 4.25-bit). |
| **ONNX** | `.onnx` | Open Neural Network Exchange. Cross-platform format enabling model execution across PyTorch, TensorFlow, TensorRT, and OpenVINO engines. |
| **TensorRT-LLM / AWQ / GPTQ** | Internal / `.safetensors` | Quantized GPU formats specialized for enterprise serving engines like vLLM, TensorRT-LLM, and TGI. |

---

## 2. Deep Dive: What is GGUF?

### Definition & Origin
**GGUF (GPT-Generated Unified Format)** is an open binary file format created by **Georgi Gerganov** and the `llama.cpp` development team. It was introduced to replace the older **GGML** format, establishing a modern, extensible standard for local LLM deployment on CPU and GPU hardware.

### Why GGUF Replaced GGML
1. **Key-Value Metadata Header:** GGML broke compatibility with every architecture update. GGUF solves this by using extensible KV pairs in the header, allowing parser compatibility across versions.
2. **Backward & Forward Compatibility:** Future versions of runtime software can safely load older GGUF files.
3. **Self-Contained Distribution:** A GGUF file contains all components required for inference: architecture specs, hyperparameters, tokenizer dictionary, and model weights.

### Key Features & Advantages

1. **Post-Training Quantization (K-Quants):**
   * GGUF supports various quantization schemes (`Q4_K_M`, `Q5_K_M`, `Q8_0`, `IQ3_XS`).
   * Reduces memory requirements by 50%–75% with minimal accuracy loss (e.g., compressing a 16GB FP16 model down to ~4.5GB Q4 file).

2. **CPU + GPU Hybrid Offloading:**
   * Layers can be dynamically split between VRAM (Metal on Mac, CUDA on NVIDIA) and system RAM / CPU cores, allowing models larger than VRAM to run seamlessly.

3. **Fast Memory Mapping (`mmap`):**
   * Enables near-instantaneous model loading without slow deserialization loops.

4. **Universal Client Support:**
   * Natively supported across popular local LLM tools: **Ollama**, **LM Studio**, **Jan.ai**, **llama-cpp-python**, and **Text Generation WebUI**.

---

## 3. Format Conversion Flow

```
PyTorch (.pt / .bin) ───[Convert to Safetensors]───> .safetensors ───[Quantize / llama.cpp]───> GGUF (.gguf)
     (Training)                                      (Distribution)                               (Local Inference)
```
