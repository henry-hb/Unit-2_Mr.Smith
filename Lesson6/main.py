from PIL import Image, ImageFilter, ImageEnhance

orange_cat = Image.open(r"Unit-2\Lesson6\orange_cat.jpg")
blurry_cat = orange_cat.filter(ImageFilter.GaussianBlur(20))
blurry_cat.save(r"Unit-2\Lesson6\blurry_cat.jpg")
blurry_cat.show()
bw_cat = ImageEnhance.Color(orange_cat).enhance(0).save(r"Unit-2\Lesson6\bw_cat.jpg")
bright_cat = ImageEnhance.Color(orange_cat).enhance(10).save(r"Unit-2\Lesson6\bright_cat.jpg")