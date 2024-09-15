import sqlite3
conn = sqlite3.connect('grocery.db')
cursor = conn.cursor()

cursor.execute('''
                CREATE TABlE IF NOT EXISTS groceries (
               id INTEGER PRIMARY KEY,
               name TEXT NOT NULL,
               quantity TEXT NOT NULL
               )
''')

def view_items():
    cursor.execute('SELECT * FROM groceries')
    print('Groceries in your list are: ')
    rows = cursor.fetchall()
    if len(rows) == 0:
        print('No list recorded yet.')
    else:
        for row in rows:
            print(row) 

def add_item(name,quantity):
    cursor.execute('INSERT INTO groceries (name,quantity) VALUES (?, ?)', (name,quantity))
    conn.commit()

def remove_item(item_id):
    cursor.execute('DELETE FROM groceries WHERE id = ?',(item_id,))
    conn.commit()

def update_item(name,quantity,item_id):
    cursor.execute('UPDATE groceries SET name = ?, quantity = ? WHERE id = ?',(name,quantity,item_id))
    conn.commit()

def main():
    while True:
        print('\n Grocery List Manager | Enter an Option: ')
        print('1. View all items.')
        print('2. Add item.')
        print('3. Remove item.')
        print('4. Update item.')
        print('5. Exit list.')

        user_input = input('Enter an option: ')

        if user_input == '1':
            view_items()

        elif user_input == '2':
            view_items()
            name = input('Enter an item to add: ')
            quantity = input('Enter its quantity: ')
            add_item(name,quantity)

        elif user_input == '3':
            view_items()
            item_id = input('Enter the item_id to remove: ')
            remove_item(item_id)

        elif user_input == '4':
            view_items()
            item_id = input('Enter the item_id to update: ')
            name = input('Enter the new item: ')
            quantity = input('Enter its quantity: ')
            update_item(name,quantity,item_id)

        elif user_input == '5':
            break

        else:
            print('Invalid Choice.')

if __name__ == '__main__':
    main()