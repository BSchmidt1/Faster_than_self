import tkinter as tk
import threading
import time
import random

# Function to change the window color
def change_color():
    colors = ["red", "green", "blue", "yellow", "purple", "orange", "pink"]
    return random.choice(colors)

def update_color(root, label, interval, duration):
    end_time = time.time() + duration
    while time.time() < end_time:
        new_color = change_color()
        label.config(bg=new_color)
        time.sleep(interval)

def create_window(interval, duration, pos):
    # Create the main window
    root = tk.Tk()
    root.title("Color Changing Window")
    width = 400
    height = 400
    root.geometry(f"{width}x{height}+{pos[0]}+{pos[1]}")
    
    # Create a label to fill the window
    label = tk.Label(root, text="", font=("Helvetica", 20), bg="white")
    label.pack(expand=True, fill='both')
    
    # Start the color changing in a separate thread for this window
    threading.Thread(target=update_color, args=(root, label, interval, duration)).start()
    root.mainloop()
    
    return root

def main():
    root = tk.Tk()
    root.withdraw()  # Hide the root window (optional, just for aesthetics)

    # Get screen resolutions for both screens
    screen1_width = root.winfo_screenwidth()  # Primary screen width
    screen1_height = root.winfo_screenheight()  # Primary screen height

    # Assume the second screen starts to the right of the first
    screen2_width = screen1_width  # For simplicity, assume both screens have the same resolution
    screen2_height = screen1_height

    # Set window size for all windows
    window_width = 400
    window_height = 400

    # Define the corner positions for each screen (top-left, top-right, bottom-left, bottom-right)
    screen_positions = [
        (0, 0),  # Top-left
        (0, screen1_height - window_height),  # Bottom-left
        (screen1_width + screen2_width - window_width, 0),  # Top-right on second screen
        (screen1_width + screen2_width - window_width, screen2_height - window_height),  # Bottom-right on second screen
        (screen1_width - window_width, 0),  # Top-right
        (screen1_width - window_width, screen1_height - window_height),  # Bottom-right
        (screen1_width + screen2_width - window_width*2, 0),  # Top-left on second screen
        (screen1_width + screen2_width - window_width*2, screen2_height - window_height)  # Bottom-left on second screen        
    ]
    # Get user input for interval, duration, and number of windows
    #x = float(input("Enter the interval (in seconds) for color change: "))
    #duration = float(input("Enter the total duration (in seconds) for the program to run: "))
    #num_windows = int(input("Enter the number of windows to open: "))    
    x = 0.00001
    duration = 10000000000
    num_windows = 8
    # Create and start each window
    windows = []
    for i in range(num_windows):
        pos = screen_positions[i]
        threading.Thread(target=create_window, args=(x, duration, pos)).start()

if __name__ == "__main__":
    main()

