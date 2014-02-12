#!/user/bin/python
# Filename:using_file.py

poem='''programming is fun when the worik is done  if you wanan make you work also fun: use python!'''

f= file('poem.txt','w')
f.write(poem)
f.close()

f=file('poem.txt')

while True:
    line = f.readline()
    if len(line)==0:
      break;
    print line,
f.close()
