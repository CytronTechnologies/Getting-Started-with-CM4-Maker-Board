# This code will test the audio jack, you can press button #17 to repeat the audio
import RPi.GPIO as GPIO
import time
from pydub import AudioSegment
from pydub.playback import play
import os

# Set up GPIO pins
BUTTON_PLAY = 17

# Audio file path
WAVE_FILE_PATH = "L-R.wav"

GPIO.setmode(GPIO.BCM)
GPIO.setup(BUTTON_PLAY, GPIO.IN, pull_up_down=GPIO.PUD_UP)

def play_audio():
    if os.path.exists(WAVE_FILE_PATH):
        audio = AudioSegment.from_wav(WAVE_FILE_PATH)
        print("Playing audio")
        play(audio)
    else:
        print("No audio to play")

try:
    play_audio()
    print("Press Button #17 to play the audio again")
    while True:
        play_button_state = GPIO.input(BUTTON_PLAY)

        if not play_button_state:
            play_audio()
            time.sleep(1)

except KeyboardInterrupt:
    print("Interrupted")
finally:
    GPIO.cleanup()
