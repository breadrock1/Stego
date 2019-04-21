import argparse, sys
from PIL import Image, ImageDraw
from random import randint
from re import findall

def stega_encrypt():
    keys = []
    img = Image.open(input("path to image: "))
    draw = ImageDraw.Draw(img)
    width = img.size[0]
    height = img.size[1]
    pixels = img.load()
    file = open('keys.txt','w')
    
    for elem in ([ord(elem) for elem in input("text here: ")]):
        key = (randint(1,width-100),randint(1,height-100))
        green, blue = pixels[key][1:3]
        draw.point(key, (elem, green, blue))
        file.write(str(key)+'\n')

    print('keys were written to the keys.txt file')
    img.save("140.bmp", "BMP")
    file.close()

def stega_decrypt():
    msg = []
    keys = []
    img = Image.open(input("path to image: "))
    pix = img.load()
    file = open(input('path to keys: '),'r')
    kek = str([line.strip() for line in file])
    
    for i in range(len(findall(r'\((\d+)\,',kek))):
        keys.append((int(findall(r'\((\d+)\,',kek)[i]),int(findall(r'\,\s(\d+)\)',kek)[i])))
    for key in keys:
        msg.append(pix[tuple(key)][0])
    
    file.close()
    return ''.join([chr(elem) for elem in msg])


def args_parse():
    parser = argparse.ArgumentParser(description="If you wanna encrypt your message to picture " +
        "enter command without options or type '-d encrypt' else for decrypting message from " +
        "picture enter command with option '-d decrypt'. Type '-h' for help and see more information")
    parser.add_argument("-d", "--decrypt", metavar="", type=str, default="encrypt", help="To decrypt your message from picture type '-d decrypt'")
    return parser
def main():
    arg = args_parse()
    namespace = arg.parse_args(sys.argv[1:])
    if namespace.decrypt == "decrypt":
        print("your message: ",stega_decrypt())
    else:
        stega_encrypt()
        print('DONE!!! \n Your message has been encrypted!!!')

if __name__ == "__main__":
    main(sys.argv[1:])
