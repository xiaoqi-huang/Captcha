import random
from random import choice
from string import ascii_letters, digits

from PIL import Image, ImageDraw, ImageFont


class Captcha:

    def create_captcha(self):
        self.text_colour, self.background_colour = self.get_colour()
        image = Image.new('RGB', (300, 100), self.background_colour)

        text = create_text(5)
        draw = ImageDraw.Draw(image)
        font = ImageFont.truetype('Lobster/Lobster_1.3.otf', 85)
        draw.text((20, 20), text, self.text_colour, font)
        self.draw_noise_lines(image)
        self.draw_noise_points(image)
        image.save('./images/image.jpg')

    def draw_noise_lines(self, image):
        width, height = image.size

        draw = ImageDraw.Draw(image)
        for _ in range(10):
            x0 = random.randint(0, width / 4)
            y0 = random.randint(0, height)
            x1 = random.randint(width - width / 4, width)
            y1 = random.randint(0, height)
            draw.line([x0, y0, x1, y1], self.text_colour, 4)

    def draw_noise_points(self, image):
        width, height = image.size

        draw = ImageDraw.Draw(image)
        for _ in range(2000):
            x = random.randint(0, width)
            y = random.randint(0, height)

            draw.point([x, y], self.text_colour)

    def get_colour(self):
        red = random.randint(155, 255)
        green = random.randint(155, 255)
        blue = random.randint(155, 255)
        return (red - 100, green - 100, blue - 100), (red, green, blue)

def create_text(length=5):
    text = ''.join([choice(ascii_letters + digits) for _ in range(length)])
    return text


Captcha().create_captcha()
