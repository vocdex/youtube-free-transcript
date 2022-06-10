import youtube_dl
from youtube_dl.utils import DownloadError

ydl = youtube_dl.YoutubeDL()
def get_video_info(url):
    """Returns the video info as a dictionary. Can access the video title, description, format,audio url, etc."""
    with ydl:
        try:
            result = ydl.extract_info(
                url,
                download=False
            )
        except DownloadError:
            return None

    if 'entries' in result:
        # Can be a playlist or a list of videos
        video = result['entries'][0]
    else:
        # Just a video
        video = result
    return video


def get_audio_url(video):
    """Returns the audio url of a youtube video. Not used in transcription, but useful for downloading the audio."""
    for f in video['formats']:
        if f['ext'] == 'm4a':
            return f['url']
if __name__ == '__main__':
    video_info = get_video_info("https://www.youtube.com/watch?v=d6oQzE4kst0")
    print(video_info['formats']['ext'])
    print(video_info['title'])