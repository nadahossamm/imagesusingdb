import mysql.connector

MyDB = mysql.connector.connect(
    host="localhost",
    user="root",
    password="",
    database="images"
)

MyCursor = MyDB.cursor()

MyCursor.execute("CREATE TABLE IF NOT EXISTS Images (id INTEGER(45) NOT NULL AUTO_INCREMENT PRIMARY KEY, Photo LONGBLOB NOT NULL)")

def InsertBlob(FilePath):
    with open(FilePath,"rb") as File:
        BinaryData = File.read()
        SQLStatment = "INSERT INTO Images (Photo) VALUES (%s)"
        MyCursor.execute(SQLStatment,(BinaryData, ))
        MyDB.commit()


def RetrieveBlob(ID):
    SQLStatment2="SELECT * FROM Images Where id='{0}'"
    MyCursor.execute(SQLStatment2.format(str(ID)))
    MyResult = MyCursor.fetchone()[1]
    StoreFilePath = "ImageOut/img{0}.jpg".format(str(ID))
    print(MyResult)
    with open(StoreFilePath, "wb") as File:
        File.write(MyResult)
        File.close()


print("1.Insert images\n2.Read images")
MenuInput = input()

if int(MenuInput)== 1 :
    UserFilePath = input("Enter File Path")
    InsertBlob(UserFilePath)
elif int(MenuInput) == 2:
    UserIDChoise = input("Enter ID : ")
    RetrieveBlob(UserIDChoise)



