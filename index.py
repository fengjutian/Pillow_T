# Using the Image class

# from PIL import Image
# im = Image.open("hu.jpeg")
# print(im.format, im.size, im.mode)
# im.show()

# Convert files to JPEG
# import os, sys
# from PIL import Image

# for infile in sys.argv[1:]:
#     f, e = os.path.splitext(infile)
#     outfile = f + ".jpg"
#     if infile != outfile:
#         try:
#             with Image.open(infile) as im:
#                 im.save(outfile)
#         except OSError:
#             print("cannot Convert", infile)
            

# Create JPEG thumbnails

# import os, sys
# from PIL import Image
# size = (128, 128)
# for infile in sys.argv[1:]:
#     outfile = os.path.splitext(infile)[0] + ".thumbnails"
#     if infile != outfile:
#         try:
#             with Image.open(infile) as im:
#                im.thumbnail(size)
#                im.save(outfile, "JPEG")
#         except OSError:
#             print("cannot create thumbnail for", infile)


# Identify Image Files
# import os, sys
# from PIL import Image
# for infile in sys.argv[1:]:
#     try:
#         with Image.open(infile) as im:
#             print(infile, im.format, f"{im.size}x{im.mode}")
#     except OSError:
#         pass

#Copying a subrectangle from an image
# from PIL import Image
# im = Image.open("hu.jpeg")
# box = (100, 100, 400, 400)
# region = im.crop(box)
# region.show()


#Processing a subrectangle, and pasting it back
# from PIL import Image
# im = Image.open("hu.jpeg")
# box = (100, 100, 400, 400)
# region = im.crop(box)
# region = region.transpose(Image.ROTATE_180)
# im.paste(region, box)
# im.show()


#https://pillow.readthedocs.io/en/stable/handbook/tutorial.html

