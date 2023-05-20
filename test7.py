#exercise

weight = float(input("Weight: "))

ver = input("(K)g or (L)bs: ")

if ver == "K" or ver == "k":
    converted = weight * 2.205
    print("weight in lbs: " + str(converted))
elif ver == "L" or ver == "l131":
    converted = weight / 2.205
    print("weight in kgs: " + str(converted))
else:
    print("Invalid")