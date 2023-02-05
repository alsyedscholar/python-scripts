import cv2
import os


fewColors = {
    (0,0,0), 
    # (255,255,255),
    (0,255,0),
    (0,0,255),
    (255,255,0),
    (0,255,255),
    (255,0,255),
    (192,192,192),
    (128,128,128),
    (128,0,0),
    (128,128,0),
    (0,128,0),
    (128,0,128),
    (0,128,128),
    (0,0,128),
    (128,0,0)
}


i = 1 

for color in fewColors:
	# print(color)
    # # Get the list of all files and directories
    path = '/Users/adilhussain/Downloads/BedsAndFramesCanada/'
    dir_list = os.listdir(path)

    for path in dir_list:
        print(path)
        if(path == '.DS_Store'):
            continue
        image_path = '/Users/adilhussain/Downloads/BedsAndFramesCanada/'+path
        print(image_path)
    
        image_lower = cv2.imread(image_path)
        image_left = cv2.imread(image_path)
        image_right = cv2.imread(image_path)
        image_upper = cv2.imread(image_path)

        height = image_lower.shape[0]
        width = image_lower.shape[1]
        
        # left line
        cv2.line(image_lower, (0,0), (0, height), color, 90)

        # top line
        cv2.line(image_lower, (0,0), (width, 0), color, 90)

        # bottom line
        cv2.line(image_lower, (width, height), (0, height), color, 90)

        # right line
        cv2.line(image_lower, (width, height), (width, 0), color, 90)

        lower_dir_path = '/Users/adilhussain/Downloads/BedandFrameCanada/BelowRed/'
        right_dir_path = '/Users/adilhussain/Downloads/BedandFrameCanada/RightRed/'
        left_dir_path = '/Users/adilhussain/Downloads/BedandFrameCanada/LeftRed/'
        upper_dir_path = '/Users/adilhussain/Downloads/BedandFrameCanada/UpperRed'
        name_file = str(i) + path
        cv2.imwrite(os.path.join(lower_dir_path , name_file), image_lower)
        # cv2.imwrite(os.path.join(right_dir_path , name_file), image_right)
        # cv2.imwrite(os.path.join(left_dir_path , name_file), image_left)
        # cv2.imwrite(os.path.join(upper_dir_path , name_file), image_upper)
        i += 1
    

