# -*- coding: utf-8 -*-
"""
Created on Tue Jul 10 14:01:08 2018

@author: Dhaval
"""

# -*- coding: utf-8 -*-
"""
Created on Mon May 28 14:55:34 2018

@author: Dhaval
"""

import cx_Oracle

con=cx_Oracle.connect("system/sys@localhost/xe")
cur=con.cursor()


cur.execute("drop table courierc")

print("\nCreating courier table for courierc(fromname,toname,weight,shipmenttype,trackid,status,cost) ")
cur.execute("""create table courierc(
        tfrom number(30),
        tto number(30),
        tweight number(20,3),
        tshipmenttype varchar2(20),
        ttrackid , 
        tstatus varchar2(20),
        tcost number(20)
        )""")
con.commit()
print("\n courierc table created Successfully")

print("\nInserting in courierc table")
putfrom=848
putto=32
putweight=20.6666
putshipmenttype="fast"
puttrackid='100'
putstatus='ahmedabad'
putcost=300
cur.execute("""insert into courierc values(:1,:2,:3,:4,:5,:6,:7)""",(putfrom,putto,putweight,putshipmenttype,puttrackid,putstatus,putcost))
#cur.execute("""insert into courierc values(:1,:2,:3,:4,:5,:6)""",(putfrom,putto,putweight,putshipmenttype,putstatus,putcost))
putfrom=848
putto=909
puttrackid='10'
putstatus='ahmedabad'
putcost=300
cur.execute("""insert into courierc values(:1,:2,:3,:4,:5,:6,:7)""",(putfrom,putto,putweight,putshipmenttype,puttrackid,putstatus,putcost))
#cur.execute("""insert into courierc values(:1,:2,:3,:4,:5,:6,:7)""",(putfrom,putto,putweight,putshipmenttype,putstatus,putcost))
con.commit()



print("\nDisplay data of courier table")
cur.execute("""select * from courierc""")
print(cur.fetchall())

con.commit()
con.close()