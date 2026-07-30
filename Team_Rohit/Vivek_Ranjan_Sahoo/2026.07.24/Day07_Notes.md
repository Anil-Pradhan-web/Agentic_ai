# Day 7  
##   
****Topic: Model Training, Fine-Tuning, SLMs, LLMs, GGUF, LM Studio, Jan, and Unsloth****  
  
## Lecture Summary  
Today's session mainly focused on ****why AI engineers should learn model training and fine-tuning instead of only using ChatGPT or other AI tools****.  
The instructor explained:  
* Why Full Stack AI Engineers are in demand.  
* Difference between using an AI model and training one.  
* Why fine-tuning is necessary.  
* Open Source vs Closed Source models.  
* Open Weight models.  
* Difference between Large Language Models (LLMs) and Small Language Models (SLMs).  
* LM Studio vs Jan vs Unsloth.  
* GGUF model format.  
* High-level workflow of model training.  
The practical fine-tuning was postponed to the next session because today's class focused on building strong fundamentals.  
  
## 1. Career Advice  
The instructor started with career guidance.  
****Key Messages****  
* Decide your target early.  
* Don't chase money.  
* Build capability.  
* Once you become skilled,  
    * companies will come to you,  
    * your resume will speak for itself.  
****Goal****  
Become  
Full Stack AI Engineer  
instead of only learning random AI tools.  
  
## 2. What Industry Expects  
Companies do ****NOT**** expect freshers to build foundation models.  
Instead, they expect you to know  
* AI concepts  
* Model training workflow  
* Fine-tuning process  
* Standard Operating Procedures (SOPs)  
* Deployment basics  
Even if you cannot practically train huge models because of GPU limitations, you should understand the complete process.  
  
## 3. Infrastructure Challenge  
Training AI models requires  
* High-end GPUs  
* Large RAM  
* Expensive hardware  
The instructor mentioned that industries understand students usually don't have such infrastructure.  
He also mentioned India is investing more in AI GPU infrastructure.  
Example:  
* HCL Tech investing in AI data centers (mentioned as recent news during the lecture).  
  
## 4. India's AI Situation  
According to the instructor:  
India is  
* excellent at software development  
* excellent programmers  
* produces many CTOs  
But  
India lacks  
* GPU infrastructure  
* risk-taking investment  
Meanwhile  
USA  
* has strong infrastructure  
China  
* focuses on building efficient models using less hardware.  
  
## 5. Agent Development Roadmap  
The instructor said upcoming sessions will focus almost entirely on AI Agents.  
Tools that will be explored:  
1. Unsloth  
2. OpenClaw  
3. Multi-agent frameworks (mentioned informally)  
Goal:  
Learn vendor-independent agent development.  
  
## 6. Local LLMs  
The instructor explained why local models are important.  
Benefits  
* Internet not required  
* Privacy  
* Works during travel  
* No dependency on OpenAI subscriptions  
Example  
Working inside  
* airport  
* airplane  
without internet.  
  
## 7. LM Studio  
Purpose  
Run local models.  
Workflow  
Download model  
↓  
Run locally  
↓  
Expose OpenAI-compatible API  
↓  
VS Code / IDE connects to local model.  
Advantages  
* Easy setup  
* Local inference  
* API compatible  
Limitation  
Not suitable for model training.  
  
## 8. Jan AI  
Jan provides both  
* Cloud models  
* Local models  
Features mentioned  
* Download local models  
* Use API keys  
* Supports MCP  
* Suggests models according to hardware  
* Chat interface  
The instructor personally liked Jan but emphasized:  
Choose whichever suits your workflow.  
  
## 9. Difference Between LM Studio and Jan  
Both are mainly  
Model runners.  
Meaning  
They run models.  
They do NOT specialize in training.  
  
## 10. Why Unsloth?  
This was the biggest topic of today's lecture.  
Instructor repeatedly emphasized  
Use ****Unsloth**** for  
* model training  
* model fine-tuning  
Reason  
It is specifically designed for  
training open models.  
Unlike LM Studio or Jan,  
Unsloth is built for  
* training  
* tuning  
* optimization  
##   
##   
  
### Comparison  

| Tool      | Main Purpose               |
| --------- | -------------------------- |
| LM Studio | Run local models           |
| Jan       | Run local + cloud models   |
| Unsloth   | Train and Fine-tune models |
  
##   
## 11. Why Fine-Tuning?  
This was explained using multiple examples.  
Without fine-tuning  
Model gives  
generic answers.  
Example  
Suppose you build an AI for  
a hospital.  
General LLM  
doesn't know  
hospital SOPs  
or  
company policies.  
So it must be trained.  
  
### Why Train?  
Because  
Open models  
have  
limited knowledge.  
Instructor compared this to  
A brilliant student  
who stopped studying after graduation.  
Very intelligent  
but outdated.  
Exactly like many open models.  
  
## 12. Why Closed Models are Better  
Examples  
* GPT  
* Claude  
Reason  
They continuously receive  
new training.  
New user interactions  
↓  
Better model  
↓  
Continuous improvement.  
  
## 13. Hallucination  
Instructor explained hallucination.  
Meaning  
Model gives  
incorrect  
or  
irrelevant  
answers.  
Even RAG cannot completely eliminate hallucination because  
RAG retrieves information,  
but  
decision making still depends on the model.  
Therefore  
Fine-tuning improves accuracy further.  
  
## 14. Open Source vs Closed Source  
Important assignment given.  
Students were asked to research  
Difference between  
Closed Source  
vs  
Open Source  
vs  
Open Weight.  
Important point mentioned  
To fine-tune a model  
It must be  
✅ Open Source  
AND  
✅ Open Weight  
Open Source alone is not enough.  
  
## 15. LLM vs SLM  
Another major concept.  
  
****LLM****  
Large Language Model  
Characteristics  
* Generic  
* Huge  
* Trained on trillions of parameters  
* Cannot realistically be retrained by students  
Examples  
GPT  
Claude  
Gemini  
  
****SLM****  
Small Language Model  
Characteristics  
* Domain-specific  
* Easier to fine-tune  
* Used inside organizations  
Examples  
Hospital AI  
Legal AI  
Banking AI  
Coding assistant  
  
Instructor's line  
LLM = Jack of all trades  
SLM = Specialist.  
  
## 16. GGUF Format  
One of today's most important technical concepts.  
GGUF  
=  
compressed model format.  
Think of it like  
ZIP file.  
Model runners understand GGUF.  
Examples  
LM Studio  
Jan  
Unsloth  
can directly run GGUF models.  
  
But  
You cannot fine-tune GGUF.  
Instead  
download  
original source model  
from Hugging Face.  
Instructor compared this to  
Editing a ZIP file.  
You must  
extract first  
↓  
edit  
↓  
compress again.  
Exactly same idea.  
  
## 17. Hugging Face vs GitHub  
Important interview question.  
****GitHub****  
Stores  
software  
code.  
  
****Hugging Face****  
Stores  
AI models  
datasets  
model cards.  
  
Hugging Face requires  
* Model  
* Dataset  
* Documentation  
* Version  
* Training details  
Everything should be transparent.  
  
## 18. High-Level Fine-Tuning Workflow  
This is probably the most important section.  
  
****Step 1****  
Choose a model.  
  
****Step 2****  
Download model.  
  
****Step 3****  
Test whether model is good enough.  
  
****Step 4****  
Choose domain  
Example  
* Legal  
* Banking  
* Healthcare  
  
****Step 5****  
Collect dataset  
Formats  
* PDF  
* DOCX  
* TXT  
  
****Step 6****  
Use Unsloth  
Extract  
↓  
Prepare dataset  
↓  
Train model  
↓  
Export trained model.  
  
## Human Analogy Used  
This analogy was repeated many times.  
Base Model  
↓  
B.Tech Graduate  
Dataset  
↓  
University curriculum  
Trainer Model  
↓  
Professor  
Fine-tuned Model  
↓  
M.Tech graduate with specialization  
This analogy explains the entire fine-tuning process.  
  
## Assignments Given  
Students were asked to prepare short reports on:  
****1****  
Difference between  
Open Source  
Open Weight  
Closed Source  
  
****2****  
Top 3 tools available in the market for model training and tuning.  
Explain why Unsloth is preferred.  
  
****3****  
Difference between  
LLM  
SLM  
  
****4****  
GGUF  
What is it?  
Other model formats.  
  
****5****  
Download a GGUF model  
Run it using  
* Jan  
* LM Studio  
* Unsloth  
  
## Important Interview Questions  
1. Why do we fine-tune a model?  
2. Difference between LM Studio and Unsloth.  
3. Why can't GGUF models be trained directly?  
4. What is Open Weight?  
5. Difference between Open Source and Open Weight.  
6. Difference between Hugging Face and GitHub.  
7. Difference between LLM and SLM.  
8. Why are SLMs preferred inside organizations?  
9. Why are Closed Source models generally stronger?  
10. Explain the high-level workflow of model training.  
  
## Key Takeaways  
* Don't just learn prompts—learn how models are trained.  
* Understanding the workflow is more important than owning expensive GPUs.  
* LM Studio and Jan are for running local models.  
* Unsloth is the preferred tool for training and fine-tuning.  
* Fine-tuning requires an ****open-source, open-weight**** model.  
* GGUF is a deployment/runtime format, not a training format.  
* Organizations mostly use ****specialized SLMs**** tailored to their domain rather than generic LLMs.  
* Hugging Face is the standard repository for sharing AI models, datasets, and model documentation, whereas GitHub is primarily for software code.  
#   
  
  
  
