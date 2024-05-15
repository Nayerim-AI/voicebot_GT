import pyglet
import logging
import os

frame_count = {'blink': 39, 'happy': 60, 'sad': 47, 'dizzy': 67, 'excited': 24,
               'neutral': 61, 'happy2': 20, 'angry': 20, 'happy3': 26, 'bootup3': 124, 'blink2': 20}
config = pyglet.gl.Config(double_buffer=True)


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
        pyglet.clock.schedule_interval(draw_frames, 1/30.0)

        # Start the Pyglet event loop
        pyglet.app.run()

    except IOError as e:
        logging.info(e)


# Example usage
show('bootup3')  # Menampilkan semua frame dari emosi 'blink'
