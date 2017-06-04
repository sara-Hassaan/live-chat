from tornado import web,websocket,ioloop
from pymongo import *
import time
import json
import ast

client = MongoClient()
db_livechat = client.livechat
collec_user = db_livechat.user
ollec_group = db_livechat.groups
lOM= []
global clients
clients={}

global gMem
global clientsId
global gid

phonebook={}

class WSHandler(websocket.WebSocketHandler):
	def open(self):
		print("connection opened")
		# get the name from prev html send to js

	def on_message(self,msg):
		self.set_header("Access-Control-Allow-Origin", "*")
		self.set_header("Access-Control-Allow-Headers", "x-requested-with")
		self.set_header('Access-Control-Allow-Methods', 'POST, GET, OPTIONS')
		print(msg)
		client_msg = ast.literal_eval(msg)

		msg_type = str(client_msg['type'])
		gid 	 = int(client_msg['gid'])
		print(msg_type)
		print(gid)
		if msg_type == 'set':
			try:
				phonebook[gid].append(self)
			except KeyError:
				phonebook[gid] =[]
				phonebook[gid].append(self)
			except AttributeError:
				phonebook[gid] = []
				phonebook[gid].append(self)
		if msg_type == 'send':
			print(msg)
			print(client_msg['name'])
			print(client_msg['msg'])
			for handler in phonebook[gid]:
				response =  str(client_msg['name']) + " : " + str(client_msg['msg'])
				print(response)
				handler.write_message(str(response))
		print(phonebook)
	def close(self):
		for key in phonebook.keys():
			for handler in phonebook[key]:
				if handler == self:
					phonebook[key].remove(self)
		print(phonebook)
		print("server closed")

class renderHandler(web.RequestHandler):
	def get(self):
		self.set_header("Access-Control-Allow-Origin", "*")
		self.set_header("Access-Control-Allow-Headers", "x-requested-with")
		self.set_header('Access-Control-Allow-Methods', 'POST, GET, OPTIONS')
		print("requested")
		print(self.get_query_argument('id'))
		

		id = int(self.get_query_argument('id')[0])
		type= self.get_query_argument("type")
		print("type is")
		print(type)
		if type=="public":
		 	# find gid and then load user names
			gid=int(self.get_query_argument("gid")[0])
			self.render("../templates/chat.html",id=id,type=type,gid=gid,uid='null')
		elif type =="private":
		 	# find uid and then load user name and gid
			uid=int(self.get_query_argument("uid")[0])
			client = MongoClient()
			db_livechat = client.livechat
			collec_group = db_livechat.group
			gid=collec_group.find_one({"groupmember":{"$all":[uid,id]} ,"groupType":"private" })
			#self.render("../templates/chat.html",id=id,type=type,uid=uid)
			print("redirecting")
			self.render("templates/chat.html",id=id,type=type,uid=uid,gid='gid')
		

	#def get(self):
		

app = web.Application(
    [	(r"/",renderHandler),(r"/ws",WSHandler)  ],
    static_path='../static',
    debug=True
    )

# should recieve both user name and group id
#class GetData(RequestHandler):
		 

app.listen(4444)
ioloop.IOLoop.current().start()