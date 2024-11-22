import requests
import json

def emotion_detector(text_to_analyse):
    url = 'https://sn-watson-emotion.labs.skills.network/v1/watson.runtime.nlp.v1/NlpService/EmotionPredict'
    myobj = {"raw_document": {"text": text_to_analyse}}
    header = {"grpc-metadata-mm-model-id": "emotion_aggregated-workflow_lang_en_stock"}
    
    response = requests.post(url, json=myobj, headers=header)
    formatted_response = json.loads(response.text)
    
    emotion_scores = {}
    if "emotionPredictions" in formatted_response and len(formatted_response["emotionPredictions"]) > 0:
        emotion_scores = formatted_response["emotionPredictions"][0].get("emotion", {})
    
    required_emotions = ['anger', 'disgust', 'fear', 'joy', 'sadness']
    result = {emotion: emotion_scores.get(emotion, 0) for emotion in required_emotions}
    
    if any(result.values()):
        result['dominant_emotion'] = max(result, key=result.get)
    else:
        result['dominant_emotion'] = 'none'
    
    return result
