# TrucksBeerandRatings
Outputs number of times top country artists use "truck" or "beer" in their songs.

# Requirements to install
$ pip install Spotipy
$ pip install requests
$ pip install re
$ pip install beautifulsoup
$ pip install urllib
$ pip install sys

# To run

$ python getLyrics.py {spotify username} #this redirects you to login to spotify (must be registered for free API access through spotify)
-after entering in your login, you will be directed to a localhost site that will not be found... but you must copy the url into your command prompt (it will ask you to do this).
-The result is a token to allow spotify connections, but the code takes care of the rest so that anytime you want to rerun the analysis you enter: $ python getLyrics.py {spotify username}

