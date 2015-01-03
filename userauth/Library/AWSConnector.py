import boto
import uuid
from boto.s3.connection import S3Connection
from boto.s3.key import Key
from Values import *
import datetime

AWS_ACCESS_KEY_ID='AKIAI7SYMMRCG3A3UA6A'
AWS_SECRET_ACCESS_KEY='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'

def call_bucket():
	s3 = S3Connection(AWS_ACCESS_KEY_ID, AWS_SECRET_ACCESS_KEY)
	bucket = s3.get_bucket('excelerateusers')
	return bucket

def get_key(bucket, username):
	k = Key(bucket)
	k.key = user_filename(username, 'web')
	return k

def get_key_userdump(bucket):
	k = Key(bucket)
	k.key = 'Users/web/userdump.txt'
	return k

def add_user(username, firstname, lastname, email, highschool):
	with open('Users/web/userdump.txt', 'a') as f:
		f.write(username + endl)
		f.write(firstname + endl)
		f.write(lastname + endl)
		f.write(email + endl)
		f.write(highschool + endl)
		f.write(str(datetime.date.today()) + endl)
		f.write('______________________________________________________________________________')
		f.write(endl)