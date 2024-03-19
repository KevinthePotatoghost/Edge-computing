import pyaudio
import numpy as np
import tkinter as tk

# Constants
FORMAT = pyaudio.paInt16
CHANNELS = 1
RATE = 44100
CHUNK = 1024
THRESHOLD = 80  # Adjust threshold based on your requirements


# Function to detect sound above threshold
def detect_sound(stream):
    data = np.frombuffer(stream.read(CHUNK), dtype=np.int16)
    rms = np.sqrt(np.mean(np.square(data)))
    if rms > THRESHOLD:
        popup_window()


# Function to create GUI pop-up
def popup_window():
    popup = tk.Tk()
    popup.geometry("500x100")
    popup.title("Sound Detected! Please Stop Talking")

    # Larger font size
    label = tk.Label(popup, text="Sound detected Please follow the rules and stop talking", font=("Arial", 20))
    label.pack()

    popup.mainloop()


# Main function
def main():
    # Initialize PyAudio
    p = pyaudio.PyAudio()

    # Open stream
    stream = p.open(format=FORMAT,
                    channels=CHANNELS,
                    rate=RATE,
                    input=True,
                    frames_per_buffer=CHUNK)

    # Continuously detect sound
    while True:
        detect_sound(stream)

    # Close stream and PyAudio
    stream.stop_stream()
    stream.close()
    p.terminate()


if __name__ == "__main__":
    main()
