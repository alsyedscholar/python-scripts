from PIL import Image
import imagehash
import os

def main():
    PATH = input("Enter Your Right Path: ")
    dir_list = os.listdir(PATH)
    cutoff = 1  # maximum bits that could be different between the hashes. 

    with open("compareImages.txt", "w") as f:    
        for path in dir_list:
            if(path == '.DS_Store'):
                continue
            path1 = PATH + "/" + path
            # print(path)
            hash0 = imagehash.average_hash(Image.open(path1)) 
            
            for curr_path in dir_list:
                # print(curr_path+ "IS AN ERROR...")
                if(curr_path == '.DS_Store'):
                    continue
                curr_path1 = PATH + "/" + curr_path
                hash1 = imagehash.average_hash(Image.open(curr_path1)) 
                if hash0 - hash1 < cutoff:
                    print('images are similar')
                    # print(curr_path)
                    # print(path)
                    if(path != curr_path):
                        f.write(path +", "+ curr_path)
                        f.write("\n")

                # else:
                #     print('images are not similar')


#  Driver Code
if __name__ == '__main__':
	# Calling main() function
	main()