import os
import shutil

def organizar_arquivos(diretorio):
    # Define os caminhos para as pastas do sistema
    caminho_imagens = os.path.join(os.path.expanduser('~'), 'Pictures')

    # Organiza os arquivos
    for arquivo in os.listdir(diretorio):
        # Verifica se é um arquivo e não uma pasta
        if os.path.isfile(os.path.join(diretorio, arquivo)):
            extensao = os.path.splitext(arquivo)[1].lower()
            destino_encontrado = False
            
            if extensao in ['.jpg', '.jpeg', '.png', '.gif']:
                shutil.move(os.path.join(diretorio, arquivo), os.path.join(caminho_imagens, arquivo))
                destino_encontrado = True
            
            
            # Se a extensão não for reconhecida, você pode optar por deixá-los no diretório original
            if not destino_encontrado:
                print(f"Extensão não reconhecida para o arquivo: {arquivo}")

if __name__ == "__main__":
    # Obtém o caminho da pasta Downloads do usuário
    caminho_diretorio = os.path.join(os.path.expanduser('~'), 'Downloads')
    organizar_arquivos(caminho_diretorio)
