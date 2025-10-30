import tkinter as tk
from PIL import Image, ImageTk
import random
import os

# === 可调参数 ===
IMAGE_FOLDER = "./images"   # 图片目录
SIZE_RANGE = (150, 400)     # 随机窗口大小范围 (最小, 最大)
SHOW_COUNT = 80             # 总窗口数量
SHOW_DELAY = 150            # 每个窗口之间的间隔（毫秒）
AUTO_CLOSE_MS = 3000        # 自动关闭时间（毫秒）
FADE_STEPS = 10             # 淡入动画帧数
FADE_INTERVAL = 50          # 每帧间隔（毫秒）

def show_random_image():
    try:
        # 获取随机图片
        images = [f for f in os.listdir(IMAGE_FOLDER)
                  if f.lower().endswith(('.png', '.jpg', '.jpeg', '.gif', '.bmp', '.webp'))]
        if not images:
            print("⚠️ 请在 ./images 文件夹中放入图片")
            return
        selected = random.choice(images)
        path = os.path.join(IMAGE_FOLDER, selected)

        # 随机窗口大小
        size = random.randint(*SIZE_RANGE)
        img = Image.open(path)
        img = img.resize((size, size), Image.Resampling.LANCZOS)
        photo = ImageTk.PhotoImage(img)

        # 创建无边框窗口
        window = tk.Toplevel()
        window.overrideredirect(True)  # 无标题栏
        sw, sh = window.winfo_screenwidth(), window.winfo_screenheight()
        x = random.randint(0, sw - size)
        y = random.randint(0, sh - size)
        window.geometry(f"{size}x{size}+{x}+{y}")

        # 显示图片
        label = tk.Label(window, image=photo, borderwidth=0, highlightthickness=0)
        label.image = photo
        label.pack(fill="both", expand=True)

        # 淡入动画
        def fade_in(step=0):
            if step <= FADE_STEPS:
                alpha = step / FADE_STEPS
                window.attributes('-alpha', alpha)
                window.after(FADE_INTERVAL, fade_in, step + 1)
            else:
                window.attributes('-alpha', 1.0)

        window.attributes('-topmost', True)
        window.attributes('-alpha', 0.0)
        fade_in()

        # 自动关闭
        window.after(AUTO_CLOSE_MS, window.destroy)
    except Exception as e:
        print("❌ 出错：", e)

def start_show(root):
    for i in range(SHOW_COUNT):
        root.after(i * SHOW_DELAY, show_random_image)

# === 主程序 ===
root = tk.Tk()
root.withdraw()  # 隐藏主窗口
start_show(root)
root.mainloop()