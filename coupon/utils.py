import barcode
from barcode.writer import ImageWriter
import os

def generate_barcode_image(code):
    # Generate barcode using python-barcode library
    code128 = barcode.get_barcode_class('code128')
    barcode_instance = code128(code, writer=ImageWriter())

    # Set path to save the barcode image
    filename = f"barcode_{code}.png"  # You can specify the image format here
    filepath = os.path.join('media', 'barcode_images', filename)

    # Save the barcode image
    barcode_instance.save(filepath)
    return filepath