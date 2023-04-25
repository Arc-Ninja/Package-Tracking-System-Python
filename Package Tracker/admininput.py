import mysql.connector as mc

def admin():
    user = mc.connect(
        host = "localhost",
        user = "root",
        password = "",
        database = "Package")

    username = str (input("Username (max: 10): "))
    product = str(input("Product (max: 20): "))
    status = str(input("Status (max: 15): "))

    query = "insert into packageinfo (username,packname,status) values(%s,%s,%s)"
    values = (username,product,status)

    cmd = user.cursor()

    cmd.execute(query,values)

    user.commit()
    print("Inserted Successfully")

while(True):
    admin()