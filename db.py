import datetime
import sqlite3

DB_FILE = "spinlog.db"

def get_connection():
    conn = sqlite3.connect(DB_FILE)
    conn.execute("PRAGMA foreign_keys = ON;") # foreign key enforcement
    return conn

def name_to_artist_id(conn, name: str): 
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

def name_to_album_id(conn, name: str): 
    cursor = conn.cursor()
    
    cursor.execute(
        """
        SELECT id
        FROM Album
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

def insert_artist(conn, name: str):
    cursor = conn.cursor()
    try: 
        cursor.execute("INSERT INTO Artist (name) VALUES(?)", (name,))
        conn.commit()
        return cursor.lastrowid
    except sqlite3.IntegrityError:
        print(f"Artist '{name}' already exists")
    finally: 
        conn.close()
        
def insert_album(conn, album_name: str, artist_name: str, year, record_format: str): 
    cursor = conn.cursor()
    artist_id = name_to_artist_id(artist_name)
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
            print(f"Album '{album_name}' by '{artist_name}' already exists.")
        finally: 
            conn.close()
            
def insert_pressing(conn, album_name: str, catalog_number: str, rpm: int, year: int, ): 
    cursor = conn.cursor()
    # album_id = name_to_album_id(album_name)
    
def print_all_artists(conn):
    cursor = conn.cursor()
    cursor.execute("""
               SELECT *
               FROM Artist               
               """)
    print(cursor.fetchall())
    conn.close()
    
    
def print_all_albums(conn): 
    cursor = conn.cursor()
    cursor.execute(
        """
        SELECT Album.id, Album.title, Artist.name, Album.year, Album.record_format
        FROM Album
        JOIN Artist ON Album.artist_id = Artist.id
        """)
    rows = cursor.fetchall()
    conn.close()
    return rows 
    
    
# returns an array of album entries from specified artist 
def list_albums(conn, artist_name: str):
    cursor = conn.cursor()
    cursor.execute(
        """
        SELECT Album.id, Album.title, Artist.name, Album.year, Album.record_format
        FROM Album
        JOIN Artist ON Album.artist_id = Artist.id
        WHERE Artist.name = ? COLLATE NOCASE
        ORDER BY Artist.name, Album.year
        """
        , (artist_name,)
    )
    rows = cursor.fetchall()
    conn.close
    return rows

    