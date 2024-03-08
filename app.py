from flask import Flask, request, jsonify
from textblob import TextBlob

app = Flask(__name__)

@app.route('/sentiment', methods=['POST'])
def sentiment_analysis():
    data = request.get_json()
    text = data['text']

    # Perform sentiment analysis using TextBlob
    analysis = TextBlob(text)
    sentiment = analysis.sentiment.polarity

    # Classify sentiment
    if sentiment > 0:
        sentiment_class = 'Positive'
    elif sentiment < 0:
        sentiment_class = 'Negative'
    else:
        sentiment_class = 'Neutral'

    return jsonify({
        'text': text,
        'sentiment': sentiment_class
    })

if __name__ == '__main__':
    app.run(debug=True)
