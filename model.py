import requests

def getImageUrlFrom(query, key):
    giphy_query=f"https://api.giphy.com/v1/gifs/search?api_key={key}&q={query}&limit=25&offset=0&rating=g&lang=en"

    # get is a method in the requests module
    response = requests.get(giphy_query).json()
    # print(response)
    
    source = response['data'][2]['images']['fixed_width']['url']
    print(source)
    
    # Until I actually get an image, will return knwon pic
    # test = "/static/images/micropig.jpg"
    return source
    