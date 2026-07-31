# Fine-Tuning with Unsloth on Google Colab

This guide covers the process of fine-tuning a Large Language Model (e.g., Llama-3-8B) on a custom dataset using the Unsloth framework within Google Colab. Unsloth is chosen because it allows 2x faster training and uses 70% less VRAM, making it possible to fine-tune on a free Colab T4 GPU.

## 1. Dataset Selection & Formatting
For instruction tuning, the dataset must follow a specific chat template. We will use the **Alpaca** format.
1. Find a dataset on Hugging Face (e.g., `yahma/alpaca-cleaned` or a custom finance QA dataset).
2. The format should look like this:
   ```json
   {
     "instruction": "What is a neural network?",
     "input": "",
     "output": "A neural network is a machine learning model inspired by the human brain..."
   }
   ```

## 2. Model Selection
1. Go to Hugging Face and select an unsloth-optimized base model.
2. Recommended starting model: `unsloth/llama-3-8b-bnb-4bit`. This model is pre-quantized to 4-bit, meaning it will load instantly into Colab without blowing up the VRAM.

## 3. Fine-Tuning Process (Colab)
1. **Open the Unsloth Notebook:** Navigate to the [Unsloth GitHub repository](https://github.com/unslothai/unsloth) and open the provided Google Colab notebook for Llama 3.
2. **Install Dependencies:** Run the first cell to install `unsloth`, `xformers`, and `trl`.
3. **Load the Model & PEFT:**
   - The notebook loads the 4-bit model and applies LoRA (Low-Rank Adaptation) adapters. 
   - Set the `r` value to `16` or `32` (higher means more complex learning, but takes longer).
4. **Load the Dataset:** Map your selected dataset to the model's expected prompt format.
5. **Start Training:**
   - The `SFTTrainer` (Supervised Fine-Tuning Trainer) from Hugging Face is used.
   - Run the cell. You will see the training loss decrease over the epochs. A typical 1-epoch run on a small dataset takes about 30-45 minutes on a T4.

## 4. Exporting the Model
Once training is complete, the model's new knowledge is stored in the LoRA adapters.
1. **Inference Test:** Run the inference cell in the notebook to ask a question and verify the model learned the new style/data.
2. **Save to GGUF:** Unsloth allows you to merge the adapters into the base model and export it as a GGUF file directly in Colab.
3. **Download:** Download the `.gguf` file to your local machine and load it into LM Studio to use your newly trained, custom AI!
