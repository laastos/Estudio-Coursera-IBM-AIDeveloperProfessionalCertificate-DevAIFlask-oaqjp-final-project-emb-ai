import requests
import json

def emotion_detector(text_to_analyze):
    # URL of the emotion detection service
    url = 'https://sn-watson-emotion.labs.skills.network/v1/watson.runtime.nlp.v1/NlpService/EmotionPredict'
    # Create a dictionary with the text to be analyzed
    myobj = { "raw_document": { "text": text_to_analyze } }
    # Set the headers required for the API request
    header = {"grpc-metadata-mm-model-id": "emotion_aggregated-workflow_lang_en_stock"}
    # Send a POST request to the API with the text and headers
    response = requests.post(url, json = myobj, headers=header)
    # Parsing the JSON response from the API
    formatted_response = json.loads(response.text)
    # Extracting emotion label and score from the response
    if response.status_code == 200:
        emotions = {
            'anger' : formatted_response['emotionPredictions'][0]['emotion']['anger'],
            'disgust' : formatted_response['emotionPredictions'][0]['emotion']['disgust'],
            'fear' : formatted_response['emotionPredictions'][0]['emotion']['fear'],
            'joy' : formatted_response['emotionPredictions'][0]['emotion']['joy'],
            'sadness' : formatted_response['emotionPredictions'][0]['emotion']['sadness']
        }
        emotions['dominant_emotion'] = max(emotions, key=emotions.get)
    elif response.status_code == 400:
        emotions = {
            'error': 'Bad Request: Please check the input text format.',
            'anger' : None,
            'disgust': None,
            'fear': None,
            'joy': None,
            'sadness': None,
            'dominant_emotion': None,
        }
    elif response.status_code == 500:
        emotions = {'error': 'Internal Server Error: Please try again later.'}
    # Return the response text from the API
    return emotions