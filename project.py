#imports the relevant packages and modules

from gtts import gTTS
from playsound import playsound
from functions import *

#initializes and makes the start of the application
print("Started application...")

loop = True

while (loop):
	text = input("""
What text do you want to convert?
Input an empty line to terminate the programe: \n""")

	if (text == ""):
		loop = False
		print("Terminating application")
		break

	if (not ValidInput(text)):
		print("Invalid input!")

	else:
		lang = 'en'
		obj = gTTS(text=text, lang=lang, slow=False)
		obj.save("file.mp3")
		playsound("file.mp3")

