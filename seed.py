import sqlite3

import db

# small seed to recreate test data quickly
db.insert_artist("Frank Sinatra")
db.insert_album("In the Wee Small Hours", "Frank Sinatra", 1955, "LP")


db.insert_artist("Mac Demarco")
db.insert_album("Guitar", "Mac Demarco", 2025, "LP")
db.insert_album("Another One", "Mac Demarco", 2015, "LP")

db.insert_artist("Elijah Fox")
db.insert_album("Wyoming", "Elijah Fox", 2023, "LP")

db.insert_artist("Laufey")
db.insert_album("Bewitched", "Laufey", 2022, "LP")

db.insert_artist("Pink Floyd")
db.insert_album("The Dark Side of the Moon", "Pink Floyd", 1975, "LP")
