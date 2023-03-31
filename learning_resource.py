import re
import random
import webbrowser

def getTutorial(responses):
    print("Chatbot: sure, please mention a technology you wanna learn")
    technology = input("You: ")
    technology = re.sub('[^A-Za-z0-9]+', '', technology)
    if technology in responses['learning']:
        random_resource = random.choice(responses['learning'][technology])
        webbrowser.open_new_tab(random_resource)
        return random_resource