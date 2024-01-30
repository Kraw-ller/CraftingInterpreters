#from pyreadline3 import Readline
#import pyreadline

def main(args):
    try: 
        if len(args) > 1:
            print("Usage: jlox [script]")
            exit(64)
        elif len(args) == 1:
            runFile(args[0])
        else:
            runPrompt()
    except IOError as e:
        print(f"Error in main:{e}")

def runFile(path):
    try:
        f = open(path, "rb")
        byte = f.read()
        run(byte.decode('utf-8'))
    except IOError as e:
        print(f"Error in runFile:{e}")

def runPrompt():
    try:
        while True:
            line = input(">")
            print("running your code")
    except EOFError: #To be fixed later CTRL-Z + ENTER (windows)
        print("Exiting interactive LoxPy shell.")
    except IOError as e:
        print("\nError in runPrompt:{e}")

def run(source):
    print("run")





