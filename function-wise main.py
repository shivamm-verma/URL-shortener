def data_upload():   
    """
    equivalence === main program.py
    This function would create a connection between MySQL, 
    input a origional link and provide a shortlink.
    This function also would upload distinct(not retundant/duplicate) to 
    MySQL database named dwarflink(auto-creatable) and in table links(auto-creatable).
    """
    def shortlink_ret():           # program to return a random short link
        import random
        list_alpha = ['a','b','c','d','e','f','g','h','i','j','k','l',\
            'm','n','o','p','q','r','s','t','u','v','w','x','y','z'] 
        lst_shortlink_code = []
        i = 1
        while i <= 6:                 # password unique-code length = 6
            lst_elem = random.choice(list_alpha)
            str_case = random.randint(0,1)
            if str_case == 1:
                lst_elem = lst_elem.upper()
            lst_shortlink_code.append(lst_elem)
            i += 1
        shortlink_code = "".join(lst_shortlink_code)
        shortlink = []
        shortlink.append("https://www.dwarflink.com/")       # server name(OUR)
        shortlink.append(shortlink_code)
        shortlink = "".join(shortlink)
        return shortlink

    def record_link_dev():            # for execution
        import mysql.connector as mc
        mydb = mc.connect(host = "localhost",user = "root",passwd = "")
        print(f"Your connection ID: {mydb}")
        cursor = mydb.cursor()
        cursor.execute("select * from links")
        list_rec = []
        for i in cursor:
            i = list(i)
            list_rec.append(i)
        return list(list_rec)

    import mysql.connector as mc
    mydb = mc.connect(host = "localhost",user = "root",passwd = "")
    print("_________________________________________________________________")
    print(f"Your connection ID: {mydb}")
    print()
    orig_link = input("Enter Link: \n")
    orig_link = orig_link.strip()
    print()    
    cursor = mydb.cursor()
    try:            # if database is not existing, it'd create a database named dwarflink
        cursor.execute("create database dwarflink")
        cursor.execute("commit")
    except:
        cursor.execute("use dwarflink")
        cursor.execute("commit")
    if orig_link.startswith("https://www.") or  orig_link.startswith("https://") or  orig_link.startswith("www."):
        # check if shortlink is already exsiting in database or not
        true_count  = 0
        for i in record_link_dev():
            global shortlink
            i = list(i)     
            if i[0] == orig_link:          
                true_count = 1
                # shortlink already exisiting
                print("shortlink already exisiting!~~~~")
                shortlink = i[1]
                print(f"Shortlink: {shortlink}")
                break
        if true_count == 0:
            shortlink = str(shortlink_ret())
            print(f"Shortlink: {shortlink}")
    else:
        print("Enter a Valid Link.")
        

    try:            # creates table named links if not existing else pass and finally, and adding data to it.
        cursor.execute("create table links (longlink varchar(500) UNIQUE NOT NULL, shortlink varchar(50))")
        cursor.execute("commit")
        #print("Table,links, created.")
    except:
        #print("Table ,links, is already existing.")
        pass
    finally:
        try:
            cursor.execute(f"insert into links values ('{orig_link}','{shortlink}')")
            cursor.execute("commit")
            print("~~data is added to database!~~")
            pass
        except Exception as e:
            print("__ __ __ __ __ __ __ __ __ __")
            print("~~data couldn't be added to database!~~")
            print(f"Reason: {e}")
            print("__ __ __ __ __ __ __ __ __ __")        
            pass

    print()
    print("_________________________________________________________________")
    # program is done to input origional link and return shortlink on valid conditions(ref. line 55)

def record_links():       # for printing(all records in the database, dwarflink)
    import mysql.connector as mc
    mydb = mc.connect(host = "localhost",user = "root",passwd = "")
    print(f"Your connection ID: {mydb}")
    print("______________database records________________")
    print()
    cursor = mydb.cursor()
    cursor.execute("use dwarflink")
    cursor.execute("select * from dwarflink.links")
    for i in cursor:
        print(i)
    print("______________________________________________")

def database_and_table_maker():
    import mysql.connector as mc
    mydb = mc.connect(host = "localhost",user = "root",passwd = "")
    cursor = mydb.cursor()
    print(f"Your connection ID: {mydb}")
    print("______________________________________________")
    try:
        cursor.execute("create database dwarflink")
        cursor.execute("commmit")         
        pass
    except Exception as e:
        print(f"Error: {e}")
        pass
    # table making
    try:
        cursor.execute("create table links (longlink varchar(500) UNIQUE NOT NULL, shortlink varchar(50))")
        cursor.execute("commit")
        pass
    except Exception as e:
        print(f"Error: {e}")
        pass

if __name__ == "__main__":
    #data_upload()
    record_links()
    pass