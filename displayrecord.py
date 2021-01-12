import mysql.connector as ms
try:
    con = ms.connect(
        host="localhost",
        user="root",
        password="root",
        database="sample"
 )

    cursor=con.cursor()
    cursor.execute("SELECT * FROM products")
    data=cursor.fetchall()
    for row in data:
        print(row)
except ms.DatabaseError as e:
    if con:
        con.rollback()
        print("There is a problem with sql",e)
finally:
    if cursor:
        cursor.close()
    if con:
        con.close()