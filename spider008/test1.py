import re

# 测试文本
test = '<h1>hello 你好, world 世界</h1>'

# 中文匹配正则
chinese_pattern = '[\u4e00-\u9fa5]+'
says = re.findall(chinese_pattern, test)

hi = ''
for say in says:
    # print(say)
    hi += say + ','
hi = hi.strip(',')

# 打印结果：你好,世界
print(hi)
