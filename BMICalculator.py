'''
Created on Jun 24, 2018

@author: Trevor Pirone
'''

# A simple BMI calculator created using Python.

def main():
    print("BMI Calculator")
    weight = input("Please enter your weight in pounds!")
    print(weight)
    storeWeight = int(weight)
    height = input("Please enter your height in inches!")
    print(height)
    storeHeight = int(height)
    bmi = (storeWeight*703)/(storeHeight*storeHeight)
    bmi = round(bmi, 1)
    print("Your BMI value is",bmi,)
    if (bmi < 18.5): {
        print("Underweight")
    }
    elif (bmi >= 18.5 and bmi <= 24.9): {
        print("Normal weight")
    }
    elif (bmi > 24.9 and bmi < 30): {
        print("Overweight")
    }
    else: {
        print("Obesity")
    }
    
if __name__ == "__main__":
    main()
    