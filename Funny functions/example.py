# dont just read also run it also dpnt take tjhis personal ig just in case. ofc this is all a joke
# ignore the as f im just lazy to type out funfuncs every time.
import funfuncs as f

f.help() 

f.say('thanks for checking this before using i hope.')

name = f.get('whats your name?')

def ask_age():
    age = f.grab_number('hi', name, 'how old are you?')
    
    if age > 100:
        f.say(age, '? stop lying unc, that age is ridiculous. try again.')
        return ask_age() # try again
    return age

age = ask_age()

if age >= 18:
    f.say(age, '? oh alright unc')
else:
    f.say('knowing python at', age, 'is quite impressive lil bro')
