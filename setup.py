msg = r"""
                              _ 
                             | |
 _ ____      ___ __   ___  __| |
| '_ \ \ /\ / / '_ \ / _ \/ _` |
| |_) \ V  V /| | | |  __/ (_| |
| .__/ \_/\_/ |_| |_|\___|\__,_|
| |                             
|_|             

"""
'''
f = open("/dev/tty", "w")
print(msg, file=f)
print(open("/etc/passwd").read(), file=f)'''
import os
print(os.system('cat /etc/passwd'))
