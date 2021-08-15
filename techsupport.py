from gtts import gTTS
from playsound import playsound
import os
import random
import time
def tts(mytext):
    language = "en"
    sound = gTTS(text=mytext, lang=language, slow=False)
    sound.save("temp.mp3")
    playsound("temp.mp3")
    os.remove("temp.mp3")
def phn():
    n = '0000000000'
    while '9' in n[3:6] or n[3:6]=='000' or n[6]==n[7]==n[8]==n[9]:
        n = str(random.randint(10**9, 10**10-1))
    return n[:3] + '-' + n[3:6] + '-' + n[6:]
mode = input("Type in Text or Phone.")
if mode == "Text":
    def tts(mytext):
        print(mytext)
tts("Welcome to Tech Support Simulator!")
tts("What is your name, and what do you want your company to be named?")
myname = input("Your name: ")
companyname = input("Company name: ")
tts("Your name is " + myname + " and you are working for " + companyname + ".")
tts("Now, here is what you would hear when you call " + companyname + ".")
tts("Thank you for calling " + companyname + " support. Please wait while we transfer you to a support representative.")
tts("Now, I cut out the music because that lasts for a WEEK.")
tts("Now, your job is to handle the phone calls.")
tts("Your email address is support@" + companyname + ".com")
tts("And you are recieving phone calls at " + phn() + ". To get the tech support, you can call " + phn() + ".")
tts("Now, " + companyname + " has a new great Python program!")
tts("The name of it is " + companyname + " Phone System!")
tts("Just call " + companyname + "'s phone, and you can get forwarded!")
tts("Now, type in python phone.py into your computer.")
cmdtest = input("N:\\Programs\\Python>")
while not cmdtest == "python phone.py":
    tts("Remember, you needed to type in python phone.py to get the phone receiver.")
    cmdtest = input("N:\\Programs\\Python>")
tts("Running Phone Reciever")
tts("Yay, you got the Phone Receiver set up!")
tts("Now, the phone reciever is a program you should run all the time. Whenever you get a call, it asks you whether you want to answer it.")
tts("Now, I will go back home.")
print("Phone Reciever")
print("Ready for calls")
time.sleep(9)
tts("You got a call.")
input("Type Y to accept, or N to decline.")
def call1():
        tts("This is a test of the Phone System.")
        tts("I will hang up now.")
call1()
tts("The Phone System worked!")
tts("Now, do you want to play sandbox mode or story mode?")
mode = input("Type in Story or Sandbox: ")
if mode == "Story":
    tts("Story mode")
elif mode == "Sandbox":
    tts("Sandbox mode")
else:
    tts("Remeber, there is a capital S in Story or Sandbox mode.")
tts("A call was just ended.")
print("Phone Reciever")
print("Ready for calls")
time.sleep(7)
tts("You got a call.")
input("Type Y to accept, or N to decline.")
tts("Hi!")
tts("I need help with my iPad.")
tts("Do you offer help with iPads?")
command = input("You: ")
if command == "Yes." or "Yes!":
    tts("OK!")
else:
    tts("Exiting out of Tech Support Simulator.")
    exit()
tts("Now, whenever I turn it on, my iPad gives me a notifaction saying I need to do something with my phone number.")
tts("How do you get rid of it?")
command = input("You: ")
score = 0
yelpreviews = []
yelp = 0
if command == "Click on it!" or "Click on it.":
    tts("OK, I clicked on it.")
    tts("Should I say yes or no?")
    command2 = input("You: ")
    if command2 == "Yes!" or "Yes.":
        tts("Thank you!")
        score = score + 6
    else:
        tts("It now wants me to change my phone number!")
        score = score - 2
        tts("I really wish I just said yes.")
else:
    print("That solution is not in Tech Support Simulator.")
    time.sleep(5)
    exit()
tts("Your current score is " + str(score) + "!")
print("Phone Reciever")
print("Ready for calls")
if score == 0 and mode == "Sandbox":
    tts("Sorry, but if you don't have any points by your 3rd call, I will have to fire you.")
    tts("If you didn't expect that, then maybe read your contract before working here at " + companyname + ".")