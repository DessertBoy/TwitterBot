from bs4 import BeautifulSoup as bs
import requests
from random import choice


class WebScraper:

    def __init__(self,url:str,parser:str,element:str,class_name:str,class_name2:str,headers:dict):
        """
        This class will scrape AllMusic.com and randomly select albums from our sub genres listed under our four parent genres.
        """
        self.url = url
        self.parser = parser    
        self.element = element
        self.class_name = class_name
        self.class_name2 = class_name2
        self.headers = headers
        self.genre = None

    def choose_genre(self) -> str:
        """
        Select a random genre from limited set of genres
        """

        electronic = {"Acid House":"filters%5B%5D=%26subgenre%3DMA0000013621&filters%5B%5D=%26subgenreBooleanOperator%3DOR&sort=",
                    "Chicago House":"filters%5B%5D=%26subgenre%3DMA0000002507&filters%5B%5D=%26subgenreBooleanOperator%3DOR&sort=",
                    "Deep House":"filters%5B%5D=%26subgenre%3DMA0000013621&filters%5B%5D=%26subgenreBooleanOperator%3DOR&sort=",
                    "Dubstep":"filters%5B%5D=%26subgenre%3DMA0000004465&filters%5B%5D=%26subgenreBooleanOperator%3DOR&sort=",
                    "House":"filters%5B%5D=%26subgenre%3DMA0000002651&filters%5B%5D=%26subgenreBooleanOperator%3DOR&sort=",
                    "French House":"filters%5B%5D=%26subgenre%3DMA0000013529&filters%5B%5D=%26subgenreBooleanOperator%3DOR&sort=",
                    "Progressive House":"filters%5B%5D=%26subgenre%3DMA0000005002&filters%5B%5D=%26subgenreBooleanOperator%3DOR&sort=",
                    "Techno":"filters%5B%5D=%26subgenre%3DMA0000002893&filters%5B%5D=%26subgenreBooleanOperator%3DOR&sort=",
                    "Trance":"filters%5B%5D=%26subgenre%3DMA0000002903&filters%5B%5D=%26subgenreBooleanOperator%3DOR&sort=",
                    "Vapor Wave":"filters%5B%5D=%26subgenre%3DMA0000013555&filters%5B%5D=%26subgenreBooleanOperator%3DOR&sort="}

        rock = {"British Psychedelia":"filters%5B%5D=%26subgenre%3DMA0000012038&filters%5B%5D=%26subgenreBooleanOperator%3DOR&sort=",
                "Emo":"filters%5B%5D=%26subgenre%3DMA0000004447&filters%5B%5D=%26subgenreBooleanOperator%3DOR&sort=",
                "Glam Rock":"filters%5B%5D=%26subgenre%3DMA0000002619&filters%5B%5D=%26subgenreBooleanOperator%3DOR&sort=",
                "Heavy Metal":"filters%5B%5D=%26subgenre%3DMA0000002721&filters%5B%5D=%26subgenreBooleanOperator%3DOR&sort=",
                "Indie":"filters%5B%5D=%26subgenre%3DMA0000004453&filters%5B%5D=%26subgenreBooleanOperator%3DOR&sort=",
                "Latin Rock":"filters%5B%5D=%26subgenre%3DMA0000011908&filters%5B%5D=%26subgenreBooleanOperator%3DOR&sort=",
                "New Wave":"filters%5B%5D=%26subgenre%3DMA0000002750&filters%5B%5D=%26subgenreBooleanOperator%3DOR&sort=",
                "Post Punk":"filters%5B%5D=%26subgenre%3DMA0000004450&filters%5B%5D=%26subgenreBooleanOperator%3DOR&sort=",
                "Pyschedelic":"filters%5B%5D=%26subgenre%3DMA0000013414&filters%5B%5D=%26subgenreBooleanOperator%3DOR&sort=",
                "Punk":"filters%5B%5D=%26subgenre%3DMA0000002806&filters%5B%5D=%26subgenreBooleanOperator%3DOR&sort="}

        rap = {"Alternative Rap":"filters%5B%5D=%26subgenre%3DMA0000012203&filters%5B%5D=%26subgenreBooleanOperator%3DOR&sort=",
            "Dirty South":"filters%5B%5D=%26subgenre%3DMA0000011851&filters%5B%5D=%26subgenreBooleanOperator%3DOR&sort=",
            "East Coast":"filters%5B%5D=%26subgenre%3DMA0000002563&filters%5B%5D=%26subgenreBooleanOperator%3DOR&sort=",
            "Gangster Rap":"filters%5B%5D=%26subgenre%3DMA0000002611&filters%5B%5D=%26subgenreBooleanOperator%3DOR&sort=",
            "Instrumental HipHop":"filters%5B%5D=%26subgenre%3DMA0000013592&filters%5B%5D=%26subgenreBooleanOperator%3DOR&sort=",
            "Jazz Rap":"filters%5B%5D=%26subgenre%3DMA0000012180&filters%5B%5D=%26subgenreBooleanOperator%3DOR&sort=",
            "Latin Rap":"filters%5B%5D=%26subgenre%3DMA0000002696&filters%5B%5D=%26subgenreBooleanOperator%3DOR&sort=",
            "OldSchool Rap":"filters%5B%5D=%26subgenre%3DMA0000002762&filters%5B%5D=%26subgenreBooleanOperator%3DOR&sort=",
            "Trap":"filters%5B%5D=%26subgenre%3DMA0000013576&filters%5B%5D=%26subgenreBooleanOperator%3DOR&sort=",
            "West Coast":"filters%5B%5D=%26subgenre%3DMA0000002932&filters%5B%5D=%26subgenreBooleanOperator%3DOR&sort="}

        latin = {"Bachata":"filters%5B%5D=%26subgenre%3DMA0000002441&filters%5B%5D=%26subgenreBooleanOperator%3DOR&sort=",
                "Banda":"filters%5B%5D=%26subgenre%3DMA0000002447&filters%5B%5D=%26subgenreBooleanOperator%3DOR&sort=",
                "Corrido":"filters%5B%5D=%26subgenre%3DMA0000011893&filters%5B%5D=%26subgenreBooleanOperator%3DOR&sort=",
                "Cumbia":"filters%5B%5D=%26subgenre%3DMA0000002541&filters%5B%5D=%26subgenreBooleanOperator%3DOR&sort=",
                "Electro Cumbia":"filters%5B%5D=%26subgenre%3DMA0000013579&filters%5B%5D=%26subgenreBooleanOperator%3DOR&sort=",
                "Latin Dance":"filters%5B%5D=%26subgenre%3DMA0000002694&filters%5B%5D=%26subgenreBooleanOperator%3DOR&sort=",
                "Latin Pop":"filters%5B%5D=%26subgenre%3DMA0000004461&filters%5B%5D=%26subgenreBooleanOperator%3DOR&sort=",
                "Latin Soul":"filters%5B%5D=%26subgenre%3DMA0000012248&filters%5B%5D=%26subgenreBooleanOperator%3DOR&sort=",
                "Reggaeton":"filters%5B%5D=%26subgenre%3DMA0000002976&filters%5B%5D=%26subgenreBooleanOperator%3DOR&sort=",
                "Sonidera":"filters%5B%5D=%26subgenre%3DMA0000002783&filters%5B%5D=%26subgenreBooleanOperator%3DOR&sort="}
        
        genres = [electronic,
          rock,
          rap,
          latin]

        
        parent_genre = choice(genres) #Randomly choosing one of our four parent genres
        
        
        chosen_genre = choice(list(parent_genre.keys())) #Choosing a sub genre

        self.genre = parent_genre[chosen_genre]

        print(f"The genre that was chosen was {chosen_genre}")
        print("\n")
        
        
        try: #If there is a some sort of error connecting to allmusic.com an error message will be returned.
            self.album_names = [f"{name} by {artist}" for artist,album in self.scrape().items() for name in album]

        except AttributeError:
            print("It looks like there was an error with the self.scrape() method inside the AllMusicScraper module.")
            raise



        return self.genre

    def scrape(self) -> dict:
        """
        Return artist and album data from AllMusic.com
        """
        artist_album = {}
        
        
        #Send genre filter and headers to the AllMuisc.com database.
        try: 
            response = requests.post(self.url, data = self.genre, headers = self.headers)
            # response = requests.post(1234)

            response.raise_for_status()

        #return messages are for testing purposes. If requests.post returns an error, the error message will come from self.choose_genre().
        except requests.exceptions.Timeout: 
            return "Looks like the connection timed out. Please review requests.post inside self.scrape()."
        
        except requests.exceptions.ConnectionError:
            return "Looks like there was a connection error. Please review requests.post inside self.scrape()."
        
        except requests.exceptions.HTTPError:
            return "An HTTPError was raised. Please try again and make sure all paramaters are correct."
        
        except requests.exceptions.RequestException:
            return "Excpetion error, please review requests.post inside self.scrape()."

        
        soup = bs(response.content,self.parser) #Parsing the data that is returned

        
        titles = soup.find_all(self.element,self.class_name) #Locating album titles
        artist = soup.find_all(self.element,self.class_name2) #Locating artist name


        #Creating a dictionary with the artist as key and album as item.
        for i in range(len(titles)):
            try: #If an artist has multiple albums we want to make sure to include them
                if artist[i].contents[1].contents[0] in artist_album.keys(): 
                    artist_album[artist[i].contents[1].contents[0]].append(titles[i].contents[1].contents[0])
                else:
                    artist_album[artist[i].contents[1].contents[0]] = [titles[i].contents[1].contents[0]]
            except: #Artist that are labled as "Various Artists" will not be included. It is too vague.
                print("We do not include artists with the name Various Artists")
                print("\n")


        return artist_album
    
    def album_check(self):
        """
        If the genre selected did not return any albums another genre will be chosen.
        """
        print("Checking album list...")

        empty_genre = False

        #Checking to see if the album list is empty. If it is empty we want to re-run our code.
        if not self.album_names: 
            empty_genre = True
        else:
            print("Album list is good to go!")
            print("\n")
            empty_genre = False

        #If the album list is empty we will re-select a new genre until a genre returns a list of albums.
        while empty_genre == True: 
            print("It seems there is no albums currently available for the chosen genre. Re-running code...")
            print("\n")
            self.choose_genre()
            self.scrape()

            #Once albums are inside our list, we can end the while loop.
            if self.album_names:
                print("Album list is good to go!")
                print("\n")
                empty_genre = False
