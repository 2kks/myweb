import re
import json

#keys=[ "city",   "education" ,  "positionName" ,  ]



class GetDataClass(object):
	
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
			if  re.search( findv


			 , x[key] , re.I   )  :
				datas.append( x )
			else:
				pass

		return datas

	def getdatas(  self , tag):
		keys=[ "city",   "education" ,  "positionName" ,  ]
		thetag=[ x.split("=")  for x in  tag.split("&") ]
		nums=int(thetag[1][1])*20
		key=thetag[0][1]
		theurl=tag.split("&")[0]


		if tag and thetag[0][0] in keys :
			datas=self.find_json_func( self.get_json_func() , thetag[0][0] , thetag[0][1]  )
			lens=len( datas )

		return lens , datas , nums , key , theurl

	def get_keys_function(self , city_v , positionName_v , education_v  ):
		keys_list=[ 'city' , 'positionName' , 'education' ]
		thejson=self.get_json_func()
		datas=[]
		for x in thejson["RECORDS"]:
			if re.search( city_v , x[keys_list[0]] , re.I ) and re.search( positionName_v , x[keys_list[1]] , re.I ) and re.search( education_v , x[keys_list[2]] , re.I ):
				datas.append( x )
			else:
				pass

		return datas




def getlist():
	list_4=[ "全国:" , "北京" , "上海" , "深圳" , "广州" , "杭州", "成都", "武汉" , "长沙"  , "西安" , "南京"  ]

	list_0=[ "后端开发:" , "Go", "c" , "php" , "java"   , "python" ]
	list_1=[ "移动开发:" ,"HTML5" , "android" , "ios" , "wp"  ]
	list_2=[ "前端开发:" , "html5" , "JavaScript" , "Flash" , "U3D"  , "web" , "UI"  ]
	list_3=[ "学历要求:", "大专" , "本科" , "硕士" , "博士" ]
	datalist_01=[ list_4 ]
	datalist_02=[list_3]
	datalist_3=[ list_0 , list_1 , list_2  ]
	return  datalist_01 , datalist_02 , datalist_3


# "city": , "positionName": , "education":


if __name__ == '__main__':
	pass

	


