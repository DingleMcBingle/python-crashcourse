def make_album(album_artist, album_title, album_tracks=''):
    """returns an album artist and title."""
    album = {'artist': album_artist, 'title':album_title}
    if album_tracks:
        album['tracks'] = album_tracks
    return album

album1 = make_album('Queen','Jazz','13')
print(album1)

