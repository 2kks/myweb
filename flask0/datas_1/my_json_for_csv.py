import json

my_json=""
my_list=[]
with open( "lagou.json" , "r"   ,  encoding='utf-8' ) as f:
       my_json=f.read()

obj=json.loads( my_json )

for the_one in obj["RECORDS"]:
       str_list=[ v  for  k , v in the_one.items()]
       str_1=",".join( str_list  )
       my_list.append(str_1+"\n")
       
with open("the_lago.csv" ,"w" , encoding='utf-8' ) as f:
       f.writelines(my_list)

#str_list=[ v  for  k , v in obj["RECORDS"][ 0 ].items()]
