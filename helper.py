import spacy
from youtube_transcript_api import YouTubeTranscriptApi
def get_transcript(video_id):
    """Returns the transcript of a youtube video as a raw string without punctuation or capitalization"""
    transcript = (YouTubeTranscriptApi.get_transcript(video_id))
    # print(transcript[0]['text'])
    texts = []
    for i in range(len(transcript) - 1):
        texts.append(transcript[i]['text'])
    texts = " ".join(texts)
    return texts
def punctuate(raw_text):
    """Punctuates the raw transcription with Spacy's en_core_web_lg model"""
    nlp = spacy.load('en_core_web_lg')
    doc = nlp(raw_text)
    sentences=""
    for sent in doc.sents:
        sentences+=(sent.text.capitalize()+".")
    return sentences

