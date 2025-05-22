from PIL import Image, ImageFilter

# Pikachu - Sharpen
img = Image.open('./pokedox/pikachu.jpg')
sharp_pikachu = img.filter(ImageFilter.SHARPEN)
sharp_pikachu.save("sharp_pikachu.png")

# Bulbasaur - Blur
img = Image.open('./pokedox/bulbasaur.jpg')
blur_bulbasaur = img.filter(ImageFilter.BLUR)
blur_bulbasaur.save("blur_bulbasaur.png")

# Squirtle - Smooth
img = Image.open('./pokedox/squirtle.jpg')
smooth_squirtle = img.filter(ImageFilter.SMOOTH)
smooth_squirtle.save("smooth_squirtle.png")

# Charmander - Grayscale
img = Image.open('./pokedox/charmander.jpg')
grey_charmander = img.convert('L')
grey_charmander.save("grey_charmander.png")

