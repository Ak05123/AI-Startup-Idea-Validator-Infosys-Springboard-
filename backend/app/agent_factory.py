from app.config import (
    gemini_model_1,
    gemini_model_2,
    gemini_model_3
)

models = [
    gemini_model_1,
    gemini_model_2,
    gemini_model_3
]

current = 0

def get_model():
    global current
    return models[current]

def next_model():
    global current
    current = (current + 1) % len(models)
    return models[current]