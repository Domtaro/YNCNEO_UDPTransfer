#=====================================================
# YNC_NEO UDP Transfer Plugin
# (c) Copyright 2024 by Domtaro
# Licensed under the LGPL-3.0
#=====================================================
# * Transfer the SR result to any UDP server
#=====================================================

import socket
port_no = 25555 # change a port if you need
server_adress = ('127.0.0.1', port_no)

#=====================================================
# Post Recognition Process
#=====================================================
def PostRecognition(Message):
    if (Message["TextFixed"] and Message["UpdateTranslation"]):
        my_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        sent_length = my_socket.sendto(Message["Text"].encode(encoding='utf-8', errors='replace'), server_adress)
        my_socket.close()
