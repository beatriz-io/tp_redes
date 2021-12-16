#!/usr/bin/env python

import sys
import socket


def client(host, port):
    # Create a TCP/IP socket
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    # Connect the socket to the server
    server_address = (host, port)
    print("Connecting to %s port %s" % server_address)
    sock.connect(server_address)
    # Send data
    try:
        # Send data
        request = "GET http://127.0.0.1:5000/api/games/3 HTTP/1.1\r\nHost:" + \
            host + "\r\n\r\n"
        print("Sending %s" % request)
        sock.sendall(request.encode())

        response = sock.recv(4096)
        http_response = repr(response)
        http_response_len = len(http_response)

        print(response)
        print(http_response)
        print(http_response_len)
        print(str(response, 'utf-8'))

    except socket.error as e:
        print("Socket error: %s" % str(e))
    except Exception as e:
        print("Other exception: %s" % str(e))
    finally:
        print("Closing connection to the server")
        sock.close()


serverIp = sys.argv[1][0:sys.argv[1].find(':')]
serverPort = sys.argv[1][sys.argv[1].find(':')+1:]
analysis = sys.argv[2]

print(serverIp)
print(serverPort)

client(serverIp, int(serverPort))
