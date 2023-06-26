
import sqlite3


try:
    sqlite_connection = sqlite3.connect(f'database.db')
    cursor = sqlite_connection.cursor()
    print("База данных создана и успешно подключена к SQLite")
    cursor.execute("CREATE TABLE notes  (note VARCHAR(500))")
except sqlite3.Error as error:
        print("Ошибка при подключении к sqlite", error)