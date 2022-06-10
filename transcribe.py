"""Downloads youtube transcript word-by-word (or chunk) and combines it to one big string without any punctuation and
capitalization.
Raw text is then structured into sentences using spacy's pretrained en_core_web_lg model(400.7MB). It's not perfect, but it's free and quite good"""
from yt_extractor import get_video_info
from helper import get_transcript, punctuate
import argparse
base_url="https://www.youtube.com/watch?v="

def save_transcript(video_id):
    """Saves the transcript of a youtube video as a string"""
    url=base_url+video_id
    title=get_video_info(url)['title']
    title=title.strip().replace(" ", "_")
    filename="transcripts/"+title+".txt"
    transcript=get_transcript(video_id)
    if transcript=="":
        print("No transcript found for this video")
    else:
        with open(filename, "w") as f:
            f.write(punctuate(transcript))
        print("Transcript saved to "+filename)

def main():
    """Main function"""
    parser = argparse.ArgumentParser(description="Download auto-generated youtube transcripts by URL")
    # system/input/output
    parser.add_argument('--url', '-i', type=str,help="URL of the youtube video")
    args = parser.parse_args()
    video_id = args.url.split("=")[1]
    save_transcript(video_id)
if __name__ == "__main__":
    main()