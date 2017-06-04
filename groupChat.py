from tornado import web,websocket,ioloop
from pymongo import *
import time
import json
import ast

client = MongoClient()
client = MongoClient()
db_livechat = client.livechat
collec_user = db_livechat.user
collec_group = db_livechat.groups
collec_stat= db_livechat.stat
global name
global uname
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
		print(msg)
		client_msg = ast.literal_eval(msg)
		msg_type = str(client_msg['type'])
		gid 	 = int(client_msg['gid'])
	#	name = str(client_msg['name'])
	#	uname=str(client_msg['uname'])
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

	def on_close(self):
		clients.remove(self);
		for c in clients:
			c.write_message("sorry guys!! someone died along the way !!")

class renderHandler(web.RequestHandler):
	def get(self):
		self.set_header("Access-Control-Allow-Origin", "*")
		self.set_header("Access-Control-Allow-Headers", "x-requested-with")
		self.set_header('Access-Control-Allow-Methods', 'POST, GET, OPTIONS')

		id = int(self.get_query_argument('id'))
		type= self.get_query_argument("type")

		name=collec_user.find_one({"_id":id},{"userName":1,"_id":0})
		name=name["userName"]
		print(name)
		print("type is")
		print(type)
		if type=="public":
		 	# find gid and then load user names
			gid=int(self.get_query_argument("gid"))
			uname="group"
			lOM= []
			gMem={}
			clientsId=collec_group.find_one({"_id":gid,"groupType":"public" },{"groupmember":1, "_id":0, 'file':1})
		 	# find gid and then load user names
			print("in if")
			print(clientsId)
			for arr in clientsId["groupmember"]:
				if arr[1]==1:
		 		#	LOM.append(arr[0])
					memNames=collec_user.find_one({"_id":arr[0] },{"userName":1, "_id":0})
		 		#	LOMnames.append(memNames["userName"])
		 			#print(arr[0])
					status=collec_stat.find_one({"userId":arr[0]},{"stat":1, "_id":0})
					status=status["stat"]
					print(status)
					if status==0:
						print("status")
		 			#	LOMstat.append(" :offline: ")
						gMem["stat"]=	" :offline: "
						gMem["name"]=memNames["userName"]
						print("members")
						print(gMem)
					elif status==1.0 and arr[0]!=id:
						print("status1")
						gMem["stat"]=	" :online: "
						gMem["name"]=memNames["userName"]
						#online members
					#	self.write(gMem["name"])
					elif status==1 and arr[0]==id:
						gMem["stat"]=	" :me: "
						gMem["name"]=memNames["userName"]
						print("the user")
					#lOM.append(gMem)
			self.render("templates/chat.html",id=id,type=type,gid=gid,uid='null',name=name,uname=uname, gMem=gMem)
		elif type =="private":
			print("in if")
		 	# find uid and then load user name and gid
			uid=int(self.get_query_argument("uid"))
			uname=collec_user.find_one({"_id":uid},{"userName":1,"_id":0})
			uname=uname["userName"]
#			client = MongoClient()
#			db_livechat = client.livechat
#			collec_group = db_livechat.groups
			#print(arr)
			#gid=collec_group.find_one({"groupmember":{"$or":[[[str(id),1],[str(uid),1]],[[str(uid),1],[str(id),1]]],{"groupType":"private"}},{"_id":1})
			gid=collec_group.find_one({"$or":[{"groupmember":[[str(id),1],[str(uid),1]]},{"groupmember":[[str(uid),1],[str(id),1]]}],'groupType':"private"},{"_id":1})
			print("gid", gid)
			print("uname", uname)
			# 	print(obj)
			print("redirecting")
			gid=gid['_id']
			#self.render("../templates/chat.html",id=id,type=type,uid=uid)
			self.render("templates/chat.html",id=id,type=type,uid=uid,gid=gid,name=name,uname=uname)


	#def get(self):


app = web.Application(
    [	(r"/",renderHandler),(r"/ws",WSHandler)  ],
    static_path='static',
    debug=True
    )

# should recieve both user name and group id
#class GetData(RequestHandler):


app.listen(4444)
ioloop.IOLoop.current().start()
