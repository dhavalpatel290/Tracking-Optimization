# -*- coding: utf-8 -*-
"""
Created on Sun Jul  8 23:44:56 2018

@author: Dhaval
"""

import cx_Oracle
from Ccourier import MainCourier

class MainDashboard:
    def __init__(self, gotphone):  
        con=cx_Oracle.connect("system/sys@localhost/xe")
        cur=con.cursor()
        cur.execute("""select * from c_details where tphone=:1 """,{"1":gotphone})
        putlist=cur.fetchall()
        con.close()
        gottuple=putlist[0]
        self.fullname = gottuple[0]
        self.email=gottuple[1]
        self.phone=gottuple[2]
        self.address=gottuple[3]
        self.postalcode=gottuple[4]
        self.city=gottuple[5]

   