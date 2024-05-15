import multiprocessing.process
import speech_recognition as sr
import pyttsx3
import pyglet
import logging
from PIL import Image
import multiprocessing

frame_count = {'blink':39, 'happy':60, 'sad':47,'dizzy':67,'excited':24,'neutral':61,'happy2':20,'angry':20,'happy3':26,'bootup3':124,'blink2':20}
emotion = ['angry','sad','excited']
normal = ['neutral','blink2']

q = multiprocessing.Queue()
event = multiprocessing.Event()

recognizer = sr.Recognizer()
engine = pyttsx3.init()

def takeCommand():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        r.pause_threshold = 1
        audio = r.listen(source)

    try:
        print("Recognizing...")
        # reaksi.main('2')
        query = r.recognize_google(audio, language='en-in')
        print(f"User said: {query}\n")

    except Exception as e:
        print("Say that again please...")
        return "None"
    return query

def listen(queue):
    try:
        with sr.Microphone() as source:
            print("Listening...")
            recognizer.adjust_for_ambient_noise(source)
            print("Recognizing...")
            audio = recognizer.listen(source)
            text = recognizer.recognize_google(audio)
            print("You said:", text)
            queue.put(text.lower())  # Masukkan hasil teks ke dalam antrian (queue)
    except sr.UnknownValueError:
        print("Sorry, I didn't understand.")
        queue.put("")  # Masukkan string kosong ke dalam antrian jika tidak terdeteksi
    except sr.RequestError as e:
        print("Sorry, there was an error retrieving the audio:", str(e))
        queue.put("")  # Masukkan string kosong ke dalam antrian jika terjadi kesalahan
    except Exception as e:
        print("An error occurred:", str(e))
        queue.put("")  # Masukkan string kosong ke dalam antrian jika terjadi kesalahan

def speak(text):
    engine.say(text)
    engine.runAndWait()
    print("Assistant said:", text)

def show(emotion):
    try:
        # Create a Pyglet window
        window = pyglet.window.Window()

        # Load frames for the given emotion
        frames = []
        for i in range(frame_count[emotion]):
            image_path = f'./emotions/{emotion}/frame{i}.png'
            image = pyglet.image.load(image_path)
            frames.append(image)

        # Function to draw frames
        def draw_frames(dt):
            current_frame = draw_frames.frame_index
            window.clear()
            frames[current_frame].blit(0, 0)
            draw_frames.frame_index += 1

            # Close window after displaying all frames
            if draw_frames.frame_index >= len(frames):
                window.close()
                logging.info("quit:")

        draw_frames.frame_index = 0  # Initialize frame index

        # Schedule the draw function to be called at a fixed interval (30 FPS)
        pyglet.clock.schedule_interval(draw_frames, 1/60.0)

        # Start the Pyglet event loop
        pyglet.app.run()

    except IOError as e:
        logging.info(e)

def bootup():
    show('bootup3')





if __name__ == '__main__':
    # Buat antrian (queue) untuk berbagi hasil antara proses utama dan proses latar belakang
    result_queue = multiprocessing.Queue()

    # Buat proses latar belakang untuk menjalankan fungsi listen()
    listen_process = multiprocessing.Process(target=listen, args=(result_queue,))
    listen_process.start()  # Mulai proses latar belakang

    # Panggil fungsi show() di sini dengan argumen yang sesuai
    show('blink')

    # Tunggu sampai proses latar belakang selesai
    listen_process.join()

    # Dapatkan hasil teks dari antrian (queue)
    if not result_queue.empty():
        text_result = result_queue.get()
        print("Result from listening process:", text_result)
    else:
        print("No result from listening process")