from service_managers.service_manager import ServiceManager

import spotipy
from settings import SPOTIFY_CLIENT_ID, SPOTIFY_CLIENT_SECRET, SPOTIFY_REDIRECT_URI

SPOTIFY_SCOPES = [
    'user-read-playback-state',
    'user-modify-playback-state',
    'user-read-currently-playing',

    'app-remote-control',
    'streaming',

    'playlist-read-private',
    'playlist-read-collaborative',
    'playlist-modify-private',
    'playlist-modify-public',

    'user-follow-modify',
    'user-follow-read',

    'user-read-playback-position',
    'user-top-read',
    'user-read-recently-played',

    'user-library-modify',
    'user-library-read',
]


class SpotifyManager(ServiceManager):
    def __init__(self):
        self.spotify_oauth = spotipy.SpotifyOAuth(
            client_id=SPOTIFY_CLIENT_ID,
            client_secret=SPOTIFY_CLIENT_SECRET,
            redirect_uri=SPOTIFY_REDIRECT_URI,
            scope=SPOTIFY_SCOPES
        )
        self.spotify = spotipy.Spotify(auth_manager=self.spotify_oauth)

    # TODO finish the function. Remake return value. Add spotify desktop support.
    def spotify_play_song(self, name):
        """
        Search a song by its name and play it in Spotify.

        :param name: A name of the song, e.g. Smells like teen spirit, Californication
        :return: True if the function worked.
        """
        search_result = self.spotify.search(name, 1, 0, "track")
        songs_dict = search_result["tracks"]
        song_items = songs_dict['items']
        song = song_items[0]['external_urls']['spotify']
        return self.spotify.start_playback(uris=[song])

    def spotify_get_my_playlists(self, ):
        """
        Get current Spotify playlists of the user.

        :return: The information about user's playlists.
        """
        return self.spotify.current_user_playlists()

    def transfer_playback(self, device_type):
        """
        Transfer Playback to another device.

        :param string device_type: A type of device: computer or smartphone
        :return: Playback transfer result.
        """
        devices = self.spotify.devices()['devices']
        fitting_devices = [device for device in devices if device['type'].lower() == device_type]
        if not fitting_devices:
            return {
                "status": "error",
                "message": "No fitting device Found",
            }
        device_to_play = fitting_devices[0]
        try:
            self.spotify.transfer_playback(device_id=device_to_play['id'])
            return {
                "status": "success",
            }
        except Exception as e:
            return {
                "status": "error",
                "message": e,
            }
