import os
import requests
import json
from datetime import datetime
from speech_module import speak

API_KEY = "your_google_bard_api_key_here"

def fetch_response_from_bard(user_query):
    url = f"https://bard.googleapis.com/v1/query?key={API_KEY}"
    payload = {"query": user_query}
    headers = {"Content-Type": "application/json"}

    try:
        response = requests.post(url, data=json.dumps(payload), headers=headers)
        if response.status_code == 200:
            result = response.json()
            return result.get("response", "Sorry, I couldn't process your request.")
        else:
            return "Error fetching response."
    except Exception as e:
        return f"An error occurred: {e}"

def execute_task(command):
    if "open notepad" in command:
        os.system("notepad")
        speak("Opening Notepad")
    elif "time" in command:
        time_now = datetime.now().strftime("%H:%M")
        speak(f"The time is {time_now}")
    elif "exit" in command or "stop" in command:
        speak("Goodbye!")
        exit()
    else:
        response = fetch_response_from_bard(command)
        speak(response)
