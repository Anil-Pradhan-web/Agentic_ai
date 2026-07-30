# Assignment

## (1) Difference Between Closed Source Model, Open Source Model, and Open Weight Model

Artificial Intelligence (AI) models can be classified into three categories based on how much access users have to the model's code and trained weights.

| Feature | Closed Source Model | Open Source Model | Open Weight Model |
|---------|---------------------|-------------------|-------------------|
| Source code available | No | Yes | Usually No |
| Model weights available | No | Yes | Yes |
| Can modify the model | No | Yes | Limited |
| Can study how it works | Very Limited | Yes | Partially |
| Examples | GPT-4, Claude, Gemini | OLMo, OpenELM | Llama 3, Mistral, Gemma |

### Closed Source Model

A closed source model is developed and controlled by a company. Users can access it through a website or API, but they cannot see the source code or download the trained model. The company manages updates, pricing, and usage.

**Examples:** GPT-4, Claude, Gemini.

### Open Source Model

An open source model provides both the source code and the trained weights. Developers and researchers can study, modify, and improve the model according to their needs.

**Examples:** OLMo and OpenELM.

### Open Weight Model

An open weight model shares its trained weights but may not release the complete training code or dataset. Users can run the model locally and fine-tune it for their own tasks.

**Examples:** Llama 3, Mistral, Gemma.

### Conclusion

Closed source models provide the least flexibility but are simple to use. Open source models offer complete transparency and freedom. Open weight models provide a balance by allowing users to run and fine-tune the model while keeping some parts of the training process private.

---

# (2) One-Page Summary: Top 3 Tools for Model Training and Fine-Tuning

Training and fine-tuning AI models require software that helps manage datasets, computing resources, and machine learning workflows. Among the many tools available today, the following three are widely used by students, researchers, and industry professionals.

## 1. Hugging Face

Hugging Face is one of the most popular platforms for working with AI models. It provides thousands of pre-trained models, datasets, and easy-to-use libraries for fine-tuning.

### Advantages

- Large collection of open models
- Easy fine-tuning with Transformers and PEFT
- Excellent documentation
- Strong community support

**Best for:** Students, beginners, and researchers.

---

## 2. Google Colab

Google Colab is a cloud-based notebook environment that allows users to run Python code using free or paid GPU resources. It removes the need for expensive hardware during learning.

### Advantages

- Free GPU access (with limits)
- No software installation
- Easy collaboration
- Good for experiments and assignments

**Best for:** Learning and small AI projects.

---

## 3. PyTorch

PyTorch is a deep learning framework used to build and train neural networks. It is widely used in research and industry because it is flexible and beginner-friendly.

### Advantages

- Industry-standard framework
- Easy debugging
- Flexible model development
- Large developer community

**Best for:** Custom AI model development.

---

## Recommendation

For students beginning AI and machine learning, the best combination is:

1. **Hugging Face** for accessing and fine-tuning pre-trained models.
2. **Google Colab** for running experiments without powerful hardware.
3. **PyTorch** for understanding and building deep learning models.

Together, these tools provide a complete environment for learning and developing AI applications.

---

# (3) LLM and SLM: Why LLMs Cannot Usually Be Trained by Individuals

Large Language Models (LLMs) and Small Language Models (SLMs) are AI models designed to understand and generate human language. Their main difference is the number of parameters and the computing resources needed.

## Large Language Models (LLMs)

LLMs contain billions of parameters and are trained on massive datasets collected from books, websites, articles, and other sources. Training these models requires thousands of high-performance GPUs, huge storage capacity, and significant financial investment.

Because of these requirements, students and individual developers generally cannot train an LLM from scratch. Instead, they use existing open-weight models and fine-tune them for specific tasks.

**Examples:** GPT-4, Llama 3 70B, Claude.

---

## Small Language Models (SLMs)

SLMs contain fewer parameters and require much less computing power. They can often be fine-tuned using a single GPU and sometimes even run efficiently on laptops.

They are suitable for chatbots, mobile applications, educational projects, and domain-specific tasks.

**Examples:** Phi-3 Mini, Gemma 2B, TinyLlama.

---

## Conclusion

Training an LLM from scratch is usually beyond the reach of individual developers due to the high cost and hardware requirements. However, fine-tuning existing open-weight LLMs is possible using techniques such as LoRA and QLoRA. For students, SLMs are an excellent choice because they are faster, cheaper, and easier to work with.

---

# (4) One-Page Summary: Difference Between LLM and SLM

Language models are AI systems trained to understand and generate human language. They are generally divided into Large Language Models (LLMs) and Small Language Models (SLMs).

| Feature | LLM | SLM |
|---------|-----|-----|
| Model size | Billions of parameters | Millions to a few billion parameters |
| Training cost | Very High | Low |
| Hardware needed | Multiple high-end GPUs | Single GPU or CPU |
| Speed | Slower | Faster |
| Memory usage | High | Low |
| Best suited for | General-purpose AI | Specific and lightweight applications |

## Large Language Models (LLMs)

LLMs are designed for a wide variety of tasks such as answering questions, coding, summarising text, and reasoning. They generally produce higher-quality responses but require powerful hardware and large amounts of memory.

## Small Language Models (SLMs)

SLMs focus on efficiency rather than size. They consume less memory, respond faster, and can run on laptops, edge devices, and mobile phones. They are often preferred when the task is limited to a specific domain.

## Summary

LLMs offer better performance on complex tasks but require significant computing resources. SLMs provide a practical alternative for students and developers who need fast, efficient, and affordable AI models.

---

# (5) Other Model Formats and What is GGUF?

AI models are stored in different file formats depending on the framework and their intended use.

| Model Format | Purpose |
|--------------|---------|
| `.pt` / `.pth` | PyTorch model files used during training and inference |
| `.safetensors` | Safe format for storing model weights without executing code |
| `.onnx` | Portable format for deploying models across different platforms |
| TensorFlow SavedModel | Standard format used by TensorFlow |
| `.gguf` | Optimised format for running language models locally |

## What is GGUF?

GGUF (GPT-Generated Unified Format) is a file format designed to run large language models efficiently on personal computers. It is mainly used with **llama.cpp** and other local inference tools.

### Advantages of GGUF

- Faster model loading.
- Supports quantised models, reducing memory usage.
- Can run efficiently on CPUs and consumer GPUs.
- Ideal for offline AI applications.

For example, if someone wants to run a Llama or Mistral model on a laptop without an internet connection, they can download the GGUF version of the model and run it locally using a compatible inference program.

## Conclusion

Different model formats are designed for different purposes. PyTorch and TensorFlow formats are commonly used during model development and training. SafeTensors is used for securely sharing model weights. ONNX helps deploy models across different platforms, while GGUF is widely used for running language models efficiently on local devices.