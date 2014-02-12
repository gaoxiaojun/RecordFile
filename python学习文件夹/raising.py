#!/user/bin/python
# Filename:raising.py

class shortinputexception(Exception):
    '''A user_defined exception class'''
    def __init__(self,length,atleast):
        Exception.__init__(self)
        self.length=length
        self.atleast=atleast

try:
    s=raw_input('Enter something->')
    if len(s)<3:
        raise shortinputexception(len(s),3)
except shortinputexception,x:
    print 'shortinputexception:the input was of length %d,\
           was excepting at least %d' %(x.length,x.atleast)
else:
    print 'no exception was raised'
