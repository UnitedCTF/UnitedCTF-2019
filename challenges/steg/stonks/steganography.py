import numpy as np
from PIL import Image

class Steganography:
    def embed(self, cover_file, secret_file, color_plane, pixel_bit):
        cover_array = self.image_to_matrix(cover_file)
        secret_array = self.image_to_matrix(secret_file)
        # every bit except the one at `pixel_bit` position is 1
        mask = 0xff ^ (1 << pixel_bit)
        # shift the MSB of the secret to the `pixel_bit` position
        secret_bits = ((secret_array[...,color_plane] >> 7) << pixel_bit)
        height, width, _ = secret_array.shape
        cover_plane = (cover_array[:height,:width,color_plane] & mask) + secret_bits
        cover_array[:height,:width,color_plane] = cover_plane
        stego_image = self.matrix_to_image(cover_array)
        return stego_image

    def extract(self, stego_file, color_plane, pixel_bit):
        stego_array = self.image_to_matrix(stego_file)
        change_index = [0, 1, 2]
        change_index.remove(color_plane)
        stego_array[...,change_index] = 0
        stego_array = ((stego_array >> pixel_bit) & 0x01) << 7
        exposed_secret = self.matrix_to_image(stego_array)
        return exposed_secret

    def image_to_matrix(self, file_path):
        return np.array(Image.open(file_path))

    def matrix_to_image(self, array):
        return Image.fromarray(array)

plane = 0
bit = 1

cover_file = "stonks.png"
secret_file = "secretstonks.png"

stego_file = "stego.png"
extracted_file = "extracted.png"

S = Steganography()
S.embed(cover_file, secret_file, plane, bit).save(stego_file)
S.extract(stego_file, plane, bit).save(extracted_file)
