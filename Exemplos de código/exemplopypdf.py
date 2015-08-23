from fpdf import FPDF

class PDF(FPDF):
        def header(this):
                
                # Arial bold 15
                this.set_font('Arial','B',15)
                # Move to the right
                this.cell(80)
                # Title
                this.cell(30,10,'Contrato',1,0,'C')
                # Line break
                this.ln(20)

        # Page footer
        def footer(this):
                # Position at 1.5 cm from bottom
                this.set_y(-15)
                # Arial italic 8
                this.set_font('Arial','I',8)
                # Page number
                this.cell(0,10,'Page '+str(this.page_no())+'/{nb}',0,0,'C')

# Instanciation of inherited class
pdf=PDF()
pdf.alias_nb_pages()
pdf.add_page()
pdf.set_font('Times','',12)
#fazer um select, e depois uma interação para puxar cada valor no banco
for i in range(1,41):
        pdf.cell(0,10,'Printing line number '+str(i),0,1)
        pdf.cell(0,10,'Printing line  '+str(i),0,1)
pdf.output('tuto.pdf','F', )
