from PIL import Image

def gcl(p):
    if p / 5 - int(p / 5) >= 5:
        return lum[int(p / 5) + 1]
    else:
        return lum[int(p / 5)]

sbase = "-"
sselect = "█"
sint = 5
sfnt = [10 + 2 * i for i in range(sint)]
ssldr = [sbase for i in range(sint)]
curr = 3
ssldr[3] = sselect

lum = "$@B%8&WM#*oahZO0QLzcvt/\|()1{}[]?-_+~<>i!lI;:,\" `   "
lum = lum[::-1]

image = Image.open("q.jpg")

w, h = image.size

image = image.resize((int(w/(sfnt[curr] / 2)), int(h/sfnt[curr])))

image.save("r.jpg")

pimg = Image.open("r.jpg")
pix = pimg.load()

w, h = pimg.size

strarr = []

for i in range(h):
    cstr = ""
    for j in range(w):
        cstr += gcl(sum(pix[j, i]) / len(pix[j, i]))
    strarr.append(cstr)

p = open("echo.txt", "a")

for i in strarr:
    print(i)
    p.write(f"{i}\n")