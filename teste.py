import os

caminho = r'C:\Users\joab.alves\Desktop\imagens cadastro linha pesada\Img2\outros'

os.chdir(caminho)
for x in os.listdir():
    os.rename(rf'{caminho}\{x}', rf'{caminho}\{x.replace('.jpg', '')}-2.jpg')
    print(x)
