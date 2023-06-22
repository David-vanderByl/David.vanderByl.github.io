from PIL import Image, ImageOps

def change_image_transparency(image_path, transparency, bw=False):
    # Open the image
    image = Image.open(image_path)

    # Convert the image to RGBA if it's not already
    if image.mode != 'RGBA':
        image = image.convert('RGBA')

    # Get the image data as a list of tuples
    data = list(image.getdata())

    # Update the alpha value (transparency) for each pixel
    new_data = [(r, g, b, int(alpha * transparency)) for r, g, b, alpha in data]

    # Update the image data
    image.putdata(new_data)
    
    if bw:
        image = ImageOps.grayscale(image)


    # Save the modified image
    image.save('transparent_image.png')

# Usage example

# Example usage
input_image_path = "Aura wallpaper - Anahata (Lead Time 8-10 Weeks).jpeg"
transparency_value = 0.1  # Range from 0.0 (fully transparent) to 1.0 (fully opaque)
bw = True


change_image_transparency(input_image_path, transparency_value, bw)