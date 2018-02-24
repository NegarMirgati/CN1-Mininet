import socket
import datetime
 
while True:
    print " Enter IP address : "
    TCP_IP = raw_input()
    TCP_PORT = 8000

    for i in range(2) :
        if i < 1 :
            BUFFER_SIZE = 1024
            with open('file1.txt', 'r') as content_file:
                MESSAGE = content_file.read()
        else :
            BUFFER_SIZE = 1024 * 10
            with open('file2.txt', 'r') as content_file:
                MESSAGE = content_file.read()

     
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        s.connect((TCP_IP, TCP_PORT))
        s.send(MESSAGE)
        start = datetime.datetime.now()
        data = s.recv(BUFFER_SIZE)
        end = datetime.datetime.now()
        diff = end - start
        elapsed_ms = (diff.days * 86400000) + (diff.seconds * 1000) + (diff.microseconds / 1000)
        if i < 1 :
            elapsed_2 = elapsed_ms
        else :
            elapsed_1 = elapsed_ms
        s.close()
 
        print "packet time : ", elapsed_ms

    print "difference : ", elapsed_2 - elapsed_1