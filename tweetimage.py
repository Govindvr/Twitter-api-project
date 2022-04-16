import os
import tweepy
from PIL import Image, ImageDraw, ImageFont
from dotenv import load_dotenv

load_dotenv() 
bearer_token = os.getenv("bearer_token")
client = tweepy.Client(bearer_token=bearer_token)

url = input("Enter the url: ")

url_elements = url.split('/')

tweet_id = url_elements[-1]

response = client.get_tweet(id=tweet_id)


text = response.data.text

image = Image.open('background.png')

draw = ImageDraw.Draw(image)
lines = []
font = ImageFont.truetype(font = "arial.ttf",size=25)
delim = [' ','. ',',','#']
while(len(text)>80):
    l = 80

    while(True):
        if(text[l] in delim):
            lines.append(text[0:l+1])
            text = text[l+1:]
            break
        else:
            l -=1


lines.append(text)

(x,y) = (50,image.height/4)

for line in lines:
    draw.text((x,y),line,("white"),font=font)
    y += 50

image.save("result.jpg")