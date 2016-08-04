from PIL import Image
darkBlue = (0, 51, 76)
rojo = (217, 26, 33)
lightBlue = (112, 150, 158)
yellow = (252, 227, 166)
im = Image.open("sunset.jpg")

data = im.getdata()
data_list = list(data)

def colorize(image_data):
	new_pic = []
	for pixel in image_data:
		red = pixel[0]
		green = pixel[1]
		blue = pixel[2]
		total_value_of_pixels = red + green + blue
		
		if total_value_of_pixels < 182:
			new_pic.append(darkBlue)
		elif total_value_of_pixels < 364:
			new_pic.append(rojo)
		elif total_value_of_pixels < 546:
			new_pic.append(lightBlue)
		else:
			new_pic.append(yellow)
		'''
		Alternate Solution:
		if total_value_of_pixels >= 182 && total_value_of_pixels < 364:
			new_pic.append(rojo)
		if total_value_of_pixels >= 364 && total_value_of_pixels < 546:
			new_pic.append(lightBlue)
		if total_value_of_pixels >= 546:
			new_pic.append(yellow)	
		'''
	return new_pic
new_data_list = colorize(data_list)

new_image = Image.new(im.mode, im.size)
new_image.putdata(new_data_list)
new_image.show()
new_image.save = ("output.jpg", "jpeg")

		
	
