import sys

def main_func():
    print('Number of arguments: {}'.format(len(sys.argv)))
    print('Argument(s) passed: {}'.format(sys.argv))
    
    print("Script name:", sys.argv[0]) # Output: code.py
    
    # The rest are the arguments passed to the script
    print("Arguments:", sys.argv[1:])

    if len(sys.argv) > 3:
        print("More arguments provided. Exiting.")
        sys.exit()
    
if __name__ == "__main__":
    main_func()

