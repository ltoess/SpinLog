import datetime
import sqlite3

DB_FILE = "spinlog.db"

def get_connection():
    conn = sqlite3.connect(DB_FILE)
    conn.execute("PRAGMA foreign_keys = ON;") # foreign key enforcement
    cursor = conn.cursor()

def name_to_id(name: str): 
    conn = get_connection()
    cursor = conn.cursor
    try: 
        cursor.execute(
            """
            SELECT id
            FROM Artist 
            WHERE name = ? COLLATE NOCASE            
            """
            , (name,)
        )
        result = cursor.fetchone()
        if result:
            return result[0]
        else: 
            return None
    except sqlite3.IntegrityError:
        print(f"Couldn't find '{name}' in database")
    finally: 
        conn.close()
    

def insert_artist(name: str):
    conn = get_connection()
    cursor = conn.cursor()
    try: 
        cursor.execute("INSERT INTO Artist (name) VALUES(?)", (name,))
        conn.commit()
    except sqlite3.IntegrityError:
        print(f"Artist '{name}' already exists")
    finally: 
        conn.close()
        
def insert_album(album_name: str, artist_name: str, year: int, format: str): 
    conn = get_connection()
    cursor = conn.cursor()
    artist_id = name_to_id(artist_name)
    
    if artist_id == None: 
        print("No artist: ", artist_name, ". Add the artist first.")
        conn.close()
        return
    else:     
        # input validation  
        # check year  
        if year == "": 
            year = None
        else: 
            try:
                year_input = int(year)
                if not(1000 <= year <= datetime.now().year_input + 1):
                    print("year out of range")
                    year_input = None
            except ValueError: 
                print("invalid year format")
                year_input = None
                
        # check format
        if format == "": 
            format_input = None
        else: 
            format_input = str.strip(format)
            format_input = str.upper(format_input)
            valid_formats = {"LP", "EP", "7\""}
            if format_input not in valid_formats: 
                format_input = None
                print("Format not inputted correctly. Logging as none. ")
        
        try: 
            cursor.execute("INSERT INTO Album (title, artist_id, year, format) VALUES(?, ?, ?, ?)"
            return cursor.lastrowid()
            conn.commit()
        except sqlite3.IntegrityError(): 
            print(f"Album '{album_name}' couldn't be added")
        finally: 
            conn.close()
    
def print_all_artists():
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute("""
               SELECT *
               FROM Artist               
               """)
    print(cursor.fetchall())
    conn.close()
    

print_all_artists()