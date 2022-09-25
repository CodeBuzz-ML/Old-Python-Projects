print("Welcome to the calculator!")
print("+ = Addition")
print("- = Subtraction")
print("* = Multiplication")
print("/ = Division")

opval = str(input("Enter the operation: - "))

if opval == "+":
    numa1 = int(input("Enter the first number: "))
    numa2 = int(input("Enter the second number: "))
    aans = numa1 + numa2
    print(aans)
if opval == "-":
    nums1 = int(input("From? : "))
    nums2 = int(input("What? : "))
    sans = nums1 - nums2
    print(sans)
if opval == "*":
    numm1 =  int(input("Enter the first number: - "))
    numm2 =  int(input("Enter the second number: - "))
    mans = numm1 * numm2 
if opval == "/":
    numd1 = int(input("Enter the first number: - "))
    numd2 = int(input("Enter the second number: - "))
    dans = numd1 / numd2 
    print(dans)