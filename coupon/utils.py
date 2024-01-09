import barcode
from barcode.writer import ImageWriter
import secrets

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

def generate_coupon_code():
    """ Generate a random coupon code using secrets and order number """
    # Define the length of the random part
    length = 8
    # Create the random part
    random_part = secrets.token_hex(length)
    # Append the order number
    coupon_code = random_part
    # Return the coupon code
    return coupon_code