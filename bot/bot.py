from instagrapi import Client
import config as cfg
import sqlite3
from pillow.pillow import create_image
import utils


class Bot:
    def __init__(self, login, password, table_name):
        self.cl = Client()
        self.cl.login(login, password)
        self.user_id = self.cl.user_id_from_username(login)
        utils.set_interval(lambda: self.release(
            table_name), cfg.RELEASE_INTERVAL)

    def upload_photo(self, path, caption):
        self.cl.photo_upload(path, caption)

    def album_upload(self, photos, caption):
        self.cl.album_upload(photos, caption)

    def release(self, table_name):
        self.con = sqlite3.connect("../spottedmaster/db.sqlite3")
        self.cur = self.con.cursor()
        photos = []
        rows = self.cur.execute("SELECT * FROM " + table_name +
                                " WHERE is_posted = 0 ORDER BY created_at ASC LIMIT 5").fetchall()
        if len(rows) == 5:
            for row in rows:
                print(row)
                path = create_image(
                    row[1], row[3][row[3].find(" "):row[3].rfind(":")], row[0])
                photos.append(path)
                self.cur.execute("UPDATE " + table_name +
                                 " SET is_posted = 1 WHERE id = " + str(row[0]))
                self.con.commit()
            self.con.close()
            self.album_upload(photos, "Opis placeholder")


fitnessForLife = Bot(cfg.FITNESSFORLIFE_USERNAME,
                     cfg.FITNESSFORLIFE_PASSWORD, "gymmaster_fitnessforlife")
