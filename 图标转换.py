import tkinter as tk
from tkinter import filedialog
from PIL import Image

def convert_png_to_ico():
    # 打开文件选择框让用户选择PNG文件
    file_path = filedialog.askopenfilename(title="选择PNG图片", filetypes=[("PNG files", "*.png")])
    if not file_path:
        return

    # 打开PNG文件
    img = Image.open(file_path)

    # 让用户选择保存路径
    save_path = filedialog.asksaveasfilename(defaultextension=".ico", filetypes=[("Icon files", "*.ico")])
    if not save_path:
        return

    # 将图片保存为ICO格式
    img.save(save_path, format="ICO")
    print(f"图片已保存为 {save_path}")

# 创建Tkinter窗口
root = tk.Tk()
root.title("PNG转ICO图标")
root.geometry("300x150")

# 创建转换按钮
convert_button = tk.Button(root, text="转换PNG为ICO", command=convert_png_to_ico)
convert_button.pack(expand=True)

# 运行Tkinter主循环
root.mainloop()
