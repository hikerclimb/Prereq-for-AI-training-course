import ctypes
import locale
import platform
import psutil
import shutil

# Get the general OS name (e.g., 'Windows', 'Linux', 'Darwin' for macOS)
os_name = platform.system()

# Get the OS release version
os_version = platform.release()

print(os_name)
print(os_version)

memory = psutil.virtual_memory()

print(memory.total / (1024 ** 3))

path = '/'
total, used, free = shutil.disk_usage(path)
print(f"Free:  {free / (2**30):.2f} GiB")

lang_id = ctypes.windll.kernel32.GetSystemDefaultUILanguage()
print(locale.windows_locale.get(lang_id))