f = open(".vscode\\day7\\text.txt", "w",encoding="utf-8")
f.write("我是豆包，今天学习了文件读写！")
f.close()
f = open(".vscode\\day7\\text.txt", "r",encoding="utf-8")
content = f.read()
f.close()
print("文件内容：", content) 
# 写入文件（with版）
#with open("test.txt", "w", encoding="utf-8") as f:
   # f.write("用with语句更安全！")
# 读取文件（with版）
#with open("test.txt", "r", encoding="utf-8") as f:
    #content = f.read()
    #print(content)