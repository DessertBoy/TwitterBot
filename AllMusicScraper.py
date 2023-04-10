from bs4 import BeautifulSoup as bs
import requests

""" 
Creating a class to scrape albums and artist names from allmusic.com

bs4 documentation: https://beautiful-soup-4.readthedocs.io/en/latest/
requests documentation: https://requests.readthedocs.io/en/latest/user/quickstart/

"""

class WebScraper:

    def __init__(self,url,parser,element,class_name,class_name2,headers):
        """
        This class will scrape random albums from four different parent genres (Electronic,Rock, Rap, and Latin) and their sub genres from allmusic.com.
        For this class it is highly recommended you understand basic HTML in case you'd like to implement more genres.

        The wesbite we are scrapping music from (allmusic.com) is an AJAX website. We will need to send a post request straight to the database where this website retrieves its data from.

        The headers will be found in the main.py file. In order to find the headers for the POST request we need to right click on the page after you've selected a genre (https://www.allmusic.com/advanced-search) and select Inspect > Network.
        Once you are in the Networks section, in the search bar search for "results" and you will get a list of requests (if nothing appears refresh the page or click on your genre with the Network tab open). 

        To find the genre header, search for your request by searching "results" in the Network search bar, and click on your "results" request. Once you click on your request a new window will appear. It will have the
        headers of "Header", "Payload", "Preview", "Response", "Initiator", "Timing", and "Cookies". To find the genre header click on "Payload". A window will open up that looks like this:
        *filters[]: some ID
        *filter[]: The rest of the ID (this is a continuation of the first filters [])
        *sort:

        Go ahead and click on the column next to it, "view source", and the ID there will be your genre filter. Copy that and paste that as the genre_filter variable.

        The last thing you need to do is copy the headers from "Request Headers". You will be using these headers when you send out your request. We are extracting the data from the same source allmusic.com imports it's data from.
        The only headers that I use are "host", "connection","accept","content-type","x-requested-with","sec-ch-ua-mobile","user-agent","origin","sec-fetch-site","sec-fetch-mode","sec-fetch-dest","referer", "accept-encoding", and
        "accept-language".

        url: The url of the website we will be scrapping
        parser: The type of parser we will be using
        element: HTTP element
        class_name: name of the HTTP element class
        class_name2: name of the HTTP element class
        genre: the genre we are extracting music from
        discography: a dictionary containing all the artist and albums that were scraped
        album_names: a list containing the names of the albums scraped

        """

        self.url = url
        self.parser = parser
        self.element = element
        self.class_name = class_name
        self.class_name2 = class_name2
        self.headers = headers
        self.genre = None
        self.discography = None
        self.album_names = []

    def choose_genre(self,random):
        """
        This function will help us select a random genre from our four parent genre.
        """

        electronic = {'Acid House':'filters%5B%5D=%26subgenre%3DMA0000005001&filters%5B%5D=%26subgenreBooleanOperator%3DOR&sort=',
                    'Chicago House':'filters%5B%5D=%26subgenre%3DMA0000002507&filters%5B%5D=%26subgenreBooleanOperator%3DOR&sort=',
                    'Deep House':'filters%5B%5D=%26subgenre%3DMA0000013621&filters%5B%5D=%26subgenreBooleanOperator%3DOR&sort=',
                    'dubstep':'filters%5B%5D=%26subgenre%3DMA0000004465&filters%5B%5D=%26subgenreBooleanOperator%3DOR&sort=',
                    'House':'filters%5B%5D=%26subgenre%3DMA0000002651&filters%5B%5D=%26subgenreBooleanOperator%3DOR&sort=',
                    'French House':'filters%5B%5D=%26subgenre%3DMA0000013529&filters%5B%5D=%26subgenreBooleanOperator%3DOR&sort=',
                    'Progressive House':'filters%5B%5D=%26subgenre%3DMA0000005002&filters%5B%5D=%26subgenreBooleanOperator%3DOR&sort=',
                    'Techno':'filters%5B%5D=%26subgenre%3DMA0000002893&filters%5B%5D=%26subgenreBooleanOperator%3DOR&sort=',
                    'Trance':'filters%5B%5D=%26subgenre%3DMA0000002903&filters%5B%5D=%26subgenreBooleanOperator%3DOR&sort=',
                    'Vapor Wave':'filters%5B%5D=%26subgenre%3DMA0000013555&filters%5B%5D=%26subgenreBooleanOperator%3DOR&sort='}

        rock = {'British Psychedelia':'filters%5B%5D=%26subgenre%3DMA0000012038&filters%5B%5D=%26subgenreBooleanOperator%3DOR&sort=',
                'Emo':'filters%5B%5D=%26subgenre%3DMA0000004447&filters%5B%5D=%26subgenreBooleanOperator%3DOR&sort=',
                'Glam Rock':'filters%5B%5D=%26subgenre%3DMA0000002619&filters%5B%5D=%26subgenreBooleanOperator%3DOR&sort=',
                'Heavy Metal':'filters%5B%5D=%26subgenre%3DMA0000002721&filters%5B%5D=%26subgenreBooleanOperator%3DOR&sort=',
                'Indie':'filters%5B%5D=%26subgenre%3DMA0000004453&filters%5B%5D=%26subgenreBooleanOperator%3DOR&sort=',
                'Latin Rock':'filters%5B%5D=%26subgenre%3DMA0000011908&filters%5B%5D=%26subgenreBooleanOperator%3DOR&sort=',
                'New Wave':'filters%5B%5D=%26subgenre%3DMA0000002750&filters%5B%5D=%26subgenreBooleanOperator%3DOR&sort=',
                'Post Punk':'filters%5B%5D=%26subgenre%3DMA0000004450&filters%5B%5D=%26subgenreBooleanOperator%3DOR&sort=',
                'Pyschedelic':'filters%5B%5D=%26subgenre%3DMA0000013414&filters%5B%5D=%26subgenreBooleanOperator%3DOR&sort=',
                'Punk':'filters%5B%5D=%26subgenre%3DMA0000002806&filters%5B%5D=%26subgenreBooleanOperator%3DOR&sort='}

        rap = {'Alternative Rap':'filters%5B%5D=%26subgenre%3DMA0000012203&filters%5B%5D=%26subgenreBooleanOperator%3DOR&sort=',
            'Dirty South':'filters%5B%5D=%26subgenre%3DMA0000011851&filters%5B%5D=%26subgenreBooleanOperator%3DOR&sort=',
            'East Coast':'filters%5B%5D=%26subgenre%3DMA0000002563&filters%5B%5D=%26subgenreBooleanOperator%3DOR&sort=',
            'Gangster Rap':'filters%5B%5D=%26subgenre%3DMA0000002611&filters%5B%5D=%26subgenreBooleanOperator%3DOR&sort=',
            'Instrumental HipHop':'filters%5B%5D=%26subgenre%3DMA0000013592&filters%5B%5D=%26subgenreBooleanOperator%3DOR&sort=',
            'Jazz Rap':'filters%5B%5D=%26subgenre%3DMA0000012180&filters%5B%5D=%26subgenreBooleanOperator%3DOR&sort=',
            'Latin Rap':'filters%5B%5D=%26subgenre%3DMA0000002696&filters%5B%5D=%26subgenreBooleanOperator%3DOR&sort=',
            'OldSchool Rap':'filters%5B%5D=%26subgenre%3DMA0000002762&filters%5B%5D=%26subgenreBooleanOperator%3DOR&sort=',
            'Trap':'filters%5B%5D=%26subgenre%3DMA0000013576&filters%5B%5D=%26subgenreBooleanOperator%3DOR&sort=',
            'West Coast':'filters%5B%5D=%26subgenre%3DMA0000002932&filters%5B%5D=%26subgenreBooleanOperator%3DOR&sort='}

        latin = {'Bachata':'filters%5B%5D=%26subgenre%3DMA0000002441&filters%5B%5D=%26subgenreBooleanOperator%3DOR&sort=',
                'Banda':'filters%5B%5D=%26subgenre%3DMA0000002447&filters%5B%5D=%26subgenreBooleanOperator%3DOR&sort=',
                'Corrido':'filters%5B%5D=%26subgenre%3DMA0000011893&filters%5B%5D=%26subgenreBooleanOperator%3DOR&sort=',
                'Cumbia':'filters%5B%5D=%26subgenre%3DMA0000002541&filters%5B%5D=%26subgenreBooleanOperator%3DOR&sort=',
                'Electro Cumbia':'filters%5B%5D=%26subgenre%3DMA0000013579&filters%5B%5D=%26subgenreBooleanOperator%3DOR&sort=',
                'Latin Dance':'filters%5B%5D=%26subgenre%3DMA0000002694&filters%5B%5D=%26subgenreBooleanOperator%3DOR&sort=',
                'Latin Pop':'filters%5B%5D=%26subgenre%3DMA0000004461&filters%5B%5D=%26subgenreBooleanOperator%3DOR&sort=',
                'Latin Soul':'filters%5B%5D=%26subgenre%3DMA0000012248&filters%5B%5D=%26subgenreBooleanOperator%3DOR&sort=',
                'Reggaeton':'filters%5B%5D=%26subgenre%3DMA0000002976&filters%5B%5D=%26subgenreBooleanOperator%3DOR&sort=',
                'Sonidera':'filters%5B%5D=%26subgenre%3DMA0000002783&filters%5B%5D=%26subgenreBooleanOperator%3DOR&sort='}
        
        genres = [electronic,
          rock,
          rap,
          latin]

        parent_genre = random.choice(genres)

        chosen_genre = random.choice(list(parent_genre.keys()))

        self.genre = parent_genre[chosen_genre]

        print(f'The genre that was chosen was {chosen_genre}')
        print('\n')

        return self.genre

    def scrape(self):
        """
        This scrape method will help us scrape https://www.allmusic.com/advanced-search.

        """

        artist_album = {}

        s = requests.Session()

        #Sending our genre filter and headers to the databse allmusic.com recieves its data from.
        response = s.post(self.url, data = self.genre, headers = self.headers)

        #Parsing the data that is returned
        soup = bs(response.content,self.parser)

        #Looking for album titles and album artists
        titles = soup.find_all(self.element,self.class_name)
        artist = soup.find_all(self.element,self.class_name2)

        #Creating a dictionary with the artist as the key and album as the value/item.
        for i in range(len(titles)):
            try:
                #If an artist has multiple albums we want to make sure to include them as well
                if artist[i].contents[1].contents[0] in artist_album.keys():
                    artist_album[artist[i].contents[1].contents[0]].append(titles[i].contents[1].contents[0])
                else:
                    artist_album[artist[i].contents[1].contents[0]] = [titles[i].contents[1].contents[0]]
            except:
                #Artist that are labled as "Various Artists" will not be included. It is too vague and will not be found on Spotify.
                print('We do not include artists with the name "Various Artists"')
                print('\n')


        return artist_album
    
    def album_check(self):
        """
        This album_check method will help us check whether there is currently any albums available for our genre. If no albums are available for the genre that was chosen, we will re-run our choose_genre,
        scrpae, and choose_album methods until we select a genre that has albums available.
        """
        print("Checking album list...")

        empty_genre = False

        #Checking to see if the album list is empty. If it is empty we want to re-run our code.
        if not self.album_names:
            print("It seems there is no albums currently available for the genre chosen. Re-running code...")
            print('\n')
            empty_genre = True
        else:
            print("Album list is good to go!")
            print('\n')
            empty_genre = False

        #If the album list is empty we will re-select a new genre until a genre returns a list of albums.
        while empty_genre == True:
            self.choose_genre()
            self.scrape()
            self.choose_album()

            if self.album_names:
                empty_genre = False

    
    def choose_album(self):
         """
         This choose_album method will select
         """
         self.discography = self.scrape()
         
         for artist,album in self.discography.items():
            for name in album:
                self.album_names.append(f'{name} by {artist}')

    
    def album_search(self):
        """
        

        

        random_page_number: The page number our scrapper will scrape from.
        parser: The type of parser we will be using
        element: HTTP element
        class_name: name of the HTTP element class
        class_name2: name of the HTTP element class
        """

        #Assigning the random page number that we will be scraping from


        #To change the headers you are going to have to go back to the website and inspect the page again, depending on the genre you want. You will find the filter in Inspect>Network>
        #On the search bar search for "results" and click on "results/". From there a window will pop up, click on the "Payload" tab, and click on "view source".


        # return discography