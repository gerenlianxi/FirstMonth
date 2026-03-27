user_info = {
    "user-id":"1001",
    "username":"豆包用户",
    "history":["你好","Python怎么学","字典怎么用"],
    "is_vip":False
}
user_info["history"].append("列表和字典的区别")
user_info["is_vip"] = True
print("用户ID:", user_info["user-id"])
print("用户名:", user_info["username"])
print("历史记录:", user_info["history"])
print("是否为VIP:", user_info["is_vip"])