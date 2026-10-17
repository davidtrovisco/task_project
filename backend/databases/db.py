import sqlite3 as sql

def connect_db():
    return sql.connect('database.db')

def create_table():
    conn = connect_db()
    cursor = conn.cursor()
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS tasks (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            title TEXT NOT NULL,
            description TEXT,
            done BOOLEAN NOT NULL CHECK (done IN (0, 1))
        )
    ''')
    conn.commit()
    conn.close()

def add_task(title, description, done):
    conn = connect_db()
    cursor = conn.cursor()
    cursor.execute('''
        INSERT INTO tasks (title, description, done)
        VALUES (?, ?, ?)
    ''', (title, description, done))
    conn.commit()
    conn.close()

def get_tasks():
    conn = connect_db()
    cursor = conn.cursor()
    cursor.execute('SELECT * FROM tasks')
    tasks = cursor.fetchall()
    conn.close()
    return tasks

def get_task(task_id):
    conn = connect_db()
    cursor = conn.cursor()
    cursor.execute('SELECT * FROM tasks WHERE id = ?', (task_id,))
    task = cursor.fetchone()
    conn.close()
    return task

def update_task(task_id, title, description, done):
    conn = connect_db()
    cursor = conn.cursor()
    cursor.execute('''
        UPDATE tasks
        SET title = ?, description = ?, done = ?
        WHERE id = ?
    ''', (title, description, done, task_id))
    conn.commit()
    conn.close()

def delete_task(task_id):
    conn = connect_db()
    cursor = conn.cursor()
    cursor.execute('DELETE FROM tasks WHERE id = ?', (task_id,))
    conn.commit()
    conn.close()