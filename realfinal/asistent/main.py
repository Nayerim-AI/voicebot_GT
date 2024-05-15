import pyglet
import cv2
import pyttsx3
from mutagen.mp3 import MP3
from TextToSpeech import takeCommand

# Fungsi untuk membuat file MP3 dari teks
def create_mp3(text, filename):
    engine = pyttsx3.init()
    voices = engine.getProperty('voices')
    engine.setProperty('rate', 150)
    engine.setProperty('volume', 1.0)
    engine.setProperty('voice', voices[1].id)
    engine.save_to_file(text, filename)
    engine.runAndWait()

def change_mp3(mssg):
    global mp3_filename
    mp3_filename = 'output.mp3'
    create_mp3(mssg, mp3_filename)

def play_mp3(filename):
    global duration
    # duration = get_mp3_duration(mp3_filename)
    sound = pyglet.media.load(filename)
    sound.play()
    
def get_mp3_duration(mp3_file):
    audio = MP3(mp3_file)
    duration_in_seconds = audio.info.length
    return duration_in_seconds

def play_mp4(video_path):
    global cap, texture, width, height
    cap = cv2.VideoCapture(video_path)
    width = int(cap.get(cv2.CAP_PROP_FRAME_WIDTH))
    height = int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))

def update(dt):
    global cap, texture, width, height
    ret, frame = cap.read()
    if ret:
        frame_rgb = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
        texture.blit_into(pyglet.image.ImageData(width, height, 'RGB', frame_rgb.tobytes(), pitch=width * 3), 0, 0, 0)

def on_draw():
    window.clear()
    texture.blit(0, 0)

# Path video default
default_video_path = 'Senang.mp4'

change_mp3("Hallo good morning, welcome to Greentech Laboratory")
play_mp4(default_video_path)

pyglet.clock.schedule_interval(update, 1 / 30.0)

window = pyglet.window.Window()
texture = pyglet.image.Texture.create(width, height)

def update_animation_voice(path) :
    global default_video_path
    new_video_path = path
    if new_video_path:
        default_video_path = new_video_path
        cap.release()
        play_mp4(default_video_path)
        
    global default_audio_mssg
    new_audio_mssg = takeCommand()
    if new_audio_mssg:
        default_audio_mssg= new_audio_mssg
        change_mp3(default_audio_mssg)
        play_mp3(mp3_filename)
    
pyglet.clock.schedule_interval(lambda dt: update_animation_voice("LOADING.mp4"), 10)

@window.event
def on_draw():
    window.clear()
    texture.blit(0, 0)

@window.event
def on_close():
    cap.release()

play_mp3(mp3_filename)
        
pyglet.app.run()
