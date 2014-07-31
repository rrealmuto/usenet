import sqlite3
from nntplib import NNTP

group = 'alt.binaries.movies.x264'
chunk_size = 100000
sql = sqlite3.connect('usenet.db')

print "About to start dumping articles from " + group
serv = NNTP('news.astraweb.com', 119, 'arealmuto', 'stock1114')

resp = serv.group(group)
count = int(resp[1])
first = int(resp[2])
last = int(resp[3])

print "There are " + str(count) + " articles to get"
print "First: " + str(first)
print "Last: " + str(last)
print "Using chunks size of: " + str(chunk_size)
print "It should take " + str(count/chunk_size) + " requests to finish"

id = int(first)

i = 0
master_list = []
while id < last:
	print str(i) +": Getting id's " + str(id) + " - " + str(id + chunk_size)
	resp, list = serv.xover(str(id), str(id+ chunk_size))
	print "Done fetching"
	print "Adding to master list"
	for line in list:
		article = (line[0], line[1], line[2], line[3], line[4])
		master_list.append(article)			
	id += chunk_size + 1
	i += 1
