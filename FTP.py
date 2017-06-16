#-*- coding:utf-8 -*-
from ftplib import FTP
import os

def start():
    print ("""
    please choose an option:
    1:download fix files from store Controller
    2:upload fix files to store Controller
    3:Quit
    """)
    choise = raw_input(">> ")
    if choise == "1":
        download("ip")
    elif choise == "2":
        upload("ip")
    else:
        exit()
    
  
    
def download(ip):
    print "please enter the #number of Source store"
    print "e.g.: 2007"
    ipaddr = raw_input(">> ")
    a1 = ipaddr[0]
    a2 = ipaddr[1]
    a3 = ipaddr[2]
    a4 = ipaddr[3]
    
    if a3 != "0":
        ipaddr = "10." + a1 + a2 + "." + a3 + a4 + "." + "151"
    else:
        ipaddr = "10." + a1 + a2 + "."  + a4 + "." + "151"
        
    print ("""
    Plase choose a file you want to download:
    1:Items
    2:Promotion
    3:Coupon
    4:TPR
    5:Quit
    """)
    choise = raw_input(">> ")
    
    if choise == "1":
        print "Deleting Local Item File..."
        if  os.path.exists('c:/python27/EALITEMR.dat'):
            os.remove ('c:/python27/EALITEMR.dat')
        if  os.path.exists('c:/python27/EALITMRS.dat'):
            os.remove ('c:/python27/EALITMRS.dat')
        if  os.path.exists('c:/python27/EALTRUPC.dat'):
            os.remove ('c:/python27/EALTRUPC.dat')
    if choise == "2":
        print "Deleting Local Promotion File..."
        if  os.path.exists('c:/python27/PROMOGEN.dat'):
            os.remove ('c:/python27/PROMOGEN.dat')
        if  os.path.exists('c:/python27/PRGROUPS.dat'):
            os.remove ('c:/python27/PRGROUPS.dat')
        if  os.path.exists('c:/python27/PRINDEX.dat'):
            os.remove ('c:/python27/PRINDEX.dat')
        if  os.path.exists('c:/python27/EAPRSPOFLITEMR.dat'):
            os.remove ('c:/python27/PRSPOF.dat')
        if  os.path.exists('c:/python27/PROFFMLD.dat'):
            os.remove ('c:/python27/PROFFMLD.dat')
    if choise == "3":
        print "Deleting Local Coupon File..."
        if  os.path.exists('c:/python27/EALSCCTL.dat'):
            os.remove ('c:/python27/EALSCCTL.dat')
        if  os.path.exists('c:/python27/EALSCITL.dat'):
            os.remove ('c:/python27/EALSCITL.dat')
        if  os.path.exists('c:/python27/EALSCVNL.dat'):
            os.remove ('c:/python27/EALSCVNL.dat')
        if  os.path.exists('c:/python27/EALSCMST.dat'):
            os.remove ('c:/python27/EALSCMST.dat')
    if choise == "4":
        print "Deleting Local TPR File..."
        if  os.path.exists('c:/python27/TRUTPACM.dat'):
            os.remove ('c:/python27/TRUTPACM.dat')
        if  os.path.exists('c:/python27/TRUTPPCK.dat'):
            os.remove ('c:/python27/TRUTPPCK.dat')
        if  os.path.exists('c:/python27/TRUTPCHG.dat'):
            os.remove ('c:/python27/TRUTPCHG.dat')
        if  os.path.exists('c:/python27/TPRRPORT.286'):
            os.remove ('c:/python27/TPRRPORT.286')

          
    try:
        ftp = FTP(ipaddr)
    except:
        print "Ping %s Falied!" % ipaddr
        exit()
       
    else:
        print "Ping to %s ok!" % ipaddr
        
    try:    
        ftp.login("","")
    except:
        print "Login Falied!"
        exit()
    else:
        print "Login in Sucessful!"
        
    if choise == "1":
        ftp.cwd('/adx_idt1/')
        ftp.retrbinary('RETR EALITEMR.dat', open('EALITEMR.dat', 'wb').write)
        ftp.retrbinary('RETR EALITMRS.dat', open('EALITMRS.dat', 'wb').write)
        ftp.retrbinary('RETR EALTRUPC.dat', open('EALTRUPC.dat', 'wb').write)
        print "Items download complete!"
        start()
    elif choise == "2":
        ftp.cwd('/adx_idt1/')
        ftp.retrbinary('RETR PROMOGEN.dat', open('PROMOGEN.dat', 'wb').write)
        ftp.cwd('/adx_udt1/')
        ftp.retrbinary('RETR PRGROUPS.dat', open('PRGROUPS.dat', 'wb').write)
        ftp.retrbinary('RETR PRINDEX.dat', open('PRINDEX.dat', 'wb').write)
        ftp.retrbinary('RETR PRSPOF.dat', open('PRSPOF.dat', 'wb').write)
        ftp.retrbinary('RETR PROFFMLD.dat', open('PROFFMLD.dat', 'wb').write)
        print "Promotion download complete!"
        start()
    elif choise == "3":
        ftp.cwd('/adx_idt1/')
        ftp.retrbinary('RETR EALSCCTL.dat', open('EALSCCTL.dat', 'wb').write)
        ftp.retrbinary('RETR EALSCITL.dat', open('EALSCITL.dat', 'wb').write)
        ftp.retrbinary('RETR EALSCVNL.dat', open('EALSCVNL.dat', 'wb').write)
        ftp.retrbinary('RETR EALSCMST.dat', open('EALSCMST.dat', 'wb').write)
        print "Coupon download complete!"
        start()
    elif choise == "4":
        ftp.cwd('/adx_idt1/')
        ftp.retrbinary('RETR PROMOGEN.dat', open('PROMOGEN.dat', 'wb').write)
        ftp.retrbinary('RETR TRUTPACM.dat', open('TRUTPACM.dat', 'wb').write)
        ftp.cwd('/adx_udt1/')
        ftp.retrbinary('RETR TRUTPPCK.dat', open('TRUTPPCK.dat', 'wb').write)
        ftp.retrbinary('RETR TRUTPCHG.dat', open('TRUTPCHG.dat', 'wb').write)
        ftp.cwd('/adx_upgm/')
        ftp.retrbinary('RETR TPRRPORT.286', open('TPRRPORT.286', 'wb').write)
        print "TPR download complete!"
        start()
        #用循环改写
    else:
        ftp.quit()
        start()
    
def upload(ip):
    print "please enter the #number of Destination store"
    print "e.g.: 2007"
    ipaddr = raw_input(">> ")
    a1 = ipaddr[0]
    a2 = ipaddr[1]
    a3 = ipaddr[2]
    a4 = ipaddr[3]

    if a3 != "0":
        ipaddr = "10." + a1 + a2 + "." + a3 + a4 + "." + "151"
    else:
        ipaddr = "10." + a1 + a2 + "."  + a4 + "." + "151"
        
    try:
        ftp = FTP(ipaddr)
    except:
        print "Ping %s Falied!" % ipaddr
        exit()
       
    else:
        print "Ping to %s ok!" % ipaddr
        
    try:    
        ftp.login("ftpuser","4690tcpip")
    except:
        print "Login Falied!"
        exit()
    else:
        print "Login in Sucessful!"
    
    print ("""
    Plase choose a file you want to upload:
    1:Items
    2:Promotion
    3:Coupon
    4:TPR
    5:Quit
    """)
    
    choise = raw_input(">> ")
    if choise == "1":
        ftp.cwd('/adx_idt1/')
        ftp.storbinary('STOR EALITEMR.dat', open('EALITEMR.dat', 'rb'))
        ftp.storbinary('STOR EALITMRS.dat', open('EALITMRS.dat', 'rb'))
        ftp.storbinary('STOR EALTRUPC.dat', open('EALTRUPC.dat', 'rb'))
        print "Items upload complete!"
        start()
    elif choise == "2":
        ftp.cwd('/adx_idt1/')
        ftp.storbinary('STOR PROMOGEN.dat', open('PROMOGEN.dat', 'rb'))
        ftp.cwd('/adx_udt1/')
        ftp.storbinary('STOR PRGROUPS.dat', open('PRGROUPS.dat', 'rb'))
        ftp.storbinary('STOR PRINDEX.dat', open('PRINDEX.dat', 'rb'))
        ftp.storbinary('STOR PRSPOF.dat', open('PRSPOF.dat', 'rb'))
        ftp.storbinary('STOR PROFFMLD.dat', open('PROFFMLD.dat', 'rb'))
        print "Promotion upload complete!"
        start()
    elif choise == "3":
        ftp.cwd('/adx_idt1/')
        ftp.storbinary('STOR EALSCCTL.dat', open('EALSCCTL.dat', 'rb'))
        ftp.storbinary('STOR EALSCITL.dat', open('EALSCITL.dat', 'rb'))
        ftp.storbinary('STOR EALSCVNL.dat', open('EALSCVNL.dat', 'rb'))
        ftp.storbinary('STOR EALSCMST.dat', open('EALSCMST.dat', 'rb'))
        print "Coupon upload complete!"
        start()
    elif choise == "4":
        ftp.cwd('/adx_idt1/')
        ftp.storbinary('STOR PROMOGEN.dat', open('PROMOGEN.dat', 'rb'))
        ftp.storbinary('STOR TRUTPACM.dat', open('TRUTPACM.dat', 'rb'))
        ftp.cwd('/adx_udt1/')
        ftp.storbinary('STOR TRUTPPCK.dat', open('TRUTPPCK.dat', 'rb'))
        ftp.storbinary('STOR TRUTPCHG.dat', open('TRUTPCHG.dat', 'rb'))
        ftp.cwd('/adx_upgm/')
        ftp.storbinary('STOR TPRRPORT.286', open('TPRRPORT.286', 'rb'))
        print "TPR upload complete!"
        start()
        #用循环改写
    else:
        ftp.quit()
        start()

        
start()        



