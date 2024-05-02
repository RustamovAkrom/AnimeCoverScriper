from anime import anime_scriping
from db import DBConnection
import json


def appender_on_json_file(filename: str, data: dict):
    with open(filename, "w") as json_file:
        json.dump(data, json_file, indent=4)

    
def main():
    
    response = anime_scriping(input("Search anime type --> "))

    if response != "Now data":

        for response in response:
            id = int(response['id'])
            type = str(response['type'])
            created_at = str(response['created_at'])
            updated_at = str(response['updated_at'])
            description = str(response['description'])
            cover = str(response['cover'])
            youtube_video = str(response['youtube_video'])

            data = {
                "id":id,
                "type":"type",
                "created_at":created_at,
                "updated_at":updated_at,
                "description":description,
                "cover":cover,
                "video":youtube_video
            }
            print(data)
            # appender_on_json_file("data.json", data)
            # connection.add_image(image_id = id, image_type = type,
            #                      created_at = created_at, updated_at = updated_at,
            #                      description = description, cover = cover,
            #                      youtube_video = youtube_video)
            

if __name__=="__main__":
    # connection = DBConnection()
    # connection.create_all_tables()
    
    main()