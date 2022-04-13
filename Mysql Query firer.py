
import mysql.connector as mc
mydb = mc.connect(host = "localhost",user = "root",passwd = "")
print("------------------------------------------------")
print(f"Your connection ID: {mydb}")
# UNLIMITED QUERY FIRER
input_1 = input("Enter query: ")
while input_1.lower() != "n":
    cursor = mydb.cursor()
    try:
        cursor.execute(input_1)
    except Exception as e:
        print(f"Error: {e}")
    
    try:
        for rec in cursor:
            print(rec)
    except Exception as e:
        print(f"    : {e}")
    input_1 = input("Enter query: ")
    if input_1.lower() == "n":
        print("\n")
        print("Thankyou for using!")
        print("------------------------------------------------")