# -*- coding: utf-8 -*-
"""
Created on Sun Jul  8 15:15:29 2018

@author: Dhaval
"""
import cx_Oracle

def login(putuname,putpass):
    con=cx_Oracle.connect("system/sys@localhost/xe")
    cur=con.cursor()
    cur.execute("""select * from users where tusername=:1 and tpassword=:2""",{"1":putuname,"2":putpass})
    cur.fetchall()
    if(cur.rowcount>=1):
        print("\t\tLogin Successful")
        con.close()
        return True
    else:
        con.close()
        return False
    
putuname=input("enter name : ")
putpass='pass'

if(login(putuname,putpass)):
    print("Dashboard")
else:
    print("Enter the valid username or password")
    print("\t\tTry again")
    
con=cx_Oracle.connect("system/sys@localhost/xe")
cur=con.cursor()
print("\nDisplay data of users table")
cur.execute("""select * from users""")
putlist=cur.fetchall()
print("The total entries are : "+str(len(putlist)))
print(putlist)
con.close()