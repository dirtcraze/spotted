from instagrapi import Client
import config as cfg
import sqlite3
import utils
class Bot:
    def __init__(self, login, password, table_name):
        self.cl = Client()
        self.cl.login(login,password)
        self.user_id = self.cl.user_id_from_username(login)
        utils.set_interval(lambda: self.release(table_name), cfg.RELEASE_INTERVAL)
    def upload_photo(self, path, caption):
        self.cl.photo_upload(path, caption)
    def album_upload(self, photos, caption):
        self.cl.album_upload(photos, caption)
    def release(self, table_name):
        self.con = sqlite3.connect("../../db.sqlite3")
        self.cur = self.con.cursor()
        photos = []
        rows = self.cur.execute("SELECT * FROM " + table_name + " WHERE is_posted = 0 ORDER BY created_at ASC LIMIT 5").fetchall()
        if len(rows) == 5:
            for row in rows:
                print(row)
                # create img from string, save it, and add path to list
                photos.append('gymmaster/bot/test.jpg')
                self.cur.execute("UPDATE " + table_name + " SET is_posted = 1 WHERE id = " + str(row[0]))
                self.con.commit()
            self.con.close()
            self.album_upload(photos, "Opis placeholder")


fitnessForLife = Bot(cfg.FITNESSFORLIFE_USERNAME, cfg.FITNESSFORLIFE_PASSWORD, "gymmaster_fitnessforlife")
