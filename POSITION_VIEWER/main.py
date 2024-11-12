import tkinter as tk
from tkinter import messagebox
import subprocess
import os
import i2_poslog
import i3_poslog

def run_i2_poslog():
    try:
        # i2_poslog.py 실행
        script_path = os.path.join(os.getcwd(), "i2_poslog.py")
        subprocess.run(['python', script_path], check=True)
        messagebox.showinfo("실행 완료", "i2_poslog.py가 성공적으로 실행되었습니다.")
    except Exception as e:
        messagebox.showerror("실행 오류", f"i2_poslog.py 실행 중 오류 발생: {e}")

def run_i3_poslog():
    try:
        # i3_poslog.py 실행
        script_path = os.path.join(os.getcwd(), "i3_poslog.py")
        subprocess.run(['python', script_path], check=True)
        messagebox.showinfo("실행 완료", "i3_poslog.py가 성공적으로 실행되었습니다.")
    except Exception as e:
        messagebox.showerror("실행 오류", f"i3_poslog.py 실행 중 오류 발생: {e}")

# 메인 GUI 창 생성
root = tk.Tk()
root.title("GNSS 데이터 처리 프로그램")

# 창 크기 설정
root.geometry("300x150")

# i2_poslog.py 실행 버튼
i2_button = tk.Button(root, text="i2_poslog 실행", width=20, height=2, command=run_i2_poslog)
i2_button.pack(pady=10)

# i3_poslog.py 실행 버튼
i3_button = tk.Button(root, text="i3_poslog 실행", width=20, height=2, command=run_i3_poslog)
i3_button.pack(pady=10)

# GUI 창 실행
root.mainloop()
