
import spotipy
import sys
import spotipy.util as util

def getToken ():
    SPOTIPY_CLIENT_ID = '311940949ffb4afd98de6284b46fc15b'
    SPOTIPY_CLIENT_SECRET = '2f654b5b80104d15826b041335485813'
    SPOTIPY_REDIRECT_URI = 'http://localhost:8888/callback'
    PORT_NUMBER = 8080
    SCOPE = 'user-library-read'
    CACHE = '.spotipyoauthcache'

    #print(len(sys.argv))
    if len(sys.argv) > 1:
        username = sys.argv[1]
    else:
        print("Usage: %s username" % (sys.argv[0],))
        sys.exit()
    token = util.prompt_for_user_token(username, SCOPE, client_id='311940949ffb4afd98de6284b46fc15b',
                                       client_secret='2f654b5b80104d15826b041335485813',
                                       redirect_uri='http://localhost:8888/callback')


    if token:
        sp = spotipy.Spotify(auth=token)
        # results = sp.current_user_saved_tracks()
        # for item in results['items']:
        #     track = item['track']
        #     print(track['name'] + ' - ' + track['artists'][0]['name'])
    else:
        print("Can't get token for", username)

    return(token)