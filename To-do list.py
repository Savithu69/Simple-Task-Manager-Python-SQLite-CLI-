import sqlite3


conn = sqlite3.connect("info.db")
cursor = conn.cursor()
cursor.execute("""
CREATE TABLE IF NOT EXISTS data(
               id INTEGER PRIMARY KEY AUTOINCREMENT,
               task TEXT,
               completed INTEGER DEFAULT 0
)

""")
cursor.execute('ALTER TABLE data ADD COLUMN completed INTEGER DEFAULT 0')
conn.commit()
conn.close()

def create_task():
    conn = sqlite3.connect("info.db")
    cursor = conn.cursor()
    task = input('Enter your tasks: ')
    cursor.execute('INSERT INTO data (task) VALUES(?)',(task,))
    print('task successfully created.')
    print()
    conn.commit()
    conn.close()
    display_to_do()

def edit_task():
    conn = sqlite3.connect("info.db")
    cursor = conn.cursor()
    task_id = input('Enter the ID of the task to edit: ')
    updated_task = input('Enter the updated task: ')
    cursor.execute('UPDATE data SET task = ? WHERE id = ?', (updated_task, task_id))
    print('task successfully updated.')
    conn.commit()
    conn.close()

def delete_task():
    conn = sqlite3.connect("info.db")
    cursor = conn.cursor()
    task_id = input('Enter the ID of the task to delete: ')
    try:
        cursor.execute('DELETE FROM data WHERE id = ?', (task_id,))
        
        if cursor.rowcount == 0:
            print('No tasks to delete. Please add a task first.')
        else:
            print('Task successfully deleted.')
        conn.commit()
    except ValueError:
        print('Please enter a valid task.')
    cursor.execute('SELECT id FROM data ORDER BY id')
    tasks = cursor.fetchall()
    for index, (old_id,) in enumerate(tasks, start=1):
        cursor.execute('UPDATE data SET id = ? WHERE id = ?', (index, old_id))
    cursor.execute("DELETE FROM sqlite_sequence WHERE name='data'")
    conn.commit()
    conn.close()
    display_to_do()

def display_to_do():
    conn = sqlite3.connect("info.db")
    cursor = conn.cursor()
    cursor.execute('SELECT * FROM data')
    records = cursor.fetchall()
    
    if records:
        print('\nTo-Do List')
        print('------------')
        for record in records:
            status = '✓' if record[2] == 1 else 'x'
            print(f'{record[0]}. {record[1]}  [{status}]')
    else:
        print('\nNo tasks found.')

    conn.close()

def checking_task_off():
    conn = sqlite3.connect('info.db')
    cursor = conn.cursor()
    task_id = input('Enter the ID of the task to mark as completed: ')

    cursor.execute('SELECT * FROM data WHERE id = ?', (task_id,))
    task = cursor.fetchone()
    if not task:
        print('Task not found.')
    else:
        if task[2] == 1:
            print('Task is already marked as complete')
        else:
            cursor.execute('UPDATE data SET completed = 1 WHERE id = ?', (task_id,))
            print('Task successfully marked as complete')
            conn.commit()
    conn.close()
def main():
    while True:
        print()
        print('Press 1 for creating a task')
        print('Press 2 for editing a task')
        print('Press 3 for deleting a task')
        print('Press 4 for checking off a task')
        print('Press 5 for exiting')
        try:
          choice = int(input('Enter your choice: '))
        except ValueError:
            print('error')
            continue
        if choice in [1,2,3,4]:
            display_to_do()
           
        if choice == 1:
           create_task()
        elif choice == 2:
           edit_task()
        elif choice == 3:
            delete_task()
        elif choice == 4:
            checking_task_off()
        elif choice == 5:
            print('connection ended.')
            break 
    

if __name__ == "__main__":
   main()

