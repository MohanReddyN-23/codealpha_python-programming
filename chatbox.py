def get_response(user_input):
    user_input = user_input.lower()
    responses = {
        'hi': 'Hello! How can I assist you today?',
        'hello': 'Hi there! How can I help you?',
        'how are you?': 'I am just a computer program, but thanks for asking!',
        'what is your name?': 'I am a chatbot created by you.',
        'bye': 'Goodbye! Have a great day!',
        'quit': 'Goodbye! Have a great day!'
    }
    
    return responses.get(user_input, "Sorry, I didn't understand that.")

def chat():
    print("Hello! I am a basic chatbot. Type 'quit' or 'bye' to end the conversation.")
    while True:
        user_input = input("You: ")
        response = get_response(user_input)
        print(f"Chatbot: {response}")
        if user_input.lower() in ['quit', 'bye']:
            break

if __name__ == "__main__":
    chat()
