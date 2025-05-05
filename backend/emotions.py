from transformers import pipeline

classifier = pipeline("text-classification", model="cardiffnlp/twitter-roberta-base-emotion")

def detect_emotion(text):
    return classifier(text)[0]['label']
