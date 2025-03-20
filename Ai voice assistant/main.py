from .Modules.speech_module import recognize_speech, speak
from .Modules.task_executor import execute_task

if __name__ == "__main__":
    speak("Hello! How can I assist you today?")
    while True:
        command = recognize_speech()
        if command:
            execute_task(command)
