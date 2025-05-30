# 🧠 Chatbot Using Python & NLTK

**COMPANY**: CODTECH IT SOLUTION

**NAME**: ALLEN SAM AJI

**INTERN ID**: CT08DL1122

**DURATION**: 8 WEEKS

**MENTOR**: NEELA SANTOSH

---

# DESCRIPTION OF TASK LIKE HOW YOU PERFORMED AND WHAT YOU HAVE DONE AND PASTE PICTURES OF OUTPUT

## Overview
This project demonstrates the creation of a simple yet functional AI-powered chatbot using **Python** and **Natural Language Processing (NLP)** techniques with **NLTK (Natural Language Toolkit)**. It is a console-based chatbot that processes user input, performs tokenization, and responds to various queries using a rule-based intent-matching approach.

---

## 🚀 Features

- 💬 Responds to greetings and FAQs using keyword matching
- 🧠 Tokenizes input using `RegexpTokenizer` (no external downloads required)
- 🔠 Preprocesses input via lowercasing and word extraction
- 🔄 Pattern-based response matching with fallback replies
- 🛠️ Easily extendable intent-response dictionary

---

## 🛠 Technologies Used

- **Python 3.13**
- **NLTK (Natural Language Toolkit)**
- **RegexpTokenizer** for efficient, no-dependency tokenization
- **Random** (to return varied responses)

---

## 🎯 Objective

The objective of this project is to build a rule-based NLP chatbot using Python. This task introduces fundamental concepts in natural language processing such as text tokenization, preprocessing, and pattern matching to simulate a basic conversation flow. It avoids reliance on large datasets or ML models to keep it lightweight and easy to understand.

---

## 🧩 Implementation

### 1. Input Preprocessing

We used `RegexpTokenizer` with the regex pattern `\w+` to split the user’s input into words while removing punctuation and symbols. The input is also converted to lowercase to ensure uniformity during matching.

### 2. Intent Matching

A Python dictionary named `responses` maps specific keywords to a list of possible responses. The chatbot loops through these patterns and checks whether the keywords exist in the preprocessed input.

### 3. Response Logic

Using Python’s `random` module, a response is randomly selected from the matched intent. If no match is found, a default fallback response is returned.

### 4. Error Handling

Originally, `word_tokenize()` was used, but it required downloading the `punkt` tokenizer, which caused errors on some systems. To resolve this, we replaced it with `RegexpTokenizer`, eliminating external dependencies and improving portability.

---

## ▶️ How to Run

1. Clone this repository or download the script.
2. Install the required library:
   ```bash
   pip install nltk
3. Run the chatbot:
   ```bash
   python Chatbot.py
Type exit to quit the chatbot at any time.

---

## 💡 Sample Conversation (Terminal Output)
    Chatbot is running. Type 'exit' to quit.
    
    You: hi
    Bot: Hello! How can I assist you today?
   
    You: what is your name?
    Bot: I am your friendly chatbot assistant.
   
    You: bye
    Bot: Goodbye! Have a nice day!

---

## 🧪 Sample Response Dictionary
    responses = {
       "hello": ["Hi there!", "Hello!", "Greetings!"],
       "hi": ["Hi!", "Hey!", "Hello!"],
       "how are you": ["I'm good, thanks!", "Doing well! How can I help?"],
       "what is your name": ["I'm your friendly chatbot.", "Call me ChatBot!"],
       "bye": ["Goodbye!", "See you soon!", "Take care!"],
       "help": ["How can I assist you?", "Sure, I'm here to help."]
      }

---

## 📷 Output
![Image](https://github.com/user-attachments/assets/e0cbdf41-a1de-42b4-8667-d85385c7035f)

---

## ✅ Conclusion

This chatbot project demonstrates a beginner-friendly application of NLP using Python. It uses keyword-based responses and text preprocessing to understand and respond to user input. With the help of RegexpTokenizer, we avoid dependency issues common with punkt and make the chatbot portable and lightweight.

This project is a great starting point for those looking to understand how conversational agents work and can be expanded to include:

ML/NLP models for intent classification

Integration with APIs

GUI or web-based interfaces

---

## 📜 License
This project is open-source and free to use or modify for personal and educational purposes.
