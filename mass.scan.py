import pydnsbl
import os
import time
import datetime
from datetime import date
#import csvt
from fpdf import FPDF
import numpy as np
import pandas as pd
from reportlab.lib.pagesizes import letter
from reportlab.pdfgen import canvas
import matplotlib.pyplot as plt
from matplotlib.pyplot import pie, axis, show
from pandas import DataFrame

title_custom = str(input("Enter title for the report: "))
#file = input('drag and drop here the file that contains the ips list \n\n >>>')

ip_checker = pydnsbl.DNSBLIpChecker()
#------------------------------lectura del archivo para scan masivo
with open('archivo.txt') as file:
    ips = file.read().splitlines()
    #------------------------------scan de ips
    for ip in ips:
        if ip_checker.check(ip).blacklisted:
            blacklist = ip_checker.check(f'{ip}')

            #------------------------------resultado en pantalla
            print(f"{ip} blacklisted")
            print(blacklist)
            #------------------------------guardar resultados para informe
            resultados =  open('blacklist.result.log','a')
            resultados.write(str((f'{blacklist}''\n')))
            resultados.close()
            #------------------------------cuenta lista original ips para INFORME
            count_ips = os.system(f"grep -c '.*' archivo.txt > count_ips.log")
            save_acount_ips_orig = os.popen('cat count_ips.log').read()
            #------------------------------contador de ips resultado para INFORME
            count_ips = os.system("grep -c '.*' blacklist.result.log > count_ips.log")
            save_acount_ips_result = os.popen('cat count_ips.log').read()
            #resta de lineas para resultado final
            str(int(save_acount_ips_orig))
            str(int(save_acount_ips_result))
            resta = (int(save_acount_ips_orig) - int(save_acount_ips_result))

            #------------------------------guardar datos en archivo para grafica
            archivo = open("csv_grafica.csv","w")
            activos = 'ips_reported'
            inactivos = 'ips_no_reporte'
            a2 = 'reported'
            b2 = 'no_report'

            archivo.write(str((f'{activos},{inactivos}''\n')))
            archivo.write(str((f'{a2},{save_acount_ips_result}''\n')))
            archivo.write(str((f'{b2},{resta}''\n')))

            archivo.close()

            #------------------------------generando grafica en jpg

            df =  pd.read_csv('csv_grafica.csv')
            country_data = df["ips_reported"]
            medal_data = df["ips_no_reporte"]
            colors = ["#d62728", "#2ca02c"]
            explode = (0, 0.1,)
            plt.pie(medal_data, labels=country_data, explode=explode, colors=colors,
            autopct='%1.1f%%', shadow=True, startangle=140)
            plt.title("Pie - percentages IPs - reported")
            plt.savefig('grafica.png')
            plt.show(block=False)
            plt.pause(3)
            plt.close()

            #-----------------------------generando PDF

            title = f'{title_custom}'



            class PDF(FPDF):
                def header(self):

                    # Logo
                    self.image('DaveNISC.png', 10, 8, 15)
                    # Arial bold 15
                    self.set_font('Arial', 'B', 15)
                    # Calcular ancho del texto (title) y establecer posición
                    w = self.get_string_width(title) + 6
                    self.set_x((210 - w) / 2)
                    # Colores del marco, fondo y texto
                    self.set_draw_color(36, 113, 163)
                    self.set_fill_color(36, 113, 163)
                    self.set_text_color(300)
                    # Grosor del marco (1 mm)
                    self.set_line_width(1)
                    # Titulo
                    self.cell(w, 9, title, 1, 1, 'C', 1)
                    # Salto de línea
                    self.ln(10)

                def footer(self):
                    # Posición a 1.5 cm desde abajo
                    self.set_y(-15)
                    # Arial italic 8
                    self.set_font('Arial', 'I', 8)
                    # Color de texto en gris
                    self.set_text_color(128)
                    # Numero de pagina
                    self.cell(0, 10, 'Page ' + str(self.page_no()), 0, 0, 'C')

                def chapter_title(self, num, label):
                    # Arial 12
                    self.set_font('Arial', '', 12)
                    # Color de fondo
                    self.set_fill_color(200, 220, 255)
                    # Titulo
                    #self.cell(0, 6, 'Chapter %d : %s' % (num, label), 0, 1, 'L', 1)
                    # Salto de línea
                    self.ln(112)

                def chapter_body(self, name):
                    # Leer archivo de texto
                    with open(name, 'rb') as fh:
                        txt = fh.read().decode('latin-1')
                    # Grafica
                    self.image('grafica.png', 20, 25, 170)
                    # Times 12
                    self.set_font('Arial', '', 12)
                    # Emitir texto justificado
                    self.multi_cell(0, 5, txt)
                    # Salto de línea
                    self.ln()
                    # Mención en italic -cursiva-
                    self.set_font('Arial', '', 12)
                    num1 = 2
                    num2 = 10
                    self.cell(0, 5, f'IPs analyzed : {save_acount_ips_orig} IPs reported: {save_acount_ips_result}')
                    # Salto de línea
                    self.ln()
                    self.ln()
                    # Salto de línea
                    self.ln()
                    self.ln()
                    self.ln()
                    self.ln()
                    self.ln()
                    self.ln()
                    self.ln()
                    self.ln()
                    self.ln()
                    # Mención en italic -cursiva-
                    self.set_font('Times', '', 12)
                    today = date.today()
                    self.cell(0, 5, f'Report date: {today}')
                    # Salto de línea
                    self.ln()
                    self.ln()


                def print_chapter(self, num, title, name):
                    self.add_page()
                    self.chapter_title(num, title)
                    self.chapter_body(name)

            pdf = PDF()
            pdf.set_title(title)
            pdf.set_author('Jules Verne')
            pdf.print_chapter(1, 'A RUNAWAY REEF', 'blacklist.result.log')
            pdf.output('Informe-blacklist.pdf', 'F')
            print()

#-----------------------------Limpiar logs
delete_log = os.system('rm blacklist.result.log')
delete_csv = os.system('rm csv_grafica.csv')

print()
print("thanks for using my script, visit www.davenisc.com")
