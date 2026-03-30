# 练习1：写入文件（w模式，清空原有内容）
with open(".vscode\\day7\\note.txt", "w", encoding="utf-8") as f:
    f.write("2026-03-23 学习文件读写\n")
    f.write("核心：open()、write()、close()\n")
print("写入完成！")
# 练习2：读取文件（r模式，读取全部内容）
with open(".vscode\\day7\\note.txt", "r", encoding="utf-8") as f:
    all_content = f.read()
print("文件全部内容：")
print(all_content)
# 练习3：追加内容（a模式，不清空原有内容）
with open(".vscode\\day7\\note.txt", "a", encoding="utf-8") as f:
    f.write("追加：推荐用with语句自动关文件\n")
print("追加完成！")
# 练习4：读取文件的每一行（readlines()）
with open(".vscode\\day7\\note.txt", "r", encoding="utf-8") as f:
    lines = f.readlines()  # 返回列表，每个元素是一行内容
print("按行读取内容：")
for line in lines:
    print(line.strip())  # strip()去掉换行符