from service_managers.service_manager import ServiceManager

from settings import youtube


class YoutubeManager(ServiceManager):

    def __init__(self):
        self.youtube = youtube

    def create_youtube_playlist(self, title, description, video_ids):
        """
        Creates a YouTube playslist with provided videos.

        :param title: A title of the playlist
        :param description: A description of the playlist
        :param video_ids: A list of IDs for the videos to put in the playlist
        :return: True if the function worked.
        """
        playlist_insert_request = youtube.playlists().insert(
            part="snippet",
            body={
                "snippet": {
                    "title": title,
                    "description": description,
                }
            }
        )
        playlist_response = playlist_insert_request.execute()

        for video_id in video_ids:
            youtube.playlistItems().insert(
                part="snippet",
                body={
                    "snippet": {
                        "playlistId": playlist_response["id"],
                        "resourceId": {
                            "kind": "youtube#video",
                            "videoId": video_id,
                        },
                    }
                }
            ).execute()
        return "True"
