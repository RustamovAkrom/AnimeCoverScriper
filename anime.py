import requests
from fake_useragent import UserAgent


def anime_scriping(search: str, cover_image_name: str = "original") -> dict:

    context_list = []

    url = f"https://kitsu.io/api/edge/anime?filter[text]={search}"

    headers = {"User-Agent":UserAgent().random}

    response = requests.get(url=url, headers=headers)

    if response.status_code == 200:
        
        data_json = response.json()['data']

        if data_json != []:

            for argument in data_json:
                

                # main
                id = argument['id']
                type = argument['type']
                attributes = argument['attributes'] # json 

                created_at = attributes['createdAt']
                updated_at = attributes['updatedAt']
                description = attributes['description']
                
                cover = ""
                youtube_video = "Now Video"

                # Cover images
                cover_image = attributes['coverImage']
                if cover_image != None:
                    if cover_image[cover_image_name] != None:
                        cover = cover_image[cover_image_name]

                # YouTube video
                if str(attributes['youtubeVideoId']) != "None":
                    youtube_video = "https://www.youtube.com/embed/" + str(attributes['youtubeVideoId']).strip("https://youtu.be/")

                context = {}
                context['id'] = id
                context['type'] = type
                context['created_at'] = created_at
                context['updated_at'] = updated_at
                context['description'] = description
                context['cover'] = cover
                context['youtube_video'] = youtube_video
                
                context_list.append(context)

            return context_list
        
        else:
            return "Now data"
        
    else:
        return int(response.status_code)
    
