"""
Voice control / recognition
"""

# This file is no longer used : all logic has been moved to main.py
# (voice_loop with threading)
# Do not use listen_command() as it is blocking and slow.

import speech_recognition

def listen_command():
    recognizer = speech_recognition.Recognizer()
    
    with speech_recognition.Microphone() as source:
        recognizer.adjust_for_ambient_noise(source)
        print("Parler maintenant ('monter' ou 'descendre')")
        
        try:
            audio = recognizer.listen(source, timeout=5, phrase_time_limit=3)
            print("Audio capté, reconnaissance en cours...")
            command = recognizer.recognize_google(audio, language="fr-FR").lower()
            print(f"Commande Vocale reconnue : {command}")
            
            if any(word in command for word in ["haut", "monte", "monter"]):
                return "up"
            elif any(word in command for word in ["bas", "descend", "descendre"]):
                return "down"
            else:
                print("Commande vocale non reconnue dans la liste attendue")
        
        except speech_recognition.UnknownValueError:
            print("Pas compris")
        
        except speech_recognition.RequestError:
            print("Erreur de reconnaissance")
        
        except speech_recognition.WaitTimeoutError:
            print("Timeout")
    
    return None