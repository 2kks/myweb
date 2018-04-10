from flask import Flask
from flask import render_template
from flask import request
from flask import make_response
from flask.ext.bootstrap import Bootstrap 
from flask.ext.sqlalchemy import SQLAlchemy
import os

import GetJson


app=Flask(__name__)

bootstrap=Bootstrap(app)

# covers 
# return redirect("http://www.example.com")
 






@app.route( "/xingwei" )
def the_function():
	return render_template( "xingwei.html" )

@app.route('/zhufang')
@app.route('/zhufang/<name>')
def welcome(name=None):
	return render_template("zhufang.html" , name=name)


@app.route('/user/<name>')
def function(name):

	return render_template( "user.html" , name=name )


@app.route('/login', methods=[  'POST'])
def login():
    if request.form['username']=='1482419163@qq.com' and request.form['password']=='123456':
        return redirect("/job/city=北京&num=1")
    return '<h2>bad username or password</h2>'



@app.route('/')
def index():
	return  render_template("boots1.html" ,)



@app.route( "/job/<tag>" )
def show_func(tag=None):
	#tag=="city=北京&num=1"
	keys=[ "city",   "education" ,  "positionName" ,  ]
	theclass=GetJson.GetDataClass()
	datalist_01 , datalist_02 , datalist_3=GetJson.getlist()

	
	lens , datas , nums , key , theurl =theclass.getdatas( tag )

	return render_template( "mywork.html"  , get_dict=datas[nums:nums+50]  , lens=lens  , key=key , theurl=theurl , datalist_01=datalist_01 ,datalist_02=datalist_02 , datalist_3=datalist_3 )




@app.route("/datas", methods=['POST'])
def signin():
	lists=[ request.form['city'] , request.form['positionName' ]  ,  request.form['education']  ] 
	thedatas=GetJson.GetDataClass()
	datas=thedatas.get_keys_function( lists[0]  , lists[1] , lists[2] )
	if  lists and datas :
		return  render_template( "show_datas.html"  ,  get_dict=datas ,  lists=lists )
	else :
		return "<h1>无效</h1>"


if __name__ == '__main__':
	#app.run(host='0.0.0.0')
	app.run(debug=True) 

