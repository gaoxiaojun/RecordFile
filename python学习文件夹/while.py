#!/user/bin/python
# Filename:while.py

numner = 23
running= True
while running:
    guess = int(raw_input('Enter an integer :'))
    if guess == numner:
        running=False
    elif guess<numner:
        print 'higher'
    else:
        print 'lower'
else :
    print 'the over'
print 'done'
