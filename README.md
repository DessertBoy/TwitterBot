# TwitterBot
This is the python syntax for the Twitter bot [@5HourlyAlbums](https://twitter.com/5HourlyAlbums) on Twitter. @5HourlyAlbums is designed to tweet 5 random albums from 40 different genres every day from 5 a.m. - 10 p.m.

The wesbite we will be scrapping music from (allmusic.com) is an AJAX website. We will need to send a post request straight to the database where this website retrieves its data from. I will post a video below to demonstrate how to obtain the genre ID and headers.

This is a personal project. I decided to share it with the public in case anybody would like to create something similar and is looking for a reference or base. I have included links to the documentation for the libraries I used.

**Note:** UnitTest.py is not necessary for anything to work. It was created/used for testing purposes.

# Requirements
1. Have basic/intermediate knowledge of Python.
<br />

2. Basic knowledge of HTML

<br />

3. You must create a Twitter developer account in order to obtain access to Twitter's API. This [link](https://developer.twitter.com/en/support/twitter-api/developer-account) goes into detail on how to apply for a Twitter developer account.

# Resources

### Changing the Genre ID
The video below will demonstrate how to obtain the genre ID for any genre on allmusic.com in case you'd like to add/change genres.

https://user-images.githubusercontent.com/56139759/231022979-afa485ee-d2e9-4d25-81df-074d08e121af.mp4

<br />

### Requests.Post Headers Location
The video below will demonstrate where to find the necessary headers for your post request.


https://user-images.githubusercontent.com/56139759/233507828-5cfd3210-bbd9-4f0b-99a2-83927f7504fb.mp4

<br />

[How to Run a Python Script with Windows Task Scheduler](https://www.youtube.com/watch?v=4n2fC97MNac). Windows Task Scheduler is what I use to run my python script every hour.

### Documentation
* [Tweepy Documentation](https://docs.tweepy.org/en/stable/)
* [Beautiful Soup documentation](https://beautiful-soup-4.readthedocs.io/en/latest/)
* [requests documentation](https://requests.readthedocs.io/en/latest/user/quickstart/)
