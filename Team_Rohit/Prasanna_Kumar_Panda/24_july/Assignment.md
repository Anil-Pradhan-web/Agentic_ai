# Agentic AI Assignment – 24 July

**Name:** Prasanna Kumar Panda  
**Team:** Team_Rohit

---

# 1. Chatbot vs AI Agent

Although chatbots and AI agents both use artificial intelligence, they are designed for different purposes.

A chatbot is mainly built to interact with users through conversation. It receives a question, generates a response, and waits for the next message. Most chatbots are reactive, meaning they only respond when a user asks something. Their primary goal is to answer questions, provide information, or assist with simple tasks.

An AI agent goes beyond conversation. It can reason, make decisions, plan multiple steps, use external tools, retrieve information, and execute tasks with little or no human intervention. Instead of simply answering a question, an AI agent works towards achieving a goal.

For example, if a user asks, "Book me the cheapest flight to Bangalore next weekend," a chatbot may only provide flight information or links. An AI agent can search flights, compare prices, fill in booking details, ask for confirmation, and complete the booking.

| Feature | Chatbot | AI Agent |
|---------|---------|----------|
| Primary Purpose | Conversation | Goal completion |
| Decision Making | Limited | Advanced |
| Planning | No | Yes |
| Uses External Tools | Usually No | Yes |
| Memory | Limited | Can maintain long-term memory |
| Autonomy | Low | High |

**Conclusion:** Every AI agent can communicate like a chatbot, but not every chatbot is an AI agent.

---

# 2. Privacy Policies of Major LLM Providers (OpenAI, Google, Claude)

Large Language Model providers collect user data differently, and understanding their privacy policies is important before using their services.

## OpenAI (ChatGPT)

OpenAI may use conversations submitted through ChatGPT to improve future models unless the user disables chat history or uses enterprise offerings where data handling is different. Users can also request deletion of their data. Enterprise and Team plans provide stronger privacy protections.

### Key Points
- Conversations may improve models (depending on settings and plan)
- Chat history can be disabled
- Enterprise data is generally not used for training

---

## Google (Gemini)

Google's Gemini follows Google's privacy framework. Conversations may be reviewed by human reviewers to improve AI quality. Users are advised not to enter confidential or sensitive information.

### Key Points
- Some conversations may be reviewed
- User controls are available
- Data handling follows Google's privacy policy

---

## Anthropic (Claude)

Anthropic emphasizes AI safety and responsible data handling. Claude conversations may be used to improve services depending on the product and user settings. Enterprise customers receive stronger privacy guarantees.

### Key Points
- Focus on responsible AI development
- Enterprise customer data receives additional protection
- Privacy controls vary by product

---

## Comparison

| Provider | Free User Data May Improve Models | Enterprise Privacy | User Controls |
|-----------|-----------------------------------|--------------------|---------------|
| OpenAI | Yes (depending on settings) | Strong | Good |
| Google | Yes | Strong | Good |
| Anthropic | Depends on product | Strong | Good |

**Recommendation:** Always avoid sharing passwords, financial details, confidential business information, or personal identification data with any public AI model.

---

# 3. Difference Between Closed Models, Open Source Models, and Open Weight Models

These three terms are often confused but represent different concepts.

## Closed Models

Closed models keep both the source code and model weights private. Users can only access them through APIs or official applications.

Examples:
- GPT-5
- Claude
- Gemini

### Advantages
- High performance
- Better support
- Regular updates

### Disadvantages
- Limited transparency
- API costs
- Vendor lock-in

---

## Open Source Models

Open source models release both the model and supporting source code, allowing anyone to inspect, modify, and contribute according to the license.

Examples:
- Some research models released with full source
- Community AI projects

### Advantages
- Complete transparency
- Community contributions
- Highly customizable

### Disadvantages
- Maintenance responsibility
- Requires technical expertise

---

## Open Weight Models

Open weight models release the trained model weights but not necessarily the complete training code or datasets.

Examples:
- Llama family
- Mistral
- Gemma

### Advantages
- Can run locally
- Fine-tuning is possible
- Lower inference cost

### Disadvantages
- Training process is not fully transparent
- License restrictions may apply

---

# 4. Top 3 Tools for Model Training and Fine-Tuning

Training and fine-tuning modern AI models require specialized frameworks. Three of the most popular tools are PyTorch, TensorFlow, and Hugging Face Transformers.

## 1. PyTorch

PyTorch is the most widely used deep learning framework in research and industry. It provides dynamic computation graphs, making experimentation simple and flexible.

### Strengths
- Easy debugging
- Python-friendly
- Large community
- Industry standard

---

## 2. TensorFlow

TensorFlow is Google's deep learning framework designed for scalable production deployment.

### Strengths
- Excellent production support
- TensorFlow Serving
- TensorFlow Lite for mobile deployment

---

## 3. Hugging Face Transformers

Hugging Face provides thousands of pre-trained models and tools for fine-tuning modern LLMs.

### Strengths
- Large model library
- Easy fine-tuning
- Excellent documentation
- Works with PyTorch and TensorFlow

---

## Comparison

| Tool | Best For |
|------|----------|
| PyTorch | Research and general deep learning |
| TensorFlow | Production deployment |
| Hugging Face | Fine-tuning LLMs |

## My Recommendation

If I were starting a new AI project today, I would choose **PyTorch together with Hugging Face Transformers**. PyTorch offers flexibility for experimentation, while Hugging Face significantly reduces the effort required to work with state-of-the-art language models. TensorFlow remains an excellent choice for organizations that already rely on Google's ecosystem or require mature production deployment tools.

---

# 5. Difference Between LLM and SLM

Language models vary greatly in size and capability.

An **LLM (Large Language Model)** contains billions or even trillions of parameters and is designed to solve a wide range of complex tasks.

An **SLM (Small Language Model)** contains significantly fewer parameters and is optimized for speed, efficiency, and local deployment.

| Feature | LLM | SLM |
|---------|-----|-----|
| Size | Very Large | Small |
| Hardware | Powerful GPU | Can run on laptops and mobile devices |
| Cost | Higher | Lower |
| Accuracy | Higher on complex tasks | Good for focused tasks |
| Speed | Slower | Faster |

Examples of LLMs:
- GPT-5
- Claude
- Gemini

Examples of SLMs:
- Phi
- Gemma 3 1B
- TinyLlama

**Conclusion:** LLMs are better for advanced reasoning, while SLMs are ideal when efficiency, lower cost, and local execution are priorities.

---

# 6. Other Model Formats and GGUF

AI models can be stored in different file formats depending on the framework and intended use.

Some common formats include:

- PyTorch (.pt, .pth)
- SafeTensors (.safetensors)
- TensorFlow SavedModel
- ONNX (.onnx)
- GGUF (.gguf)

## What is GGUF?

GGUF (GPT-Generated Unified Format) is a modern file format designed primarily for running large language models efficiently with tools such as **llama.cpp**. It stores the model weights together with metadata in a single optimized file, making local inference faster and easier.

### Advantages of GGUF

- Faster model loading
- Better compatibility with llama.cpp
- Supports quantized models
- Reduces memory usage
- Ideal for CPU-based local inference

GGUF has become one of the most popular formats for developers who want to run open-weight language models on personal computers without requiring expensive GPUs.

---

# Conclusion

The rapid growth of Generative AI has introduced powerful tools, models, and deployment methods. Understanding the differences between chatbots and AI agents, privacy practices of LLM providers, model licensing approaches, training frameworks, language model sizes, and deployment formats helps developers make informed technical decisions. As AI continues to evolve, selecting the right tools and models based on project requirements will become increasingly important. 