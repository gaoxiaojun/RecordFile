#!/user/bin/python
# Filename : using_dict.py
# 'ab' is short for 'a'address'b'ook
ab = {  'swaroop' : 'swaroopch@byteofpython.info',
        'larry'   : 'larry@wall.org',
        'matsumoto':'matz@ruby-lang.org',
        'spammer':'spammer@hotmail.com'
     
    }
print "swaroop's addressis %s" %ab['swaroop']

ab['guido']= 'guido@python.org'

del ab['larry']

print '\n there are %d contacts in the address-book\n'%len(ab)

for name,address in ab.items():
    print 'Conteat %s at %s' % (name,address)

if 'guidao' in ab:
    print "\nguidao's address is %s" %ab['guidao']
