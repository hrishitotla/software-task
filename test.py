Python 3.11.2 (v3.11.2:878ead1ac1, Feb  7 2023, 10:02:41) [Clang 13.0.0 (clang-1300.0.29.30)] on darwin
Type "help", "copyright", "credits" or "license()" for more information.
>>> import socket
>>> 
>>> serverIP='172.17.29.11'
>>> serverPORT=6000
>>> serveraddress=(serverIP, serverPORT)
>>> buffersize=1024
>>> UDPClientSocket=socket.socket(family=socket.AF_INET, type=socket.SOCK_DGRAM)
>>> message='Hi my name is Hrsihikesh Totla'
>>> bytestosend=str.encode(message)
