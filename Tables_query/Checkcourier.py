# -*- coding: utf-8 -*-
"""
Created on Mon Jul  9 00:23:44 2018

@author: Dhaval
"""

import cx_Oracle
from Cdashboard import MainDashboard

class MainCourier():
    
    def __init__(self,puttrackid):
        con=cx_Oracle.connect("system/sys@localhost/xe")
        cur=con.cursor()
        cur.execute("""select * from courier where ttrackid=:1 """,{"1":puttrackid})
        putlist=cur.fetchall()
        print(putlist)
        con.close()
        gottuple=putlist[0]
        self.fromcmpphone = gottuple[0]
        self.tocustphone=gottuple[1]
        self.weight=gottuple[2]
        self.shipmenttype=gottuple[3]
        self.trackid=gottuple[4]
        self.status=gottuple[5]
        self.cost=gottuple[6]
        
    def printReceipt(self):
        print("\n\n--------------------------------------------")
        print("------------- Shipping Details -------------")
        print("--------------------------------------------")
        cmpobj=MainDashboard(self.fromcmpphone)
        custobj=MainDashboard(self.tocustphone)
        print("\n\nTrackid : "+self.trackid)
        print("\t\t Shipment type : "+self.shipmenttype)
        print("\t\t Shipment weight : "+str(self.weight))
        print("\t\t Final Amount to be paid : "+str(self.cost))
        print("\nCustomer Details")
        print(" \t\t Name      : "+custobj.fullname)
        print(" \t\t Address   : "+custobj.address)
        print(" \t\t City      : "+custobj.city)
        print(" \t\t Pin Code  : "+str(custobj.postalcode))
        print(" \t\t Email     : "+custobj.email)        
        print(" \t\t Phone no. : "+str(custobj.phone))
        print("\nCompany Details")
        print(" \t\t Name      : "+cmpobj.fullname)
        print(" \t\t Address   : "+cmpobj.address)
        print(" \t\t City      : "+cmpobj.city)
        print(" \t\t Pin Code  : "+str(cmpobj.postalcode))
        print(" \t\t Email     : "+cmpobj.email)        
        print(" \t\t Phone no. : "+str(cmpobj.phone))
        print("\n\n--------------------------------------------")
        print("--------------------------------------------")
        return 



obj=MainCourier('101')	
#print("done")
obj.printReceipt()	