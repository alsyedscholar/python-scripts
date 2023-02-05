import os

def main():
	# i = 1
	PATH = input("Enter your value: ")
	number = input("Enter number form where you want to start! ")
	number = int(number)
	dir_list = os.listdir(PATH)
	for path in dir_list:
		# print(path)
		path = PATH + "/" + path
		new_name = PATH + "/ " + str(number) + '.jpg'
		os.rename(path,new_name)
		number += 1

# Driver Code
if __name__ == '__main__':
	# Calling main() function
	main()