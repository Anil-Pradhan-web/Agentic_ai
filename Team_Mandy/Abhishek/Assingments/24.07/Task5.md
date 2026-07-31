What are the other format models are available? what is GGUF

Some other model format available in the market are:
->Safetensor(Hugging face)
->ONNX-Open Neural Network Exchange(TensorRT)
->TensorRT Engine(NVIDIA GPUs)
->MLX 
->TFlite (TensorFlow lite)


GGUF is a model format developed for llama.cpp. It is specifically designed for efficient local inference, especially on consumer hardware.

Features
Stores model weights and metadata in one file.
Supports quantization (e.g., Q4_K_M, Q5_K_M, Q8_0).
Runs efficiently on CPUs and GPUs.
Compatible with:
->llama.cpp
->LM Studio
->Ollama
->Jan
->KoboldCpp