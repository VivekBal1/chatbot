import datetime
import pytz

def getTime(responses):
    print("Chatbot: sure, please mention a country name anyone from this list (india, australia, usa, uk)")
    country = input("You: ")
    if country in responses['world_clock']:
        timezone = responses['world_clock'][country]
        tz = pytz.timezone(timezone)
        current_time = datetime.datetime.now(tz)
        msg = f"The current date and time in {timezone} is {current_time.strftime('%Y-%m-%d %H:%M:%S')}"
        return msg