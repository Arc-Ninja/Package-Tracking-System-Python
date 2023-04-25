import mysql.connector as mc

def register():
    user = mc.connect(
        host = "localhost",
        user = "root",
        password = "",
        database = "Package")

    username = str (input("Username (max: 10): "))
    name = str(input("Name (max: 20): "))
    phno = str(input("PhNo (+91): "))
    addr = str(input("Address (max: 50): "))
    password = str(input("Password (max: 16): "))

    query = "insert into userinfo (username,name,phno,address,password) values(%s,%s,%s,%s,%s)"
    values = (username,name,phno,addr,password)

    cmd = user.cursor()

    cmd.execute(query,values)

    user.commit()
    print("Registered Successfully")



