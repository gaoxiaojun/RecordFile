# -*- coding: cp936 -*-
#Filename:backup_ver1.py

import os
import time

source = [r'C:\Users\xiaxiaoyu\Desktop\pythonѧϰ�ļ���']
target_dir = r'C:\Users\xiaxiaoyu\Desktop\pythonѧϰ�ļ���/'
target = target_dir + time.strftime('%Y%m%d%H%M%S')+'.zip'
zip_command="zip -qr '%s' %s" %(target, source)

if os.system(zip_command)==0 :
    print 'successful',target
else :
    print 'failed'
