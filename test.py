def start():
    print ("""
    please choose an option:
    1:download fix files from store Controller
    2:upload fix files to store Controller
    3:Quit
    """)
    option = raw_input(">> ")

    print "please enter the #number of Store"
    print "e.g.: 2007"
    ipaddr = raw_input(">> ")
    a1 = ipaddr[0]
    a2 = ipaddr[1]
    a3 = ipaddr[2]
    a4 = ipaddr[3]
    if a3 != "0":
        ipaddr = "10." + a1 + a2 + "." + a3 + a4 + "." + "151"
    else:
        ipaddr = "10." + a1 + a2 + "." + a4 + "." + "151"

    return str(option),str(ipaddr)

w = start()
