import datetime
import sqlite3

DB_FILE = "spinlog.db"

def get_connection():
    conn = sqlite3.connect(DB_FILE)
    conn.execute("PRAGMA foreign_keys = ON;") # foreign key enforcement
    return conn

def name_to_id(name: str): 
    conn = get_connection()
    cursor = conn.cursor()
 
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
        conn.close()
        return result[0]
    else: 
        conn.close()
        return None

def insert_artist(name: str):
    conn = get_connection()
    cursor = conn.cursor()
    try: 
        cursor.execute("INSERT INTO Artist (name) VALUES(?)", (name,))
        conn.commit()
        return cursor.lastrowid
    except sqlite3.IntegrityError:
        print(f"Artist '{name}' already exists")
    finally: 
        conn.close()
        
def insert_album(album_name: str, artist_name: str, year, record_format: str): 
    conn = get_connection()
    cursor = conn.cursor()
    artist_id = name_to_id(artist_name)
    year_input = year
    
    if artist_id == None: 
        print("No artist: ", artist_name, ". Add the artist first.")
        conn.close()
        return
    else:     
        # input validation  
        # check year  
        if year in (None, ""): 
            year_input = None
        else: 
            try:
                year_input = int(year)
                if not(1000 <= year <= datetime.datetime.now().year + 1):
                    print("year out of range")
                    year_input = None
            except ValueError: 
                print("invalid year format")
                return None
                
        # check format
        if record_format in (None, ""): 
            format_input = None
        else: 
            format_input = record_format.strip().upper()
            valid_formats = {"LP", "EP", "7\""}
            if format_input not in valid_formats: 
                print('Format must be one of: LP, EP, 7" (or leave blank)')
                return
        
        try: 
            cursor.execute(
                "INSERT INTO Album (title, artist_id, year, record_format) VALUES(?, ?, ?, ?)", 
                (album_name, artist_id, year_input, format_input)
            )
            conn.commit()
            return cursor.lastrowid
        except sqlite3.IntegrityError: 
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
    
    
def print_all_albums(): 
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute(
        """
        SELECT Album.id, Album.title, Artist.name, Album.year, Album.record_format
        FROM Album
        JOIN Artist ON Album.artist_id = Artist.id
        """)
    print(cursor.fetchall())
    conn.close()
    
def list_albums(artist_name: str):
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute(
        """
        SELECT Album.id, Album.title, Artist.name, Album.year, Album.record_format
        FROM Album
        WHERE Artist.name = ? COLLATE NOCASE
        JOIN Artist ON Album.artist_id = Artist.id
        ORDER BY Artist.name, Album.year
        """
        
    )

    