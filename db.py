import sqlite3

DB_FILE = "spinlog.db"

def get_connection():
    conn = sqlite3.connect(DB_FILE)
    conn.execute("PRAGMA foreign_keys = ON;") # foreign key enforcement
    cursor = conn.cursor()


# fix the rest of these so they use get connection() function bc now they dont work 

def insert_artist(name):
    conn = get_connection()
    cursor = conn.cursor()
    try: 
        cursor.execute("INSERT INTO Artist (name) VALUES(?)", (name,))
        conn.commit()
    except sqlite3.IntegrityError:
        print(f"Artist '{name}' already exists")
        
#def insert_release(release_name, artist_name, year, format): 
    
def print_all_artists():
    cursor.execute("""
               SELECT *
               FROM Artist               
               """)
    print(cursor.fetchall())
    
   



cursor.execute("DELETE FROM Artist WHERE id = ?", (4,))
conn.commit()

print_all_artists()