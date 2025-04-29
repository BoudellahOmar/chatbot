import openai

# Replace with your own API key from https://platform.openai.com/account/api-keys
openai.api_key = "your-api-key-here"

def chat_with_ai(message):
    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=[
            {"role": "system", "content": "You are a helpful assistant."},
            {"role": "user", "content": message}
        ]
    )
    return response['choices'][0]['message']['content']

# Simple command-line chatbot loop
if __name__ == "__main__":
    print("Hello! I'm your chatbot. Type 'exit' to quit.\n")
    while True:
        user_input = input("You: ")
        if user_input.lower() in ["exit", "quit"]:
            print("👋 Goodbye!")
            break
        reply = chat_with_ai(user_input)
        print("Bot:", reply)
