# -*- coding: utf-8 -*-

import socket
import threading

# ==================================================
# Example for interprocess communication
# ==================================================
#   
#   # Sender
#   # --------------------------
#   import communication as com
#
#   sender = Sender("localhost", 11000)
#   sender.send({'ID': 100, 'time':"2014-01-01"})
#
#
#   # Receiver:
#   # --------------------------
#   import ast
#   import communication as com
#   
#   def getIt(data):
#       obj = ast.literal_eval(data)
#       print "Received from ID={} at {}".format(obj['ID'], obj['time'])
#   
#   rec = com.Receiver("localhost", 11000, getIt)
#   rec.start()


class Sender():
    ''' This class is a simple wrapper class for an easy access to sending udp
    or tcp informations to a specified address and port over the network. 
    '''
    
    UDP = socket.SOCK_DGRAM
    TCP = socket.SOCK_STREAM

    def __init__(self, address, port, socktype=Sender.UDP):
        ''' Specifies an object with the given address and port, 
        but don't connect to the port

        arguments:
            address    -- IPv4 address (string)
            port       -- port (int)
            callback   -- function pointer for incoming routine
            socktype   -- socket type for UDP or TCP, e. g. Sender.UDP  
        '''

        self.address = address
        self.port = port
        self.sock = None
        self.type = socktype

        if not self.type == UDP and not self.type == TCP:
            raise ValueError("socket type have to be Sender.UDP or Sender.TCP")
        
    def send(self, message):
        ''' Sends the given message as a string to the specified address and port.

        arguments:
            message    -- information, maybe a list or dict
        '''
        if self.sock == None:
            sock = socket.socket(socket.AF_INET, self.type)
            
        sock.sendto(str(message), (self.address, self.port))
        

def send(address, port, message, socktype="UDP"):
    ''' This function is a quiet simple procedure to send a
    message as a string to the given address and port.
    After the sending process the socket will closed.

    arguments:
        address    -- IPv4 address (string)
        port       -- port (int)
        message    -- information, maybe a list or dict
        socktype   -- socket type for UDP or TCP, use "UDP" or "TCP"
    '''

    t = socket.SOCK_DGRAM
    if not socktype == "UDP":
        t = socket.SOCK_STREAM

    sock = socket.socket(socket.AF_INET, t)
    sock.sendto(str(message), (address, port))
    sock.close()
 

class Receiver(threading.Thread):
    ''' This class is build to receive data over a socket with out
    blocking the program. The waiting process for new data is running
    in a new thread. 
    
    The receiver waits for UDP packages. If the class gets incoming data
    a user specified callback function will called.
    '''

    UDP = socket.SOCK_DGRAM
    TCP = socket.SOCK_STREAM
    
    def __init__(self, address, port, callback, socktype=Receiver.UDP):
        '''
        arguments:
            address    -- IPv4 address (string)
            port       -- port (int)
            callback   -- function pointer for incoming routine
            socktype   -- socket type for UDP or TCP, e. g. Receiver.UDP 
        
        callback definition:
            def callback(data):
                # data is the incoming data as string        
        '''
        threading.Thread.__init__(self)
        self.address = address
        self.port = port
        self.sock = None
        self.running = False
        self.callback = callback
        self.type = socktype

        if not self.type == UDP and not self.type == TCP:
            raise ValueError("socket type have to be Receiver.UDP or Receiver.TCP")


    def stop(self):
        ''' Stops the listening process, closes the socket and stops the thread '''
        self.running = False

        try:
            self.sock.shutdown(socket.SHUT_RDWR)
            self.sock.close()
        except: 
            pass


    def start(self):
        ''' Starts the listening process '''
        self.running = True
        self.sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        self.sock.bind((self.address, self.port))
        threading.Thread.start(self)

    
    def run(self):
        
        while self.running:
            data, _ = self.sock.recvfrom(10240)
            if not self.callback == None:
                if data == None or data == '': continue
                self.callback(data)
