import socket
if __name__ == '__main__':
	try:
		client_socket=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
		print('socket got created at the client end')

		host='data.pr4e.org'
		port_no=80
		address=(host,port_no)
		client_socket.connect(address)
		print(f'client got connected to the server whose ip address:{host} running on the port no:{port_no}')

		data='GET http://data.pr4e.org/romeo.txt HTTP/1.0\r\n\r\n'
		client_socket.send(data.encode())

		#to collect the response sent from the server
		bufsize=1024
		recv_data=client_socket.recv(bufsize).decode()
		print(recv_data)

	except socket.error as msg:
		print(f'The cause of the exception is : {msg}')
	finally:
		client_socket.close()
		print('socket got closed at the client end')

# o/p:
# ----
# socket got created at the client end
# client got connected to the server whose ip address:data.pr4e.org running on the port no:80
# HTTP/1.1 200 OK

# Date: Mon, 22 Jun 2020 11:30:10 GMT

# Server: Apache/2.4.18 (Ubuntu)

# Last-Modified: Sat, 13 May 2017 11:22:22 GMT

# ETag: "a7-54f6609245537"

# Accept-Ranges: bytes

# Content-Length: 167

# Cache-Control: max-age=0, no-cache, no-store, must-revalidate

# Pragma: no-cache

# Expires: Wed, 11 Jan 1984 05:00:00 GMT

# Connection: close

# Content-Type: text/plain



# But soft what light through yonder window breaks
# It is the east and Juliet is the sun
# Arise fair sun and kill the envious moon
# Who is already sick and pale with grief

# socket got closed at the client end



