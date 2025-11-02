import sqlite3

class DatabaseHandler:
    def __init__(self, db_name='sql.db'):
        self.connection = sqlite3.connect(db_name)
        self.cursor = self.connection.cursor()
        self.cursor.execute("CREATE TABLE IF NOT EXISTS PLAYS (id INTEGER PRIMARY KEY, player CHAR(25) NOT NULL, clip_name CHAR(250) NOT NULL, upload_date TIMESTAMP DEFAULT CURRENT_TIMESTAMP);")
    def execute_query(self, query, params=()):
        try:
            self.cursor.execute(query, params)
            self.connection.commit()
            return self.cursor.fetchall()
        except sqlite3.Error as e:
            print(f"An error occurred: {e}")
            return None

    def close(self):
        self.connection.close()

db_handler = DatabaseHandler()

if __name__ == "__main__":
    # Example usage
    # db_handler.execute_query("INSERT INTO PLAYS (player, clip_name) VALUES (?, ?)", ("TestPlayer", "test_clip.mp4"))
    # db_handler.execute_query("DELETE FROM PLAYS")
    results = db_handler.execute_query("SELECT * FROM PLAYS")
    for row in results:
        print(row)
    db_handler.close()