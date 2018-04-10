import re
import json

#keys=[ "city",   "education" ,  "positionName" ,  ]



class GetDataClass(object):
	"""docstring for GETDataClass"""
	def __init__(self,):
		pass
	
	def get_json_func( self , fname="lagou.json" ):
		strjson=""
		with open( fname , "r" , encoding="utf-8" ) as f:
			strjson=f.read()

		thejson = json.loads( strjson )

		return thejson

	def find_json_func(  self , thejson , key , findv ):
		datas=[]
		for x in thejson["RECORDS"]:
			if  re.search( findkey , x[key] , re.I   )  :
				datas.append( x )
			else:
				pass

		return datas

	def getdatas(  self , tag):
		keys=[ "city",   "education" ,  "positionName" ,  ]
		thetag=[ x.split("=")  for x in  tag.split("&") ]
		nums=int(thetag[1][1])*20
		key=thetag[0][1]
		theurl=thetag.split("&")[0]


		if tag and thetag[0][0] in keys :
			datas=self.find_json_func( self.get_json_func() , thetag[0][0] , thetag[0][1]  )
			lens=len( datas )

		return lens , datas , nums , key , theurl








if __name__ == '__main__':
	pass
	


