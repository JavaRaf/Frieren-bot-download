import subprocess
import os
import math

def subtitle(comment: dict) -> None:

        if 'subtitle' in comment and 'file_path' in comment and 'frame_number' in comment:
            subtitle = comment['subtitle']

            # Divide o subtítulo em palavras
            subtitle_partes = subtitle.split(' ')

            # Calcula o número de linhas e ajusta o tamanho do fundo
            lines = math.ceil(len(subtitle_partes) / 5)
            backgound_size = f'0x{str(int(lines) * 120)}'

            # Insere quebras de linha a cada 5 palavras, mas evita a última quebra de linha desnecessária
            subtitle_com_quebras = []
            for i in range(0, len(subtitle_partes), 5):
                subtitle_com_quebras.append(' '.join(subtitle_partes[i:i+5]))

            # Junta as linhas com '\n' para que o texto seja exibido corretamente
            subtitle = '\n'.join(subtitle_com_quebras).strip()

            # Configuração dos parâmetros do comando
            file_path = comment['file_path']
            gravity = '-gravity'
            gravity_value = 'North'
            font = '-font'
            font_path = 'font/Cooper.otf'
            font_size = '-pointsize'
            font_size_value = '100'
            background_color = '-background'
            background_color_value = 'White'
            splice = '-splice'
            splice_value = backgound_size
            annotate = '-annotate'
            annotate_position = '+0+20'
            output_name = file_path
            image_magick_command = 'magick' if os.name == 'nt' else 'convert'

            # Criação da lista de comandos
            command = [
                image_magick_command,  # Ou 'convert' se estiver usando no Linux
                file_path,
                gravity, gravity_value,
                background_color, background_color_value,
                splice, splice_value,
                font, font_path,
                font_size, font_size_value,
                annotate, annotate_position,
                subtitle,
                output_name
            ]

            try:
                # Executa o comando
                subprocess.run(command, check=True)
            except subprocess.CalledProcessError as e:
                print(f"Ocorreu um erro ao executar o comando: {e}")