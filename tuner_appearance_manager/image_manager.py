
try:
    import Image
except ImportError:
    from PIL import Image

try:
    import ImageTk
except ImportError:
    from PIL import ImageTk


class ImageManager(object):
    def __init__(self, main_path):
        self.bell_image = ImageTk.PhotoImage(
            Image.open(main_path + "/assets/images/bell.png").resize((50, 50), Image.ANTIALIAS))

        print(self.bell_image.width(), self.bell_image.height())

        self.bell_hovered_image = ImageTk.PhotoImage(
            Image.open(main_path + "/assets/images/bell_hovered.png").resize((50, 50), Image.ANTIALIAS))

        self.bell_muted_image = ImageTk.PhotoImage(
            Image.open(main_path + "/assets/images/mutedBell.png").resize((50, 50), Image.ANTIALIAS))

        self.bell_muted_hovered_image = ImageTk.PhotoImage(
            Image.open(main_path + "/assets/images/mutedBell_hovered.png").resize((50, 50), Image.ANTIALIAS))

        self.arrowUp_image = ImageTk.PhotoImage(
            Image.open(main_path + "/assets/images/arrowUp.png").resize((147, 46), Image.ANTIALIAS))

        self.arrowUp_image_hovered = ImageTk.PhotoImage(
            Image.open(main_path + "/assets/images/arrowUp_hovered.png").resize((147, 46), Image.ANTIALIAS))

        self.arrowDown_image = ImageTk.PhotoImage(
            Image.open(main_path + "/assets/images/arrowDown.png").resize((147, 46), Image.ANTIALIAS))

        self.arrowDown_image_hovered = ImageTk.PhotoImage(
            Image.open(main_path + "/assets/images/arrowDown_hovered.png").resize((147, 46), Image.ANTIALIAS))
