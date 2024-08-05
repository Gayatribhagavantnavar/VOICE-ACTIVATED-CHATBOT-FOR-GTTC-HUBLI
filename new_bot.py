import nltk
import speech_recognition as sr
from nltk.chat.util import Chat, reflections
import pyttsx3

# Define responses for the chatbot
pairs = [
    ['Can i Get Address', ['yup, Gokul Road, Hubballi, Karnataka 580030']],
    ['can i get contact details', ['yup, you can contact to this number 155267']],
    ['can i get Email id', ['gttcsdchubli@gmail.com']],
    ['what are Working Hours', ['Monday to Friday – 10 am to 5pm']],
    ['What are the facilities available?', ['Regular classes, \n Certified teachers, \n Sufficient classroom, \n Creative lessons, \n Sports facilities, \n Safety first']],
    ['available facilities?', ['Regular classes, \n Certified teachers, \n Sufficient classroom, \n Creative lessons, \n Sports facilities, \n Safety first']],
    ['what are the special events in campus?', ['Cultural events, \n Work shops, \n Job fairs,\n Sports events']],
    ['what about placements', ['From well known companies like Wipro, ORACLE, Zensar Technologies, Quess Corp, Infosys, Xentrix, Informatica, And many more']],
    ['How about teaching', ['Teachings at its best with highly qualified staff with certified teachers.']],
    ['Do we get placement assistance training?', ['yes ofcourse']],
    ['interview training?', [
        'yes ofcourse']],
    ['thanks for guiding me', [
        'you are welcome, see you later. have a great day']],
    ['bye', ['you are welcome, see you later. have a great day']],
    ['after completion of the course when i will get my certificate', ['it may take 1 month for internships and 6 months for free courses']],
    ['when i will get my certificate', ['it may take 1 month for internships and 6 months for free courses']],
    ['is there hostel facility', ['no']],
    ['hostel and food', [
        'no']],
    ['any other gttc centers near my place', [
        'gttc centers are available in hubli and also in dharwad']],
    ['gttc centers', [
        'gttc centers are available in hubli and also in dharwad']],
    ['can we pay the course fee by installments', [
        'ohh sorry,fee need to pay completely at a time']],
    ['installments', [
        'ohh sorry,fee need to pay completely at a time']],
    ['course fee in installments', [
        'ohh sorry,fee need to pay completely at a time']],
    ['emi', [
        'ohh sorry,fee need to pay completely at a time']],
    ['quit', ['Bye!', 'Goodbye!', 'See you later.']],
]
def speak(text):
    engine = pyttsx3.init()
    engine.say(text)
    engine.runAndWait()


def get_audio():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        audio = r.listen(source)
        try:
            text = r.recognize_google(audio)
            print("You:", text)
            return text.lower()
        except sr.UnknownValueError:
            speak("Sorry, I couldn't understand that.")
            return ""
        except sr.RequestError:
            speak("Sorry, I'm having trouble processing your request.")
            return ""

# Create a chatbot using the defined pairs
chatbot = Chat(pairs, reflections)
def chat():
    speak("Hello! Welcome to GTTC Hubli  Please ask me your queries. I'll help you")
    while True:
        user_input = get_audio()
        if user_input.lower() == 'quit':
            speak("Goodbye! Have a nice day")
            break
        else:
            response = chatbot.respond(user_input)
            speak(response)
            print(response)

# Start the chat loop
if __name__ == "__main__":
    chat()
