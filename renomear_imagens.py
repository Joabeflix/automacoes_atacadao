import os

caminho = r'C:\Users\joab.alves\Desktop\IMG\IMG 3'



os.chdir(caminho)
for x in os.listdir():
    os.rename(rf'{caminho}\{x}', rf'{caminho}\{x.replace('.jpg', '')}-3.jpg')
    print(x)
