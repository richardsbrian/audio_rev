import tkinter as tk
from tkinter import filedialog
from pydub import AudioSegment
import pygame
import os
from tkinter import messagebox



# Global variables
input_audio_path = ""
output_audio_path = ""


def browse_audio_file():
    global input_audio_path

    # Use the filedialog to open a file dialog window
    input_audio_path = filedialog.askopenfilename(
        filetypes=[("Audio Files", "*.wav *.mp3")]
    )




def reverse_audio():
    global input_audio_path, output_audio_path

    # Check if an input audio file path is provided
    if input_audio_path:
        try:
            # Load the audio from the provided input path
            audio = AudioSegment.from_file(input_audio_path)
            
            # Reverse the loaded audio
            reversed_audio = audio.reverse()
            
            # Create an output audio file path
            output_audio_path = "reversed_" + os.path.basename(input_audio_path)
            
            # Export the reversed audio to the output path in WAV format
            reversed_audio.export(output_audio_path, format="wav")
            
            # Show a success message box with the output file name
            messagebox.showinfo(
                "Success", "Audio reversed and saved as " + output_audio_path
            )
        except Exception as e:
            # Show an error message box if an exception occurs
            messagebox.showerror("Error", "An error occurred: " + str(e))
    else:
        # Show a warning message box if no input audio file is selected
        messagebox.showwarning("Warning", "Please select an audio file first.")



def play_original_audio():
    global input_audio_path
    if input_audio_path:
        pygame.mixer.init()  # Initialize the Pygame mixer
        pygame.mixer.music.load(input_audio_path)  # Load the audio file
        pygame.mixer.music.play()  # Play the loaded audio



def play_reversed_audio():
    global output_audio_path
    if output_audio_path:
        pygame.mixer.init()  # Initialize the Pygame mixer
        pygame.mixer.music.load(output_audio_path)  # Load the reversed audio file
        pygame.mixer.music.play()  # Play the loaded reversed audio

# Main GUI
root = tk.Tk()
root.title("Reversal")

# Icon
icon_path = "image\icon16.ico"
root.iconbitmap(icon_path)

# Set the background color of the root window
root.config(bg="#2A363B")

# Frame 1
frame1 = tk.Frame(root, bg="#99B898", borderwidth=2, relief="ridge")
frame1.grid(row=0, column=0, padx=10, pady=10, sticky="nsew")

# Label
label = tk.Label(frame1, bg="#99B898", text="Select an audio file to reverse:")
label.grid(row=0, column=0, pady=10, padx=5, sticky="nsew")

# Button Browse
browse_button = tk.Button(
    frame1, bg="#FECEA8", text="Browse", command=browse_audio_file
)
browse_button.grid(row=1, column=0, padx=20, sticky="nsew")

# Frame 3
frame3 = tk.Frame(root, bg="#99B898", borderwidth=2, relief="ridge")
frame3.grid(row=1, column=0, padx=10, pady=5, sticky="nsew")


# Spacer
spacer_label_bottom = tk.Label(frame3, bg="#99B898")
spacer_label_bottom.grid(row=0, column=0, padx=20, sticky="e")

# Button Reverse Audio
reverse_button = tk.Button(
    frame3, bg="#E84A5F", text="Reverse Audio", command=reverse_audio
)
reverse_button.grid(row=0, column=1, padx=5, pady=20)

# Spacer
spacer_label_bottom = tk.Label(frame3, bg="#99B898")
spacer_label_bottom.grid(row=0, column=2, padx=20, sticky="w")


# Frame 2
frame2 = tk.Frame(root, bg="#99B898", borderwidth=2, relief="ridge")
frame2.grid(row=2, column=0, padx=10, pady=10, sticky="nsew")

# Button Play Original
play_original_button = tk.Button(
    frame2, bg="#FF847C", text="Play Original", command=play_original_audio
)
play_original_button.grid(row=0, column=0, pady=20, padx=5, sticky="nsew")

# Button Play Reversed
play_reversed_button = tk.Button(
    frame2, bg="#FF847C", text="Play Reversed", command=play_reversed_audio
)
play_reversed_button.grid(row=0, column=1, pady=20, padx=5, sticky="nsew")

# Configure columns and rows to expand and center the frames
root.grid_rowconfigure(0, weight=1)
root.grid_columnconfigure(0, weight=1)

frame1.grid_rowconfigure(0, weight=1)
frame1.grid_rowconfigure(2, weight=1)

frame3.grid_rowconfigure(0, weight=1)
frame3.grid_rowconfigure(2, weight=1)

frame2.grid_rowconfigure(0, weight=1)
frame2.grid_rowconfigure(1, weight=1)


root.mainloop()
