import builtins
import random
import time
import os

# exclusive reminder for you nerd looking here using regular python wont work while using funfuncs xd to improve your 'gift''

_real_print = builtins.print
_real_input = builtins.input

def scream(*args, **kwargs):
    raise Exception("USE THE ENGLISH WAY! Check funfuncs.help() you moron!")

builtins.print = scream
builtins.input = scream

def say(*args):
    _real_print(*args)

def get(*args):
    prompt = " ".join(map(str, args)) + " "
    return _real_input(prompt)

def grab_number(*args):
    try:
        user_input = get(*args)
        return int(user_input)
    except ValueError:
        say("That's not a number, you clown. Try again.")
        return grab_number(*args)

def rng(start, end):
    return random.randint(start, end)

def maybe():
    return random.choice([True, False])

def wait(seconds):
    time.sleep(seconds)

def wipe():
    os.system('cls' if os.name == 'nt' else 'clear')

def stop():
    say("Goodbye, quitter.")
    exit()

def help():
    _real_print("\n--- 🐍 FUNFUNCS v1.0.0-beta.1 ---")
    _real_print('friendly reminder everything funfuncs can do has to be done woth funfuncs or it wont work, regular python is blocked for what we can do!')
    _real_print("say(...)         -> Display text")
    _real_print("get(...)         -> Ask for text")
    _real_print("grab_number(...) -> Ask for a NUMBER")
    _real_print("rng(s, e)        -> Get random number")
    _real_print("maybe()          -> Random True/False")
    _real_print("wait(s)          -> Pause execution")
    _real_print("wipe()           -> Clear terminal")
    _real_print("stop()           -> Kill the program")
    _real_print("----------------------------------\n")

_real_print("Funny-Funcs CBT Loaded. Use funfuncs.help() to see the list.")
