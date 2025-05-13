import os

caminho = r'C:\Users\joab.alves\Desktop\cadastro_linha_pesada-12-05\img2'

os.chdir(caminho)
for x in os.listdir():
    os.rename(rf'{caminho}\{x}', rf'{caminho}\{x.replace('.jpg', '')}-2.jpg')
    print(x)
