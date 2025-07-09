import sqlite3

def create_database():
    print("📦 Connecting to DB...")
    conn = sqlite3.connect('tutorials.db')
    cur = conn.cursor()

    print("🧱 Creating tables...")
    cur.execute('''
    CREATE TABLE IF NOT EXISTS tutorials (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        title TEXT,
        description TEXT,
        image TEXT
    )
    ''')

    cur.execute('''
    CREATE TABLE IF NOT EXISTS steps (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        tutorial_id INTEGER,
        step_number INTEGER,
        step_text TEXT,
        FOREIGN KEY (tutorial_id) REFERENCES tutorials(id)
    )
    ''')

    print("📝 Inserting sample data...")
    cur.execute("INSERT INTO tutorials (title, description, image) VALUES (?, ?, ?)",
                ("Assemble a Computer", "Learn how to assemble a PC from scratch.", None))
    tutorial_id = cur.lastrowid

    steps = [
        (tutorial_id, 1, "Install the motherboard into the case."),
        (tutorial_id, 2, "Attach the CPU to the motherboard."),
        (tutorial_id, 3, "Install RAM and storage."),
        (tutorial_id, 4, "Connect power supply and cables."),
        (tutorial_id, 5, "Power on and test the system.")
    ]

    cur.executemany("INSERT INTO steps (tutorial_id, step_number, step_text) VALUES (?, ?, ?)", steps)

    conn.commit()
    conn.close()
    print("✅ Database created and sample data inserted.")

if __name__ == "__main__":
    create_database()
import sqlite3

def create_database():
    print("📦 Connecting to DB...")
    conn = sqlite3.connect('tutorials.db')
    cur = conn.cursor()

    print("🧱 Creating tables...")
    cur.execute('''
    CREATE TABLE IF NOT EXISTS tutorials (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        title TEXT,
        description TEXT,
        image TEXT
    )
    ''')

    cur.execute('''
    CREATE TABLE IF NOT EXISTS steps (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        tutorial_id INTEGER,
        step_number INTEGER,
        step_text TEXT,
        FOREIGN KEY (tutorial_id) REFERENCES tutorials(id)
    )
    ''')

    print("📝 Inserting sample data...")
    cur.execute("INSERT INTO tutorials (title, description, image) VALUES (?, ?, ?)",
                ("Assemble a Computer", "Learn how to assemble a PC from scratch.", None))
    tutorial_id = cur.lastrowid

    steps = [
        (tutorial_id, 1, "Install the motherboard into the case."),
        (tutorial_id, 2, "Attach the CPU to the motherboard."),
        (tutorial_id, 3, "Install RAM and storage."),
        (tutorial_id, 4, "Connect power supply and cables."),
        (tutorial_id, 5, "Power on and test the system.")
    ]

    cur.executemany("INSERT INTO steps (tutorial_id, step_number, step_text) VALUES (?, ?, ?)", steps)

    conn.commit()
    conn.close()
    print("✅ Database created and sample data inserted.")

if __name__ == "__main__":
    create_database()
