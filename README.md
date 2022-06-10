## Transcribing a Youtube video with a given URL
### Install:
Make sure you have downloaded the folder and changed to the folder directory in the command line. Install the required dependencies by running the following command:
```bash
git clone 
cd youtube-free-api
conda create -n youtube-free-api python=3.9
pip install -r requirements.txt
``` 
###Libraries Used:
* [youtube-dl](https://ytdl-org.github.io/youtube-dl/index.html)
* [youtube-transcript-api](https://github.com/jdepoix/youtube-transcript-api)
* [spacy](https://spacy.io/) (en-core-web-lg model)

### Usage:
While staying in your project directory, run the following command and type in the URL of the video you want to transcribe:
```
$ python transcribe.py --url "urlOfTheVideo"
```
<p align="center">
**BAM!**
</p>
It takes only a few seconds to retrieve the transcript of the video. 

### Costs: Free
### Transcripts
Transcripts are saved in a folder named **transripts** in the project folder as an .txt file.　  
The title of each transcript is the name of the YouTube video.
### Warnings
youtube-transcript-api is not officicially documented and is not guaranteed to work in case of Youtube changes access restrictions or updates the API.
Refer to [youtube-transcript-api](https://github.com/jdepoix/youtube-transcript-api) for more information.
###Further usages:
#### Translate transcript

YouTube has a feature which allows you to automatically translate subtitles. This module also makes it possible to access this feature. To do so `Transcript` objects provide a `translate()` method, which returns a new translated `Transcript` object:

```python
transcript = transcript_list.find_transcript(['en'])
translated_transcript = transcript.translate('de')
print(translated_transcript.fetch())
```
#### List available transcripts

If you want to list all transcripts which are available for a given video you can call:

```python
transcript_list = YouTubeTranscriptApi.list_transcripts(video_id)