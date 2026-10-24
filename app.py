"""
Mood Checker - a tiny practice app.
Type a sentence, a Hugging Face model says if it's POSITIVE or NEGATIVE.
The model is downloaded from Hugging Face and runs on your own computer (free, no token).
"""

import gradio as gr
from transformers import pipeline

MODEL_ID = "distilbert/distilbert-base-uncased-finetuned-sst-2-english"

# Load the model once when the app starts (not on every click)
classifier = pipeline("sentiment-analysis", model=MODEL_ID)


def check_mood(text: str) -> dict:
    """Run the model on the text and return {label: score} for Gradio."""
    if not text.strip():
        return {"Type something first": 1.0}

    results = classifier(text, top_k=None)

    # Some versions wrap the answer in an extra list; unwrap it if so
    if results and isinstance(results[0], list):
        results = results[0]

    # results is a list like [{"label": "POSITIVE", "score": 0.99}, ...]
    return {r["label"]: r["score"] for r in results}


demo = gr.Interface(
    fn=check_mood,
    inputs=gr.Textbox(label="Your sentence", placeholder="I love hackathons!"),
    outputs=gr.Label(label="Mood"),
    title="Mood Checker",
    description="Practice app: Hugging Face model + Gradio + GitHub.",
)

if __name__ == "__main__":
    demo.launch()  # change to demo.launch(share=True) for a public link
