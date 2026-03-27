#/字典dict 每个键key对应一个值value，键必须是唯一的，值可以重复
student={"name": "张三", "age": 20,"score":90}
print(student.keys())
print(student.values())
print(student.items())  
print(student["name"]) 
print(student["age"])
student["score"]=95
print(student) 
del student["age"]
print(student)
#/列表list 可变的有序集合，可以包含重复元素，可以修改列表中的元素
scores=[85,90,95,88]
scores.append(100)
scores[1]=92
scores.insert(2, 93)
del scores[0]
print(scores[2])
print(scores)
#/元组tuple 不可变的有序集合，可以包含重复元素，不能修改元组中的元素
point=(10,20)
print(point[0])
print(point[1])
print(point)
#/集合set 无序的可变集合，不允许重复元素，可以进行集合运算
nums={1,2,2,3}
nums.add(4)
print(nums)
nums.remove(2)
print(nums)
