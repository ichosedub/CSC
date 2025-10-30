def make_album(artist, title, songs):
    album_creator = {
        'artist': artist.title(),
        'title': title.title(), 
        'songs': songs
    }
    return album_creator

print(make_album("XXXTENTACION", "?", "18 tracks"))
print(make_album("Trippie Redd", "A Love Letter To You 3", "16 tracks"))
print (make_album("Polo G", "Die a Legned", "14 tracks"))