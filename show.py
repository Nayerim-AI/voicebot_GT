
import pyglet
import logging
import os

frame_count = {'blink':39, 'happy':60, 'sad':47,'dizzy':67,'excited':24,'neutral':61,'happy2':20,'angry':20,'happy3':26,'bootup3':124,'blink2':20}

def show(emotion, count):
    try:
        # Create a Pyglet window
        window = pyglet.window.Window()

        # Load frames for the given emotion
        frames = []
        frame_count = count  # Assuming count is the total number of frames to display

        for i in range(frame_count):
            image_path = f'./emotions/{emotion}/frame{i}.png'
            image = pyglet.image.load(image_path)
            frames.append(image)

        # Function to update and draw frames
        def update_frame(dt):
            current_frame = update_frame.frame_index % frame_count
            window.clear()
            frames[current_frame].blit(0, 0)
            update_frame.frame_index += 1

        update_frame.frame_index = 0  # Initialize frame index

        # Schedule the update function to be called at a fixed interval (30 FPS)
        pyglet.clock.schedule_interval(update_frame, 1/60.0)

        # Event handler to close window on key press
        @window.event
        def on_key_press(symbol, modifiers):
            window.close()
            logging.info("quit:")

        # Start the Pyglet event loop
        pyglet.app.run()

    except IOError as e:
        logging.info(e)

# Example usage
show('blink',39)
