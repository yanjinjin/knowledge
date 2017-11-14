#coding=utf-8
import time,datetime
import sqlite3 as db
import math
import hashlib
import os

class Model:
    def __init__(self):
	self.db = os.path.join(os.path.dirname(__file__),"video.db")
	self.table_user="user"
	self.table_product = "product"
	self.admin = "admin"
        if os.path.exists(self.db):
            self.conn = db.connect(self.db, check_same_thread=True)
        else:
            self.conn = db.connect(self.db, check_same_thread=True)
	    sql = "create table %s(id integer primary key,username text,passwd text, verifier int,date text,domain1 text,domain2 text) "%(self.table_user)
            self.conn.execute(""+sql+"")
            print 'create db %s'%(self.table_user)
	    sql = "insert into %s (username,passwd,verifier,date) values ('%s', '%s', %d,'%s')"%(self.table_user, self.admin, "admin", 1, datetime.datetime.now())
            print sql
	    self.conn.execute(""+sql+"")
            sql = "create table %s(id integer primary key, name text, detail text,username text,file text, date text,domain1 text, domain2 text) "%(self.table_product)
            self.conn.execute(""+sql+"")
            print 'create db %s'%(self.table_product)    
	    
	    self.conn.commit()

        self.cu = self.conn.cursor()
    
    def select_from_user_for_admin(self):
        sql = "select id , username, date from %s order by date DESC"%(self.table_user)
        self.cu.execute(""+sql+"")
        return self.cu.fetchall()

    def select_verify_from_user_by_username(self,username):
        sql = "select id from %s where username ='%s' and verifier =1 limit 1"%(self.table_user,username)
        self.cu.execute("select id from user where username =? and verifier =? limit 1" , (username,1))
        res = self.cu.fetchall()
        for i in res:
            return i[0]
        return None

    def select_rowcount_from_user_by_login(self,username,passwd):
        sql = "select id from %s where username ='%s' and passwd = '%s'"%(self.table_user,username,passwd)
        print sql
        self.cu.execute("select id from user where username =? and passwd = ?",(username,passwd))
        res = self.cu.fetchall()
        rowcount=0
        for i in res:
            rowcount = rowcount + 1
        return rowcount

    def select_rowcount_from_user(self):
        sql = "select id from %s"%(self.table_user)
        self.cu.execute(""+sql+"")
        res = self.cu.fetchall()
        rowcount=0
        for i in res:
            rowcount = rowcount + 1
        return rowcount

    def select_userid_from_user_by_username(self,username):
        sql = "select id from %s where username ='%s' limit 1"%(self.table_user,username)
        self.cu.execute("select id from user where username =? limit 1" , (username,))
        res = self.cu.fetchall()
        for i in res:
            return i[0]
        return None

    def insert_into_user(self,username,passwd):
        sql = "insert into %s (username,passwd,verifier,date) values ('%s', '%s', %d, '%s')"%(self.table_user, username, passwd, 0,datetime.datetime.now())
        print sql
        self.conn.execute("insert into user (username,passwd,verifier,date) values (?, ?, ?, ?)" , (username, passwd, 0,datetime.datetime.now()))
        self.conn.commit()

    def update_verify_from_user_by_username(self,username):
        sql = "update %s set verifier = 1 where username = '%s'"%(self.table_user,username)
        print sql
        self.conn.execute("update user set verifier = ? where username = ?" ,(1,username))
        self.conn.commit()
    
    def insert_into_product(self, name , detail,username,uploadfile):
        sql = "insert into %s (name, detail,username,file,date) values ('%s', '%s', %s,'%s', '%s')"%(self.table_product, name, detail,username,uploadfile,datetime.datetime.now().strftime('%Y%m%d'))
        print sql
        self.conn.execute("insert into product (name, detail,username,file,date) values (?,?,?,?,?)" , (name, detail,username,uploadfile,datetime.datetime.now()))
        self.conn.commit()
	return True
    
    def select_from_product(self):
        sql = "select id, name ,date from %s order by date DESC"%(self.table_product)
        self.cu.execute(""+sql+"")
        return self.cu.fetchall()

    def select_from_product_by_product_id(self,product_id):
        sql = "select name ,detail,username,file,date from %s where id = %s order by date DESC"%(self.table_product,product_id)
        self.cu.execute(""+sql+"")
        return self.cu.fetchall()

    def select_from_product_by_product_name(self,product_name):
        sql = "select id, name ,date from %s where (name like '%s') order by date DESC"%(self.table_product,"%"+product_name+'%')
	self.cu.execute(""+sql+"")
        return self.cu.fetchall()

    def select_rowcount_from_product(self):
        sql = "select id from %s"%(self.table_product)
        self.cu.execute(""+sql+"")
        res = self.cu.fetchall()
        rowcount=0
        for i in res:
            rowcount = rowcount + 1
        return rowcount
   
    def __del__(self):
	print 'close db conn'
	self.cu.close()
        self.conn.close()

