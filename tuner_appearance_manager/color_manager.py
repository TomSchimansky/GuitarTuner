import darkdetect
import sys


class ColorManager(object):
    def __init__(self):
        self.set_mode("Light")

    def set_mode(self, mode):
        if mode == "Dark":
            self.background_layer_1 = self.rgb_to_hex((50, 50, 50))
            self.background_layer_0 = self.rgb_to_hex((33, 33, 33))
            self.text_main = self.rgb_to_hex((255, 255, 255))
            self.text_2 = self.rgb_to_hex((169, 169, 169))
            self.text_2_highlight = self.rgb_to_hex((240, 240, 240))
            self.theme_main = self.rgb_to_hex((51, 94, 145))
            self.theme_dark = self.rgb_to_hex((26, 51, 82))
            self.theme_light = self.rgb_to_hex((85, 140, 200))
            self.needle = self.rgb_to_hex((107, 42, 28))
            self.needle_hit = self.rgb_to_hex((43, 113, 53))

        elif mode == "Light":
            self.background_layer_1 = self.rgb_to_hex((241, 239, 238))
            self.background_layer_0 = self.rgb_to_hex((209, 208, 206))
            self.text_main = self.rgb_to_hex((0, 0, 0))
            self.text_2 = self.rgb_to_hex((36, 36, 36))
            self.text_2_highlight = self.rgb_to_hex((0, 0, 0))
            self.theme_main = self.rgb_to_hex((83, 147, 213))
            self.theme_dark = self.rgb_to_hex((51, 94, 145))
            self.theme_light = self.rgb_to_hex((128, 175, 223))
            self.needle = self.rgb_to_hex((107, 42, 28))
            self.needle_hit = self.rgb_to_hex((43, 113, 53))

    @staticmethod
    def rgb_to_hex(rgb):
        return "#%02x%02x%02x" % rgb

    @staticmethod
    def detect_os_dark_mode():
        if sys.platform == "darwin":
            if darkdetect.theme() == "Dark":
                return True
            else:
                return False
        else:
            return True
