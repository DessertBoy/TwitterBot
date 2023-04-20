from AllMusicScraper_v2 import WebScraper
import tweepy
from random import randint,sample

#Twitter Credentials
consumer_key_v2 = 'Your consumer key'
consumer_secret_v2 ='Your consumer secret'
access_token_v2 = 'Your access token'
access_token_secret_v2 = 'You access token secret'
bearer_token_v2 = 'bearer token'


random_page_number = randint(1,20) #Selecting a random page number to scrape from.


#WebScraper paramaters
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


def main():
    try:
        scraper = WebScraper(url,parser,element,class_name,class_name2,headers)

        print('\n')
        print(f'Page number {random_page_number} has been selected')
        print('\n')

        scraper.choose_genre() #selecting a sub genre from our parent genre
        scraper.album_check() #checking that the genre selected has albums available
    
        client = tweepy.Client(bearer_token_v2,consumer_key_v2,consumer_secret_v2,access_token_v2,access_token_secret_v2)  #Twitter Authorization

        
        random_albums = sample(scraper.album_names,5) #Randomly selecting album names

        #Using the print statement to make sure albums were successfully selected before posting our tweet.
        print(f'The 5 albums of the hour:\n1. {random_albums[0]}\n2. {random_albums[1]}\n3. {random_albums[2]}\n4. {random_albums[3]}\n5. {random_albums[4]}\n')

        # client.create_tweet(text = f'The 5 albums of the hour:\n1. {sample[0]}\n2. {sample[1]}\n3. {sample[2]}\n4. {sample[3]}\n5. {sample[4]}\n')

    except:
        print("An error has occured. Please review/test code.")
        return

if __name__ == "__main__":
    main()