height_as_float = float(input("Enter the height in meter:"))
weight_as_int = int(input("Enter the weight in kilogram:"))
BMI = weight_as_int/height_as_float**2
print("Your Body Mass Index is:",BMI)
if BMI<=18.5:
    print("You are underweight.")
elif BMI<=25:
    print("You are healthy.")
elif BMI<=30:
    print("You are overweight.")
else:
    print("You are obese.")            