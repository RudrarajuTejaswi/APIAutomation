from utilities.configurations import *

'''
connection_obj = mysql.connector.connect(host="localhost",database="APIDevelop",
                                         user="root",password="root")

print(connection_obj.is_connected()) # to check wether connection is established
'''

connection_obj = get_db_connection()
#to traverse in DB a cursor_obj is required
cursor_obj = connection_obj.cursor()
cursor_obj.execute('select * from CustomerInfo')
# row = cursor_obj.fetchone() #gets first row of table as tuple based on cusor position
# print(row)
# print(row[2])#  to get particular value in the row

complete_table = cursor_obj.fetchall() #gives all table data in list of tuples  based on cusor position
print(complete_table)
total = 0 #for loop to get sum of a column data in the table
for n in complete_table:
    total += n[2]
print(f"total cost for all books is {total}")
assert not 241 == total

#to update a value in the table without hardcoding query and values
query = "update customerInfo set Location = %s where CourseName = %s"
data = ("India","Jmeter")
cursor_obj.execute(query,data)
connection_obj.commit()
# to check wether the value is updated
cursor_obj.execute("select * from CustomerInfo")
table = cursor_obj.fetchall()
print(table)

#to delete a particular row
delete_query = "delete from CustomerInfo where CourseName = %s"
delete_data = ("Appium",)
cursor_obj.execute(delete_query,delete_data)
connection_obj.commit()
cursor_obj.execute("select * from CustomerInfo")
after_delete = cursor_obj.fetchall()
print(after_delete)

connection_obj.close()#to close the connection