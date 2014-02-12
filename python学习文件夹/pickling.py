#!/user/bin/puthon
#Filename:picking.py

import cPickle as p

shoplistfile='shoplist.data'

shoplist=['apple','mango','carrot']
shoplist1=('apple','mama','lala')

f = file(shoplistfile,'w')

p.dump(shoplist,f)
p.dump(shoplist1,f)
f.close()

del shoplist
del shoplist1

f= file(shoplistfile)
storedlist1=p.load(f)
storedlist=p.load(f)


print storedlist
print storedlist1
