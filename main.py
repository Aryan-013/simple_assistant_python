import pyttsx3
import speech_recognition as speech
import datetime
engine=pyttsx3.init("sapi5")
voices=engine.getProperty('voices')
engine.setProperty('voices',voices[0].id)


def speaking(audio):
    engine.say(audio)
    engine.runAndWait()

def listen_to_voice():
    r_speech=speech.Recognizer()
    with speech.Microphone() as input_source:
        print("Please speak something")
        r_speech.pause_threshold=3
        audio=r_speech.listen(input_source) 

    try:
        print("recogonizing")
        query=r_speech.recognize_google(audio,language='en-in')
        audio=[]
        list.append("whats your name")
        list.append("who are you")
        list.append("what can you do")
        print(audio)
        for i in audio:
            if(audio[i]=="whats your name"):
                speaking("my name is Jarvis, how can i help you")
            elif(audio[i=="who are you"]):
                speaking("im an assistant")  
            elif(audio[i]=="what can you do"):
                speaking("i can help you with a number of tasks")
                  
                
        
        
        print(query)
       
    except Exception as e:
        
        print("System cannot recogonize please say again")
        return "none"

    return query    
if __name__ == "__main__":
    speaking("This is an assistant name Fybeq")
    listen_to_voice()
    