---
title: Mood Checker
emoji: 🙂
colorFrom: blue
colorTo: green
sdk: gradio
app_file: app.py
pinned: false
---

# Mood Checker

A tiny practice app: type a sentence and a Hugging Face sentiment model tells you if it's positive or negative.

## Run locally

1. `pip install -r requirements.txt`
2. Copy `.env.example` to `.env` and paste your Hugging Face token
3. `python app.py`

## Built with

- [Hugging Face Inference](https://huggingface.co/docs/huggingface_hub/guides/inference) with `distilbert-base-uncased-finetuned-sst-2-english`
- [Gradio](https://www.gradio.app/) for the web UI