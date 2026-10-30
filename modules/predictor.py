import torch
import json
from transformers import AutoTokenizer, AutoModelForSequenceClassification

MODEL_PATH = "models/fine_tuned_distilbert"

tokenizer = AutoTokenizer.from_pretrained(MODEL_PATH)
model = AutoModelForSequenceClassification.from_pretrained(MODEL_PATH)

model.eval()

with open(f"{MODEL_PATH}/label_mapping.json", "r") as f:
    label_mapping = json.load(f)


def predict_resume(text):
    inputs = tokenizer(
        text,
        return_tensors="pt",
        truncation=True,
        padding=True,
        max_length=512
    )

    with torch.no_grad():
        outputs = model(**inputs)

    probabilities = torch.softmax(outputs.logits, dim=1)
    top_predictions = torch.topk(probabilities, k=3)

    results = []

    for score, index in zip(
        top_predictions.values[0],
        top_predictions.indices[0]
    ):
        results.append({
            "category": label_mapping[str(index.item())],
            "confidence": round(score.item() * 100, 2)
        })

    return results