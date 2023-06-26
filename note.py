

import sqlite3


note = ""

def init(new_note: str):
    global note
    note =  new_note


def add_new_note():
    database = input("В какую базу данных вы хотите создать заметку?: ") 
    new_note = init(input("Введите заметку: "))
    try:
        sqlite_connection = sqlite3.connect(f'{database}.db')
        cursor = sqlite_connection.cursor()
        cursor.execute(f"INSERT INTO notes ('note') VALUES ('{new_note}')")
        print("Запись успешно добавлена")
        sqlite_connection.commit()
        cursor.close()
    except sqlite3.Error as error:
        print("Ошибка при подключении к sqlite", error)

def update_note():
   
        database = input("В какой базе данных вы хотите обновить заметку?: ") 
        try:
            print("Какую заметку вы хотите обновить?")
            sqlite_connection = sqlite3.connect(f'{database}.db')
            cursor = sqlite_connection.cursor()
            cursor.execute("SELECT note FROM notes")
            while True:
                results = cursor.fetchall()
                if results:
                    while True:
                        available_notes = []
                        for i, note in enumerate(results):
                            print(f"{i}: {note}")
                            available_notes.append(i)
                        num_old_note = input("Введите номер заметки: ")
                        if not num_old_note:
                            break
                        elif num_old_note.isdigit() and int(num_old_note) in available_notes:
                            old_note = init(results[int(num_old_note)][0])
                            upd_note = init(input("На какую заметку хотите поменять?: "))
                            cursor.execute(f"UPDATE notes SET note = '{upd_note}' WHERE note == '{old_note}'")
                            print("Запись успешно обновлена")
                            sqlite_connection.commit()
                            cursor.close()
                            break
                        else:
                            print("Такой записи нет, повторите снова")
                    break
                else:
                    print("База данных пустая, попробуйте другую")
           
        except sqlite3.Error as error:
            print("Ошибка", error)


def delete_note():
    

    
        database = input("Из какой базы данных вы хотите удалить заметку?: ") 
             
        try:
            print("Какую заметку вы хотите удалить?")
            sqlite_connection = sqlite3.connect(f'{database}.db')
            cursor = sqlite_connection.cursor()
            cursor.execute("SELECT note FROM notes")

            while True:
                results = cursor.fetchall()
                if results:

                    while True:
                        available_notes = []
                        for i, note in enumerate(results):
                            print(f"{i}: {note}")
                            available_notes.append(i)
                        num_del_note = input("Введите номер: ")
                        if not num_del_note:
                            break
                        elif num_del_note.isdigit() and int(num_del_note) in available_notes:
                            del_note = init(results[int(num_del_note)][0])
                            print(del_note)
                            cursor.execute(f"DELETE FROM notes WHERE note = '{del_note}'")
                            print("Запись успешно удалена")
                            sqlite_connection.commit()
                            cursor.close()
                            break   
                            
                        else:
                            print("Такой записи нет, повторите снова")
                            
                    break
                else:
                    print("База данных пустая, попробуйте другую")

                    
                
        except sqlite3.Error as error:
            print("Ошибка", error)
           



def show_all_notes():
    while True:
        database = input("В какой базе данных вы хотите посмотреть заметки?: ") 
        if database:
            try:
                sqlite_connection = sqlite3.connect(f'database.db')
                cursor = sqlite_connection.cursor()
                cursor.execute("SELECT note FROM notes")
                results = cursor.fetchall()
                if results:
                    for i, res in enumerate(results):
                        print(f"{i}: {res}")
                    break
                else:
                    print("База данных пуста, попробуйте другую")
            except sqlite3.Error as error:
                    print("Ошибка при подключении к sqlite", error)

