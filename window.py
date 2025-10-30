import tkinter as tk
import random

tips = [
    "多喝水哦~",
    "保持微笑呀",
    "每天都要元气满满",
    "记得吃水果",
    "保持好心情",
    "好好爱自己",
    "我想你了",
    "梦想成真期待下一次见面",
    "聊游戏把把五杀",
    "身体健康顺顺利利",
    "早点休息",
    "愿所有烦恼都消失",
    "别熬夜",
    "今天过得开心嘛",
    "天冷了，多穿衣服",
    "麻将把把胡",
]

bg_colors = [
    "lightpink", "skyblue", "lightgreen", "lavender", "lightyellow", "plum",
    "coral", "bisque", "aquamarine", "mistyrose", "honeydew", "lavenderblush", "oldlace",
]


def show_warm_tip():
    window = tk.Toplevel()  # 注意这里改成 Toplevel，而不是 Tk()
    screen_width = window.winfo_screenwidth()
    screen_height = window.winfo_screenheight()
    window_width = 280
    window_height = 100
    x = random.randint(0, screen_width - window_width)
    y = random.randint(0, screen_height - window_height)
    window.title("温馨提示")
    window.geometry(f"{window_width}x{window_height}+{x}+{y}")
    tip = random.choice(tips)
    bg = random.choice(bg_colors)
    tk.Label(window, text=tip, font=("Arial", 12), bg=bg, width=30, height=5).pack()
    window.attributes('-topmost', True)
    window.after(10000, window.destroy)  # 自动关闭窗口（3秒后）


def start_tips(root, total=500, delay=100):
    """主线程中定时弹窗"""
    for i in range(total):
        root.after(i * delay, show_warm_tip)


root = tk.Tk()
root.withdraw()  # 隐藏主窗口
start_tips(root, total=500, delay=100)  # 每 100ms 弹出一个窗口
root.mainloop()
