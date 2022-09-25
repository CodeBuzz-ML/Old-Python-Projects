#35 > = FAIL 
#36 - 49 = C 
#50 - 59 = B
#60 - 75 = B+ 
#76 - 85 = A 
#86 - 100 = A+ 
#Tasks = Input Data From User.
#        Calculate the average of all the marks
#        Calculate the grades for individual marks
#        If any subject is failed, Total Marks == Failed. 
#Subjects: English 
    #      Maths 
    #      Physics
    #      Chemistry 
    #      Biology 
    #      Hindi
    #      Marathi
    #      Art
#actual code start: -
#User Input 
EnglishMarks = int(input("Enter Your English Marks Here: - "))
MathMarks = int(input("Enter Your Mathematics Marks Here: - "))
PhysicsMarks = int(input("Enter Your Physics Marks Here: - "))
ChemistryMarks = int(input("Enter Your Chemistry Marks Here: - "))
BiologyMarks = int(input("Enter Your Biology Marks Here: - "))
HindiMarks = int(input("Enter Your Hindi Marks Here: - "))
MarathiMarks = int(input("Enter Your Marathi Marks Here: - "))
ArtMarks = int(input("Enter Your Art Makrs Here: - "))
print("Calculation in progress...")
#Calculation Start
#English Marks Calculation
if EnglishMarks <= 35:
    print("Failed In English")
elif 35 < EnglishMarks <= 49:
    print("English Grade: C")
elif 50 < EnglishMarks <= 59:
    print("English Grade: B")
elif 60 < EnglishMarks <= 75:
    print("English Grade: B+")
elif 76 < EnglishMarks <= 85:
    print("English Grade: A")
elif 86 < EnglishMarks <= 100:
    print("English Grade: A+")
#Maths Marks Calculation
if MathMarks <= 35:
    print("Failed In Math")
elif 35 < MathMarks <= 49:
    print("Math Grade: C")
elif 50 < MathMarks <= 59:
    print("Math Grade: B")
elif 60 < MathMarks <= 75:
    print("Math Grade: B+")
elif 76 < MathMarks <= 85:
    print("Math Grade: A")
elif 86 < MathMarks <= 100:
    print("Math Grade: A+")
#Physics Marks Calculation
if PhysicsMarks <= 35:
    print("Failed In Physics")
elif 35 < PhysicsMarks <= 49:
    print("Physics Grade: C")
elif 50 < PhysicsMarks <= 59:
    print("Physics Grade: B")
elif 60 < PhysicsMarks <= 75:
    print("Physics Grade: B+")
elif 76 < PhysicsMarks <= 85:
    print("Physics Grade: A")
elif 86 < PhysicsMarks <= 100:
    print("Physics Grade: A+")
#Chemistry Marks Calculation
if ChemistryMarks <= 35:
    print("Failed In Chemistry")
elif 35 < ChemistryMarks <= 49:
    print("Chemistry Grade: C")
elif 50 < ChemistryMarks <= 59:
    print("Chemistry Grade: B")
elif 60 < ChemistryMarks <= 75:
    print("Chemistry Grade: B+")
elif 76 < ChemistryMarks <= 85:
    print("Chemistry Grade: A")
elif 86 < ChemistryMarks <=100:
    print("Chemistry Grade: A+")
#Biology Marks Calculation
if BiologyMarks <= 35:
    print("Failed In Biology")
elif 35 < BiologyMarks <= 49:
    print("Biology Grade: C")
elif 50 < BiologyMarks <= 59:
    print("Biology Grade: B")
elif 60 < BiologyMarks <= 75:
    print("Biology Grade: B+")
elif 76 < BiologyMarks <= 85:
    print("Biology Grade: A")
elif 86 < BiologyMarks <= 100:
    print("Biology Grade: A+")  
#Hindi Marks Calculation
if HindiMarks <= 35:
    print("Failed In Hindi")
elif 35 < HindiMarks <= 49:
    print("Hindi Grade: C")
elif 50 < HindiMarks <= 59:
    print("Hindi Grade: B")
elif 60 < HindiMarks <= 75:
    print("Hindi Grade: B+")
elif 76 < HindiMarks <= 85:
    print("Hindi Grade: A")
elif 86 < HindiMarks <= 100:
    print("Hindi Grade: A+")
#Marathi Marks Calculation
if MarathiMarks <= 35:
    print("Failed In Marathi")
elif 35 < MarathiMarks <= 49:
    print("Marathi Grade: C")
elif 50 < MarathiMarks <= 59:
    print("Marathi Grade: B")
elif 60 < MarathiMarks <= 75:
    print("Marathi Grade: B+")
elif 76 < MarathiMarks <= 85:
    print("Marathi Grade: A")
elif 86 < MarathiMarks <= 100:
    print("Marathi Grade: A+")
#Art Marks Calculation
if ArtMarks <= 35:
    print("Failed In Art")
elif 35 < ArtMarks <= 49:
    print("Art Grade: C")
elif 50 < ArtMarks <= 59:
    print("Art Grade: B")
elif 60 < ArtMarks <= 75:
    print("Art Grade: B+")
elif 76 < ArtMarks <= 85:
    print("Art Grade: A")
elif 86 < ArtMarks <= 100:
    print("Art Grade: A+")
    
#Overall Marks Calculation
OverallMarks = (EnglishMarks + MathMarks +  PhysicsMarks + ChemistryMarks + BiologyMarks + HindiMarks + MarathiMarks + ArtMarks)/8
print("Overall marks = ")
print(OverallMarks)

#Fail Or Pass Calculation 

if ArtMarks or BiologyMarks or ChemistryMarks or EnglishMarks or HindiMarks or MarathiMarks or MathMarks < 35:
    print("Overall Result: FAIL")
else:
    print("Overall Result: PASS ")
▲