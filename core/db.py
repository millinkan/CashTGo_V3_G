import sqlite3

class Database:
    def __init__(self, db_name="app_data.db"):
        """Initialisiert die Verbindung zur SQLite-Datenbank."""
        self.connection = sqlite3.connect(db_name)
        self.cursor = self.connection.cursor()
        self.create_tables()

    def create_tables(self):
        """Erstellt notwendige Tabellen, falls sie nicht existieren."""
        self.cursor.execute("""
        CREATE TABLE IF NOT EXISTS users (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            username TEXT NOT NULL UNIQUE,
            password TEXT NOT NULL
        )
        """)
        self.cursor.execute("""
        CREATE TABLE IF NOT EXISTS transactions (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            user_id INTEGER,
            amount REAL,
            description TEXT,
            timestamp DATETIME DEFAULT CURRENT_TIMESTAMP,
            FOREIGN KEY(user_id) REFERENCES users(id)
        )
        """)
        self.connection.commit()

    def add_user(self, username, password):
        """Fügt einen neuen Benutzer hinzu."""
        try:
            self.cursor.execute("INSERT INTO users (username, password) VALUES (?, ?)", (username, password))
            self.connection.commit()
        except sqlite3.IntegrityError:
            print("Benutzername existiert bereits.")

    def add_transaction(self, user_id, amount, description):
        """Fügt eine neue Transaktion hinzu."""
        self.cursor.execute(
            "INSERT INTO transactions (user_id, amount, description) VALUES (?, ?, ?)",
            (user_id, amount, description)
        )
        self.connection.commit()

    def get_user(self, username):
        """Ruft Benutzerdaten basierend auf dem Benutzernamen ab."""
        self.cursor.execute("SELECT * FROM users WHERE username = ?", (username,))
        return self.cursor.fetchone()

    def get_transactions(self, user_id):
        """Holt alle Transaktionen eines Benutzers."""
        self.cursor.execute("SELECT * FROM transactions WHERE user_id = ?", (user_id,))
        return self.cursor.fetchall()

    def close(self):
        """Schließt die Verbindung zur Datenbank."""
        self.connection.close()
