def make_album(album_artist, album_title, album_tracks=''):
    """returns an album artist and title."""
    album = {'artist': album_artist, 'title':album_title}
    if album_tracks:
        album['tracks'] = album_tracks
    return album

active = True
while active:
    artist_name = input("Who made the album?")
    album_name = input("What is the name of the album?")
    album1 = make_album(artist_name, album_name)
    print(album1)
    active = False



