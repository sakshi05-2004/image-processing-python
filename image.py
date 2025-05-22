from PIL import Image, ImageFilter
img = Image.open('./pokedox/pikachu.jpg')
sharp_img = img.filter(ImageFilter.SHARPEN)
img.save("sharp.png", 'png')

img = Image.open('./pokedox/bulbasaur.jpg')
blur_img = img.filter(ImageFilter.BLUR)
img.save("blur.png", 'png')

img = Image.open('./pokedox/squirtle.jpg')
smooth_img = img.filter(ImageFilter.SMOOTH)
img.save("smooth.png", 'png')

img = Image.open('./pokedox/charmander.jpg')
grey_img = img.convert('L')
grey_img.save("grey.png", 'png')