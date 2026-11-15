
a = 10
status = "active"

if (a < 5) \
    & (status == "active"):
    print("a is less than 5 and its active")
elif (a<10) \
    & (status == "active"):
    print("a is less than 10 and its active")
else:
    print("a more than 10 and its active")

for item in range(1,10):
    if item < 4:
        print("a is less than 4")
    elif item < 8:
        print("a is more than 4 and less than 8")
    else:
        print("a is more than 8")

my_dict = { "name":"prasoon gupta",
            "sex" :"male",
            "city":"mumbai",
            }