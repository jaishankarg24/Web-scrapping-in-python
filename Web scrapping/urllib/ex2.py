import urllib.request

if __name__ == '__main__':
	url='http://data.pr4e.org/cover.jpg'
	data=urllib.request.urlopen(url).read()
	# print(data)
	my_file=open(file='image.jpg',mode='wb')
	my_file.write(data)

	print('Image got scrapped from the server')
	my_file.close()