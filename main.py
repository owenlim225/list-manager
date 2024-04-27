import tkinter as tk
from pathlib import Path

# Access the asset from the main folder
SCRIPT_PATH = Path(__file__).resolve().parent
ASSETS_PATH = SCRIPT_PATH.parent / "assets"

def relative_to_assets(path: str) -> Path:
    return ASSETS_PATH / Path(path)

class Gui(tk.Tk):
    def __init__(self):
        super().__init__()
        self.geometry("500x500")
        self.configure(bg="#FFFFFF")
        self.title("Pomodoro App")
        self.resizable(False, False)

        self.main()
        self.timer()

    def main(self):
        # Create canvas
        self.canvas = tk.Canvas(
            self,
            bg="#FFFFFF",
            height=500,
            width=500,
            bd=0,
            highlightthickness=0,
            relief="ridge"
        )
        self.canvas.place(x=0, y=0)

        # Load and place images
        images = [
            "image_1.png", "image_2.png", "image_3.png", "image_4.png", "image_5.png",
            "entry_1.png", "image_6.png", "image_7.png", "image_8.png", "image_9.png", "image_10.png"
        ]
        self.image_objects = []
        for image_path in images:
            image = tk.PhotoImage(file=relative_to_assets(image_path))
            self.image_objects.append(image)

        # Coordinates for images
        coordinates = [
            (250, 250), (408, 465), (250, 36),
            (196, 388), (304, 389), (250, 346),
            (113, 484), (250, 255), (106, 32), (468, 465),
            (349, 465)
        ]
        for i, coord in enumerate(coordinates):
            self.canvas.create_image(coord[0], coord[1], image=self.image_objects[i])

        # Entry widget
        entry_image_1 = self.image_objects[5]
        entry_bg_1 = self.canvas.create_image(250, 346, image=entry_image_1)
        entry_1 = tk.Entry(self, bd=0, bg="#FFFFFF", fg="#000716", highlightthickness=0)
        entry_1.place(x=208, y=335, width=83, height=15)


    def timer(self):
        # Create a label to display the timer
        timer_label = tk.Label(self, text="00:00", font=("Inter BlackItalic", 24 * -1), bg="#FF2929")
        timer_label.place(x=215, y=232)

if __name__ == "__main__":
    app = Gui()
    app.mainloop()
