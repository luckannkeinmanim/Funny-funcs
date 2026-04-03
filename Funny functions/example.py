import funfuncs as f

f.help() 

f.say('thanks for checking this before using i hope.')

# Get the name
name = f.get('whats your name? ')

# Get the age and turn it into a number (int)
# We use an f-string to combine the name into the question
age_input = f.get(f'hi {name}, how old are you? ')
age = int(age_input)

if age >= 18:
    f.say(age, '? oh alright unc')
else:
    f.say('knowing python at', age, 'is quite impressive lil bro')
