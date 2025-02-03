from core.db import Database

db = Database()

# Test-Benutzer hinzufügen
db.add_user("testuser", "securepassword")

# Benutzer abfragen
user = db.get_user("testuser")
print("Benutzer:", user)

# Transaktion hinzufügen
db.add_transaction(user[0], 10.0, "Test Transaktion")

# Transaktionen abfragen
transactions = db.get_transactions(user[0])
print("Transaktionen:", transactions)

db.close()
