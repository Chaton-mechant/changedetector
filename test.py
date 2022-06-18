from pyfiglet import Figlet

with open("test.txt", "w+") as file:
    f = Figlet(font='banner3-D', width=80)
    file.writelines(f.renderText('Change'))
    file.writelines(f.renderText('Detect'))
