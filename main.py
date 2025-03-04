import random,pygame,threading
import tkinter as tk
from tkinter import Label

MAX_WINDOWS = 100
window_count = 0

class BouncingWindow:
    def __init__(self, root=None):
        global window_count
        if window_count >= MAX_WINDOWS:
            return  
        window_count += 1

        self.root = tk.Tk() if root is None else tk.Toplevel(root)
        self.root.geometry("400x150")
        self.root.configure(bg="black")
        self.root.title="you are an idiot"
        self.screen_width = self.root.winfo_screenwidth()
        self.screen_height = self.root.winfo_screenheight()

        self.x = random.randint(0, self.screen_width - 400)
        self.y = random.randint(0, self.screen_height - 150)

        self.dx = random.choice([-5, 5])
        self.dy = random.choice([-5, 5])

        self.root.geometry(f"400x150+{self.x}+{self.y}")
        self.root.protocol("WM_DELETE_WINDOW", self.spawn_new)

        self.idiot_label = Label(self.root, text="You are an idiot",
                                 bg="black", fg="white", font=("Comic Sans MS", 25, "bold"))
        self.idiot_label.pack(pady=2)

        self.idiot_label1 = Label(self.root, text="☺ ☺ ☺",
                                  bg="black", fg="white", font=("Comic Sans MS", 40, "bold"))
        self.idiot_label1.pack(pady=2)

        self.move()
        self.pulse_color()

    def move(self):
        self.x += self.dx
        self.y += self.dy

        if self.x <= 0 or self.x >= self.screen_width - 400:
            self.dx = -self.dx
        if self.y <= 0 or self.y >= self.screen_height - 150:
            self.dy = -self.dy

        self.root.geometry(f"400x150+{self.x}+{self.y}")
        self.root.after(30, self.move)

    def pulse_color(self):
        current_bg = self.root.cget("bg")
        new_bg = "white" if current_bg == "black" else "black"
        new_fg = "black" if current_bg == "black" else "white"

        self.root.configure(bg=new_bg)
        self.idiot_label.configure(bg=new_bg, fg=new_fg)
        self.idiot_label1.configure(bg=new_bg, fg=new_fg)

        self.root.after(500, self.pulse_color)

    def spawn_new(self):
        for _ in range(6):
            BouncingWindow()

def play_sound():
    pygame.mixer.init()
    pygame.mixer.music.load(r"you-are-an-idiot.mp3")
    pygame.mixer.music.play(-1)

if __name__ == "__main__":
    threading.Thread(target=play_sound, daemon=True).start()
    BouncingWindow()
    tk.mainloop()

