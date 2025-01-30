# import os

# if __name__ == "__main__":
#     print("Welcome to RoboSpeaker 2.0!")
#     while True:
#         x = input("enter what you want me to speak: ")
#         if x == "q":
#             os.system("say'bye bye friend")
#             break
    
#         command = f"say{x}"
#         os.system(command)
import pyttsx3

engine = pyttsx3.init()

if __name__== "_main_":
    print("Welcome to RoboSpeaker 1.1. Created by Harry")
    while True:
        x = input("Enter what you want me to speak: ")
        if x.lower() == "q":
            engine.say("Bye bye, friend!")
            engine.runAndWait()
            break
        engine.say(x)
        engine.runAndWait()