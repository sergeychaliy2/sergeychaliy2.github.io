import os, sys
from PIL import Image
root = sys.argv[1]
names = sorted(os.listdir(os.path.join(root, "screens")))
ims = [Image.open(os.path.join(root, "screens", n)).resize((330, 587), Image.LANCZOS) for n in names]
sheet = Image.new("RGB", (330*3+40, 587*2+30), (20, 20, 26))
for i, im in enumerate(ims):
    sheet.paste(im, ((i % 3)*340+5, (i//3)*597+5))
sheet.save(os.path.join(root, "_preview", "sheet.png"))
print("saved", sheet.size, names)
