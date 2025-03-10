## **Chatbot with Keras and Flask Deployment**

### **Overview**
This project implements a **seq2seq chatbot** using an **LSTM encoder-decoder model** in Keras. The chatbot can process text at either **character-level** or **word-level**. The trained models are deployed using **Flask**, making them accessible via a web API.

---

## **Project Structure**
```
chatbot_train/
│── data/                    # Contains the datasets for training
│── models/                  # Stores trained chatbot models
│── very_large_data/         # Contains the GloVe embeddings (auto-downloaded if not present)
│── train_chatbot.py         # Script for training the chatbot model
│── inference.py             # Model inference for chatbot responses
│── requirements.txt         # Python dependencies
│── README.md                # Documentation
│── flask_app/
│   ├── app.py               # Flask web deployment
│   ├── templates/           # HTML templates for UI
│   ├── static/              # Static files (CSS, JS)
│   ├── model_loader.py      # Load trained models into Flask
│   ├── requirements.txt     # Dependencies for Flask server
```

---

## **Setup Instructions**

### **1. Install Dependencies**
Ensure you have Python **3.8+** installed. Then, install the required dependencies:

```bash
pip install -r requirements.txt
```

For Flask web deployment, install additional dependencies:
```bash
pip install -r flask_app/requirements.txt
```

---

### **2. Train the Chatbot Model**
To train the chatbot model, run:

```bash
python train_chatbot.py
```
This script:
- Loads training data from the **data/** directory.
- Trains an LSTM encoder-decoder seq2seq model.
- Saves trained models in the **models/** directory.

---

### **3. Running the Chatbot Locally**
Once training is complete, you can test the chatbot in the terminal:

```bash
python inference.py
```
This script:
- Loads the trained model from the **models/** directory.
- Accepts user input and returns chatbot-generated responses.

---

### **4. Web Deployment Using Flask**
To deploy the chatbot via Flask, navigate to the **flask_app/** directory:

```bash
cd flask_app
python app.py
```
- The chatbot will be accessible at: `http://127.0.0.1:5000`
- The API will accept text input and return chatbot-generated responses.

---

## **GloVe Embeddings**
- The chatbot uses **GloVe word embeddings** for improved language understanding.
- If the embeddings are not present in the **very_large_data/** directory, they will be automatically downloaded when the chatbot runs.

---

## **API Usage**
The Flask API exposes an endpoint for chatbot interactions:

### **Endpoint: `/chat`**
- **Method**: `POST`
- **Request**: JSON `{ "message": "Hello" }`
- **Response**: JSON `{ "response": "Hi! How can I assist you?" }`

Example usage:

```bash
curl -X POST http://127.0.0.1:5000/chat -H "Content-Type: application/json" -d '{"message": "Hello"}'
```

---

## **Technologies Used**
- **Machine Learning**: Keras, TensorFlow (LSTM seq2seq)
- **Natural Language Processing (NLP)**: Tokenization, GloVe embeddings
- **Backend**: Flask (Web API)
- **Deployment**: Flask server

---

## **Future Enhancements**
- Improve response quality using Transformer models.
- Deploy using **Docker & Kubernetes** for scalability.
- Implement real-time chatbot interactions via WebSockets.

---



