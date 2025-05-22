from PIL import Image, ImageFilter
img = Image.open('./pokedox/pikachu.jpg')
sharp_pikachu = img.filter(ImageFilter.SHARPEN)
img.save("sharp_pikachu", 'png')

img = Image.open('./pokedox/bulbasaur.jpg')
blur_bulbasaur = img.filter(ImageFilter.BLUR)
img.save("blur_bulbasaur", 'png')

img = Image.open('./pokedox/squirtle.jpg')
smooth_squirtle = img.filter(ImageFilter.SMOOTH)
img.save("smooth_squirtle" , 'png')

img = Image.open('./pokedox/charmander.jpg')
grey_charmander = img.convert('L')
grey_charmander.save("grey_charmander", 'png')
