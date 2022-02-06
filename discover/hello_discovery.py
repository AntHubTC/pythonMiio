# import logging
# import miio
#
# logging.basicConfig(level=logging.DEBUG)
#
# if __name__ == '__main__':
#     mdns = miio.Discovery().discover_mdns(timeout=2000)
#     print(mdns)

#-*-coding:utf8-*-
import codecs
import socket
from miio.protocol import Message

def sendHelloByte(ip, port = 54321):
    global data
    # hello数据包，参考mihome protocol协议https://github.com/OpenMiHome/mihome-binary-protocol/blob/master/doc/PROTOCOL.md
    hello_bytes = bytes.fromhex('21310020ffffffffffffffffffffffffffffffffffffffffffffffffffffffff')
    s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    s.sendto(hello_bytes, (ip, port))  # 插座ip，端口54321
    return s.recvfrom(1024)

def getDeviceToken(ip, port = 54321):
    data, addr = sendHelloByte(ip, port)
    msg = Message.parse(data)
    print(msg)
    return codecs.encode(msg.checksum, 'hex')


token = getDeviceToken("192.168.1.9", 54321)
# 如果返回 token: b'ffffffffffffffffffffffffffffffff'，表示没有获取到
print('token:', token)