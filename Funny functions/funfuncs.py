# funfuncs.py

def say(*args):
    print(*args)

def list(*args):
    # This just prints a list of things you give it
    for item in args:
        print(f"- {item}")
