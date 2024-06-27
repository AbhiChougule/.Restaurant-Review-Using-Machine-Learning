# database creation
#import mysql.connector
#conn=mysql.connector.connect(user='root',password='abhijeet@123',host='localhost')
#qur='create database rest_review_db'
#mycur=conn.cursor()
#mycur.execute(qur)
#mycur.close()
#conn.close()


#create table
#import mysql.connector
#conn=mysql.connector.connect(user='root',password='abhijeet@123',host='localhost',
    #                         database='rest_review_db')
#qur='create table project(food VARCHAR(40),good_review INT,bad_review INT,customer INT)'
#mycur=conn.cursor()
#mycur.execute(qur)
#mycur.close()
#conn.close()

# insert food
import mysql.connector
foods = ["Idly", "Dosa", "Vada", "Roti", "Meals", "Veg Biryani",
         "Egg Biryani", "Chicken Biryani", "Mutton Biryani",
         "Ice Cream", "Noodles", "Manchooriya", "Orange juice",
         "Apple Juice", "Pineapple juice", "Banana juice"]


for i in foods:
    conn = mysql.connector.connect(user='root', password='abhijeet@123', host='localhost',
                                   database='rest_review_db')
    qur = f'INSERT INTO project VALUES("{i}",{0},{0},{0})'
    mycur = conn.cursor()
    mycur.execute(qur)
    conn.commit()
    mycur.close()
    conn.close()


