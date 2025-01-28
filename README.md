mario.py
height = int(input("Height (1-23): "))

while height > 23 or height < 1:
    print("Error: Number out of bounds")
    height = int(input("Height (1-23): "))

if height == 1:
    print("# #")
else:
    # for each row
    for i in range(0, height, 1):
        
        # print the spaces
        for j in range(1, (height - i), 1):
            print(" ", end="")
            
        # then print the pound symbol
        for k in range(i+1):
            print("#", end="")

        # print the center 2 wide gap
        print("  ", end="")
        
        # begin right pyramid
        for l in range(i+1):
            # if l == i print the a newline after the #
            if l == i:
                print("#")
            else:
                # print # without a newline
                print("#", end="")
