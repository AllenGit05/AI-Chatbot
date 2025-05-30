import random
from nltk.tokenize import RegexpTokenizer

tokenizer = RegexpTokenizer(r'\w+')

responses = {
    "hello": ["Hi there!", "Hello!", "Hey, how can I help you today?"],
    "hi": ["Hello!", "Hi! What can I do for you?", "Hey there!"],
    "how are you": ["I'm just a bunch of code, but I'm doing great!", "All systems go!", "I'm functioning as expected. Thanks for asking!"],
    "what is your name": ["I'm ChatPy!", "They call me Chatbot.", "I go by many names, but you can call me ChatPy!"],
    "bye": ["Goodbye!", "See you soon!", "Take care!", "Bye! Have a great day!"],
    "thank you": ["You're welcome!", "No problem!", "Glad to help!"],
    "thanks": ["Anytime!", "You're welcome!", "Happy to help!"],
    "help": ["I'm here to assist! Ask me anything.", "Sure, how can I help you today?", "Help is on the way! What do you need?"],
    "what can you do": ["I can chat with you and answer basic questions.", "I'm a simple chatbot created using Python and NLTK."],
    "who created you": ["I was created by a developer named Allen using Python and NLTK!", "A programmer named Allen brought me to life during an internship task."],
    "what is nlp": ["NLP stands for Natural Language Processing. It's how computers understand human language.", 
                    "Natural Language Processing is a field of AI that helps machines understand and respond to human language."]
}

def preprocess(text):
    text = text.lower()
    tokens = tokenizer.tokenize(text)
    return tokens

def chatbot_response(user_input):
    tokens = preprocess(user_input)
    for key in responses:
        key_tokens = key.split()
        if all(word in tokens for word in key_tokens):
            return random.choice(responses[key])
    return "I'm sorry, I didn't understand that. Try asking something else!"

def chat():
    print("Chatbot is running. Type 'exit' to quit.\n")
    while True:
        user_input = input("You: ")
        if user_input.lower() == "exit":
            print("Chatbot: Goodbye!")
            break
        response = chatbot_response(user_input)
        print("Chatbot:", response)

if __name__ == "__main__":
    chat()
