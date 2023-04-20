from requests.exceptions import Timeout,ConnectionError,HTTPError,RequestException
from unittest.mock import patch, MagicMock
from AllMusicScraper import WebScraper
import Twitter_UnitTest
import unittest
import requests.exceptions

class TestTwitterBot(unittest.TestCase):
    def setUp(self):
        self.url = f"https://www.allmusic.com"
        self.parser = "html.parser"
        self.element = "td"
        self.class_name = "title"
        self.class_name2 = "artist"
        self.headers = { 
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
        self.scrappy = WebScraper(self.url,self.parser,self.element,self.class_name,self.class_name2,self.headers)
    


    def test_numeric_values(self):
        self.assertIsInstance(Twitter_UnitTest.random_page_number,int)
    
    def test_token_values(self):
        self.assertIsInstance(Twitter_UnitTest.consumer_key_v2, str)
        self.assertIsInstance(Twitter_UnitTest.consumer_secret_v2, str)
        self.assertIsInstance(Twitter_UnitTest.access_token_v2, str)
        self.assertIsInstance(Twitter_UnitTest.access_token_secret_v2, str)
        self.assertIsInstance(Twitter_UnitTest.bearer_token_v2, str)
    
    def test_webscraper_arguments(self):
        self.assertIsInstance(Twitter_UnitTest.url, str)
        self.assertIsInstance(Twitter_UnitTest.parser, str)
        self.assertIsInstance(Twitter_UnitTest.element, str)
        self.assertIsInstance(Twitter_UnitTest.class_name, str)
        self.assertIsInstance(Twitter_UnitTest.class_name2, str)
        self.assertIsInstance(Twitter_UnitTest.headers, dict)

    @patch("AllMusicScraper_v2.WebScraper")
    def test_class_attribute_type(self,mock_value):
        self.assertIsInstance(self.scrappy.url,str)
        self.assertIsInstance(self.scrappy.parser,str)
        self.assertIsInstance(self.scrappy.element,str)
        self.assertIsInstance(self.scrappy.class_name,str)
        self.assertIsInstance(self.scrappy.class_name2,str)
        self.assertIsInstance(self.scrappy.headers,dict)
        self.assertIsInstance(self.scrappy.scrape(),dict)


    @patch("AllMusicScraper.requests")
    def test_general_exception(self,mock_request):
        mock_request.exceptions = requests.exceptions
        mock_request.post.side_effect = RequestException("Exception Error")
        self.assertEqual(self.scrappy.scrape(),"Excpetion error, please review requests.post inside self.scrape().")

    @patch("AllMusicScraper.requests")
    def test_timeout_exception(self,mock_request):

        mock_request.exceptions = requests.exceptions
        mock_request.post.side_effect = Timeout("Looks your connection timed out")
        self.assertEqual(self.scrappy.scrape(),"Looks like the connection timed out. Please review requests.post inside self.scrape().")

    @patch("AllMusicScraper.requests")
    def test_connection_exception(self,mock_request):

        mock_request.exceptions = requests.exceptions
        mock_request.post.side_effect = ConnectionError("Looks like there was a connection error")
        self.assertEqual(self.scrappy.scrape(),"Looks like there was a connection error. Please review requests.post inside self.scrape().")

    @patch("AllMusicScraper.requests")
    def test_httperror_exception(self,mock_request):

        mock_request.exceptions = requests.exceptions
        mock_request.post.side_effect = HTTPError("HTTPError")
        self.assertEqual(self.scrappy.scrape(),"An HTTPError was raised. Please try again and make sure all paramaters are correct.")



if __name__ == '__main__':
    unittest.main()