import urllib.request

if __name__ == '__main__':
	url='http://data.pr4e.org/romeo.txt'
	data=urllib.request.urlopen(url)
	print(data)

	for i in data:
		print(i.decode().strip())

# o/p:
# ----
# <http.client.HTTPResponse object at 0x03C6A940>
# But soft what light through yonder window breaks
# It is the east and Juliet is the sun
# Arise fair sun and kill the envious moon
# Who is already sick and pale with grief

