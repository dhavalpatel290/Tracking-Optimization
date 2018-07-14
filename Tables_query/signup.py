# -*- coding: utf-8 -*-
"""
Created on Sun Jul  8 15:00:36 2018

@author: Dhaval
"""

import cx_Oracle

def signup(putfname,putemail,putphone,putadd,putpost,putcity,putuname,putpass):

    con=cx_Oracle.connect("system/sys@localhost/xe")
    cur=con.cursor()
    cur.execute("""select * from users where tusername = :1""", {"1":putuname})
    putlist=cur.fetchall()
    if(len(putlist)>0):
        print("\t\tSorry, This username already exists")
        print("\t\tPlease use other username")
        con.close()
        return False
    else:
        cur.execute("""insert into users values(:1,:2,:3,:4,:5,:6,:7,:8)""",{"1":putfname,"2":putemail,"3":putphone,"4":putadd,"5":putpost,"6":putcity,"7":putuname,"8":putpass})
        con.commit()
        con.close()
        return True



putfname="dhabbmval"
putemail="gmail"
putphone=1243
putadd="hira"
putpost=382481
putcity="adi"
putuname='dhjj'
putpass="pass"


if(signup(putfname,putemail,putphone,putadd,putpost,putcity,putuname,putpass)):
    print("Registration Successfull")
else:
    print("\t\tTry again")
    
con=cx_Oracle.connect("system/sys@localhost/xe")
cur=con.cursor()
print("\nDisplay data of users table")
cur.execute("""select * from users""")
putlist=cur.fetchall()
print("The total entries are : "+str(len(putlist)))
print(putlist)
con.close()