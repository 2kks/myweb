import json


def get_list_data_function():
	

	with open("the_lago.csv" ,"r" , encoding='utf-8' ) as f:
		the_list=f.readlines()

	return the_list[0:50]



def get_func(num):
	try:
		fnum=0
		endnum=10
		if num>=0:
			with open( "the_lago.csv" , "r"  , encoding='utf-8') as f:
				the_list=f.readlines()

			return the_list[int(num) : int(num)+endnum]
		else:
			return the_list[0:20]
	except Exception as e:
		raise e
	finally:
		pass
	

def get_urls_func():
	urls="/work/"
	urlslist=[]
	the_list=[ x for x in range( 0 , 500 ) ]
	list_1=the_list[::20]
	for x in list_1:
		urlslist.append( urls+str(x) )
	return urlslist



if __name__ == '__main__':
	pass

