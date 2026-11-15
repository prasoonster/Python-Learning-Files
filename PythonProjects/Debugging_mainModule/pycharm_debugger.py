
import numpy as np

def generateRabdom(upper):

    r = np.random.randint(1,upper)
    return r


def main():
    run = True
    num1 = generateRabdom(10)
    num2 = generateRabdom(10)
    result = num1 * num2

    while run:
        ans = input("what is " + str(num1) + " and " + str(num2) + " multiplication ?")

        if ans.isdigit():
            if int(ans)  == result:
                print("answer is correct")
                run = False

            else:
                print("answer is not correct, give correct answer")
        else:
            print("answer must be a number")


times = 10

for x in range(times):
    main()