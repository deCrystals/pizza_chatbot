from openai import OpenAI
import os
from dotenv import load_dotenv, find_dotenv

_=load_dotenv(find_dotenv())

# Set your OpenAI API key
client=OpenAI(api_key = os.getenv("OPENAI_API_KEY"))

# Pizza menu and pricing
pizza_menu = {
    "Margherita": 10,
    "Pepperoni": 12,
    "Vegetarian": 11,
    "Hawaiian": 13,
}

# Function to generate chatbot responses using OpenAI's GPT
def generate_chatbot_response(user_input, conversation_history):
    # Define the chatbot's role and instructions
    system_prompt = """
    You are a friendly and helpful customer service chatbot for a pizza company. 
    Your tasks include:
    1. Helping customers choose pizzas from the menu.
    2. Providing pricing information.
    3. Taking orders and confirming them.
    4. Answering general questions about the company.
    Be polite and concise in your responses.
    """

    # Combine system prompt, conversation history, and user input
    messages = [
        {"role": "system", "content": system_prompt},
        *conversation_history,
        {"role": "user", "content": user_input},
    ]

    # Call the OpenAI API
    response = client.chat.completions.create(
        model="gpt-4o-mini",  
        messages=messages,
        max_tokens=150,
    )

    # Extract and return the chatbot's response
    return response["choices"][0]["message"]["content"].strip()

# Function to handle the conversation
def pizza_chatbot():
    print("Welcome to PizzaBot! How can I assist you today?")
    conversation_history = []

    while True:
        user_input = input("You: ")

        # Exit the conversation if the user says "bye" or "exit"
        if user_input.lower() in ["bye", "exit", "quit"]:
            print("PizzaBot: Thank you for visiting! Have a great day!")
            break

        # Generate a response using the chatbot
        bot_response = generate_chatbot_response(user_input, conversation_history)
        print(f"PizzaBot: {bot_response}")

        # Update conversation history
        conversation_history.append({"role": "user", "content": user_input})
        conversation_history.append({"role": "assistant", "content": bot_response})

# Run the chatbot
if __name__ == "__main__":
    pizza_chatbot()