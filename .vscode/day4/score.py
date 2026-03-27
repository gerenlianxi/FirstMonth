score=float(input("请输入成绩：（0-100）"))
if score>=90 and score<=100:
    grade="A"
elif score>=80 and score<90:
    grade="B"
elif score>=70 and score<80:
    grade="C"
elif score>=60 and score<70:
    grade="D"
elif score>=0 and score<60:
    grade="E"
else:
    grade="输入成绩有误，请重新输入！"
print("成绩等级：", grade)
print(f"你的成绩是{score}分,等级是{grade}")