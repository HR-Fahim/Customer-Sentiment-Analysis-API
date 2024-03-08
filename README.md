# Customer Sentiment Analysis API

This project demonstrates how to create a simple Sentiment Analysis API using Python, Flask, and TextBlob.

## Setup

### 1. Prerequisites

- Python 3.x
- pip (Python package manager)

### 2. Clone the Repository

```bash
git clone https://github.com/your-username/Sentiment-Analysis-API.git
cd Sentiment-Analysis-API
```

### 3. Set Up Virtual Environment (Optional but Recommended)

```bash
python -m venv myenv
```

Activate the virtual environment:
- On Windows:
  ```bash
  myenv\Scripts\activate
  ```
- On macOS/Linux:
  ```bash
  source myenv/bin/activate
  ```

### 4. Install Dependencies

```bash
pip install -r requirements.txt
```

## Usage

### Running the Flask Application

```bash
python app.py
```

The application should start running at `http://localhost:5000`.

### Testing the API

Use `curl` or Postman to test the API. Send a POST request to `http://localhost:5000/sentiment` with a JSON payload containing the text to be analyzed.

Example using `curl`:

```bash
curl -X POST http://localhost:5000/sentiment -H "Content-Type: application/json" -d '{"text": "I love this product!"}'
```
or

```bash
Invoke-RestMethod -Method Post -Uri http://localhost:5000/sentiment -ContentType "application/json" -Body '{"text": "I love this product!"}'
```

### Result

![Sentiment Analysis API](https://github.com/HR-Fahim/Customer-Sentiment-Analysis-API/assets/66734379/26ed9402-0fd7-4baa-a477-ce388c563dd2)

It shows a response indicating the sentiment analysis result.

## Future Work

To extend this project into a more sophisticated sentiment analysis system the following steps can be considered in future:
- Collect a labeled dataset for training.
- Train a machine learning model using libraries like scikit-learn or TensorFlow/Keras.
- Integrate the trained model into the Flask API for sentiment analysis.
