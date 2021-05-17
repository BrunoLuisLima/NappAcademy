import csv
import os
import glob

caso_file = open('caso_full.csv', encoding='utf8')
candidatura_file = open('candidatura.csv', encoding='utf8')
log_file = open('access.log', encoding='utf8')


def abre_log_file(log_file):
    for linha in log_file:
        yield linha, linha.upper()


def abre_csv_file(csv_file):
    for linha in csv_file:
        yield linha


def busca_leme(csv_file):
    for linha in csv_file:
        if 'Leme' in linha:
            yield linha


def separa_arquivos_por_ano(csv_file):
    path = 'output'
    already = 0
    all_lines = abre_csv_file(csv_file)

    # Clean output folder
    if not os.path.exists(path):
        os.mkdir(path)
    files = glob.glob(path + '\\*.csv')
    for file in files:
        os.remove(file)

    while True:
        try:
            linha = next(all_lines).replace('\n', '').split(',')
            ano = linha[0]
            if ano == 'ano_eleicao':
                header = linha
            else:
                filename = f'output/eleicoes_{ano}.csv'

                # Create file with header
                if not os.path.exists(filename):
                    print('Criando novo arquivo com dados de ', ano)
                    with open(filename, 'w', newline='') as csv_w:
                        csv_writer = csv.writer(csv_w, delimiter=';')
                        csv_writer.writerow(header)

                # Append lines in file
                with open(filename, 'a', newline='') as csv_a:
                    csv_writer = csv.writer(csv_a, delimiter=';')
                    csv_writer.writerow(linha)
                    already += 1
                    print(already)

        except StopIteration:
            del all_lines
            break


arquivo_carregado_em_memoria = open('caso_full.csv', encoding='utf8').read()
separa_arquivos_por_ano(candidatura_file)
