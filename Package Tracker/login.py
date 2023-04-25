import mysql.connector as mc
def login():
    user = mc.connect(
        host = "localhost",
        user = "root",
        password = "",
        database = "Package"
    )

    cursor = user.cursor()
    cursor.execute("select * from userinfo")
    values = cursor.fetchall()

    username = str(input("Username: "))
    password = str(input("Password: "))
    flag = 0
    for i in values:
        if(i[0]==username):
            flag = 1
            if(i[4]==password):
                flag = 2
                print("Login Successfull\n")
            else:
                print("Incorrect Password")
            break
    if(flag == 0):
        print("Username Error")
    return flag,username
