from AllMusicScraper import WebScraper
import tweepy
import random

consumer_key_v2 = '3a05FMcHkVVkvQPV1Yseon4Xg'
consumer_secret_v2 ='3tAgKRmWQlxtnDU9XVQZlOq8DKzLzTy7VclM2nkgdKtUhiZWkL'
access_token_v2 = '1529666780129505280-SqhDmYsyvJcaNczw2DSkUtdyLNACk3'
access_token_secret_v2 = 'wH5lfRrWlGfvUBOAs1VAJQMuJ13RoQHWl2jYPvQe977oZ'
bearer_token_v2 = 'AAAAAAAAAAAAAAAAAAAAAIIFdAEAAAAAOQKDPdxW%2FsZkx8C8rlx6yBX0e9M%3D2p6soZJfMKFo1RsHYeSAgcvrCDdcR8mhpQIStowKduXlUn6rUj'

#Selecting a random page number to scrape from.
random_page_number = random.randint(1,20)

url = f"https://www.allmusic.com/advanced-search/results/{random_page_number}"
parser = "html.parser"
element = "td"
class_name = "title"
class_name2 = "artist"
headers = { 
    "host": "www.allmusic.com", 
	"connection": "keep-alive", 
	"accept": "text/html, /; q=0.01", 
	"content-type": "application/x-www-form-urlencoded; charset=UTF-8", 
	"x-requested-with": "XMLHttpRequest", 
	"sec-ch-ua-mobile": "?0", 
	"user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/102.0.5005.63 Safari/537.36", 
	"origin": "https://www.allmusic.com", 
	"sec-fetch-site": "same-origin", 
	"sec-fetch-mode": "cors", 
	"sec-fetch-dest": "empty", 
	"referer": "https://www.allmusic.com/advanced-search", 
	"accept-encoding": "gzip, deflate, br",
	"accept-language": "en-US,en;q=0.9"}

scraper = WebScraper(url,parser,element,class_name,class_name2,headers)

print('\n')
print(f'Page number {random_page_number} has been selected')
print('\n')

scraper.choose_genre(random)
scraper.choose_album()
scraper.album_check()

client = tweepy.Client(bearer_token_v2,consumer_key_v2,consumer_secret_v2,access_token_v2,access_token_secret_v2)


sample = random.sample(scraper.album_names,5)

#Using the print statement to make sure albums were successfully selected before posting our tweet.
# print(f'The 5 albums of the hour:\n1. {sample[0]}\n2. {sample[1]}\n3. {sample[2]}\n4. {sample[3]}\n5. {sample[4]}\n')

client.create_tweet(text = f'The 5 albums of the hour:\n1. {sample[0]}\n2. {sample[1]}\n3. {sample[2]}\n4. {sample[3]}\n5. {sample[4]}\n')