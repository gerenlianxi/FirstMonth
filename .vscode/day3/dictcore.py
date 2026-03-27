student={"name": "张三", "age": 20,"score":90}
print("姓名：", student["name"])
print("年龄：", student["age"])
student["age"] = 21
print("更新后的年龄：", student["age"])
student["gender"] = "男"
student["class"] = "高三一班"
print("新增后的字典",student)
del student["score"]
print("删除后的字典",student)