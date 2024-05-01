from anime import anime_scriping
from db import DBConnection


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

            connection.add_image(image_id = id, image_type = type,
                                 created_at = created_at, updated_at = updated_at,
                                 description = description, cover = cover,
                                 youtube_video = youtube_video)
            

if __name__=="__main__":
    connection = DBConnection()
    connection.create_all_tables()
    
    main()