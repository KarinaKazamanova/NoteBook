import sqlite3


try:
    sqlite_connection = sqlite3.connect(f'database_1.db')
    cursor = sqlite_connection.cursor()
    # print("База данных создана и успешно подключена к SQLite")
    cursor.execute("CREATE TABLE notes_1 (note VARCHAR(500))")
    cursor.execute("INSERT INTO notes_1 VALUES ('123456'), ('dssdfghjnbvc')")
    cursor.execute("SELECT note FROM notes_1")
    results = cursor.fetchall()
    print(results)

except sqlite3.Error as error:
        print("Ошибка при подключении к sqlite", error)