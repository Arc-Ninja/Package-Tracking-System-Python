import mysql.connector as mc
def packinfo(username):
    user = mc.connect(
        host = "localhost",
        user = "root",
        password = "",
        database = "Package"
    )
   
    cursor = user.cursor()
    cursor.execute("select * from packageinfo")
    values = cursor.fetchall()
    flag = 0
    for i in values:
        if(i[0]==username):
            flag = 1
            print(i[1],": ",i[2])
    if(flag == 0):
        print("You have no orders")