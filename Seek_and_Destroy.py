from PIL import Image
import os
import shutil

def find_image_name():
    #a function that finds the python file's directory
    path = dir_path = os.path.dirname(os.path.realpath(__file__))
    files = []
    # r=root, d=directories, f = files
    #wtf i dunno i copied this from the internet
    for r, d, f in os.walk(path):
        for file in f:
            if ('.jpg' in file or '.png' in file):
                files.append(os.path.join(file))
    return files

#i didnt end up using them
#emptry a txt file
def clear_file():
    input("kill file")
    with open("pixels_list.txt","a+") as file:
        file.truncate(0)

#output array to file
def outFileHandle(info):
    with open("pixels_list.txt","a") as file:
        for element in info:
            file.write(element)
        file.write("\n")

#############################################################################################
#open designed image and take 3 sample pixels
def find_pixels(image_name):
    image = Image.open(image_name)
    data = []

    size = list(image.size)
    x = size[0] / 2
    y = size[1] / 2
    center = x,y
    data.append(image.getpixel(center))

    x = size[0] * 4 / 5
    y = size[1] * 4 / 5
    rc = x,y
    data.append(image.getpixel(rc))

    x = size[0] * 1 / 5
    y = size[1] * 1 / 5
    lc = x,y
    data.append(image.getpixel(lc))

    return data
    del image

#go through all images to creat the mega_data
def creat_pixels(files):
    for image in files:
        try:
            mega_data[image] = find_pixels(image)
        except:
            pass
#############################################################################################
#find identical values in mega_data
def find_devients():
    devients = []
    for x in mega_data:
        for y in mega_data:
            if(mega_data[x]== mega_data[y] and x != y):
                devients.append(str(x))
    return devients


#forgive me father for I am sinned, I have used a global variable today
mega_data = {}

def main():
    print("start of program\nfinding identical images in directory\n")
    #have all name of image in a list
    file_names = find_image_name()
    #create mega_data <- a collection of sample pixels
    creat_pixels(file_names)
    print("scan complete")
    #create list of redundent
    devients = find_devients()

    #print name of repeted image
    print("\nresult:")
    for i in devients:
        print(i)

    #move repeted stuff to new folder(that it will try to create)
    new_path = os.path.dirname(os.path.realpath(__file__))
    new_path += "\\devients\\"
    try:
        os.makedirs(new_path)
    except:
        pass
    for item in devients:
        try:
            shutil.move(item,new_path)
        except:
            pass

#test use function
def print_data():
    for x in mega_data:
        print(x,end='')
        print(mega_data[x])

if __name__ == "__main__":
    main()
