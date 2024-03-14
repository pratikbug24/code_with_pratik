import mysql.connector

mydb = mysql.connector.connect(
  host="localhost",
  user="root",
  password="root",
  database="sign_in_data"

)

mycursor = mydb.cursor()

sql="INSERT INTO users(user_name,email_id,password) VALUES (%s,%s,%s)"
var=({"fullname"},{"username"},{"password"})

mycursor.execute(sql, var)
mydb.commit()

print(mycursor.rowcount, "record inserted.")
