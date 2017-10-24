import subprocess
from time import  sleep
import win32com.client as wincl

proc = None


def setup_powershell():
    global proc
    subprocess.run("powershell.exe -Command Add-Type -AssemblyName System.speech\n$speak = New-Object System.Speech.Synthesis.SpeechSynthesizer\n$speak | Get-Member", shell=True)
    #subprocess.Popen("-Command Add-Type -AssemblyName System.speech")
    #subprocess.Popen("-Command $speak = New-Object System.Speech.Synthesis.SpeechSynthesizer")
    #print(proc)

'''
def run_powershell(order):
    return order

def setup():
    setup_powershell()
    commands = [
        "-Command ls"
    ]
    for c in commands:
        print(run_powershell(c))
        #subprocess.Popen(run_powershell(c))

def speak(content):
    commands = '$speak.Speak(' + content + ')'
    for c in commands:
        subprocess.Popen(run_powershell(c))
'''
def speak(content):
    commands = "powershell.exe"
    commands += " "
    commands += "-Command"
    commands += " "
    commands += "Add-Type -AssemblyName System.speech"
    commands += "\n"
    commands += "$speak = New-Object System.Speech.Synthesis.SpeechSynthesizer"
    commands += "\n"
    #commands += '$speak.Speak(0)'
    commands += ('$speak.Speak(" %s ")' % "Wow")
    #commands += "$speak | Get-Member"
    proc = subprocess.Popen(commands)
    print(proc)
    sleep(100)
    proc.terminate()

if __name__ == '__main__':
    #setup()
    #speak("Wow")
    #setup_powershell()

    speak = wincl.Dispatch("SAPI.SpVoice")
    speak.Speak("Hello World")
