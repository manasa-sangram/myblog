from transformers import pipeline

CATEGORIES = [
    "Technology",
    "Life",
    "Travel",
    "Arts"
]

_classifier = None

def get_classifier():
    global _classifier
    if _classifier is None:
        _classifier = pipeline(
            "zero-shot-classification",
            model="facebook/bart-large-mnli"
        )
    return _classifier


def suggest_category(text):
    classifier = get_classifier()
    result = classifier(text, CATEGORIES)
    return result["labels"][0], result["scores"][0]
