import win32com.client as wincl

if __name__ == '__main__':
    scripts = """print("Hello World")"""
    speak = wincl.Dispatch("SAPI.SpVoice")
    speak.Speak(scripts)
