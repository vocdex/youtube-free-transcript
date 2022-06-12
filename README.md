## Transcribing a Youtube video with a given URL
### WHAT DOES IT DO?
Retrieves automatically generated and/or manually uploaded transcript of a Youtube Video. Polishes raw transcript   
with Spacy's en-core-web-lg-model,by inserting punctuation marks wherever necessary as well as capitalizing the start of each sentence.
### IS IT ANY GOOD?
YES! Most words are grammatically correct with a very few spelling errors. However, you might see some punctuation errors such as double dots, double commas but it is bearable.Considering this is a free service, one can turn a blind eye to the occasional punctuation errors, in my opinion.
### ANY RECOMMENDATIONS?
 If you're looking for the best YouTube video or any kind of audio transcription, I recommend checking out [AssemblyAI](https://www.assemblyai.com/). It costs $0.9 per hour.
### Install:
Make sure you have downloaded the folder and changed to the folder directory in the command line. Install the required dependencies by running the following command:
```bash
cd youtube-free-api
conda create -n youtube-free-api python=3.9
pip install -r requirements.txt
``` 
### Libraries Used:
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
youtube-transcript-api is not officicially documented and is not guaranteed to work in case Youtube changes access restrictions or updates the API.
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
