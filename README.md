# Package-Tracking-System-Python
A simple system to track package using mysql and python

This package tracking system works on two databases.
One database holds the details about the customer/user and the other 
database hold the package information and status of every user.
Those two databases are named userinfo and packageinfo :-

<img width="587" alt="userdb" src="https://user-images.githubusercontent.com/98681867/234230820-195a3d5f-22ed-414b-9d34-14d4265eb8a9.png">
userinfo ^

<img width="320" alt="packdb" src="https://user-images.githubusercontent.com/98681867/234230967-56d4d5c7-e98a-44c5-b179-a8252d5c6e4c.png">
packageinfo ^

The code consists of 4 sub parts and 1 main script which holds them together.


The first sub part is for customer registration, it takes the details from the customer 
and saves those into the db. Here the customer also decides their username and 
password. Each username should be unique to one customer and it is used for 
identification and logging in. It takes details such as username, name, phone 
number, address and password.
<img width="695" alt="custregiscode" src="https://user-images.githubusercontent.com/98681867/234231192-5d014764-b0e0-4924-a2b7-430cb9dc05ea.png">



The second sub part consists of the admin input script. This script is for the admin 
and the admin can update the package information database using this script. The 
admin is responsible for updating the delivery status of the products.
<img width="692" alt="admininputcode" src="https://user-images.githubusercontent.com/98681867/234231321-8b70cbeb-7d88-4d13-aedd-a9f41295f639.png">



The third part consists of user login. This part prompts the user to input their login 
credentials and return a flag after verifying those credentials. It returns ‘0’ if the 
username doesn’t exist in the database, ‘1’ if the username exists but the password 
for it is wrong and finally ‘2’ if both username and password is correct.
<img width="659" alt="logincode" src="https://user-images.githubusercontent.com/98681867/234231389-9fe34a66-d9e2-49fb-a5d4-d3ceab7ff856.png">



The fourth part is for extracting the details from the package information database. 
This part interacts with the login script and returns the package details of the user 
only if the login script returns 2.
<img width="459" alt="packinfocode" src="https://user-images.githubusercontent.com/98681867/234231439-e810308d-9bb0-48a4-8971-60998fc03218.png">



Finally the main script is used to prompt the user for registration or login and 
connects all the 4 parts together to work as a single application.
<img width="638" alt="maincode" src="https://user-images.githubusercontent.com/98681867/234231459-4acf9418-e4d1-4dd4-ad88-a3fe09491cad.png">


