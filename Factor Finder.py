#To find the factors of the number input by the user
uinput = int(input("Enter the number to find the factors of: - "))
print("The factors are: - ")
for i in range(1,1000):
  if(uinput%i == 0):
        print(i)