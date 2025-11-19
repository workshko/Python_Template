sum_value_one_to_ten = 0
for i in range(1, 11):
    sum_value_one_to_ten += i

print("1부터 10까지의 합:", sum_value_one_to_ten)
import tkinter as tk
from tkinter import messagebox

# 콘솔 출력 예제는 주석 처리
# print("출력완료")
# sum_value_one_to_ten = 0
# for i in range(1, 11):
#     sum_value_one_to_ten += i
# print("1부터 10까지의 합:", sum_value_one_to_ten)


def add(a, b):
    return a + b

def subtract(a, b):
    return a - b

def multiply(a, b):
    return a * b

def divide(a, b):
    if b == 0:
        raise ValueError("0으로 나눌 수 없습니다.")
    return a / b

def calculate():
    try:
        a = float(entry_a.get())
        b = float(entry_b.get())
        op = operator.get()
        if op == "더하기":
            result = add(a, b)
        elif op == "빼기":
            result = subtract(a, b)
        elif op == "곱하기":
            result = multiply(a, b)
        elif op == "나누기":
            result = divide(a, b)
        else:
            result = "잘못된 연산자입니다."
        label_result.config(text=f"결과: {result}")
    except ValueError as e:
        messagebox.showerror("오류", str(e))
    except Exception:
        messagebox.showerror("오류", "숫자를 올바르게 입력하세요.")

root = tk.Tk()
root.title("파이썬 계산기")

tk.Label(root, text="첫 번째 숫자:").grid(row=0, column=0)
entry_a = tk.Entry(root)
entry_a.grid(row=0, column=1)

tk.Label(root, text="두 번째 숫자:").grid(row=1, column=0)
entry_b = tk.Entry(root)
entry_b.grid(row=1, column=1)

operator = tk.StringVar(value="더하기")
tk.OptionMenu(root, operator, "더하기", "빼기", "곱하기", "나누기").grid(row=2, column=0, columnspan=2)

tk.Button(root, text="계산", command=calculate).grid(row=3, column=0, columnspan=2)

label_result = tk.Label(root, text="결과: ")
label_result.grid(row=4, column=0, columnspan=2)

root.mainloop()

