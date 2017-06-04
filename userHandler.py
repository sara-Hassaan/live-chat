from tornado import web,ioloop
import os
from pymongo import MongoClient


#handler of get all friends request
class userHandler(web.RequestHandler):

	def get(self):
		self.set_header("Access-Control-Allow-Origin", "*")
		self.set_header("Access-Control-Allow-Headers", "x-requested-with")
		self.set_header('Access-Control-Allow-Methods', 'POST, GET, OPTIONS')
		# GET THE URL DATA
		userid = self.get_query_arguments("userid")[0]

		#MAKE DATABASE CONNECTION
		client = MongoClient()
		db_livechat = client.livechat
		usercol = db_livechat.user

		#Query The DATA
		frienddata = usercol.find_one({"_id":int(userid) },{"friend":1,"_id":0})

		#Construct JSON to send back to Client and count up data
		dic_coll ={}
		count = 0

		for value in frienddata['friend']:

			#Prepare a query to get each friend data
			dic_rep = {}
			username = value[0]
			query = usercol.find_one({"_id": int(username)},{"userName":1,"image":1,"_id":1})

			#append data in json sent file
			dic_rep['_id'] = int(query['_id'])
			dic_rep['userName'] = query['userName']
			dic_rep['img'] = query['image']
			dic_rep['status'] = int(value[1])

			dic_coll[count] = dic_rep
			count += 1


		#Send the final result
		self.write(dic_coll)


	def post(self):
		self.set_header("Access-Control-Allow-Origin", "*")
		self.set_header("Access-Control-Allow-Headers", "x-requested-with")
		self.set_header('Access-Control-Allow-Methods', 'POST, GET, OPTIONS')
		# GET THE URL DATA
		userid = self.get_query_arguments("userid")[0]

		#MAKE DATABASE CONNECTION
		client = MongoClient()
		db_livechat = client.livechat
		usercol = db_livechat.user

		#Query The DATA
		frienddata = usercol.find_one({"_id":int(userid) },{"friend":1,"_id":0})

		#Construct JSON to send back to Client and count up data
		dic_coll ={}
		count = 0

		for value in frienddata['friend']:

			#Prepare a query to get each friend data
			dic_rep = {}
			username = value[0]
			query = usercol.find_one({"_id": int(username)},{"userName":1,"image":1,"_id":1})

			#append data in json sent file
			dic_rep['_id'] = int(query['_id'])
			dic_rep['userName'] = query['userName']
			dic_rep['img'] = query['image']
			dic_rep['status'] = int(value[1])

			dic_coll[count] = dic_rep
			count += 1

		#Send the final result
		self.write(dic_coll)



#handler of get all users request
class FriendsHandler(web.RequestHandler):

	def get(self):
		self.set_header("Access-Control-Allow-Origin", "*")
		self.set_header("Access-Control-Allow-Headers", "x-requested-with")
		self.set_header('Access-Control-Allow-Methods', 'POST, GET')

		# GET THE URL DATA
		userid = self.get_query_arguments("userid")[0]

		#MAKE DATABASE CONNECTION
		client = MongoClient()
		db_livechat = client.livechat
		usercol = db_livechat.user

		frnds = []
		n = 0
		#Query The DATA
		frienddata = usercol.find_one({"_id":int(userid) },{"friend":1,"_id":0})
		#return friends id and status frienddata['friend']:  [[2.0, 1.0], [1.0, 1.0], [14.0, 1.0]]
		print("frienddata: ",frienddata)

		for j in frienddata['friend']:
			j = int(j[0])	#j =  2
			print("j is : ", j)
			frnds.append(j)
			n += 1

	#	print("frnds = ", frnds)   #frnds =  [1, 2, 14]

		#find all users the output cursor so use list or for loop
		allusers = list(usercol.find( {"_id":{'$not':{'$in': frnds} }} ))

		#Construct JSON to send back to Client and count up data
		arrList = {}
		c = 0

		for i in allusers:
			arrList[c]  = i
			c += 1

		#Send the final result
		self.write(arrList)



#handler of accept request
class addHandler(web.RequestHandler):

	def get(self):
		self.set_header("Access-Control-Allow-Origin", "*")
		self.set_header("Access-Control-Allow-Headers", "x-requested-with")
		self.set_header('Access-Control-Allow-Methods', 'POST, GET, OPTIONS')
		# GET THE URL DATA
		userid = self.get_query_arguments("userid")[0]
		friendid = self.get_query_arguments("friendid")[0]

		print("userid = ", userid)
		print("friendid = ", friendid)

		#MAKE DATABASE CONNECTION
		client = MongoClient()
		db_livechat = client.livechat
		usercol = db_livechat.user

		#Query The DATA
		r = usercol.update({"_id": int(userid)},{"$push":{"friend":[int(friendid),-1]}})
		ret = usercol.update({"_id": int(friendid)},{"$push":{"friend":[int(userid),0]}})
		frienddata = usercol.find_one({"_id":int(userid) },{"friend":1,"_id":0})

		#Send the final result
		self.write(frienddata)



#handler of remove friend
class removeHandler(web.RequestHandler):

	def get(self):
		self.set_header("Access-Control-Allow-Origin", "*")
		self.set_header("Access-Control-Allow-Headers", "x-requested-with")
		self.set_header('Access-Control-Allow-Methods', 'POST, GET, OPTIONS')
		# GET THE URL DATA
		userid = self.get_query_arguments("userid")[0]
		friendid = self.get_query_arguments("friendid")[0]

		#MAKE DATABASE CONNECTION
		client = MongoClient()
		db_livechat = client.livechat
		usercol = db_livechat.user

		#Query The DATA
		frienddata1 = usercol.find_one({"_id":int(userid) },{"friend":1,"_id":0})
		frienddata2 = usercol.find_one({"_id":int(friendid) },{"friend":1,"_id":0})

		for i in frienddata1['friend']:
			getid = int(i[0])
			if getid == int(friendid):
				r0 = usercol.update({"_id": int(userid)},{"$pull":{"friend":[getid,1]}})

		for j in frienddata2['friend']:
			usr = int(j[0])
			if usr == int(userid):
				ret0 = usercol.update({"_id": int(friendid)},{"$pull":{"friend":[usr,1]}})

		#MAKE DATABASE CONNECTION
		# client = MongoClient()
		# db_livechat = client.livechat
		# groupcol = db_livechat.groups
		#
		# groupcol.remove({"groupName": "private"+friendid+userid})

		frienddata = usercol.find_one({"_id":int(userid) },{"friend":1,"_id":0})

		#Send the final result
		self.write(frienddata)


#handler of accept request
class updateHandler(web.RequestHandler):

	def get(self):
		self.set_header("Access-Control-Allow-Origin", "*")
		self.set_header("Access-Control-Allow-Headers", "x-requested-with")
		self.set_header('Access-Control-Allow-Methods', 'POST, GET, OPTIONS')

		# GET THE URL DATA
		userid = self.get_query_arguments("userid")[0]
		friendid = self.get_query_arguments("friendid")[0]

		#MAKE DATABASE CONNECTION
		client = MongoClient()
		db_livechat = client.livechat
		usercol = db_livechat.user

		#Query The DATA
		frienddata1 = usercol.find_one({"_id":int(userid) },{"friend":1,"_id":0})
		frienddata2 = usercol.find_one({"_id":int(friendid) },{"friend":1,"_id":0})


		print("frienddata1", frienddata1)


		for i in frienddata1['friend']:
			getid = int(i[0])
			print('getid', getid)
			if getid == int(friendid):   #[13.0, 0.0]
				r0 = usercol.update({"_id": int(userid)},{"$pull":{"friend":[getid,-1]}})
				r0 = usercol.update({"_id": int(userid)},{"$pull":{"friend":[getid,0]}})
				r = usercol.update({"_id": int(userid)},{"$push":{"friend":[getid,1]}})
				r = usercol.update({"_id": int(userid)},{"$pull":{"friend":[int(friendid),-1]}})



		for j in frienddata2['friend']:
			usr = int(j[0])
			if usr == int(userid):
				ret0 = usercol.update({"_id": int(friendid)},{"$pull":{"friend":[usr,0]}})
				ret0 = usercol.update({"_id": int(friendid)},{"$pull":{"friend":[usr,-1]}})
				ret = usercol.update({"_id": int(friendid)},{"$push":{"friend":[usr,1]}})
				r = usercol.update({"_id": int(friendid)},{"$pull":{"friend":[int(userid),0]}})



		print(r)

		print(r)
		#create group for chat
		#MAKE DATABASE CONNECTION
		client = MongoClient()
		db_livechat = client.livechat
		groupcol = db_livechat.groups


		max_id  = int(groupcol.find_one({"$query":{},"$orderby":{"_id":-1}},{"_id":1})["_id"])
		grpid = max_id +1
		groupcol.insert({'_id': grpid,'groupName':"private"+userid+friendid,'image':"/pic/Male-Avatar-Hair-icon.png",'file':"/chat/time7.txt",'groupmember':[[userid, 1],[friendid, 1]], 'groupType': "private"},{'ordered':'true'})


		frienddata = usercol.find_one({"_id":int(userid) },{"friend":1,"_id":0})
		#Send the final result
		self.write(frienddata)





app = web.Application([
	(r"/people", userHandler),
	(r"/allpeople", FriendsHandler),
	(r"/add", addHandler),
	(r"/update", updateHandler),
	(r"/remove", removeHandler)
	],

    static_path='../static',
    debug=True
    )

app.listen(2222)
ioloop.IOLoop.current().start()
