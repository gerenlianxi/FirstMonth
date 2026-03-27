class_students = {
    "高一1班" : [
        {"name":"张三","age":21,"gender":"男"},
        {"name":"李四","age":20,"gender":"女"},
        {"name":"王五","age":22,"gender":"男"}    
    ],
    "高一2班" : [
        {"name":"赵六","age":19,"gender":"男"},
        {"name":"钱七","age":21,"gender":"女"},
        {"name":"孙八","age":20,"gender":"男"}
    ]              
}
all_students = class_students["高一1班"]
print("班级所有学生：", all_students)
print("第二个学生姓名",all_students[1]["name"])
two_students=class_students["高一2班"]
print("第二个学生姓名",two_students[1]["name"])
all_students[0]["score"]=95
print("更新后的学生信息：", all_students[0])
print("班级所有学生：", all_students)