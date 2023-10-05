import openai
from dotenv import load_dotenv
import os

# Configure .env
def Configure():
    load_dotenv()


def GptInit():
    # Get OpenAi API key
    openai.api_key = os.getenv("api_key")
    messages = [ {"role": "system", "content": "You are a intelligent assistant."} ]

    while 1: 
        # Prompt the user to input a message
        message = input("User : ") 
        # Check if the user entered a message (non-empty)
        if message:
            # Create a new message object representing the user's message
            messages.append( 
                {"role": "user", "content": message}, 
            ) 
             # Generate a response from the ChatGPT model based on the conversation so far
            chat = openai.ChatCompletion.create( 
                model="gpt-3.5-turbo", messages=messages 
            ) 
        # Extract the reply from the model's response
        reply = chat.choices[0].message.content 
        # Print Response
        print(f"ChatGPT: {reply}") 
        # Add respond back to history
        messages.append({"role": "assistant", "content": reply})

# Main
def main():
    Configure()
    GptInit()
    

if __name__ == "__main__":
    main()