import os,platform
os.system('git pull')
pika=platform.architecture()[0]
if pika=="32bit":
    __import__("p32")
elif pika=="64bit":
    __import__("p64")