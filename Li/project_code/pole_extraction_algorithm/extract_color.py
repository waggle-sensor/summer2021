import os   
import cv2
import glob
from sklearn.cluster import KMeans
from collections import Counter
import webcolors

# read images from files and extract names from directory
def read_images(files):
    # lists for name and image data
    names, img_data = [], []
    # iterates through all images in folder
    for myFile in files:
        img = cv2.imread(myFile)
        img_data.append(img)
        # take the name of the image from directory
        _ , name = os.path.split(myFile) 
        names.append(name)
    return names, img_data

def split_image(img):
    
    M = img.shape[0]//4
    N = img.shape[1]//4
    chunks = [img[x:x+M,y:y+N] for x in range(0,img.shape[0],M) for y in range(0,img.shape[1],N)]
    chunks = chunks[-4:]
    chunks.append(img[200:200 + 450, 100:100 + 200])
    chunks.append(img[125:125 + 450, 650:650 + 200])
    chunks.append(img[275:275 + 450, 875:875 + 200])    
    return chunks


def get_colors(image, number_of_colors, show_chart):

    # resize the image to the size 600 x 400, saves time
    modified_image = cv2.resize(image, (600, 400), interpolation = cv2.INTER_AREA)
    modified_image = modified_image.reshape(modified_image.shape[0]*modified_image.shape[1], 3)
    
    # KMeans algorithm creates clusters based on the supplied count of clusters
    clf = KMeans(n_clusters = number_of_colors)
    labels = clf.fit_predict(modified_image)
    
    # get count of all labels
    counts = Counter(labels)
    
    center_colors = clf.cluster_centers_
    # We get ordered colors by iterating through the keys
    ordered_colors = [center_colors[i] for i in counts.keys()]
    rgb_colors = [ordered_colors[i] for i in counts.keys()]

    return rgb_colors


def label_color(rgb_color):
    min_colours = {}
    for key, name in webcolors.CSS3_HEX_TO_NAMES.items():
        r_c, g_c, b_c = webcolors.hex_to_rgb(key)
        rd = (r_c - rgb_color[0]) ** 2
        gd = (g_c - rgb_color[1]) ** 2
        bd = (b_c - rgb_color[2]) ** 2
        min_colours[(rd + gd + bd)] = name
    return min_colours[min(min_colours.keys())]

def extract_rgb(chunks):
    row = []
    for i in range(len(chunks)):
        bgr = get_colors(chunks[i], 1, True)
        bgr = bgr[0]
        col = label_color(bgr)  
        row.append(col)
    return row

def classify_color(row):
    excluded_colors = ["aliceblue", "antiquewhite", "aqua", "aquamarine", "azure", "beige", "bisque", "blanchedalmond", 
           "blue", "blueviolet", "brown", "burlywood", "cadetblue", "chartreuse", "chocolate", "coral", "cornflowerblue", 
           "cornsilk", "crimson", "cyan", "darkblue", "darkcyan", "darkgoldenrod", "darkgreen", 
           "darkkhaki", "darkmagenta", "darkolivegreen", "darkorange", "darkorchid", "darkred", "darksalmon", 
            "darkseagreen", "darkturquoise", "darkviolet", "deeppink","firebrick", 
            "floralwhite", "forestgreen", "fuchsia", "gainsboro", "ghostwhite", "gold", "goldenrod", "green", "greenyellow", "honeydew", "hotpink", 
           "indianred", "indigo", "ivory", "khaki", "lavender", "lavenderblush", "lawngreen", "lemonchiffon", "lightblue", "lightcoral", 
           "lightcyan", "lightgoldenrodyellow", "lightgreen", "lightpink", "lightsalmon", "lightseagreen", "lightskyblue", 
           "lightyellow", "lime", "limegreen", "linen", "magenta", "maroon", "mediumaquamarine", "mediumblue", "mediumorchid", "mediumpurple", "mediumseagreen", 
           "mediumspringgreen","mediumturquoise", "mediumvioletred", "mintcream", "mistyrose", "moccasin", "navajowhite", 
           "navy", "oldlace", "olive", "olivedrab", 
           "orange", "orangered", "orchid", "palegoldenrod", "palegreen", "paleturquoise",
           "palevioletred", "papayawhip", "peachpuff",
            "peru", "pink", "plum", "powderblue", "purple", "rebeccapurple", "red", "rosybrown", "saddlebrown", "salmon", "sandybrown", 
           "seagreen", "seashell", "sienna", "silver", "skyblue", "snow", "springgreen", 
           "tan", "teal", "thistle", "tomato", "turquoise", "violet", "wheat", 
           "white", "whitesmoke", "yellow", "yellowgreen"]
    night_colors = ["black", "darkslategray"]
    otsu_colors = ["dimgray", "royalblue", "darkslateblue"]
    
    # labeling images
    # night colors: colors that occur at night
    # excluded colors: colors from webcolors library that may indicate no snow or 
    # do not appear at all in the images
    # otsu colors: colors that otsu performs well in
    
    if any(x in row for x in excluded_colors):
        print("There is no snow.")
        return None
    elif any(x in row for x in night_colors): 
        if any(x in row for x in otsu_colors):
            return "OTSU"
        else: 
            print("This is nighttime.")
            return None
    else:
        # finds highest occuring color
        res = max(set(row), key = row.count) 
        if any(x in res for x in otsu_colors):
            return "OTSU"
        else:
            return "CANNY"

def main():


    files = glob.glob ("C:/Users/hp/Desktop/notes_CV/tests/photos/*.JPG")
    names, img_data = read_images(files)
    
    count = 0
    for i in range(len(img_data)):
        count += 1
        print(count)
        img = cv2.cvtColor(img_data[i], cv2.COLOR_BGR2RGB) 
        chunks = split_image(img)
        row = extract_rgb(chunks)
        cat = classify_color(row)
        print(cat)
        
if __name__=="__main__":
   main()    