from tornado import web,ioloop
import os


from tornado import web,ioloop
import os
#from handlers.ajax import APIHandler

class MainHandler(web.RequestHandler):
    def get(self):
    	self.set_header("Access-Control-Allow-Origin", "*")
    	self.set_header("Access-Control-Allow-Headers", "x-requested-with")
    	self.set_header('Access-Control-Allow-Methods', 'POST, GET, OPTIONS')

    	userid = self.get_query_arguments("userid")[0]
    	username = self.get_query_arguments("username")[0]
    	imgeurl = self.get_query_arguments("imgeurl")[0]
    	self.render("templates/index.html",userid=userid,username=username,imgeurl=imgeurl)



app = web.Application(
    [ (r"/", MainHandler) ],
    static_path='static',
    debug=True
    )

app.listen(8888)
ioloop.IOLoop.current().start()
