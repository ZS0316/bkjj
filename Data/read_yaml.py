import yaml

# 读取文件

with open("./value2.yaml", "r", encoding="utf-8") as f:
    data = yaml.safe_load(f)

    # 打印数据
    print("data{}:".format(data))

    # 打印类型
    print("类型{}".format(type(data.get("value2"))))
