import math
import os

HISTORY_FILE = "calc_history.txt"

# ---------- 数学运算函数（5个以上） ----------
def add(a, b):
    """加法"""
    return a + b

def subtract(a, b):
    """减法"""
    return a - b

def multiply(a, b):
    """乘法"""
    return a * b

def divide(a, b):
    """除法"""
    if b == 0:
        raise ValueError("除数不能为零")
    return a / b

def power(a, b):
    """幂运算 (a^b)"""
    return a ** b

def sqrt(a):
    """开平方根（单目运算）"""
    if a < 0:
        raise ValueError("不能对负数开平方根")
    return math.sqrt(a)

# ---------- 历史记录管理函数 ----------
def save_history(expression, result):
    """将一条计算记录追加到历史文件"""
    with open(HISTORY_FILE, "a", encoding="utf-8") as f:
        f.write(f"{expression} = {result}\n")

def load_history():
    """读取并显示全部历史记录"""
    if not os.path.exists(HISTORY_FILE):
        print("暂无历史记录。")
        return
    with open(HISTORY_FILE, "r", encoding="utf-8") as f:
        lines = f.readlines()
    if not lines:
        print("暂无历史记录。")
    else:
        print("-------- 计算历史记录 --------")
        for line in lines:
            print(line.strip())
        print("-----------------------------")

def clear_history():
    """清空历史记录文件"""
    if os.path.exists(HISTORY_FILE):
        os.remove(HISTORY_FILE)
        print("历史记录已清空。")
    else:
        print("暂无历史记录可清空。")

# ---------- 输入获取与菜单 ----------
def get_two_numbers():
    """获取两个数字，带异常处理"""
    while True:
        try:
            a = float(input("请输入第一个数: "))
            b = float(input("请输入第二个数: "))
            return a, b
        except ValueError:
            print("输入无效，请输入数字。")

def get_one_number():
    """获取一个数字（用于单目运算），带异常处理"""
    while True:
        try:
            a = float(input("请输入一个数: "))
            return a
        except ValueError:
            print("输入无效，请输入数字。")

def show_menu():
    """显示菜单"""
    print("\n===== 数学计算器 =====")
    print("1. 加法 (+)")
    print("2. 减法 (-)")
    print("3. 乘法 (*)")
    print("4. 除法 (/)")
    print("5. 幂运算 (x^y)")
    print("6. 开平方根 (√x)")
    print("7. 查看历史记录")
    print("8. 清空历史记录")
    print("9. 退出")
    print("======================")

def main():
    while True:
        show_menu()
        choice = input("请选择操作 (1-9): ").strip()

        if choice == '1':
            a, b = get_two_numbers()
            result = add(a, b)
            expr = f"{a} + {b}"
            print(f"结果: {expr} = {result}")
            save_history(expr, result)

        elif choice == '2':
            a, b = get_two_numbers()
            result = subtract(a, b)
            expr = f"{a} - {b}"
            print(f"结果: {expr} = {result}")
            save_history(expr, result)

        elif choice == '3':
            a, b = get_two_numbers()
            result = multiply(a, b)
            expr = f"{a} * {b}"
            print(f"结果: {expr} = {result}")
            save_history(expr, result)

        elif choice == '4':
            a, b = get_two_numbers()
            try:
                result = divide(a, b)
                expr = f"{a} / {b}"
                print(f"结果: {expr} = {result}")
                save_history(expr, result)
            except ValueError as e:
                print(f"错误: {e}")

        elif choice == '5':
            a, b = get_two_numbers()
            result = power(a, b)
            expr = f"{a} ^ {b}"
            print(f"结果: {expr} = {result}")
            save_history(expr, result)

        elif choice == '6':
            a = get_one_number()
            try:
                result = sqrt(a)
                expr = f"√{a}"
                print(f"结果: {expr} = {result}")
                save_history(expr, result)
            except ValueError as e:
                print(f"错误: {e}")

        elif choice == '7':
            load_history()

        elif choice == '8':
            confirm = input("确认清空所有历史记录？(y/n): ").lower()
            if confirm == 'y':
                clear_history()

        elif choice == '9':
            print("感谢使用数学计算器，再见！")
            break

        else:
            print("无效选择，请输入1-9之间的数字。")

if __name__ == "__main__":
    main()