import os

boss = input("Directory for the image: ")
name = os.path.basename(boss)
wallpaper_bytes = str(open(boss, "rb").read())

final = open("Troll.py", "w")
final.write(f"import ctypes, pathlib\n\n"
            f"image = {wallpaper_bytes}\n\n"
            f'file = open("{name}", "wb")\n\n'
            f'file.write(image)\n\n'
            f'location = pathlib.Path().resolve()\n\n'
            f'ctypes.windll.user32.SystemParametersInfoW(20, 0, rf"{{location}}/{name}", 0)\n')
