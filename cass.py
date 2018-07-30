import random
import time
import threading
from cassandra.cluster import Cluster

cluster = Cluster(['127.0.0.1'])
session = cluster.connect()
session.execute("use userid_nickname")

f = open ('userid+nickname.csv', 'r')
users = []
names = []
for lines in f:
        u, n = lines.split("\t")
        users.append(u)
        names.append(n)
count = 0
while (count < 60):
        since = time.time()
        for i in range(len(users)):
                newuser = int(users[i]) * 100 + count
                session.execute("insert into users(id, name) values(%s, %s);", (int(userid), nickname,))
        count += 1
        print str(count) + ": " + str(time.time() - since)


userfile = open('userids.txt', 'r')
u = []
for lines in userfile:
	u.append(int(lines))
ran = random.sample(u, 100000)

since = time.time()
for lines in ran:
		row=session.execute("SELECT * FROM users where id = %s", (str(lines),))
		#print row[0].name
print time.time() - since

userfile = open('userids.txt', 'r')
u = []
for lines in userfile:
	u.append(int(lines))
ran = random.sample(u, 10000)
print time.time()

class myThread (threading.Thread):
	def __init__(self, threadID, name):
		threading.Thread.__init__(self)
		self.threadID = threadID
		self.name = name
	def run(self):
		print "Starting " + self.name
		get_name(self.name, ran)
		print "Exiting " + self.name
		print time.time()

def get_name(threadName,rand):
	for lines in rand:
		row=session.execute("SELECT * FROM users where id = %s", (str(lines),))

thread1 = myThread(1, "Thread-1")
thread2 = myThread(2, "Thread-2")
thread3 = myThread(3, "Thread-3")
thread4 = myThread(4, "Thread-4")
thread5 = myThread(5, "Thread-5")
thread6 = myThread(6, "Thread-6")
thread7 = myThread(7, "Thread-7")
thread8 = myThread(8, "Thread-8")
thread9 = myThread(9, "Thread-9")
thread10 = myThread(10, "Thread-10")
 
thread1.start()
thread2.start()
thread3.start()
thread4.start()
thread5.start()
thread6.start()
thread7.start()
thread8.start()
thread9.start()
thread10.start()