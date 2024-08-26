import fitz
import os
import re
from configparser       import RawConfigParser
from time               import sleep



config      = RawConfigParser()
diretorio   = os.getcwd()
config.read(os.path.join(diretorio, 'config.ini'), encoding='utf-8')


path_caberito = os.path.join(diretorio, config["Enem"]["ano"], f'Gabarito {config["Enem"]["ano"]}.pdf')

if not os.path.exists(path_caberito):
    print(F"Caminho não existe - ({path_caberito})")
    sleep(300)

cabarito                = fitz.open(path_caberito)
gabarito_texto          = ''

for page_num in range(cabarito.page_count):
    page                = cabarito.load_page(page_num)
    gabarito_texto      = page.get_text()


questoes_e_gabaritos = re.findall(r'(\d+)\n([A-E])', gabarito_texto)
gabarito_dict = {int(questao): resposta for questao, resposta in questoes_e_gabaritos}

while True:
    questao = input("Para sair pressione \"S\"\n\n\tQuestão: ").lower()

    os.system("cls")
    if questao == 's':
        break

    elif not questao.isnumeric():
        print("Questão inválida")
        continue

    resultado = gabarito_dict.get(int(questao))

    if not resultado:
        print("Resposta não encontrada")
    else:
        print(f"Resposta: {resultado}")

