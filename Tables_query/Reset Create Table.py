# -*- coding: utf-8 -*-
"""
Created on Mon May 28 14:55:34 2018

@author: Dhaval
"""

import cx_Oracle

con=cx_Oracle.connect("system/sys@localhost/xe")
cur=con.cursor()


cur.execute("drop table users")
cur.execute("drop table c_details")
cur.execute("drop table courier")
cur.execute("drop table cost_city")
cur.execute("drop table cost_weight")
cur.execute("drop table cost_shipmenttype")


print("\nCreating user table for users(phone,password) ")
cur.execute("""create table users(
        tphone number(30) primary key,
        tpassword varchar2(20)
        )""")
con.commit()
print("\n user table created Successfully")

print("\nCreating user table for c_details(fullname,email,phone,add,post,city) ")
cur.execute("""create table c_details(
        tfullname varchar2(20),
        temail varchar2(20),
        tphone number(30) primary key,
        taddress varchar2(50),
        tpostalcode number(10),
        tcity varchar2(20)
        )""")
con.commit()
print("\n user table created Successfully")


print("\nCreating courier table for courier(fromname,toname,weight,shipmenttype,trackid,status,cost) ")
cur.execute("""create table courier(
        tfrom number(30),
        tto number(30),
        tweight number(20,3),
        tshipmenttype varchar2(20),
        ttrackid varchar2(20), 
        tstatus varchar2(20),
        tcost number(20)
        )""")
con.commit()
print("\n courier table created Successfully")

print("\nCreating cost_city table for cost_city(from,to,cost) ")
cur.execute("""create table cost_city(        
        tfrom varchar2(20),
        tto varchar2(20),
        tcost number(20)
        )""")
con.commit()
print("\n cost_city table created Successfully")

print("\nCreating cost_weight table for cost_weight(from,to,cost) ")
cur.execute("""create table cost_weight(        
        tfrom number(20,3),
        tto number(20,3),
        tcost number(20)
        )""")
con.commit()
print("\n cost_weight table created Successfully")


print("\nCreating cost_shipmenttype table for cost_shipmenttype(type,cost) ")
cur.execute("""create table cost_shipmenttype(        
        ttype varchar2(20),
        tcost number(20)
        )""")
con.commit()
print("\n cost_shipmenttype table created Successfully")


print("\nInserting in users table")
putphone=31
putpass="pass"
cur.execute("""insert into users values(:1,:2)""",(putphone,putpass))
putphone=32
cur.execute("""insert into users values(:1,:2)""",(putphone,putpass))
putphone=848
cur.execute("""insert into users values(:1,:2)""",(putphone,putpass))
con.commit()


print("\nInserting in c_details table")
putfname="dhaval patel"
putemail="gmail"
putphone=31
putadd="hira nirma"
putpost=382481
putcity="ahmedabad"
cur.execute("""insert into c_details values(:1,:2,:3,:4,:5,:6)""",(putfname,putemail,putphone,putadd,putpost,putcity))
putphone=32
cur.execute("""insert into c_details values(:1,:2,:3,:4,:5,:6)""",(putfname,putemail,putphone,putadd,putpost,'mumbai'))
putphone=848
cur.execute("""insert into c_details values(:1,:2,:3,:4,:5,:6)""",(putfname,putemail,putphone,putadd,putpost,putcity))
putphone=909
putcity='surat'
putfname='Jagdish Patel'
putpost=395009
cur.execute("""insert into c_details values(:1,:2,:3,:4,:5,:6)""",(putfname,putemail,putphone,putadd,putpost,putcity))
con.commit()

print("\nInserting in courier table")
putfrom=848
putto=32
putweight=20.6666
putshipmenttype="fast"
puttrackid='1'
putstatus='ahmedabad'
putcost=300
cur.execute("""insert into courier values(:1,:2,:3,:4,:5,:6,:7)""",(putfrom,putto,putweight,putshipmenttype,puttrackid,putstatus,putcost))
putfrom=848
putto=909
puttrackid='2'
putstatus='ahmedabad'
putcost=300
cur.execute("""insert into courier values(:1,:2,:3,:4,:5,:6,:7)""",(putfrom,putto,putweight,putshipmenttype,puttrackid,putstatus,putcost))
con.commit()




print("\nInserting in cost_city table")
putfrom="mumbai"
putto="surat"
putcost=500
cur.execute("""insert into cost_city values(:1,:2,:3)""",(putfrom,putto,putcost))
cur.execute("""insert into cost_city values(:1,:2,:3)""",(putto,putfrom,putcost))
putfrom="mumbai"
putto="ahmedabad"
putcost=2000
cur.execute("""insert into cost_city values(:1,:2,:3)""",(putfrom,putto,putcost))
cur.execute("""insert into cost_city values(:1,:2,:3)""",(putto,putfrom,putcost))
putfrom="ahmedabad"
putto="surat"
putcost=400
cur.execute("""insert into cost_city values(:1,:2,:3)""",(putfrom,putto,putcost))
cur.execute("""insert into cost_city values(:1,:2,:3)""",(putto,putfrom,putcost))

con.commit()

print("\nInserting in cost_weight table")
putfrom=0
putto=20
putcost=0
cur.execute("""insert into cost_weight values(:1,:2,:3)""",(putfrom,putto,putcost))
putfrom=20
putto=50
putcost=100
cur.execute("""insert into cost_weight values(:1,:2,:3)""",(putfrom,putto,putcost))
putfrom=50
putto=1000
putcost=1000
cur.execute("""insert into cost_weight values(:1,:2,:3)""",(putfrom,putto,putcost))
con.commit()

print("\nInserting in cost_shipmenttype table")
putshipmenttype="regular"
putcost=50
cur.execute("""insert into cost_shipmenttype values(:1,:2)""",(putshipmenttype,putcost))
putshipmenttype="fast"
putcost=200
cur.execute("""insert into cost_shipmenttype values(:1,:2)""",(putshipmenttype,putcost))
putshipmenttype="express"
putcost=500
cur.execute("""insert into cost_shipmenttype values(:1,:2)""",(putshipmenttype,putcost))
con.commit()


print("\nDisplay data of users table")
cur.execute("""select * from users""")
putlist=cur.fetchall()
print("\t\t\t The total entries are : "+str(len(putlist)))
print(putlist)

print("\nDisplay data of c_details table")
cur.execute("""select * from c_details""")
putlist=cur.fetchall()
print("\t\t\t The total entries are : "+str(len(putlist)))
print(putlist)

print("\nDisplay data of courier table")
cur.execute("""select * from courier""")
print(cur.fetchall())

print("\nDisplay data of cost_city table")
cur.execute("""select * from cost_city""")
print(cur.fetchall())

print("\nDisplay data of cost_weight table")
cur.execute("""select * from cost_weight""")
print(cur.fetchall())

print("\nDisplay data of cost_shipmettype table")
cur.execute("""select * from cost_shipmenttype""")
print(cur.fetchall())



putnewcity='surat'
putphone=31
cur.execute("""select tcity from c_details where tphone=:1 """,{"1":putphone})
putlist=cur.fetchall()
gotoldcity=putlist[0][0]
print("\nUpdate data in  c_details table (changed city of phone "+str(putphone)+" from "+gotoldcity+" to "+putnewcity+")")
cur.execute("""update c_details set tcity=:1 where tphone=:2 """,{"1":putnewcity,"2":putphone})
con.commit()

print("\nAfter Update : Display data of c_details table")
cur.execute("""select * from c_details""")
print(cur.fetchall())

putphone=33
print("\nDelete data in c_details table (deleted phonenumber "+str(putphone)+")")
cur.execute("""delete from c_details where tphone=:1 """,{"1":putphone})
con.commit()


print("\nAfter Delete : Display data of c_details table")
cur.execute("""select * from c_details""")
putlist=cur.fetchall()
print("\t\t\t Now the total entries are : "+str(len(putlist)))
print(putlist)

con.commit()
con.close()

