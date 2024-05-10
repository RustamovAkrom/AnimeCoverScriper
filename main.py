from anime import anime_scriping
from multiprocessing import Process
import requests
import os

def add_data(search: str):
    response = anime_scriping(search)

    path = "data/"
    if not os.path.exists(path):
        os.mkdir(path)

    for i in response:
        cover = str(i['cover'])
        if cover:
            with open(f"{path}{i['id']}.jpg", 'wb') as file:
                
                get_cover = requests.get(cover)
                file.write(get_cover.content)

    

if __name__=="__main__":
    ls = []

    
    prosess = Process(target=add_data, args=('Nobana', ))
    prosess.start()
    prosess.join()

    # for i in ls:
    #     i.join()
    
    
                    
    