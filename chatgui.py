import nltk
from nltk.stem import WordNetLemmatizer
from keras.models import load_model
import pickle
import numpy as np
import json
import random
import tkinter as tk
from tkinter import Scrollbar, Text, END, DISABLED, NORMAL

# Load data and model
lemmatizer = WordNetLemmatizer()
model = load_model('chatbot_model.h5')
intents = json.loads(open('intents.json').read())
words = pickle.load(open('words.pkl', 'rb'))
classes = pickle.load(open('classes.pkl', 'rb'))


def clean_up_sentence(sentence):
    sentence_words = nltk.word_tokenize(sentence)
    return [lemmatizer.lemmatize(word.lower()) for word in sentence_words]


def bow(sentence, words, show_details=False):
    sentence_words = clean_up_sentence(sentence)
    bag = [0] * len(words)
    for s in sentence_words:
        for i, w in enumerate(words):
            if w == s:
                bag[i] = 1
                if show_details:
                    print(f"Found in bag: {w}")
    return np.array(bag)


def predict_class(sentence, model):
    p = bow(sentence, words, show_details=False)
    res = model.predict(np.array([p]))[0]
    ERROR_THRESHOLD = 0.25
    results = [[i, r] for i, r in enumerate(res) if r > ERROR_THRESHOLD]
    results.sort(key=lambda x: x[1], reverse=True)

    return [{"intent": classes[r[0]], "probability": str(r[1])} for r in results]


def get_response(intents_list, intents_json):
    if not intents_list:
        return "I'm not sure I understand. Can you rephrase?"

    tag = intents_list[0]['intent']
    for intent in intents_json['intents']:
        if intent['tag'] == tag:
            return random.choice(intent['responses'])
    return "Sorry, I didn't get that."


def chatbot_response(msg):
    intents_list = predict_class(msg, model)
    return get_response(intents_list, intents)


# GUI
class ChatbotApp:
    def __init__(self, root):
        self.root = root
        self.root.title("AI Chatbot")
        self.root.geometry("500x550")
        self.root.configure(bg="#f0f0f0")
        self.root.resizable(False, False)

        self.chat_log = Text(root, bd=0, bg="white", height="20", width="60", font=("Helvetica", 12), wrap="word")
        self.chat_log.config(state=DISABLED)

        self.scrollbar = Scrollbar(root, command=self.chat_log.yview)
        self.chat_log['yscrollcommand'] = self.scrollbar.set

        self.entry_box = Text(root, bd=0, bg="white", height="3", width="44", font=("Helvetica", 12))
        self.entry_box.bind("<Return>", self.send_message_event)

        self.send_button = tk.Button(root, text="Send", width=12, height=2, font=("Helvetica", 12, "bold"),
                                     bg="#32de97", fg="white", command=self.send_message)

        # Layout using grid
        self.chat_log.grid(row=0, column=0, columnspan=2, padx=10, pady=10, sticky="nsew")
        self.scrollbar.grid(row=0, column=2, sticky='ns', pady=10)
        self.entry_box.grid(row=1, column=0, padx=10, pady=10)
        self.send_button.grid(row=1, column=1, padx=10, pady=10)

        self.root.grid_rowconfigure(0, weight=1)
        self.root.grid_columnconfigure(0, weight=1)

    def send_message_event(self, event):
        self.send_message()
        return 'break'  # Prevent newline on Enter

    def send_message(self):
        msg = self.entry_box.get("1.0", END).strip()
        self.entry_box.delete("1.0", END)

        if msg:
            self.chat_log.config(state=NORMAL)
            self.chat_log.insert(END, "You: " + msg + "\n\n")
            self.chat_log.config(foreground="#442265", font=("Helvetica", 12))

            res = chatbot_response(msg)
            self.chat_log.insert(END, "Bot: " + res + "\n\n")
            self.chat_log.config(state=DISABLED)
            self.chat_log.yview(END)


if __name__ == "__main__":
    root = tk.Tk()
    app = ChatbotApp(root)
    root.mainloop()
