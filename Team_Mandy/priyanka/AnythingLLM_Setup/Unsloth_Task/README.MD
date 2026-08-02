# Unsloth Fine-tuning Task

## Overview
This task demonstrates fine-tuning a Large Language Model using Unsloth with LoRA (Low-Rank Adaptation) on Google Colab.

## Dataset Selection

Dataset Used:
- yahma/alpaca-cleaned

Description:
The Alpaca dataset contains instruction-following examples with three main fields:
- Instruction
- Input
- Output

It is used for instruction fine-tuning of language models.

## Model Selection

Base Model:
- unsloth/Llama-3.2-1B-Instruct

Reason for Selection:
- Lightweight model suitable for Google Colab T4 GPU
- Supports efficient fine-tuning using Unsloth
- Good performance for instruction-based tasks

## Fine-tuning Approach

Framework:
- Unsloth

Technique:
- LoRA (Low-Rank Adaptation)
- Parameter Efficient Fine-Tuning (PEFT)

Hardware:
- Google Colab Tesla T4 GPU

Training Configuration:
- Training samples: 1000
- Training steps: 60
- Batch size: 2
- Gradient accumulation steps: 4
- Learning rate: 2e-4

## Implementation Steps

1. Installed Unsloth and required libraries.
2. Loaded Llama-3.2-1B-Instruct model in 4-bit mode.
3. Loaded Alpaca instruction dataset.
4. Applied LoRA adapters for efficient training.
5. Fine-tuned the model using SFTTrainer.
6. Saved and tested the fine-tuned model.

## Result

The model was successfully fine-tuned using Unsloth and generated responses for test instructions after training.

## Files

- `finetuning.ipynb` - Complete Colab notebook containing dataset loading, model setup, training, and testing.
- `README.MD` - Documentation of the fine-tuning process.