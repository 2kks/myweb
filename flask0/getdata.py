import re
import json




class GetData_class(object):
	"""docstring for GetData_class"""
	def __init__(self):
		pass

	def get_json_fun(self , fname="lagou.json"):
		json_str=""
		with open( fname , "r" , encoding="utf-8" ) as f:
			json_str=f.read()
		thejson=json.loads( json_str )
		return thejson

	def get_data_list_fun(self , *keywordlist):
		pass


	def isdata_fun(self , keyword ):
		thejson=self.get_json_fun()
		data_list=[]
		for data_kv in thejson["RECORDS"]:
			list_str=[ x for x in data_kv.values() ]
			str_list="".join(list_str)
			if re.search( keyword , str_list , re.I ):
				data_list.append(data_kv)
			else :
				pass
		return data_list

	def anddata_fun( self , *keyword ):
		def get_re(keys):
			def the_func(thestr):
				re_0=re.compile("keys")
				if re_0.search(thestr):
					return 1
				else:
					return None
			return the_func

		flag=len( keyword )
		fun_list=[  get_re(keys) for keys in keyword  ]
		thejson=self.get_json_fun()
		data_list=[]

		# if flag==len( [ fun( str_0 ) for fun in fun_list ]  )

		for data_kv in thejson["RECORDS"] :
			list_str=[ x for x in data_kv.values() ]
			str_list="".join(list_str)
			if flag==len( [ fun( x ) for fun in fun_list  ]   ):
				data_list.append( data_kv )
			else:
				pass


		
		return data_list
















if __name__ == '__main__':
	data_obj=GetData_class()
	datalist=data_obj.isdata_fun( "上海")
	print(len(datalist))
