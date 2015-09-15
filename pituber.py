qual='360p' #Quality Settings
form='mp4'  #Format
dest='/home/pi/'  #Destination
import pafy  #Dependency
with open('url.txt') as f:
	content=f.readlines()
content=[x.strip('\n') for x in content]
print content #if required to debug
for url in content:
	mylink=''
	video=pafy.new(url)
	print "Intialised "+video.title
	print "Quality " + qual
	print "form "+form
	s=video.streams
	for x in s:
		if(x.extension==form):
			if(x.resolution.find(qual)):
				mylink=x
				break	
				#print x
	print "The file size is " + str(mylink.get_filesize())
	mylink.download(filepath=dest)

