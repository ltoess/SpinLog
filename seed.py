import sqlite3

import db


def seed_data(): 
    try: 
        with db.get_connection() as conn: 
            print("seeding database")
            db.insert_artist(conn, "Frank Sinatra")
            db.insert_album(conn, "In the Wee Small Hours", "Frank Sinatra", 1955, "LP")


            db.insert_artist(conn, "Mac Demarco")
            db.insert_album(conn, "Guitar", "Mac Demarco", 2025, "LP")
            db.insert_album(conn, "Another One", "Mac Demarco", 2015, "LP")

            db.insert_artist(conn, "Elijah Fox")
            db.insert_album(conn, "Wyoming", "Elijah Fox", 2023, "LP")

            db.insert_artist(conn, "Laufey")
            db.insert_album(conn, "Bewitched", "Laufey", 2022, "LP")

            db.insert_artist(conn, "Pink Floyd")
            db.insert_album(conn, "The Dark Side of the Moon", "Pink Floyd", 1975, "LP")
            print("seed complete")
    except (sqlite3.IntegrityError, ValueError) as e: 
        print(f"An error occurred while seeding: {e}")

if __name__ == "__main__":
    seed_data()

