from flask import Flask, render_template, request
from EmotionDetection.emotion_detection import emotion_detector

app = Flask("Emotion Detector")

@app.route("/")
def render_index_page():
    return render_template('index.html')

@app.route("/emotionDetector", methods=["GET"])
def emotion_detector_route():
    text_to_analyze = request.args.get('textToAnalyze')
    response = emotion_detector(text_to_analyze)
    
    if response['dominant_emotion'] is None:
        return "Invalid text! Please try again."
    else:
        formatted_response = (
            f"For the given statement, the system response is "
            f"'anger': {response['anger']}, 'disgust': {response['disgust']}, 'fear': {response['fear']}, "
            f"'joy': {response['joy']} and 'sadness': {response['sadness']}. "
            f"The dominant emotion is {response['dominant_emotion']}."
        )
        return formatted_response

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
