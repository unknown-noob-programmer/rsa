#-------------------------------------#
#-----------AAHIL---CODING
import os, time, platform
os.system("cd $HOME")
try:
    import requests
except ImportError:
    os.system("pip2 install requests")
    os.syatem("pip install requests")
rana=platform.architecture()[0]
if rana=="64bit":
    import rsa64
    rsa64.security()
elif rana=="32bit":
    import rsa32
    rsa32.security()
#-------------------------------------#
