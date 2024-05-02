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
