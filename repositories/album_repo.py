from db.run_sql import run_sql

from models.album import Album
from models.artist import Artist
import repositories.artist_repo as artist_repo

def save(album):
    sql = "INSERT INTO albums (title, genre, artist_id) VALUES (%s, %s, %s) RETURNING *"
    values = [album.title, album.genre, album.artist_id]
    results = run_sql(sql, values)
    id = results[0]['id']
    album.id = id
    return album


def select_all():
    albums = []

    sql = "SELECT * FROM albums"
    results = run_sql(sql)

    for row in results:
        artist = artist_repo.select(row['artist_id'])
        albmum = Album(row['title'], user, row['genre'], row['id'] )
        albums.append(album)
    return albums


def select(id):
    album = None
    sql = "SELECT * FROM tasks WHERE id = %s"
    values = [id]
    result = run_sql(sql, values)[0]

    if result is not None:
        aritst = artist_repo.select(result['user_id'])
        album = Album(result['title'], result['genre'], result['id'])
    return task


def delete_all():
    sql = "DELETE  FROM albums"
    run_sql(sql)


def delete(id):
    sql = "DELETE  FROM albums WHERE id = %s"
    values = [id]
    run_sql(sql, values)


def update(album):
    sql = "UPDATE albums SET (title, genre, user_id) = (%s, %s, %s) WHERE id = %s"
    values = [album.title, album.genre, album.user_id]
    run_sql(sql, values)

