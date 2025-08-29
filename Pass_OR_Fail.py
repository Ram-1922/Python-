sum = 0
marks = []
for i in range(0,6):
    mark= int(input(f"Enter the mark {i}: "))
    marks.append(mark)
    sum += mark
avg = sum/5
result = "PASS" if avg > 60 else "FAIL" 
for i in range(0,6):
    print(f"Mark of Subject {i}: {marks[i]}")
print(f"You have {result}ED in the Exam...")
