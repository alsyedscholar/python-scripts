import os.path
import re
import os


path = input("Enter your value: ")
# take the path and reverse split without having file name
# split_path = path.rsplit('/',1 )
# # add the path with new dir..
# save_path = split_path[0] + "/UpdatedLinks"

# # after compiling make dir to save the output
# # Check whether the specified path exists or not
# isExist = os.path.exists(save_path)
# if not isExist:
#    # Create a new directory because it does not exist
#    os.makedirs(save_path)

with open(path) as f:
    lines = f.readlines()

with open("updated-link.txt", "w") as f:
    for line in lines:
        print(line)
        split_link = re.split('_', line)
        for x in range(32):
            required_path = split_link[0] + "_" + str(x) + ".webp"
            print(required_path)
            f.write(required_path)
            f.write("\n")

