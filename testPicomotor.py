# -*- coding: utf-8 -*-
"""
Created on Thu Jun 11 10:56:03 2015

@author: BEC
"""

#!/usr/bin/env python
 
import socket
import time
 
TCP_IP = '172.16.2.18'
TCP_PORT = 23
BUFFER_SIZE = 1024
MOVE_FORWARD_MESSAGE = '1PR100'
MOVE_REVERSE_MESSAGE = '2PR-500'
#STOP_MESSAGE = 'STO'
#SET_FAST_MESSAGE = 'VEL A1 0=2000'
#SET_SLOW_MESSAGE = 'VEL A1 0=250'
## does the same job:
#SET_FAST_MESSAGE = 'RES COARSE'
#SET_SLOW_MESSAGE = 'RES FINE'
 
def send(message):
    print message
    s.send(message + '\n')
    time.sleep(0.005)
 
def receive():
    data = s.recv(BUFFER_SIZE)
    time.sleep(0.005)
    return data
 
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect((TCP_IP, TCP_PORT))
time.sleep(0.1)
 
print receive()
 
#send(SET_FAST_MESSAGE)
#print receive()
 
#send(MOVE_FORWARD_MESSAGE)
#time.sleep(0.5)
#print receive()
#time.sleep(1)
 
#send(STOP_MESSAGE)
#print receive()
#time.sleep(1)
 
send(MOVE_REVERSE_MESSAGE)
#time.sleep(0.5)
#print receive()
time.sleep(1)
 
#send(STOP_MESSAGE)
#print receive()
#time.sleep(1)
# 
#send(SET_SLOW_MESSAGE)
#print receive()
 
#send(MOVE_FORWARD_MESSAGE)
#time.sleep(0.5)
#print receive()
#time.sleep(1)
 
#send(STOP_MESSAGE)
#print receive()
#time.sleep(1)
 
 
s.close() 