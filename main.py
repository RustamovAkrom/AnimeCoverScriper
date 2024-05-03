from anime import anime_scriping
from multiprocessing import Process
import requests
import os


if __name__=="__main__":

    response = anime_scriping(input("Search anime type --> "))

    if response != "Now data":
        for response in response:
            cover = response['cover']
            
            if cover != "":
                response_cover = requests.get(cover)
                
                dir = "data/"
                if not os.path.exists(dir):
                    os.mkdir(dir)

                file = str(response['type']) + "_" +response['id'] + ".jpg"

                with open(dir + file, "wb") as file_wb:
                    file_wb.write(response_cover.content)
                    
    # proccess = Process(target=main)
    # proccess.start()

    


# if response != "Now data":
        
#         for response in response:
#             id = int(response['id'])
#             type = str(response['type'])
#             created_at = str(response['created_at'])
#             updated_at = str(response['updated_at'])
#             description = str(response['description'])
#             cover = str(response['cover'])
#             youtube_video = str(response['youtube_video'])

#             data = {
#                 "id":id,
#                 "type":type,
#                 "created_at":created_at,
#                 "updated_at":updated_at,
#                 "description":description,
#                 "cover":cover,
#                 "video":youtube_video
#             }