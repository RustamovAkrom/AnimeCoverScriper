import sqlite3


CREATE_TABLE_IMAGES = """
CREATE TABLE IF NOT EXISTS images(
id INTEGER PRIMARY KEY, 
image_id INTEGER,
image_type TEXT,
created_at DATE,
updated_at DATE,
description TEXT,
cover TEXT UNIQUE,
youtube_video TEXT UNIQUE
)
"""

ADD_TO_IMAGES = """
INSERT INTO images( image_id, image_type, 
                    created_at, updated_at, 
                    description, cover, 
                    youtube_video )
VALUES (?, ?, ?, ?, ?, ?, ?)
"""

GET_ALL_IMAGES = """
SELECT * FROM images
"""


class DBConnection:
    def __init__(self) -> None:
        self.connection = sqlite3.connect("database.db")
        self.cursore = self.connection.cursor()

    def create_all_tables(self):
        self.cursore.execute(CREATE_TABLE_IMAGES)
        self.connection.commit()

    def add_image(self, image_id, image_type, created_at, updated_at, description, cover, youtube_video):

        try:
            self.cursore.execute(ADD_TO_IMAGES, (image_id, image_type, 
                                                created_at, updated_at, 
                                                description, cover,
                                                youtube_video))
            self.connection.commit()
            print("Add image")
        
        except:
            print("Is data already exists!")
        

    def get_all_images(self):
        return self.cursore.execute(GET_ALL_IMAGES).fetchall()


# con = DBConnection()
# con.create_all_tables()
# boolean = con.add_image(7393, 'animes', '2013-02-20T17:55:09.608Z', '2024-05-01T12:00:16.756Z', 'tive story about a murder on a train based on a series of young-adult novels for women by Yamaura Hiroyasu. Seiko, while suspended from school (she has been bullied) goes to Nagasaki, where she finds herself involved in a murder mystery. \n(Source: Shoujo &amp; General Weblog)', '', 'Now Video')

# print(boolean)