import time
import mysql.connector

conn = mysql.connector.connect(host="localhost", user="root", password="1234", database="books")

mycursor = conn.cursor(buffered=True)
def AddBook():
    name_of_book = input("Enter the books name: ")
    year_of_book = int(input("Enter the year of the book: "))
    author_of_book = input("Enter the author of the book: ")

    sql = ("INSERT INTO books_info(name, year, author) VALUES(%s, %s, %s)")
    val = (name_of_book, year_of_book, author_of_book)

    mycursor.execute(sql, val)
    conn.commit()
    print ("Book successfully added...")
    time.sleep(1)
    MainMenu()
def ShowBooks():
    mycursor.execute("SELECT * FROM books_info")
    for i in mycursor:
        print(i)
    time.sleep(1)
    MainMenu()

def DeleteBook():
    sql = "DELETE FROM books_info WHERE id = %s"
    val = int(input("Enter the id of the book: "))

    mycursor.execute(sql, (val,))
    conn.commit()
    print("Book successfully deleted.")
    time.sleep(1)
    MainMenu()

def SearchBook():
    print("*******************************************")
    print("Enter how you want to search book: ")
    print("1.Search book by id: ")
    print("2.Search book by book name: ")
    ch = int(input(">>>"))
    if ch == 1:
        val = int(input("Enter the books id: "))
        sql = "SELECT * FROM books_info WHERE id=%s"
        mycursor.execute(sql, (val,))
        for i in mycursor:
            print (i)
    elif ch == 2:
        val = input("Enter name of the book: ")
        sql = "SELECT * FROM books_info WHERE name LIKE %s"
        mycursor.execute(sql, ("%" + val + "%",))
        for i in mycursor:
            print (i)
    else:
        print("Enter a valid choice.")
        SearchBook()
    MainMenu()

def MainMenu():
    print ("******************************")
    print ("What you want to do: ")
    print ("1.Add a book")
    print ("2.Show books")
    print ("3.Delete a book")
    print ("4.Search a book")
    print ("5.Exit")
    print ("******************************")
    ch = int(input("Enter your choice: "))
    if ch == 1:
        AddBook()
    elif ch == 2:
        ShowBooks()
    elif ch == 3:
        DeleteBook()
    elif ch == 4:
        SearchBook()
    elif ch == 5:
        print("Quitting now...")
        return
    else:
        print ("Enter a valid choice...")
        time.sleep(1)
        MainMenu()
MainMenu()
#Just putting a comment.
