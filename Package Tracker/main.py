import login
import PackageInfo
import CustRegister
while(True):
    options = str(input("\nSelect from the following options:\n1. Register New User\n2. Login\n>: "))
    if(options == "1"):
        CustRegister.register()
    elif(options == "2"):
        flg,usrname = login.login()
        if(flg == 2):
            PackageInfo.packinfo(usrname)
        
    else:
        print("Type 1 or 2 to select from the given options!")

