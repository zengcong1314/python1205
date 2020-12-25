#__file__表示文件名（路径）
print(__file__)

#打开
# open("",)
# with open("cases.txt") as f:
#     f.read()

# 路径操作 os.path
import  os
# os.path.realpath() 绝对路径
# os.path.abspath(__file__)：获取当前文件的绝对路径
print(os.path.abspath(__file__))


# os.path.dirname 获取父级目录
cwd = os.path.abspath(__file__)
cwd_dir = os.path.dirname(cwd)
print(cwd_dir)

# 通过现在的文件路径 获取 py36 的路径，dirname的dirname
print(os.path.dirname(cwd_dir))
print(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

# 获取 cases.txt
# 1、自己的路径
# 2、父目录的路径
# 3、父目录 + data\cases.txt

cwd = os.path.abspath(__file__)
cwd_dir2 = os.path.dirname(cwd)
# 拼接
# 到了Linux下运行不了
file = os.path.join(cwd_dir2,'data\cases.txt')
file1 = os.path.join(cwd_dir2,'data','cases.txt')
print(file1)

# 创建目录
cwd_dir3 = os.path.dirname(cwd)

#创建一个 config 目录
#os.mkdir("config")

py36 = os.path.dirname(cwd_dir3)
config_path = os.path.join(py36,"config")
if not os.path.exists(config_path):
    os.mkdir(config_path)

#os.rmdir（路径名字）：删除一个目录
# os.listdir():获取当前路径下的目录列表
# os.path.isdir:判断当前文件是否是目录，返回布尔值
# os.path.isfile:判断当前文件是否是文件，返回布尔值
# os.path.exists()
# os.getcwd():getcwd()方法显示当前的工作路径，只具体到路径，不具体到文件，实际过程中用得很少

#isdir,isfile
print(os.path.isfile(config_path))
print(os.path.isdir(config_path))

# cnblogs.wagyuze/p/11578139.html

