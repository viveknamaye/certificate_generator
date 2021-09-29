from fpdf import FPDF
import matplotlib.pyplot as plt

# pdf.add_font('custom_font', fname = './copy.ttf')

n = int(input('ENTER COUNT : '))
names = []

for i in range(0, n) : 
    name = input('ENTER NAME : ')
    names.append(name)



def make_pdf(name, dir) : 
    pdf = FPDF(orientation = 'L', unit = 'mm', format = 'A4')
    pdf.add_page()
    pdf.image('./template.png', h = 210, w = 300, x = 0, y = 0)
    pdf.set_font('Helvetica', 'B', 48) 
    pdf.set_text_color(255, 157, 125)
    pdf.set_xy(0,100)
    pdf.cell(w = 300, h = 10, txt = name, align = 'C')
    pdf.output(dir + '/' + name + '.pdf', 'F')


for name in names : 
    make_pdf(name, './outputs')

# orange 255, 157, 125
# yellow 237, 255, 122

#1414 x 2000