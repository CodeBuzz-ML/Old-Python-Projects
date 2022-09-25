#Taking a data input from the user...
resulteng = int(input("Enter your english marks: -"))
resultsci = int(input("Enter your Science marks: - "))
resulthin = int(input("Enter your hindi marks: -"))
resultmath = int(input("Enter your math marks: -")) 

#Calculating the average of the marks given by the user

# Average = 1st Value + 2nd Value + 3rd Value / 2

Average = (resulteng+resultsci+resulthin+resultmath)/4

if Average > 90:
    print("Grade = A")
elif 80 < Average < 90:
    print("Grade = B")
elif 70 > Average > 80:
    print("Grade = C")
elif 60 > Average > 70:
    print("Grade = D")
elif Average < 60:
    print("Grade = E, Needs practice")