import pdb
from models.album import Album
from models.artist import Artist

import repositories.album_repo as album_repo
import repositories.artist_repo as artist_repo

artist_repo.delete_all()
album_repo.delete_all()

artist1 = Artist("Beatles")
artist_repo.save(artist1)
artist2 = Artist("Elton")
artist_repo.save(artist2)

artist_repo.select(1)

album = Album("Hello", "Pop", artist1)
album_repo.save(album)

album_repo.select_all()

for album in album_repo.select_all():
    print(album.__dict__)
pdb.set_trace()

