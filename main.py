import json
from greeting import getResponse
from learning_resource import getTutorial
from world_time import getTime
from calculator import calculateValue
from weather import getWeather
from password_checker import validatePassword

# Load the JSON file
with open('responses.json') as f:
    responses = json.load(f)

# Define a function to handle user input
def handleInput(input_str):
    # Convert the user input to lowercase
    input_str = input_str.lower()

    # Check if the user input is a greeting
    if input_str in responses['greetings']:
        return getResponse(responses, input_str)
    elif 'learn' in input_str or 'learning' in input_str:
        return getTutorial(responses)
    elif 'time' in input_str or 'timing' in input_str:
        return getTime(responses)
    elif 'math' in input_str:
        return calculateValue(responses)
    elif 'weather' in input_str:
        return getWeather()
    elif 'password' in input_str:
        return validatePassword()
    else:
        return "I'm sorry, I didn't understand what you said."


# Main loop to receive and respond to user input
while True:
    user_input = input("You: ")

    if user_input == 'quit':
        break
    elif user_input.lower() == 'bye':
        print("Chatbot: Bye!")
        break
    else:
        response = handleInput(user_input)
        print("Chatbot:", response)