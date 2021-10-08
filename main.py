import httpx
import re

url = "http://acm.hdu.edu.cn/webcontest/contest_login.php?cid=14214"

temple = '''
## {}

Problem Description

```
{}
```

Input

```
{}
```

Output

```
{}
```

Sample Input

```
{}
```

Sample Output

```
{}
```

### MyResult

```c
//

```


'''

client = httpx.Client()

# 获取一个PHPSESSION
client.get(url=url)

# 登录
data = {"password": "woaibiancheng"}
res = client.post(url=url + "&action=login", data=data)
if len(res.history) == 1:
    print("登陆成功")
else:
    exit("登陆失败")

questionList = re.compile("<a href=\"(.*)\">(.*)</a></td>").findall(res.text)
if len(questionList) != 0:
    print("获取列表成功")
else:
    exit("获取试卷列表失败")

i = 1001
out = ""

for item in questionList:
    res = client.get(url="http://acm.hdu.edu.cn/webcontest/" + item[0])
    detail = re.compile(
        "<div class=panel_content>(.*?)</div>.*?<div class=panel_content>(.*?)</div>.*?<div class=panel_content>(.*?)</div>.*?<div style=\"font-family:Courier New,Courier,monospace;\">([\s\S]*?)</div>.*?<div style=\"font-family:Courier New,Courier,monospace;\">([\s\S]*?)</div>").findall(
        res.text)
    # print(detail)
    if len(detail) == 1 and len(detail[0]) == 5:
        print(f"获取 {i} 成功")
    else:
        exit("获取试卷失败")

    out += temple.format(i, detail[0][0], detail[0][1],
                         detail[0][2], detail[0][3],
                         detail[0][4])
    i += 1
out = out.replace("&lt;", "<").replace("&gt;", ">").replace("<br>", "\n").replace(
    "<div style='font-family:Times New Roman;font-size:14px;background-color:F4FBFF;border:#B7CBFF 1px dashed;padding:6px'><div style='font-family:Arial;font-weight:bold;color:#7CA9ED;border-bottom:#B7CBFF 1px dashed'><i>Hint</i></div>",
    "# Hint")
# print(out)
open("questions.md", "w", encoding="UTF-8").write(out)
