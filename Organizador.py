import PyPDF2
import shutil
import os

def combinar_paginas(input_pdf):
    # Cria uma cópia temporária do arquivo de entrada
    temp_pdf = "temp_combinado.pdf"
    shutil.copyfile(input_pdf, temp_pdf)

    # Abre o arquivo PDF original
    with open(temp_pdf, 'rb') as file:
        pdf_reader = PyPDF2.PdfReader(file)
        total_paginas = len(pdf_reader.pages)

        # Abre o mesmo arquivo PDF para escrita
        with open(input_pdf, 'wb') as output_file:
            pdf_writer = PyPDF2.PdfWriter()

            # Combina as páginas em pares alternados
            for indice in range(total_paginas // 2):
                # Páginas do início
                pagina_inicio = pdf_reader.pages[indice]
                # Páginas do final
                pagina_final = pdf_reader.pages[indice + total_paginas // 2]

                # Adiciona as páginas ao mesmo arquivo PDF
                pdf_writer.add_page(pagina_inicio)
                pdf_writer.add_page(pagina_final)

            # Se houver um número ímpar de páginas, adiciona a página central ao mesmo arquivo PDF
            if total_paginas % 2 != 0:
                pagina_central = pdf_reader.pages[total_paginas // 2]
                pdf_writer.add_page(pagina_central)

            # Salva as modificações no mesmo arquivo PDF
            pdf_writer.write(output_file)

    # Remove a cópia temporária do arquivo de entrada
    os.remove(temp_pdf)

if __name__ == "__main__":
    # Substitua 'input.pdf' pelo nome do seu arquivo PDF de entrada
    combinar_paginas('sem_separar.pdf')
