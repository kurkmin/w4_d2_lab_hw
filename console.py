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


album = Album("Hello", "Pop")
album_repo.save(album)

album_repo.select_all()

pdb.set_trace()

