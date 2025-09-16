import db


def filter_albums(artist_name: str):
    albums = db.list_albums(artist_name)
    if albums:
        for album_id, title, artist, year, fmt in albums:
            year_display = year if year else "Unknown Year"
            fmt_display = fmt if fmt else "Unknown Format"
            print(f"[{album_id}] {title} — {artist} ({year_display}, {fmt_display})")
    else:
        print("No albums found for that artist.")




filter_albums("Frank Sinatra")