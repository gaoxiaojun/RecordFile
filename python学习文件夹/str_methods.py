#!/user/bin/python
# Filename : str_methods.py
name = 'swaroop'
if name.startswith('swa'):
    print 'yes'
if 'a' in name:
    print 'yse'
if name.find('war') !=-1:
    print 'yres'
delimiter ='_*_'
mylist = ['breail', 'sdfa', 'fadsfa']
mytuple = ('breail', 'sdfa', 'fadsfa')
print delimiter.join(mylist)
print delimiter.join(mytuple)
