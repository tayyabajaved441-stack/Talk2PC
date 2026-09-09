import speech_recognition as sr
import webbrowser
import pyttsx3


def speak(text):
    engine = pyttsx3.init()
    engine.say(text)
    engine.runAndWait()
    engine.stop()


def processCommand(c):
    c = c.lower()

    if "open google" in c:
        speak("Opening Google")
        webbrowser.open("https://google.com")

    elif "open youtube" in c:
        speak("Opening YouTube")
        webbrowser.open("https://youtube.com")

    elif "linkedin" in c:
        speak("Opening LinkedIn")
        webbrowser.open("https://linkden.com")

    elif "time" in c:
        import datetime
        now = datetime.datetime.now().strftime("%I:%M %p")
        speak(f"The time is {now}")

    else:
        speak("Sorry, I did not understand that command")


if __name__ == "__main__":
    speak("initializing komal....")

    # Print available microphones (only needed once, for debugging)
    print("Available microphones:", sr.Microphone.list_microphone_names())

    while True:
        r = sr.Recognizer()
        r.energy_threshold = 300
        r.dynamic_energy_threshold = True

        try:
            with sr.Microphone() as source:
                print("Listening for wake word...")
                r.adjust_for_ambient_noise(source, duration=1)
                audio = r.listen(source, timeout=5, phrase_time_limit=3)

            word = r.recognize_google(audio, language="en-US")
            print("Heard:", word)

            if word.lower() == "komal":
                speak("ya")

                # Listen for actual command
                with sr.Microphone() as source:
                    print("Listening for command...")
                    r.adjust_for_ambient_noise(source, duration=1)
                    audio = r.listen(source, timeout=5, phrase_time_limit=5)

                command = r.recognize_google(audio, language="en-US")
                print("Command:", command)
                processCommand(command)

        except sr.WaitTimeoutError:
            print("Timeout, listening again...")
        except sr.UnknownValueError:
            print("Could not understand audio")
        except Exception as e:
            print("Error: {}".format(e))
