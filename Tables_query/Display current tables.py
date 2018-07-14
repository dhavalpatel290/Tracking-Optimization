# -*- coding: utf-8 -*-
"""
Created on Mon Jul  9 02:16:47 2018

@author: Dhaval
"""
import cx_Oracle
con=cx_Oracle.connect("system/sys@localhost/xe")
cur=con.cursor()
        

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

con.close()