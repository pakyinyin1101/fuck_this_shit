#!/usr/bin/python

import Cookie
import datetime
import random
import os
import cgi
import cgitb
import subprocess
import sys
import sqlite3
from os import listdir, getcwd

print"Content-type:text/html\n\n"
print

cgitb.enable()

print'<html><body>'

def create_login_database(db_file):
	db_not_yet_create = not os.path.exists(db_file)
	conn = sqlite3.connect(db_file)
	if db_not_yet_create:
		print'Create a new login table!'
		sql='''create table if not exists LOGINDATA
		(USERID INTEGER PRIMARY KEY AUTOINCREMENT,
		USERNAME CHAR(20),
		PASSWORD CHAR(20));'''
		conn.execute(sql)
	else:
		print'login table exist'
	return conn

connection=create_login_database('login_db.sqite')
form=cgi.FieldStorage()
try:
	sendusername=form.getvalue('username',None)
except IndexError:
	sendusername=None

print sendusername

try:
	sendpassword=form.getvalue('password',None)
except IndexError:
	sendpassword=None

print sendpassword

try:
	sendrepassword=form.getvalue('repassword',None)
except IndexError:
	sendrepassword=None

print sendrepassword

if(sendpassword!= sendrepassword):
	print'password is not equal to sendrepassword!<br/>'
if(sendusername == None):
	print'Empty username!<br/>' 
	
if(sendpassword == None):
	print'Empty password!<br/>'
	
if(sendrepassword == None):
	print'Empty retype password!<br/>'

if(sendusername ==None or sendrepassword==None or sendpassword== None or sendpassword!= sendrepassword):
	print'''<form action="create.py" method="post">
	 	Please fill in again!
	 	Go to<input type ="submit" value="register" name="submit" />
		</form>'''
#else:
	#check_login
print'success'

print'</body></html>'
