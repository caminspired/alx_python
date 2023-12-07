import sys 

if __name__ == "__main__":
    argv = sys.argv[1:]
    num_arguments = len(argv)
    
    if num_arguments == 0:
        print("{} arguments: \n".format(num_arguments))
        
    elif num_arguments == 1:
        print("{} argument: \n".format(num_arguments))
        
    else:
        print("{} arguments: \n".format(num_arguments))
        
        for i, arg in enumerate(argv, start=1):
            print("{}: {}".format(i, argument))
