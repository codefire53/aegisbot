'''This function will return link of the image of the search query result on wolfram alpha.''' 
import os
from urllib.parse import quote
import requests
def wolfram(keyword):
    #API Id obtained from developer.wolframalpha.com
    app_id=os.getenv('WOLFRAMALPHA_APPID',None)
    #Returning the image link
    return 'https://api.wolframalpha.com/v1/simple?appid={}&i={}'.format(app_id,quote(keyword))
    
