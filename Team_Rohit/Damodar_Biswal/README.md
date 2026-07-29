Assignment of Damodar Biswal.

Q1-> Difference between close source model and open source , open weight model??

Ans-> AI models can be classified based on what is shared with the public. A closed-source model does not provide its source code, training data, or model weights. Users can only access it through an API or application. Examples include GPT-5.5 and Claude. An open-source model shares its source code, model weights, and often the training process and datasets, allowing anyone to study, modify, and redistribute it. A true fully open-source AI model is still relatively rare. An open-weight model shares only the trained model weights, allowing users to run and fine-tune the model, but the training code or dataset is not fully released. Examples include Llama 3, Mistral, and Gemma. Open-weight models offer flexibility while keeping some development details private.

--------------------------------------------------------------------------------------------------

Q2-> Write a summary . What are the top 3 tools available in the market for model tunning and training? And why unsloth is the best ? What are your recommendation?

Ans-> Today, the three most popular tools for fine-tuning Large Language Models (LLMs) are Unsloth, Axolotl, and LLaMA-Factory. Unsloth is known for its high speed and low GPU memory usage, making it ideal for training models on consumer GPUs. Axolotl is designed for production-scale training with advanced features such as multi-GPU support and complex configurations. LLaMA-Factory focuses on ease of use by providing a web interface and support for many open-weight models. All three tools are built on the Hugging Face and PyTorch ecosystem but target different users. The best choice depends on our hardware, project size, and experience level rather than one tool being universally superior.

Unsloth is popular because it optimizes the training process instead of changing the model itself. It replaces standard PyTorch operations with optimized kernels, allowing training to run faster while using less VRAM. This means you can fine-tune models like Llama, Qwen, Gemma, and Mistral on GPUs with much less memory than traditional methods. It also supports LoRA, QLoRA, and other parameter-efficient fine-tuning techniques. For students and individual developers, this reduces hardware cost and training time significantly. However, for very large multi-GPU or enterprise workloads, frameworks like Axolotl may provide more flexibility and scalability.

If my goal is learning Agentic AI, building projects, and fine-tuning models on a personal laptop or a single GPU, I will go with Unsloth. It has the lowest hardware requirements and is easy to set up.

-------------------------------------------------------------------------------------------------------

Q3-> What am i supposed to train LLM or SLM?

Ans-> For most students, researchers, and startups, SLMs (Small Language Models) are the better choice. Large Language Models (LLMs) such as Llama 70B or GPT-scale models require expensive GPUs, large datasets, and significant training time. In contrast, SLMs (1B–8B parameters) can be fine-tuned on a single consumer GPU, are faster, cheaper, and easier to deploy. They perform very well for tasks like chatbots, document Q&A, coding assistants, and domain-specific applications. Instead of training an LLM from scratch, most developers fine-tune an open-weight SLM using tools like Unsloth. This approach provides excellent performance while keeping costs low.

Rule to remember:

LLM → Expensive, large-scale, enterprise training.
SLM → Affordable, practical, and ideal for learning and most real-world applications.

---------------------------------------------------------------------------------------------------------

Q4-> Difference between SLM and LLM?

Ans-> SLM (Small Language Model)                                                 LLM (Large Language Model)
-------------------------------------------------------                      --------------------------------------------------------
                        
1) Has fewer parameters (1B–10B approximately).                             1) Has billions to hundreds of billions of parameters. (10B+).
                                                                                       
2) Requires less GPU memory and computing power. 
                                                                            2) Requires high-end GPUs and large computing resources.                   
3) Faster for training and inference.  
                                                                            3) Slower due to larger model size.                                            
4) Lower training and deployment cost.  
                                                                            4) Higher training and deployment cost.                                        
5) Best for specific tasks like chatbots,
 document Q&A, or coding assistants.                                        5) Best for general-purpose tasks requiring broad 
                                                                                knowledge and reasoning. 
6) Can run on a single GPU or even powerful laptops (depending on size).  
                                                                            6) Usually requires multiple GPUs or cloud infrastructure.
7) Easier to fine-tune and deploy.
                                                                            7) More difficult and expensive to fine-tune. 

8) Examples: **Llama 3.2 3B, Gemma 3 4B, Qwen 2.5 3B**                      8) Examples: Llama 3.1 70B, GPT-5.5, Claude   


---------------------------------------------------------------------------------------------------------------

Q5-? Wht is GGUF format?

Ans-> GGUF (GPT-Generated Unified Format) is a special file format used to save and run AI language models efficiently on local computers. Think of it like a ZIP file that contains everything the AI model needs to work, such as model weights (knowledge), tokenizer (how text is split into words), and model settings. Instead of storing these in separate files, GGUF combines them into one optimized file. It also supports quantization, a technique that reduces the model's size (for example, from 14 GB to 4 GB) while keeping most of its performance. This makes it possible to run models on laptops or CPUs with less RAM. Tools like Ollama, LM Studio, and llama.cpp use GGUF files to load and run AI models locally.

Real-Life Analogy
Imagine you buy a new mobile phone.

To use it, you need:
Operating System
Apps
Settings
User Data

Instead of downloading everything separately, the company gives you one complete backup file.

👉 GGUF is like that backup file.
It contains everything required to run the AI model.

Example:Suppose you download:
```text
Llama-3.2-3B-Q4_K_M.gguf
```
This single .gguf file already contains:

✅ Model weights (the AI's learned knowledge)
✅ Tokenizer
✅ Model configuration
✅ Quantization information

Now, if you open Ollama or LM Studio, they simply load this .gguf file and the AI starts working.
