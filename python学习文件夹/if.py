#!/user/bin/python
# Filename: if.py
number=23
guess = int(raw_input('Enter an integer:'))

if guess == number:
    print 'congratulations'
elif guess < number:
    print 'higher'
else :
    print 'lower'
print 'Done'
