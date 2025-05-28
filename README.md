# Emotion Detection Web Application

This project is a web application that performs emotion detection on text using a natural language processing API. The application analyzes text input and determines the dominant emotion expressed, including anger, disgust, fear, joy, and sadness.

## Features

- Web interface for submitting text for emotion analysis
- Real-time emotion detection using Watson NLP API
- Display of emotion scores and dominant emotion
- Built with Flask backend and JavaScript frontend

## Project Structure

```
.
├── EmotionDetection/
│   ├── __init__.py          # Package initialization
│   └── emotion_detection.py # Core emotion detection functionality
├── static/
│   └── mywebscript.js       # Frontend JavaScript code
├── templates/
│   └── index.html           # Web application interface
├── server.py                # Flask server implementation
├── test_emotion_detection.py # Unit tests for emotion detection
├── LICENSE                  # Apache 2.0 license
└── README.md                # Project documentation
```

## Installation

1. Clone the repository
2. Install the required Python packages:
   ```
   pip install flask requests
   ```

## Usage

1. Start the Flask server:
   ```
   python server.py
   ```
2. Open a web browser and navigate to `http://localhost:5000`
3. Enter text in the input field and click "Run Sentiment Analysis"
4. View the emotion detection results

## Testing

Run the unit tests with:
```
python test_emotion_detection.py
```

## API

The application uses the Watson NLP Emotion Prediction API to analyze text.

## License

This project is licensed under the Apache License 2.0 - see the [LICENSE](LICENSE) file for details.

## Author

IBM Developer Skills Network