import builtins
import random
import time
import os

# --- THE TRAP (Do not move this!) ---
_real_print = builtins.print
_real_input = builtins.input

def scream(*args, **kwargs):
    raise Exception("USE THE ENGLISH WAY! Check funfuncs.help() you moron!")

# Kidnapping the standard functions
builtins.print = scream
builtins.input = scream

# --- THE 'FUNNY' FUNCTIONS ---

def say(*args):
    """The civilized way to show text."""
    _real_print(*args)

def get(prompt):
    """The only way to ask a question."""
    return _real_input(prompt)

def rng(start, end):
    """Generates a random number between two points."""
    return random.randint(start, end)

def maybe():
    """Let the computer decide your fate (True or False)."""
    return random.choice([True, False])

def wait(seconds):
    """Make the code take a nap."""
    time.sleep(seconds)

def wipe():
    """Clear the screen because it's messy."""
    os.system('cls' if os.name == 'nt' else 'clear')

def table(*items):
    """Creates a list variable because 'list' is too techy."""
    return list(items)

def help():
    """The only way to know what you're doing."""
    _real_print("\n--- FUNFUNCS OFFICIAL GUIDE ---")
    _real_print("say(...)   -> Use this instead of print()")
    _real_print("get(...)   -> Use this instead of input()")
    _real_print("rng(s, e)  -> Get a random number")
    _real_print("maybe()    -> Returns True or False randomly")
    _real_print("wait(s)    -> Pause for X seconds")
    _real_print("wipe()     -> Clears the terminal")
    _real_print("table(...) -> Saves a list to a variable")
    _real_print("--------------------------------\n")

# A little secret: Whenever they import it, tell them how to find help
_real_print("Funny-Funcs Loaded. If everything breaks, run funfuncs.help()")
