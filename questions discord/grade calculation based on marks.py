mark=int(input("enter the marks"))
if mark>100:
    grade="invalid"
elif mark >=90:
    grade="A+"
elif mark>=80:
    grade="A"
elif mark>=70:
    grade="B+"
elif mark>=60:
    grade="B"
elif mark>=50:
    grade="C+"
elif mark>=40:
    grade="C"
else:
    grade="fail"
print(f"the grade is {grade}")