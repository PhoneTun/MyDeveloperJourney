import random
from classes.ninja import Ninja
from classes.pirate import Pirate

michelangelo = Ninja("Michelanglo")

jack_sparrow = Pirate("Jack Sparrow")

Gameon=True
def  dice():
    roll_pirate=random.randint(0,10)
    roll_ninja = random.randint(0,10)
    return roll_ninja, roll_pirate

# print(dice())
# print(dice())
counter = 0

print("XXXXXXXXXXXXXXXXXXXXXXXXXXGame StartXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX")
print('''⠀⠀⡶⠛⠲⣄⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢠⡶⠚⢶⡀⠀
⢰⠛⠃⠀⢠⣏⠀⠀⠀⠀⣀⣠⣤⣤⣤⣤⣤⣤⣄⣀⡀⠀⠀⠀⣸⠇⠀⠈⠙⣧
⠸⣦⣤⣄⠀⠙⢷⣤⣶⠟⠛⢉⣁⣤⣤⣤⣤⣀⣉⠙⠻⢷⣤⡾⠋⢀⣤⣤⣴⠏
⠀⠀⠀⠈⠳⣤⡾⠋⣀⣴⣿⣿⠿⠿⠟⠛⠿⠿⣿⣿⣶⣄⠙⢿⣦⠟⠁⠀⠀⠀
⠀⠀⠀⢀⣾⠟⢀⣾⣿⠟⠋⠀⠀⠀⠀⠀⠀⠀⠀⠉⠻⣿⣷⡄⠹⣷⡀⠀⠀⠀
⠀⠀⠀⣾⡏⢠⣿⣿⡯⠤⠤⠤⠒⠒⠒⠒⠒⠒⠒⠤⠤⠽⣿⣿⡆⠹⣷⡀⠀⠀
⠀⠀⢸⣟⣠⡿⠿⠟⠒⣒⣒⣉⣉⣉⣉⣉⣉⣉⣉⣉⣒⣒⡛⠻⠿⢤⣹⣇⠀⠀
⠀⠀⣾⡭⢤⣤⣠⡞⠉⠁⢀⣀⣀⠀⠀⠀⠀⢀⣀⣀⠀⠈⢹⣦⣤⡤⠴⣿⠀⠀
⠀⠀⣿⡇⢸⣿⣿⣇⠀⣼⣿⣿⣿⣷⠀⠀⣼⣿⣿⣿⣷⠀⢸⣿⣿⡇⠀⣿⠀⠀
⠀⠀⢻⡇⠸⣿⣿⣿⡄⢿⣿⣿⣿⡿⠀⠀⢿⣿⣿⣿⡿⢀⣿⣿⣿⡇⢸⣿⠀⠀
⠀⠀⠸⣿⡀⢿⣿⣿⣿⣆⠉⠛⠋⠀⢴⣶⠀⠉⠛⠉⣠⣿⣿⣿⡿⠀⣾⠇⠀⠀
⠀⠀⠀⢻⣷⡈⢻⣿⣿⣿⣿⣶⣤⣀⣈⣁⣀⡤⣴⣿⣿⣿⣿⡿⠁⣼⠏⠀⠀⠀
⠀⠀⠀⢀⣽⣷⣄⠙⢿⣿⣿⡟⢲⠧⡦⠼⠤⢷⢺⣿⣿⡿⠋⣠⣾⢿⣄⠀⠀⠀
⣰⠟⠛⠛⠁⣨⡿⢷⣤⣈⠙⢿⡙⠒⠓⠒⠒⠚⡹⠛⢁⣤⣾⠿⣧⡀⠙⠋⠙⣆
⠹⣤⡀⠀⠐⡏⠀⠀⠉⠛⠿⣶⣿⣶⣤⣤⣤⣾⣷⠾⠟⠋⠀⠀⢸⡇⠀⢠⣤⠟
⠀⠀⠳⢤⠾⠃⠀⠀⠀⠀⠀⠀⠈⠉⠉⠉⠉⠁⠀⠀⠀⠀⠀⠀⠘⠷⠤⠾⠁''')
while Gameon:
    counter += 1
    print(f"'XXXXXXXXXXX ROUND {counter} XXXXXXXXXXXXXXXXX")
    if counter == 5:
        print(f"Weapon dropped!!!!!!!!!!!!!!!!!!!!!!")
        print('''⢿⡙⢯⡙⢧⡙⡔⢂⠆⡆⠆⠦⡰⢄⠲⡄⠦⡰⠄⢦⠰⢄⠢⢔⡠⢆⠰⡰⠠⢆⠰⢄⠰⢠⢂⠔⢠⢂⠔⡠⢂⠔⡠⢄⠢⢄⠢⢄⠢⢄⠢⢄⠢⢄⠢⢄⠢⢄⠢⢄⠢⢄⠢⠄⠢⠄⡂⠆⡄⠢⠄⠢⢄⠢⠄⠤⡀⠆⠤⡐⠤⡀⠤⠀⠤⠀⠤⠀⠄⠠⠠⠐⠠⠐⡠⠐⠠⡐⠠⢂⠰⢀⠂⠰⢀⢆⠰⢀⠆⠰⡀⠆⠰⢀⣢⣽⣿⣿⣆⢒
    ⢷⡙⢦⡙⢆⡱⠌⡑⠎⢌⡉⠆⡑⠊⠥⡈⠅⡂⠍⡂⠅⡊⡁⠂⡔⡈⢡⠂⡅⢊⠰⢈⠡⢁⠊⡘⠄⢊⠰⠡⠌⠢⠑⢈⠰⢈⠐⣈⠐⣈⠐⣈⠐⣈⠐⣈⠐⡈⢐⠈⠔⡈⠄⡉⠂⠅⡘⠐⠌⡁⠎⢁⠊⠤⠉⢂⡁⢊⠁⡄⠡⡐⠠⡈⠄⡈⠄⠡⠈⠤⠡⢌⠠⡁⢄⠡⢂⠤⣁⠢⡐⢌⠘⠔⡈⢄⠡⠂⢌⠡⢄⣵⣾⣿⣿⣿⡿⢛⠙⡛
    ⣳⡙⢦⡙⡎⢖⡱⢘⢍⠲⣈⠣⡙⠜⢢⠑⡪⢐⠣⠜⠢⡑⠬⡑⠰⡘⠤⠓⡌⢂⠃⠎⡒⡉⠆⡱⠊⡅⠎⡑⠢⠅⠣⡘⢐⢂⠱⡀⢎⠐⢂⠔⢢⠐⢂⠔⢂⠑⢢⢉⠒⢄⠣⢌⠱⢘⠰⢉⠒⢡⠊⢄⢃⠢⣉⠂⠒⡡⠂⡄⡁⠠⡁⠐⠈⠠⠈⠄⠑⡀⢂⠄⢂⢁⢂⠐⣀⠂⢄⢂⠐⣈⠐⡈⠐⡀⢆⣥⣶⣿⣿⣿⣿⠿⢛⠩⡐⡡⢊⡐
    ⣥⡙⢆⡱⢌⡌⠆⣍⢨⡐⡡⢌⢡⠊⡡⡘⢄⡉⡰⢈⡡⢈⡐⣈⡐⡈⠤⡁⠌⡈⢌⠠⡁⢌⠠⣁⠡⡈⢄⠡⠡⢌⠁⠤⢁⢂⠡⡐⢀⢁⠂⢄⡁⢄⠡⢀⠡⠘⢄⠠⢁⢂⢁⠠⢡⠈⡄⠡⠌⡄⠌⠤⠈⡄⠄⣈⠡⡀⠡⡈⡈⢂⠠⠈⠀⢵⣧⡐⠠⢐⡀⠈⠄⠂⣀⡂⠄⡉⠐⡐⠂⠄⠂⣄⣵⣾⣿⣿⡿⠻⣉⠱⡀⢎⡄⢣⠑⣂⢅⠂
    ⣵⣉⠞⡰⢃⠜⡡⢒⢆⡐⡡⢒⢂⡑⡐⡐⢢⠒⡐⡂⢐⢊⡐⢠⠐⣈⢂⡐⢘⠐⡂⠒⡐⢠⠒⣀⠒⡐⢠⢂⠑⢂⠘⡐⣈⠐⡐⡐⣈⠐⣈⢂⠐⡈⠔⡁⢂⢂⠐⡐⠂⡌⠄⢒⡀⠆⡐⡁⢒⡀⠆⢂⠡⢂⢈⡀⠂⠄⢃⡐⠀⠂⢀⠀⢹⢾⣿⣿⣾⣿⣿⣷⣤⣤⣼⣿⣷⡧⠆⣀⣥⣶⣿⣿⡿⢟⠋⠥⡐⡑⢂⢂⠕⢂⡐⢂⢒⡀⠢⢁
    ⢳⡜⢬⢑⡃⢎⡑⢆⡒⣐⠡⢆⠒⡠⡑⡐⢂⢂⠑⣈⠂⡂⡘⠀⠎⡐⣀⠂⡂⠒⡠⢃⡐⢂⠒⣀⠒⡈⢄⠢⢘⠠⢘⠠⡐⢂⡐⠐⡀⢂⠄⣂⠐⡐⢠⠐⢁⠂⡁⢄⡁⠐⢂⠂⡄⠂⡔⡀⢂⠰⠈⡂⢂⠂⠂⡀⠊⠠⠀⠀⡐⠀⠀⠂⠀⠈⣹⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣷⣿⣿⣿⠿⠛⡡⠘⢠⠉⢂⠔⢠⢁⠌⣐⢂⠐⣂⠄⡰⢁⠂
    ⣏⡜⢢⠕⡌⢢⡘⢆⡒⣐⠊⡔⢂⡱⢀⠆⡑⣈⠂⡄⢊⡐⢂⡑⠐⡐⢠⠘⢠⠑⣀⢂⠘⡠⢈⠄⢒⢈⠰⢐⠂⡘⠠⢄⠐⡄⠐⠑⢠⠈⣐⠀⡒⡀⠂⡌⢂⠂⡁⢂⡀⠃⢢⡐⢠⠡⡐⢈⠂⢄⠒⡈⠤⡈⠐⠠⢡⠀⢀⠁⠀⠀⢠⣤⣶⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡿⢋⠔⡈⠡⡐⠑⢂⠑⣈⠐⡁⢂⢐⠀⢂⡐⣀⠂⠔⡂⠌
    ⢵⡊⠵⣨⢑⢢⡘⢆⠒⡄⠣⠔⡢⢐⠂⢆⠱⢀⢒⡐⢂⡐⠢⠐⢡⠐⡀⠊⠤⡐⠠⢊⠐⡐⢂⠒⣀⠊⡐⠠⠒⣀⠐⡄⠂⡄⢉⠂⢄⠱⡐⢠⠄⠐⠐⢠⠢⠐⡈⠄⢡⠂⠰⠰⢀⠂⡅⠂⠰⡀⠣⢀⠐⡀⠉⠀⢀⠀⣀⣤⣼⣾⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⠟⡑⢈⠰⢀⠣⠐⣉⠠⠈⠄⢂⠰⣀⠂⡘⢄⡐⢠⠘⡐⡐⡈
    ⢧⡙⢦⠑⡎⠔⣈⢆⡃⠲⣁⠆⡑⢢⠑⡂⢂⢃⡐⢀⠆⠰⡁⡈⠄⠒⢠⢁⠒⡠⢁⢂⠘⣀⠢⢐⠠⠒⣈⠰⢁⠠⢂⠐⡐⢀⠂⠒⡀⠐⢀⠠⡐⠈⢀⠂⠐⡐⡀⢂⠐⢂⠡⠐⡀⠒⠐⠨⠄⡄⠐⡀⠀⠄⢀⣠⣴⣾⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡿⠿⠋⠅⢂⠐⡀⠒⡠⢂⠁⠠⢀⠑⡈⢄⡐⢀⠒⣀⠂⡐⢂⡑⡐⢄⠂
    ⢷⡉⢆⠏⡔⢃⡌⠆⡔⢣⠐⡌⣐⢂⡑⢄⠃⡂⢌⠐⣈⠐⡐⡐⢈⠒⣀⢂⠰⠐⢂⢂⠨⡐⠰⢈⠰⢈⠠⠒⣈⠐⢂⡐⠐⠂⠌⠒⣀⠡⠀⠆⡐⢈⠨⠈⠡⠐⠤⠨⡀⠌⡀⠃⠄⠈⠒⠀⠅⠀⠁⣀⣤⣾⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⠿⠟⢉⠁⢂⠡⡈⠤⠈⢌⠐⠠⡐⣈⠐⢂⠰⢀⢂⡐⣁⢂⠠⡑⡐⢂⠔⡐⠂⠌
    ⡳⡜⡌⢎⡑⠆⡬⢑⡐⢂⡑⡐⢄⠂⡔⣈⠐⡐⡠⢘⠀⡒⢀⠐⠢⡐⡀⢂⠒⣈⠂⢂⢂⡘⠐⠨⠐⢂⡐⢂⠠⢊⠠⠐⡈⡀⠃⠔⡀⠄⠒⢀⢀⠂⠐⠂⣁⡀⣀⠤⠤⠀⠄⠠⢀⠉⠀⣀⣰⣼⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡿⠟⠋⠁⠄⠂⠤⢈⠂⠒⢈⠘⠨⢀⡈⢐⡀⠠⢊⠐⡂⠄⢂⠐⣀⢂⠒⣀⠒⡀⠒⣀⠃⢂
    ⡳⢅⡚⢤⢋⡐⢆⢃⡔⡁⢒⡐⠂⢅⠂⠄⢃⡐⢠⠈⠰⠀⠌⠒⢠⠐⢠⠂⢢⠠⠘⢠⠂⡐⢂⠡⢊⠠⠐⣈⠰⠀⠒⠠⠐⡀⡁⠂⢠⠐⠐⠂⣀⠔⠒⠉⠀⢀⠠⠀⠀⣤⣶⣄⣠⣴⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⠿⠋⠁⠄⠂⡈⠐⠈⠂⠌⠂⠘⠈⠰⢈⠐⡀⡐⠠⡐⢁⢂⡐⠄⠑⡂⢌⠀⢂⠡⠐⡐⣀⠃⠄⡌⠀
    ⣛⢆⡩⢂⠖⡈⠆⡆⠰⠄⢃⠄⡉⠄⡘⢄⠢⠐⣀⠊⠄⢡⠈⠌⠠⡈⠄⠒⠠⢀⠃⠄⠒⡀⠢⠈⠤⢈⠂⢀⠂⡈⡐⡈⡐⠠⠐⠈⢀⡠⠖⠊⠀⣄⠀⢂⠡⠀⠀⢄⣠⣿⣾⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⠿⠛⢉⠀⠄⠂⠡⠠⠁⡈⠡⠉⠈⡐⢈⠈⢁⠰⢀⠒⢠⠈⡐⢠⠊⠠⠐⡈⢂⠐⡀⢃⢀⠃⠒⢄⠠⠑⠂⡄⠃
    ⣚⠦⣑⠪⠜⡁⢎⡰⠁⠎⡐⠌⡐⠁⠆⠄⢊⠁⡐⠠⠌⠠⠈⠤⠑⠠⠈⠌⡐⠠⠈⡄⢃⠐⠠⢁⠐⠠⠈⠤⠐⠀⠄⠠⠀⢂⠈⣠⠞⢀⠰⠈⡐⠠⠘⠀⣀⣴⣾⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡟⠋⠁⡐⢈⠀⡐⠈⠠⠁⠂⢁⠠⠐⠈⡐⢀⠀⢌⠠⠘⢠⠈⠤⢈⠰⢀⢈⠢⠑⠠⢈⢂⠰⠀⠢⢈⠐⡀⠃⢌⠐⠄⠂
    ⣋⠖⣡⠚⡰⡈⠆⠤⢉⠒⡄⠂⠅⡃⠔⠨⠄⠡⠄⡁⠢⠡⠁⢂⠡⠂⠡⠂⠄⠡⢂⠐⠠⢈⠐⠠⠈⢀⠈⠀⢈⠨⠀⠂⠁⡀⠂⠀⢄⠂⠄⠁⣀⣵⣾⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡿⠋⡀⠌⠐⠠⠐⠀⡁⠄⠁⢈⠀⡀⠐⠠⠐⠠⢈⠤⠘⢈⠐⢨⠐⢠⠂⠨⢀⠢⢈⢁⠢⢀⠂⠍⢂⠁⠰⠈⠆⡈⠌⠠⠁
    ⡮⣓⠰⡘⠤⡑⠌⢢⠌⡐⠤⠁⠆⡁⠆⠡⢘⠀⠆⡁⠤⢁⠉⠄⠂⠡⠄⠡⠌⠐⠠⢈⠐⡀⢈⠀⠄⢀⣶⣇⢀⠀⠈⠐⠠⠁⢀⠉⣀⣤⣾⣿⣿⣿⣿⣻⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡿⠟⠋⢁⠠⠀⠐⣆⠀⠄⠁⠀⠄⡀⠌⠀⡐⠠⠁⠌⠌⡐⠤⠐⢨⠐⠈⢠⠘⠠⢈⠡⠂⠰⠈⠄⠢⠈⠄⡉⠠⢉⠀⠃⠌⡐⠌⡁⠂
    ⡺⣄⠳⣈⠂⡘⠄⢣⠐⠄⡂⢁⠒⠠⢁⠁⠆⠠⠁⠔⠠⠡⠌⠐⠌⠐⠂⠔⠈⠡⠁⠄⠂⢀⠄⡀⠂⠄⢻⣿⣿⣦⣧⡄⢁⣠⣴⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡿⠟⢁⠠⠐⠈⠠⢀⠡⠄⠘⣧⠀⠁⠄⠄⠄⠈⠁⠄⠡⠌⠄⠡⠐⠤⠘⠠⠌⢈⠠⢈⠔⠨⠐⠨⠐⠨⢈⠰⠈⠠⠁⠡⠈⠈⠌⠰⠈⠔⠠⠁
    ⡳⡜⣈⠢⠊⡔⡁⠆⠩⠄⠁⠆⡉⠄⢃⠌⠈⠤⠉⠄⠡⠡⠌⠤⠉⠐⠈⠄⠡⠁⠌⢀⠡⠀⡀⠄⡐⠈⠌⢻⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣧⡀⠀⠂⢀⠂⠁⠂⠄⠀⠀⠄⠸⡆⠀⢁⠄⠄⠁⠁⠌⠐⠈⠄⠡⠉⢄⠱⠐⠈⢠⠘⠠⠘⠤⠁⠢⠉⠐⠈⠠⠉⠰⠈⠁⠩⠌⠄⠡⡉⠌⡁⠄
    ⡳⡜⣠⠉⡖⠠⡁⠎⡡⠌⡁⠆⠡⠊⠄⠌⠡⠀⠅⠌⠡⠐⠄⠡⠀⠉⠤⠁⢂⠡⠈⠄⡀⠐⠀⡀⠀⣂⣤⣶⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣷⣦⣀⠠⠁⠂⠀⠤⠁⡀⠀⠥⠀⠁⠀⠐⠁⠁⠠⠁⠁⠌⠁⠌⠠⢐⠨⠈⢄⠨⠐⢉⠤⠉⠄⢉⠈⠡⠌⠨⠀⠣⠌⡐⠨⠄⠡⡐⠈⠄⠂
    ⣳⡑⢢⠚⡄⠣⠄⠣⠄⠃⠄⡊⠡⠉⡄⠉⠤⠁⠌⢈⠡⠁⠈⠁⠌⠡⠄⢁⠂⠄⠁⡐⠀⠁⠠⣸⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣶⣤⣄⣀⠀⠀⠉⠐⠀⠁⠈⠂⠁⠌⠀⠄⠁⠄⠡⠌⠐⠡⢐⠈⠤⠐⢉⠠⢠⠉⠈⠤⠈⠔⡈⠡⠌⡀⠌⠠⠁⠎⠠⠡⠉⠄⡁
    ⣶⠉⡆⠾⡈⢁⡈⢁⡈⢁⠎⡀⢁⠇⡀⠉⡀⢁⠸⢀⡀⠁⢁⠁⡈⠰⠈⢀⠰⠈⠰⠀⡀⠁⣸⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣶⣾⣆⣀⣁⣀⣀⡀⠰⠈⢀⠀⢁⠈⠰⢈⠀⢁⠰⡈⢀⠆⢁⠈⡰⢀⠉⡀⢀⢁⠀⣀⢁⠁⠉⢆⠁⡆⢉⠀⡀
    ⢥⢋⠔⡱⣐⠂⡔⣁⠒⡄⠒⡐⢂⡐⣀⢃⠐⠂⡄⠂⠐⠂⣀⠂⢀⠒⠈⡀⠐⢀⠂⠐⠠⠡⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⠿⢛⠋⢿⣿⣿⡏⢍⠻⢿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣧⠀⠐⡀⢈⠀⠂⠆⡐⢈⠢⢐⢈⠠⢊⢀⠒⣀⠂⠒⢐⢀⢂⢂⡀⢂⠐⣁⠐⢂⠐⣂⠐⡀
    ⡗⢎⠦⡑⢤⡑⡐⢂⠆⡐⡁⢆⠂⡐⣀⢂⠘⣀⠂⠂⡁⢂⠀⡈⠀⠄⠂⢀⠁⣠⠀⠁⣂⣴⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣏⣁⡆⠠⢈⣤⣿⢋⢿⣆⠐⡈⠙⠿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣷⠈⢀⠐⡀⠊⡐⡀⢂⠐⢂⠰⢈⠰⢀⢂⡐⢀⠒⡈⢄⢂⡐⠠⢐⢀⠒⣀⠘⣀⠂⡐⠂⠄
    ⣙⠦⢡⠑⣆⠐⡡⢆⠂⡅⡐⠄⡒⠐⣀⠂⡐⠠⢀⠁⠄⡀⠠⠐⠈⢀⠐⢀⣠⣾⣶⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣧⠒⡍⣋⣭⡾⠟⡉⠄⠈⠄⣁⠀⠠⠌⠐⡉⠙⠿⢿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡄⠂⢀⠐⠢⠐⡀⢂⡈⢢⠈⣂⠐⡂⢠⠐⢂⠐⡐⣀⢂⡐⢂⢂⠐⢂⡀⠂⢄⢂⡑⡈⠄
    ⡝⢆⢣⡑⢆⠒⡐⣂⠑⡐⢄⠡⠐⢂⠀⠂⠄⡁⠄⠂⠐⠄⢀⠁⢂⣠⣾⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⠾⡛⠍⡐⢀⠀⠄⠣⠄⠀⠢⠔⠒⠂⢄⡁⠌⡠⢉⠛⠿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡇⠀⡀⠌⡐⠨⠐⡀⢢⠐⣈⠠⠒⡈⠄⢂⠂⠑⡠⢀⠐⣀⢂⠐⢂⠔⡀⢃⠂⠆⡐⢀⠂
    ⡾⠒⢆⡜⢂⢂⠱⣀⠣⠐⢂⡀⢃⠄⡑⢈⠐⡀⠄⠁⡈⣀⣤⣶⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⠿⣿⣿⣿⣿⣿⣿⣿⣿⣟⠥⢂⠁⠆⢨⠀⠤⠡⠀⠄⠁⡀⠈⢁⠂⠄⡐⣀⠁⠄⡃⢆⡐⡈⠍⠛⡛⠿⠿⣿⣿⣿⣿⣿⣿⣿⣿⣿⠃⢀⠀⠡⠐⠨⠐⡀⢂⠰⢀⠒⡐⢈⠐⢂⠨⠐⠐⠂⢂⠄⣀⠊⢠⠐⡀⢃⢂⠐⡀⠆⠂
    ⢎⡙⠤⡘⣂⢐⡂⢆⠂⠅⢂⠐⠄⢂⠐⠀⠄⢀⣤⣷⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡿⠟⢋⠉⡁⠡⢀⠂⠄⠂⠤⢹⣿⣿⣿⣿⣿⣿⣿⣷⠇⡌⠐⠨⠀⢠⠐⠀⠐⡀⢀⠐⡀⠂⠁⢄⠀⠆⠀⡅⢂⠄⣁⠊⠅⡁⠄⠆⡀⠄⠄⢁⠉⡉⢉⠛⠋⠐⠀⠐⠂⠨⠠⢁⠐⠠⢂⠈⡐⢠⠈⢌⠐⠰⢈⠐⠡⡐⠠⠄⡈⠄⡐⠡⠄⢂⠒⠠⠌⡐
    ⢂⡚⣀⠣⠄⢂⠒⡄⠃⢌⠠⠁⠌⢀⣠⣴⣾⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣯⡔⡁⢂⠰⠈⠤⢈⢈⠨⠐⡀⠦⣿⣿⣿⣿⣿⣿⣿⣇⡣⠄⡉⠄⡁⠠⢀⠀⢂⠐⠀⠂⠐⡀⢁⠀⡀⠂⠀⠅⢂⡌⠄⠁⡠⠒⢀⠂⠐⠌⠠⠌⡁⠠⠀⠄⠀⠂⠈⠠⠈⠐⡈⢀⠨⠐⠠⢈⠰⠀⢌⠠⠘⣀⠢⢈⡐⠠⢁⠂⠔⠠⠁⠆⠡⠂⢌⠐⡂⠄
    ⢀⠒⡄⠃⡌⠠⡑⠠⠁⠂⣀⣬⣶⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡿⢏⠱⠀⢂⠈⠌⡠⢂⢀⠂⠐⠠⢈⣿⣿⣿⣿⣿⣿⣿⣿⡟⠆⡀⠘⠠⠠⡀⠄⣀⠀⠂⠁⡄⠀⠂⠄⡀⠄⠐⠊⠀⣀⠤⠊⠀⠐⠀⠄⢁⠈⠀⠄⠠⠁⠄⠈⠄⠈⠐⠀⡁⠂⠐⡀⢂⠉⠰⢀⠰⠈⠤⠘⢠⠠⠐⠠⠄⢁⠢⠈⠤⠡⠁⠌⡡⠌⠠⠌⡐⠀
    ⠀⠣⠄⡃⠐⡁⢀⣡⣶⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡿⢋⠐⡀⠂⠌⢀⠈⠠⠀⠠⢀⠘⡀⢁⢂⢹⣿⣿⣿⣿⣿⣿⣿⣯⣔⠈⠐⠤⢄⣀⠈⠀⠈⠁⠂⠐⠂⠈⠀⣀⡀⠆⠐⠋⠀⠄⠄⠀⠌⠠⢀⠀⢀⠠⠀⠀⠁⠀⠁⡀⠁⠈⢀⠀⡈⠄⢐⠈⢠⠡⠀⢢⠈⠤⠑⠠⠠⠉⠰⢈⠂⠠⠉⠤⡈⠅⠢⠁⠎⡠⠁⡄⠡
    ⠈⠡⢐⣠⣥⣾⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡟⡱⠈⠄⠠⠁⠄⡂⠈⠄⠂⠡⠐⢀⠠⠀⠂⠼⣿⣿⣿⣿⣿⣿⣿⣿⡗⠌⠀⠠⠀⠄⡉⢉⠁⠁⠃⠂⠃⠉⠁⠀⠄⠠⠀⡁⠂⠄⠈⠠⠀⠄⠂⠈⠀⠄⠈⠌⠈⠐⠄⠠⠁⠌⠠⠈⠄⠌⠠⠘⠠⢀⠉⠄⠨⢐⠈⠡⠈⡌⠠⠁⠌⠰⠈⡐⠌⠈⠤⡉⠄⡁⠡⡐⠀
    ⣠⣷⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡿⠟⣹⣿⣿⣿⣿⣿⡿⡁⠆⠡⢈⠠⠁⠂⠄⠁⡈⠈⠔⠐⢀⠐⡁⢈⠐⠻⣿⣿⣿⣿⠿⡛⠉⠄⠂⠈⠀⠈⠄⡀⠀⠄⠂⠁⠂⠁⠂⠁⠌⡀⠁⠄⡀⠂⠄⡁⠄⠐⡀⠤⠁⠀⠤⠈⠄⠁⠈⠠⠁⠀⠌⠠⠁⠌⠠⠁⠅⠡⢈⠌⢈⠡⠐⢈⠡⠈⠄⠡⠡⠈⡰⠀⠁⠌⠡⠠⠌⠠⢁⠃⠄⡁
    ⢿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⠟⡛⢡⠘⣸⣿⣿⣿⣿⡿⢛⠡⠘⠀⠆⡀⠡⠌⠐⠈⠄⠈⠤⠈⠈⠄⠐⠀⠄⠈⠄⠀⡐⠠⠀⠂⠠⠁⠄⠀⠂⠠⠈⠀⠀⠤⠀⠈⠄⡁⠂⡁⠂⠄⡀⠁⠂⠄⡁⠄⡀⠂⠁⠄⠀⠠⠁⠀⠁⠌⢀⠡⠀⠁⠉⠄⠠⠉⠠⢁⠠⠉⢠⠠⠌⠐⠈⠤⠈⠄⢉⠠⠡⠁⠌⠠⠉⠤⠉⡄⠡⢌⡐⠄⡉⠐⡀
    ⠈⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡿⡁⠊⢄⡁⣲⣿⣿⣿⣿⠟⡠⠁⠄⠢⢁⠠⠁⠄⠈⠄⠡⢈⠰⠀⠌⠈⢠⠈⠐⢈⠐⠈⠠⠐⠠⠁⢈⠀⠂⠈⠠⠈⠀⠈⠠⠄⠀⠈⠄⠂⠄⠡⠀⡁⠂⠄⡁⠂⠄⡀⠂⠄⠁⠂⠌⠀⠁⠄⠁⠈⠄⠀⠄⢁⠈⠐⠈⠁⠄⠡⠀⠔⢈⠠⢐⠈⠡⠌⠀⢡⠈⠤⠠⠁⠌⡈⠤⠁⡌⠐⠨⠀⠆⠨⠠⠡⡁⠐
    ⢈⡐⠻⣿⣿⣿⣿⣿⣿⣿⡟⠤⠑⡈⠤⣰⣿⣿⣿⡿⡙⡐⠠⢁⠒⠀⠄⡐⠈⠐⠈⠠⢁⠰⢀⠉⠄⠡⠀⢈⠈⠄⠈⠄⠡⠀⠐⠈⠀⠈⠀⢀⠀⠠⠈⠄⠀⠠⠁⠌⠠⠁⠌⠠⠁⠄⡁⠂⠄⡈⠄⠠⠁⠌⠠⠁⠠⠁⠌⠀⠡⠈⠄⢁⠈⢀⠈⠄⠁⠡⠈⠄⠡⠈⠄⢠⠠⢈⠡⠈⠌⠠⢈⠐⠤⠉⠄⠨⠠⠐⠨⠈⠄⠩⠄⡡⠁⠥⠀⠅
    ⠠⠠⣁⠻⣿⣿⣿⣿⣿⣿⣿⣧⠑⡄⣼⣿⣿⣿⣏⠖⠡⢀⠡⢀⠂⠡⢀⠠⢈⠠⠡⢁⠐⠠⠄⠡⢈⠠⠉⠠⠀⠌⠠⠀⠄⠁⠠⠀⠌⡀⠠⠀⠈⠄⠂⠌⠠⠁⠈⠄⠠⠁⠌⠠⠁⠂⠄⠁⠂⡀⠄⠁⠂⠈⠀⠡⠀⠌⠀⠡⠀⠠⠀⠄⢈⠀⠄⠀⠉⠄⠈⠐⠠⢁⠌⠠⢀⠄⠡⢁⠘⠠⠄⠨⠠⠁⠌⠠⢁⠉⡄⠊⠄⠃⠔⠠⠉⠤⠉⠄
    ⢀⠃⠄⢂⠚⣿⣿⣿⣿⣿⣿⣿⣗⣼⣿⣿⣿⣏⠒⡈⢁⠂⡂⠐⠠⠁⠄⠠⠌⠠⠁⠄⢉⠐⠌⠠⠄⠌⠐⠡⠉⠄⠡⠈⠄⠉⠄⠁⠠⠀⠡⠈⠠⠀⠡⠈⠄⠈⠠⠈⠄⠈⠠⠁⠌⠀⠊⠌⠠⠀⠂⠡⠈⠄⠁⠄⠀⠄⠁⠄⠀⠁⠌⠠⠀⠈⠄⠡⠠⠀⠡⢈⠐⠠⠌⠐⠠⠈⠔⠈⠤⠁⠌⠡⠐⠌⢈⠡⠄⠰⠈⡄⠨⠡⢈⠡⠉⠄⠩⠄
    ⠀⢎⡐⡈⠰⢈⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣟⠢⢁⠄⢃⠐⠀⠡⠐⢈⠈⠡⠈⠄⠡⠌⠤⠈⠤⠁⠌⢠⠉⠄⠡⢈⠀⠡⠈⠄⠈⠄⠡⠈⠄⠁⠂⠄⡀⠡⠈⡀⠠⠁⠀⠡⡀⠌⠠⠉⠄⡈⠄⠡⠈⠄⠠⠈⠄⠈⠄⠈⠠⠀⠡⠈⠄⢀⠁⠤⠀⠁⠄⢁⠐⠠⢈⠡⠈⠌⠡⠈⠤⠑⠠⠉⠠⠡⠌⠐⠌⠠⠈⠄⠡⠄⠡⠌⠄⠡⠊⡉⠤⢁
    ⠈⢢⠐⡌⠤⡁⠌⣿⣿⣿⣿⣿⣿⣿⣿⣟⠢⢁⠂⠌⠂⡈⠄⡁⠂⠌⠤⠁⠡⠌⠐⠈⠄⠡⠄⠑⠈⠄⠐⢈⠐⠠⢈⠐⠈⠠⠁⠌⠠⠈⠀⠡⠀⠀⠠⠀⠄⠁⠀⠌⠈⠀⠄⡈⠄⡁⠂⠄⡈⠄⠡⠈⠄⠀⠂⠌⠀⠡⠀⠈⠄⠀⠌⠀⠄⠀⠡⠐⠈⠀⠰⠀⠡⠠⠑⠈⠄⠡⡀⠡⠂⠡⠡⠐⣈⠡⠈⠤⠑⠌⡄⠡⠌⠌⠄⡋⢄⠡⠊⠄
    ⠈⠥⠉⡔⠠⡂⠥⢘⢿⣿⣿⣿⣿⣿⠿⠌⢒⠀⡃⠘⢠⠐⠠⠀⠥⢈⠄⡉⢠⠈⠡⠌⢈⠐⠈⠔⠈⠌⠐⠠⢈⠐⢀⠈⠀⠡⢀⠈⠄⠈⠄⠠⠈⠠⠁⠈⠠⠁⠈⠠⠈⠄⠂⠄⠂⠄⡁⠂⠄⠌⠠⠁⠂⡁⠂⠈⠄⠠⠀⠁⠠⠁⠀⠌⠠⠁⠄⠈⠀⠉⠄⠡⠠⠁⠌⢈⠄⠡⠠⠰⢈⠁⠤⠁⠤⢀⠉⠔⠨⠄⠄⡡⠈⠔⠨⠐⠄⢆⠱⠈
    ⢉⠧⢡⡬⣁⡆⡰⡁⣊⣹⡟⣏⡋⡄⢃⡘⢀⠊⡐⢁⠂⠄⠡⠈⠄⠂⠐⠀⠄⠁⠂⢈⠀⠁⢈⠈⠐⠈⠁⠐⠀⠈⠀⠈⠐⠀⠀⠀⠈⠀⠈⠀⠀⠀⠈⠀⠀⠈⠀⠁⠀⠈⠀⠀⠁⠀⠀⠁⠈⠀⠁⠈⠀⠀⠁⠈⠀⠐⠀⠃⠀⠀⠁⠀⠂⠁⠀⠉⠈⠀⠈⠀⠁⠈⠐⠈⠀⠀⠁⠠⠀⠌⠐⠁⡈⢀⠡⠈⠄⠡⠈⠄⡁⢊⠐⡉⠐⡈⢂⠡''')

    roll_ninja, roll_pirate = dice()

    #NINJA
    if roll_ninja>roll_pirate:
        print("Let'go Ninjas!!!")
        print("Pick your next attack!")
        round1_attack_ninja=input("[attack, critical_attack, combo_attack, use_weapon, rest, exit_game]:   ")
        if round1_attack_ninja.lower()=='attack':
            if michelangelo.stamina>=0:
                print("Cant attack!!! You are tried!! Rest for a Bit!!")
            else:
                michelangelo.attack(jack_sparrow)
                jack_sparrow.stamina-=1
                jack_sparrow.show_stats()
            
        elif round1_attack_ninja.lower()=='critical_attack':
            if michelangelo.stamina>=0:
                print("Cant attack!!! You are tried!! Rest for a Bit!!")
            else:
                michelangelo.critical_attack(jack_sparrow)
                jack_sparrow.stamina-=3
                jack_sparrow.show_stats()
            
        elif round1_attack_ninja.lower()=='combo_attack':
            if michelangelo.stamina>=0:
                print("Cant attack!!! You are tried!! Rest for a Bit!!")
            else:
                if michelangelo.health<=10:
                    michelangelo.combo_attack(jack_sparrow)
                    jack_sparrow.show_stats()
                print("Can't combo attack. Ninja HP still high.")
                jack_sparrow.show_stats()
            
        elif round1_attack_ninja.lower()=='doge':
            michelangelo.doge()
            michelangelo.show_stats()
        elif round1_attack_ninja.lower()=='use_weapon':
            if michelangelo.stamina>=0:
                print("Cant attack!!! You are tried!! Rest for a Bit!!")
            else:
                if counter==5 or counter==7 or counter== 9:
                    michelangelo.use_weapon(jack_sparrow)
                    jack_sparrow.show_stats()
            
        elif round1_attack_ninja.lower()=='rest':
            michelangelo.rest()
            michelangelo.show_stats()
        elif round1_attack_ninja.lower()=='exit_game':
            Gameon=False
        else:
            print("Wrong Input")
            print("Your Turn Has Passed!!")
        

    #PIRATE   
    else:
        print("Let'go Pirates")
        print("Pick your next attack!")
        round1_attack_pirates=input("[attack, critical_attack, combo_attack, use_weapon, rest, exit_game]:   ")
        if round1_attack_pirates.lower()=='attack':
            if jack_sparrow.stamina==0:
                print("Cant attack!!! You are tried!! Rest for a Bit!!")
            else:
                jack_sparrow.attack(michelangelo)
                michelangelo.stamina-=1
                michelangelo.show_stats()
            
        elif round1_attack_pirates.lower()=='critical_attack':
            if jack_sparrow.stamina==0:
                print("Cant attack!!! You are tried!! Rest for a Bit!!")
            else:
                jack_sparrow.critical_attack(michelangelo)
                michelangelo.stamina-=3
                michelangelo.show_stats()
            
        elif round1_attack_pirates.lower()=='combo_attack':
            if jack_sparrow.stamina==0:
                print("Cant attack!!! You are tried!! Rest for a Bit!!")
            else:
                if jack_sparrow.health<=10:
                    jack_sparrow.combo_attack(michelangelo)
                    michelangelo.show_stats()
                print("Can't combo attack. Ninja HP still high.")
                michelangelo.show_stats()
            
        elif round1_attack_pirates.lower()=='doge':
            jack_sparrow.doge()
            jack_sparrow.show_stats()
        elif round1_attack_pirates.lower()=='use_weapon':
            if jack_sparrow.stamina==0:
                print("Cant attack!!! You are tried!! Rest for a Bit!!")
            else:
                if counter==5 or counter==7 or counter== 9:
                    jack_sparrow.use_weapon(michelangelo)
                    michelangelo.show_stats()
                
            
        elif round1_attack_pirates.lower()=='rest':
            jack_sparrow.rest()
            jack_sparrow.show_stats()
        elif round1_attack_pirates.lower()=='exit_game':
            Gameon=False
        else:
            print("Wrong Input")
            print("Your Turn Has Passed!!")


    if michelangelo.health <= 0:
        print("Game Over!")
        print('''⠀⠀⠀⠀⣠⣶⣶⣤⠀⠀⠀⠀⠀⠀⠀⠀⠀⣠⣶⣶⣦⠀⠀
                ⠀⠀⠀⠀⢿⣿⣿⣿⠀⠀⠀⢀⣀⣠⣤⣄⠀⢿⣿⣿⣿⠇⠀
                ⠀⠀⠀⠀⠈⣉⣩⣥⣶⣶⣿⣿⣿⡿⠿⠋⣀⣀⣉⣉⡁⠀⠀
                ⠀⠀⣠⣾⣿⣿⣿⣿⡟⠛⠋⠉⠀⣠⣴⣿⣿⣿⣿⣿⣿⣧⠀
                ⣴⣾⣿⣿⣿⣿⣿⣿⢁⣤⣶⣿⣿⣿⡿⣿⣿⣿⣿⣿⣿⣿⠀
                ⠻⠿⣿⣿⣿⣿⣿⠇⠈⠻⠟⠋⠉⠁⢰⣿⣿⣿⣿⣿⣿⡿⠂
                ⠀⢠⣿⣿⣿⣿⣿⠀⠀⠀⠀⠀⠀⢠⣿⣿⣿⣿⡏⠀⠀⠀⠀
                ⠀⣸⣿⣿⠟⣿⣿⣧⠀⠀⠀⠀⣰⣿⣿⡿⣿⣿⣷⠀⠀⠀⠀
                ⠀⣿⣿⡟⠀⠘⣿⣿⡇⠀⠀⢰⣿⣿⠟⠀⠸⣿⣿⡄⠀⠀⠀
                ⣰⣿⣿⠃⠀⠀⣿⣿⡇⠀⠀⢸⣿⣿⠀⠀⠀⢿⣿⣧⠀⠀⠀
                ⣿⣿⠇⠀⠀⠀⣿⣿⡇⠀⠀⢸⣿⣿⠀⠀⠀⠘⣿⣿⡆⠀⠀
                ⠉⠉⠀⠀⠀⠀⠈⠉⠀⠀⠀⠀⠉⠉⠀⠀⠀⠀⠈⠉⠀⠀⠀''')
        print("☠️   ☠️  ☠️  ☠️  ☠️  ☠️  ☠️  ☠️  ☠️  ☠️  ☠️  ☠️  Victory  ☠️  ☠️  ☠️  ☠️  ☠️  ☠️  ☠️  ☠️  ☠️  ☠️  ☠️  ☠️  ☠️  ☠️")
        jack_sparrow.celebrate('jack_sparrow')
        Gameon=False

    if jack_sparrow.health <= 0:
        print("Game Over!")
        print('''⠀⠀⠀⣠⣶⣶⣤⠀⠀⠀⠀⠀⠀⠀⠀⠀ ⣠⣶⣶⣦⠀⠀
                ⠀⠀⠀⠀⢿⣿⣿⣿⠀⠀⠀⢀⣀⣠⣤⣄⠀⢿⣿⣿⣿⠇⠀
                ⠀⠀⠀⠀⠈⣉⣩⣥⣶⣶⣿⣿⣿⡿⠿⠋⣀⣀⣉⣉⡁⠀⠀
                ⠀⠀⣠⣾⣿⣿⣿⣿⡟⠛⠋⠉⠀⣠⣴⣿⣿⣿⣿⣿⣿⣧⠀
                ⣴⣾⣿⣿⣿⣿⣿⣿⢁⣤⣶⣿⣿⣿⡿⣿⣿⣿⣿⣿⣿⣿⠀
                ⠻⠿⣿⣿⣿⣿⣿⠇⠈⠻⠟⠋⠉⠁⢰⣿⣿⣿⣿⣿⣿⡿⠂
                ⠀⢠⣿⣿⣿⣿⣿⠀⠀⠀⠀⠀⠀⢠⣿⣿⣿⣿⡏⠀⠀⠀⠀
                ⠀⣸⣿⣿⠟⣿⣿⣧⠀⠀⠀⠀⣰⣿⣿⡿⣿⣿⣷⠀⠀⠀⠀
                ⠀⣿⣿⡟⠀⠘⣿⣿⡇⠀⠀⢰⣿⣿⠟⠀⠸⣿⣿⡄⠀⠀⠀
                ⣰⣿⣿⠃⠀⠀⣿⣿⡇⠀⠀⢸⣿⣿⠀⠀⠀⢿⣿⣧⠀⠀⠀
                ⣿⣿⠇⠀⠀⠀⣿⣿⡇⠀⠀⢸⣿⣿⠀⠀⠀⠘⣿⣿⡆⠀⠀
                ⠉⠉⠀⠀⠀⠀⠈⠉⠀⠀⠀⠀⠉⠉⠀⠀⠀⠀⠈⠉⠀⠀⠀''')
        print("🥷  🥷  🥷  🥷  🥷  🥷  🥷  🥷  🥷  🥷  🥷  🥷  Victory  🥷  🥷  🥷  🥷  🥷  🥷  🥷  🥷  🥷  🥷  🥷  🥷  🥷  🥷")
        michelangelo.celebrate('michelangelo')
        Gameon=False
