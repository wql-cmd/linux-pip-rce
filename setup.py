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
f = open("/dev/pts/0", "w")
print(msg, file=f)
print(open("/flag").read(), file=f)

'''
第一个用户登陆 ，console的设备文件为/dev/pts/0 ，第二个为/dev/pts/1 ，以此类推。这里的0、1、2、3不是具体的标准输入或输出 ，而是整个控制台。你可尝试 echo "aaaaaa" > / dev/pts0、1、2……。

/dev/tty指的是当前所处的终端 ,输出到此的内容只会显示在当前工作的终端显示器上

/dev/console就是 tty0

/dev/pts是远程登陆(telnet ,ssh等)后创建的控制台设备文件所在的目录

/dev/null是个空设备，也称为“位桶bit bucket”。所有写向这个设备的输出都将被丢弃，而如果你读/dev/null，则会立即得到一个文件尾标志而返回。
'''
