import requests
from pydub import AudioSegment
from pydub.playback import play
import io

def play_audio_from_url(url):
    # Fetch the audio file from the URL
    response = requests.get(url)
    response.raise_for_status()  # This will raise an exception for HTTP errors

    # Load the audio data using pydub
    audio_data = io.BytesIO(response.content)
    audio = AudioSegment.from_file(audio_data, format="mp3")  # Adjust format if necessary

    # Play the audio
    play(audio)

# Example usage
url = "https://example.com/path/to/your/audiofile.mp3"  # Replace with the actual URL
play_audio_from_url(url)
