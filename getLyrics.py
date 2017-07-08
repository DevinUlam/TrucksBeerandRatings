
import requests
import getToken
import lyriccomparison


topArtists = {
    # "Chris Stapleton": {
    #     "key": "4YLtscXsxbVgi031ovDDdh"
    # },
    # "Blake Shelton": {
    #     "key": "1UTPBmNbXNTittyMJrNkvw"
    # },
    # "Florida Georgia Line": {
    #     "key": "3b8QkneNDz4JHKKKlLgYZg"
    # },
    # "Thomas Rhett": {
    #     "key": "6x2LnllRG5uGarZMsD4iO8"
    # },
    # "Carrie Underwood": {
    #     "key": "4xFUf1FHVy696Q1JQZMTRj"
    # },
    # "Luke Bryan": {
    #     "key": "0BvkDsjIUla7X0k6CSWh1I"
    # },

    # "Keith Urban": {
    #     "key": "0u2FHSq3ln94y5Q57xazwf"
    # },
    # "Sam Hunt": {
    #     "key": "2kucQ9jQwuD8jWdtR9Ef38"
    # },
    # "Jason Aldean": {
    #     "key": "3FfvYsEGaIb52QPXhg4DcH"
    # },
    "Cole Swindell": {
        "key": "1mfDfLsMxYcOOZkzBxvSVW"
    },
    "Tim McGraw": {
        "key": "6roFdX1y5BYSbp60OTJWMd"
    },
    "Dierks Bentley": {
        "key": "7x8nK0m0cP2ksQf0mjWdPS"
    },
    "Eric Church": {
        "key": "2IvkS5MXK0vPGnwyJsrEyV"
    },
    "Kenny Chesney": {
        "key": "3grHWM9bx2E9vwJCdlRv9O"
    },
    "Chris Young": {
        "key": "4BYxqVkZyFjtik7crYLg5Q"
    },
    "Zac Brown Band": {
        "key": "6yJCxee7QumYr820xdIsjo"
    },
    "Brett Eldredge": {
        "key": "0qSX3s5pJnAlSsgsCne8Cz"
    },
    "Jon Pardi": {
        "key": "4MoAOfV4ROWofLG3a3hhBN"
    },
    "Jake Owen": {
        "key": "1n2pb9Tsfe4SwAjmUac6YT"
    },
    "Brad Paisley": {
        "key": "13YmWQJFwgZrd4bf5IjMY4"
    },
    "Rascal Flatts": {
        "key": "0a1gHP0HAqALbEyxaD5Ngn"
    },
    "Brantley Gilbert": {
        "key": "5q8HGNo0BjLWaTAhRtbwxa"
    }
}

token = getToken.getToken()


albumdict = {}
songdict = {}
countdict = {}
i = 0
for artist in topArtists:

    artistID = topArtists[artist]['key']

    #request info about each artist
    artistrequest = requests.get("https://api.spotify.com/v1/artists/{0}".format(artistID), headers={"Authorization": "Bearer {0}".format(token)})
    artistinfo = artistrequest.json()

    # request the albums of each artist
    albumrequest = requests.get("https://api.spotify.com/v1/artists/{0}/albums".format(artistID), headers={"Authorization": "Bearer {0}".format(token)})
    albumdata = albumrequest.json()
    albumdict.update({'Artist{0}'.format(i): {}})
    albumdict['Artist{0}'.format(i)].update({'Name': artist})
    #albumdict['Artist{0}'.format(i)].update({'Popularity': artistinfo['popularity']})
    songdict.update({'Artist{0}'.format(i): {}})
    songdict['Artist{0}'.format(i)].update({'name': artist})

    countdict.update({'Artist{0}'.format(i): {}})
    countdict['Artist{0}'.format(i)].update({'Name': artist})
    countdict['Artist{0}'.format(i)].update({'numtruck': 0})
    countdict['Artist{0}'.format(i)].update({'numbeer': 0})
    countdict['Artist{0}'.format(i)].update({'Popularity': artistinfo['popularity']})

    j=0
    #print(albumdata)
    for items in albumdata['items']:

        if j > 0:
            if items['name'] != albumdict['Artist{0}'.format(i)]['Album{0}'.format(j-1)]:
                if items['album_type'] != "compilation":

                    albumdict['Artist{0}'.format(i)].update({'Album{0}'.format(j): items['name']})
                    albumdict['Artist{0}'.format(i)].update({'Album{0}ID'.format(j): items['uri'].replace("spotify:album:", "")})
                    albumdict['Artist{0}'.format(i)].update({'Followers': artistinfo['followers']['total']})

                    albumID = albumdict['Artist{0}'.format(i)]['Album{0}ID'.format(j)]
                    songrequest = requests.get("https://api.spotify.com/v1/albums/{0}/tracks".format(albumID), headers={"Authorization": "Bearer {0}".format(token)})
                    songdata = songrequest.json()


                    for songs in songdata['items']:

                        count = lyriccomparison.getLyrics(artist, songs['name'])
                        print(count)
                        # print(count['truck'])
                        if count != 'error':
                            if count['truck'] != 0:

                                newtruck = countdict['Artist{0}'.format(i)]['numtruck'] + 1

                                countdict['Artist{0}'.format(i)].update({'numtruck': newtruck})
                                print(countdict)
                            elif count['beer'] != 0:
                                newbeer = countdict['Artist{0}'.format(i)]['numbeer'] + 1
                                countdict['Artist{0}'.format(i)].update({'numbeer': newbeer})
                                print(countdict)

                    #k=k+1

                    j = j + 1
        else:
            if items['album_type'] != "compilation":
                albumdict['Artist{0}'.format(i)].update({'Album{0}'.format(j): items['name']})
                albumdict['Artist{0}'.format(i)].update({'Album{0}ID'.format(j): items['uri'].replace("spotify:album:", "")})
                albumdict['Artist{0}'.format(i)].update({'Popularity': artistinfo['popularity']})
                albumdict['Artist{0}'.format(i)].update({'Followers': artistinfo['followers']['total']})
                albumID = albumdict['Artist{0}'.format(i)]['Album{0}ID'.format(j)]
                #print(albumID)
                j = j + 1


    #print(i)


        #print("artistID =", artistID)
        #print(albumdict['Artist{0}'.format(i)]['Album{0}ID'.format(i)])

    i = i + 1
print(countdict)
#print(songdict)
# k=0
# for album in albumdict:
#     print(album)
#     k = k + 1
#lyriccomparison.getSongList(albumdict)
#print(albumdict)
#countTruck = lyriccomparison.getLyrics("Asking Alexandria", "Another Bottle Down")

#print(countTruck)