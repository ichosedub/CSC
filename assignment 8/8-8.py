def make_album(artist, title, songs = None):
    album_creator = {
        'artist': artist.title(),
        'title': title.title()}
    if songs:
        album_creator['songs'] = songs
    return album_creator

print(make_album("XXXTENTACION", "?", 18))
print(make_album("Trippie Redd", "A Love Letter To You 3", 16))
print (make_album("Polo G", "Die a Legned", 14))