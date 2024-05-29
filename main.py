import pyttsx3
import speech_recognition as sr
import pyglet
import logging
import os
import threading
import time

from takedata import takeData

frame_count = {'blink': 39, 'happy': 60, 'sad': 47, 'dizzy': 67, 'excited': 24, 'neutral': 61, 'happy2': 20, 'angry': 20, 'happy3': 26, 'bootup3': 124, 'blink2': 20}
emotions = ['blink', 'happy', 'sad', 'excited','sleep']

recognizer = sr.Recognizer()
engine = pyttsx3.init()

def take_command():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        r.pause_threshold = 1
        audio = r.listen(source)

    try:
        print("Recognizing...")
        query = r.recognize_google(audio, language='en-in')
        print(f"User said: {query}\n")
        return query
    except Exception as e:
        print("Say that again please...")
        return None

def speak(args1):
    engine.say(args1)
    engine.runAndWait()

class EmotionViewer:
    def __init__(self, emotion_folder):
        self.emotion_folder = emotion_folder
        self.frames = []
        self.frame_index = 0
        self.load_frames()

    def load_frames(self):
        try:
            folder_path = f'./emotions/{self.emotion_folder}'
            frame_files = sorted(os.listdir(folder_path))
            self.frames = [pyglet.image.load(os.path.join(folder_path, file)) for file in frame_files]
        except IOError as e:
            logging.error(f"Error loading frames: {e}")

    def update_frame(self, dt):
        if self.frames:
            self.frame_index = (self.frame_index + 1) % len(self.frames)


    def draw(self, x, y):
        if self.frames:
            self.frames[self.frame_index].blit(x, y)

class MyWindow(pyglet.window.Window):
    def __init__(self, width, height):
        super().__init__(width, height, caption='Emotion Viewer')

        self.background_color = (0, 0, 0, 255)  # Warna hitam untuk background
        self.black_screen = True  # Menampilkan layar hitam sebelum animasi emosi
        self.emotions = emotions
        self.current_emotion_index = 0
        self.emotion_viewer = None

        # Jadwalkan pemanggilan method untuk mengubah emosi setelah 1 detik
        pyglet.clock.schedule_once(self.start_emotion, 1.0)  # Menampilkan layar hitam selama 1 detik
        pyglet.clock.schedule_interval(self.update, 1/30.0)

    def update(self, dt):
        if self.emotion_viewer:
            self.emotion_viewer.update_frame(dt)

    def on_draw(self):
        self.clear()
        if self.black_screen:
            self.draw_black_screen()
        else:
            self.draw_background()
            if self.emotion_viewer:
                self.emotion_viewer.draw(0, 0)  # Gambar animasi frame emosi di atas background

    def draw_background(self):
        pyglet.gl.glClearColor(*[c / 255.0 for c in self.background_color])
        pyglet.gl.glClear(pyglet.gl.GL_COLOR_BUFFER_BIT)

    def draw_black_screen(self):
        pyglet.gl.glClearColor(0, 0, 0, 1)
        pyglet.gl.glClear(pyglet.gl.GL_COLOR_BUFFER_BIT)

    def start_emotion(self, dt):
        self.black_screen = False
        self.emotion_viewer = EmotionViewer(self.emotions[self.current_emotion_index])
        # Jadwalkan pemanggilan method untuk mengubah emosi setelah 10 detik
        pyglet.clock.schedule_once(self.change_emotion, 10.0)

    def change_emotion(self, dt):
        self.current_emotion_index = (self.current_emotion_index + 1) % len(self.emotions)
        self.emotion_viewer = EmotionViewer(self.emotions[self.current_emotion_index])
        # Jadwalkan lagi untuk mengubah emosi setelah 10 detik
        pyglet.clock.schedule_once(self.change_emotion, 10.0)

def mengubah_reaksi(window, emo):
    window.current_emotion_index = emotions.index(emo)
    window.emotion_viewer = EmotionViewer(window.emotions[window.current_emotion_index])

def emotion_changer(window):
    speak("Welcome to Greentech Laboratory, I hope you have a good day.")
    while True:
        query = take_command()
        data = takeData(query)
        if query and query.lower() == "do you go to school everyday":
            mengubah_reaksi(window, "happy")
            speak("Yes, I go to school everyday when the sun rises.")
            # Database operation    
        elif data:
            mengubah_reaksi(window, "blink")
            speak(data[2])
        elif query and query.lower() == "do you play video games":
            mengubah_reaksi(window, "sad")
            speak("Yes, I play the game Mobile Legends.")
        elif query and query.lower() == 'exit':
            speak("Goodbye!")
            pyglet.app.exit()
            break
        else:
            print("Invalid emotion. Please try again.")
        time.sleep(3)

def main():
    window = MyWindow(640, 480)
    threading.Thread(target=emotion_changer, args=(window,), daemon=True).start()
    pyglet.app.run()

if __name__ == '__main__':
    main()

