"""一个简易的四则运算计算器 demo。"""


def add(a, b):
    return a + b


def sub(a, b):
    return a - b


def mul(a, b):
    return a * b


def div(a, b):
    if b == 0:
        raise ValueError("除数不能为 0")
    return a / b


def mod(a, b):
    if b == 0:
        raise ValueError("除数不能为 0")
    return a % b


OPERATIONS = {
    "1": ("+ 加法", add),
    "2": ("- 减法", sub),
    "3": ("* 乘法", mul),
    "4": ("/ 除法", div),
    "5": ("% 取模", mod),
}


def main():
    print("===== 简易计算器 =====")
    for key, (label, _) in OPERATIONS.items():
        print(f"{key}. {label}")
    choice = input("请选择运算 (1/2/3/4/5): ").strip()
    if choice not in OPERATIONS:
        print("无效选项")
        return
    a = float(input("请输入第一个数: "))
    b = float(input("请输入第二个数: "))
    label, func = OPERATIONS[choice]
    print(f"结果: {a} {label.split()[0]} {b} = {func(a, b)}")


if __name__ == "__main__":
    main()
