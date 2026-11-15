import concurrent.futures
import os

def unit_task(num):
    print('module name:', __name__)                                   # __name__
    print('parent process:', os.getppid())                            # os.getppid() - parent process id
    print('process id:', os.getpid())                                 # os.getpid() - process id, if 2 cores/process used then 2 process ids 
    return num

def main():
    

    with concurrent.futures.ProcessPoolExecutor() as executor:                           
        results = executor.map(unit_task,(1,2,3,4,5))

    for result in results:
        print(result)

if __name__ == "__main__":
    main()

import sys

def main_func(*args):
    print("Script name:", sys.argv[0]) # Output: code.py

    # The rest are the arguments passed to the script
    print("Arguments:", sys.argv[1:])

    print(sys.argv[1])

    if len(sys.argv) > 3:
        print("More arguments provided. Exiting.")
        sys.exit()
    
if __name__ == "__main__":
    main_func()



