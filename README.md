## 📋 CLI To-Do List with SQLite

A simple command-line to-do list application written in Python, backed by SQLite for persistent storage.  
Designed to help you manage your daily tasks efficiently from the terminal.

---

### 🚀 Features

- Add new tasks  
- Edit existing tasks  
- Delete tasks  
- Mark tasks as completed  
- Persistent storage using SQLite  
- Auto-reindexing of task IDs after deletion  
- Simple and clean command-line interface  

---

### 💠 Technologies Used

- **Python 3**
- **SQLite** (via the `sqlite3` module — no external dependencies)

---

### 📦 How to Run

1. **Clone the repository**
   ```bash
   git clone https://github.com/your-username/cli-todo-sqlite.git
   cd cli-todo-sqlite
   ```

2. **Run the script**
   ```bash
   python To-do_list.py
   ```

3. **Follow the on-screen instructions** to create, view, or manage your tasks.

---

### 📝 Example Output

```
Press 1 for creating a task
Press 2 for editing a task
Press 3 for deleting a task
Press 4 for checking off a task
Press 5 for exiting
```

---

### 📁 File Structure

```
cli-todo-sqlite/
│
├── To-do_list.py      # Main script
├── info.db            # SQLite database (auto-generated)
└── README.md          # Project info
```

---

### 🧹 Optional Setup

To avoid tracking your SQLite database or Python cache files in version control:

Create a `.gitignore` file with:
```
*.db
__pycache__/
```

---

### 🙋‍♂️ Future Improvements

- Add an option to uncheck completed tasks  
- Add due dates and priority levels  
- Create a GUI version with Tkinter or PyQt  
- Export/import tasks as JSON or CSV  

---

### 📄 License

This project is open-source and available under the [MIT License](https://opensource.org/licenses/MIT).

