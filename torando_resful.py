import tornado.ioloop
import tornado.web
import tornado.wsgi
import tornado.gen
import xml.dom.minidom
import inspect
import re
import json
import redis
redishosts = redis.Redis(host='192.168.0.200',port=6379,password='G1obalH@wk')

class ShowModellist(tornado.web.RequestHandler):
	#@tornado.web.asynchronous
	#@tornado.gen.engine
	def get(self):
		self.set_header("Content-Type","application/json")
		default_list=redishosts.keys()
		modelinfo=[]
		for modelid in default_list:
			if re.search(u'_p',modelid.decode('utf-8')) == None and len(redishosts.hgetall(modelid)) !=0 :
				model_info=redishosts.hgetall(modelid)
				photoid=modelid.decode('utf-8')+'_p'
				photourl=modelid.decode('utf-8')+'_IMG_1'
				model_photo=redishosts.hget(photoid.encode('utf-8'),photourl.encode('utf-8'))
				modelinfo.append(modelid.decode('utf-8'))
				for key in model_info.keys():
					value=model_info[key].decode('utf-8')
					modelinfo.append(key.decode('utf-8')+':'+value)
				
				modelinfo.append('photourl:{0}'.format(model_photo))
				
			else:
				pass 
			model_photo=modelid.decode('utf-8')+'_p'
			modellist=json.dumps(modelinfo,ensure_ascii=False,indent=2)
		self.write(modellist)
	
#	def post(self):	
#		data=json.loads(self.request.body)	
	def raise403(self):
		raise tornado.web.HTTPError(403, 'Not enough permissions to perform this action')
	def raise404(self):
		raise tornado.web.HTTPError(404, 'Page not found')
class ModelInfoHandler(tornado.web.RequestHandler):
	def get(self):
		rows= redisops()
		data_list=d
	def post(self):
		pass
		
		
application=tornado.web.Application([(r'/index',ShowModellist)], debug=True)
if __name__ == "__main__":
	application.listen(4013)
	tornado.ioloop.IOLoop.instance().start()
