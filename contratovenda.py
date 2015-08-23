# -*- coding: utf-8 -*-
from fpdf import FPDF

def novoVenda(nomeVend, naturalidadeVend,estadoCivilVend,profissaoVend,rgVend,cpfVend,ruaVend,numVend,bairroVend,cepVend,cidadeVend,estadoVend,nomeComp,naturalidadeComp,estadoCivilComp,profissaoComp,rgComp,cpfComp,ruaComp,numComp,bairroComp,cepComp,cidadeComp, estado, area, registro, valor):
    #Definindo o formato do PDF
    pdf=FPDF('P','mm','A4')
    #Definindo as margens
    pdf.set_margins(10, 10, 10)
    #Adicionando página
    pdf.add_page()
    #Adicionando configurações de Fonte

    pdf.set_font('Arial','B',16)
    #Inserindo linhas cell by cell.
    contrato = 'CONTRATO E COMPROMISSO DE COMPRA E VENDA DE IMÓVEL'
    utxt1 = unicode (contrato, 'UTF-8')
    stxt1 = utxt1.encode ('iso-8859-1')
    pdf.cell(0,10,stxt1, 1,1 , 'C')
    pdf.ln(10)
    #Dados pessoais das partes interessadas

    pdf.set_font('Arial','',8)
    vendedor = 'PROMITENTE VENDEDOR: '+nomeVend+', nascido em '+naturalidadeVend+', '+estadoCivilVend+','+profissaoVend+',portador do R.G. nº '+rgVend+' ,'
    vendedor += '  e CPF/MF nº '+cpfVend+' residente e domiciliado à '+ruaVend+', '+numVend+', '+bairroVend+', '+cepVend+', '+cidadeVend+', '+estadoVend+'.'
    utxt2 = unicode (vendedor, 'UTF-8')
    stxt2 = utxt2.encode ('iso-8859-1') 
    pdf.multi_cell(0,5,stxt2, 0,'J')
    pdf.ln(1)
    
    comprador = 'PROMITENTE COMPRADOR: '+nomeComp+', '+naturalidadeComp+', '+estadoCivilComp+', '+profissaoComp+', portador do R.G. nº '+rgComp+','
    comprador += ' e CPF/MF nº '+cpfComp+' residente e domiciliado à '+ruaComp+', '+numComp+', '+bairroComp+', '+cepComp+', '+cidadeComp+', '+estado+'.'
    utxt3 = unicode (comprador, 'UTF-8')
    stxt3 = utxt3.encode ('iso-8859-1') 
    pdf.multi_cell(0,5,stxt3, 0,'J')
    pdf.ln(5)

    pdf.set_font('Arial','B',10)
    clausulas = 'Têm entre os mesmos, de maneira justa e acordada, o presente contrato particular de compromisso de compra e venda de bem imóvel, ficando desde já aceito, pelas cláusulas abaixo descritas:'
    utxt4 = unicode (clausulas, 'UTF-8')
    stxt4 = utxt4.encode ('iso-8859-1') 
    pdf.multi_cell(0,5,stxt4, 0,'J')
    pdf.ln(3)

    pdf.set_font('Arial','',8)
    pdf.ln(1)
    primeira = 'CLÁUSULA PRIMEIRA:'
    utxt5 = unicode (primeira, 'UTF-8')
    stxt5 = utxt5.encode ('iso-8859-1') 
    pdf.cell(33,5,stxt5, 1,1 , 'L')
    pdf.ln(1)
    
    clausulaPrimeira = 'Que a PROMITENTE VENDEDORA é legítima possuidora do imóvel composto por área privativa de '+area+' metros quadrados, '
    clausulaPrimeira +='inscrito no livro de registro de imóveis sob nº '+registro+', com as seguintes confrontações:'
    utxt6 = unicode (clausulaPrimeira, 'UTF-8')
    stxt6 = utxt6.encode ('iso-8859-1') 
    pdf.multi_cell(0,5,stxt6, 0,'J')
    pdf.ln(2)

    segunta = 'CLÁUSULA SEGUNDA:'
    utxt7 = unicode (segunta, 'UTF-8')
    stxt7 = utxt7.encode ('iso-8859-1') 
    pdf.cell(33,5,stxt7, 1,1 , 'L')
    pdf.ln(1)
    
    clausulaSegunda = 'O valor da presente transação é feita pelo preço de R$ '+valor+', que serão pagos de acordo com o que as partes acharem cabíveis.'
    utxt8 = unicode (clausulaSegunda, 'UTF-8')
    stxt8 = utxt8.encode ('iso-8859-1') 
    pdf.multi_cell(0,5,stxt8, 0,'J')
    pdf.ln(2)
    
    terceira = 'CLÁUSULA TERCEIRA:'
    utxt9 = unicode (terceira, 'UTF-8')
    stxt9 = utxt9.encode ('iso-8859-1') 
    pdf.cell(33,5,stxt9, 1,1 , 'L')
    pdf.ln(1)
    
    clausulaTerceira = 'Que o PROMITENTE VENDEDOR se compromete a entregar o imóvel livre e desembaraçado de todos os débitos até esta data, junto ao Agente Financeiro'
    clausulaTerceira += ', ficando daí a responsabilidade do PROMITENTE COMPRADORE o pagamento mensal da prestação.'
    utxt10 = unicode (clausulaTerceira, 'UTF-8')
    stxt10 = utxt10.encode ('iso-8859-1') 
    pdf.multi_cell(0,5,stxt10, 0,'J')
    pdf.ln(2)

    quarta = 'CLÁUSULA QUARTA:'
    utxt11 = unicode (quarta, 'UTF-8')
    stxt11 = utxt11.encode ('iso-8859-1') 
    pdf.cell(33,5,stxt11, 1,1 , 'L')
    pdf.ln(1)
    
    clausulaQuarta = 'Fica acordado entre o PROMITENTE VENDEDOR e PROMITENTE COMPRADOR que o imóvel transacionado permanecerá em nome do PROMITENTE VENDEDOR por '
    clausulaQuarta += 'prazo indeterminado, ficando o PROMITENTE VENDEDOR obrigado a apresentar os documentos necessários para transrência a partir do momento em que '
    clausulaQuarta += 'o mesmo for notificado pelo PROMITENTE COMPRADOR a qualquer época. '
    utxt12 = unicode (clausulaQuarta, 'UTF-8')
    stxt12 = utxt12.encode ('iso-8859-1') 
    pdf.multi_cell(0,5,stxt12, 0,'J')
    pdf.ln(2)
    
    quinta = 'CLÁUSULA QUINTA:'
    utxt13 = unicode (quinta, 'UTF-8')
    stxt13 = utxt13.encode ('iso-8859-1') 
    pdf.cell(33,5,stxt13, 1,1 , 'L')
    pdf.ln(1)

    clausulaQuinta = 'Todos os compromissos assumidos neste contrato são de caráter irrevogável e irrefratével, obrigado as partes, seus herdeiros e sucessores a qualquer'
    clausulaQuinta += 'título fazer sempre boa e valiosa a presente cessão, ficando sujeito às penalidades da lei.'
    utxt14 = unicode (clausulaQuinta, 'UTF-8')
    stxt14 = utxt14.encode ('iso-8859-1') 
    pdf.multi_cell(0,5,stxt14, 0,'J')
    pdf.ln(2)

    sexta = 'CLÁUSULA SEXTA:'
    utxt15 = unicode (sexta, 'UTF-8')
    stxt15 = utxt15.encode ('iso-8859-1') 
    pdf.cell(33,5,stxt15, 1,1 , 'L')
    pdf.ln(1)
    
    clausulaSexta = 'Fica ainda acordando, que caso haja necessidade de se beneficiar do seguro referente ao imóvel,os beneficiados será o PROMITENTE COMPRADOR,ou filhos.'
    utxt16 = unicode (clausulaSexta, 'UTF-8')
    stxt16 = utxt16.encode ('iso-8859-1') 
    pdf.multi_cell(0,5,stxt16, 0,'J')
    pdf.ln(2)
    
    setima = 'CLÁUSULA SÉTIMA:'
    utxt17 = unicode (setima, 'UTF-8')
    stxt17 = utxt17.encode ('iso-8859-1') 
    pdf.cell(33,5,stxt17, 1,1 , 'L')
    pdf.ln(1)
    
    clausulaSetima =  'Em caso de falecimento do PROMITENTE VENDEDOR ,fica acordando entre as partes que todo e qualquer benefício oriundo deste fato,transfere-se' 
    clausulaSetima += 'para o PROMITENTE COMPRADOR.'
    utxt18 = unicode (clausulaSetima, 'UTF-8')
    stxt18 = utxt18.encode ('iso-8859-1') 
    pdf.multi_cell(0,5,stxt18, 0,'J')
    pdf.ln(2)
    
    oitava = 'CLÁUSULA OITAVA:'
    utxt19 = unicode (oitava, 'UTF-8')
    stxt19 = utxt19.encode ('iso-8859-1') 
    pdf.cell(33,5,stxt19, 1,1 , 'L')
    pdf.ln(1)
    
    clausulaOitava = 'Caso haja manifestação pública por parte do Agente Financeiro, quando à transferência do imóvel citado neste instrumento particular de compra'
    clausulaOitava += 'venda, sem que haja o aumento das prestações fica acordo entre as partes a sua transferência.'
    utxt20 = unicode (clausulaOitava, 'UTF-8')
    stxt20 = utxt20.encode ('iso-8859-1') 
    pdf.multi_cell(0,5,stxt20, 0,'J')
    pdf.ln(2)
    
    nona = 'CLÁUSULA NONA:'
    utxt21 = unicode (nona, 'UTF-8')
    stxt21 = utxt21.encode ('iso-8859-1') 
    pdf.cell(33,5,stxt21, 1,1 , 'L')
    pdf.ln(1)
    
    clausulaNona = 'O foro deste contrato é da Comarca de, renunciando as partes quaisquer outro por mais privilegiado que seja.E por estarem assim  juntos e'
    clausulaNona += 'contra  assinam o presente em 03 (Três) vias de igual teor e forma, na presença das testemunhas abaixo.'
    utxt22 = unicode (clausulaNona, 'UTF-8')
    stxt22 = utxt22.encode ('iso-8859-1') 
    pdf.multi_cell(0,5,stxt22, 0,'J')
    pdf.ln(3)

    pdf.cell(0,10,'____________________________________________   _____ , _____ , _________', 0,1 , 'C')
    pdf.ln(10)

    pdf.cell(0,5,'PROMITENTE COMPRADOR:', 0,1 , 'C')
    pdf.cell(0,5,'__________________________________________________', 0,1 , 'C')
    pdf.cell(0,5,'PROMITENTE VENDEDOR:', 0,1 , 'C')
    pdf.cell(0,5,'__________________________________________________', 0,1 , 'C')
    pdf.cell(0,5,'TESTEMUNHA:', 0,1 , 'C')
    pdf.cell(0,5,'__________________________________________________', 0,1 , 'C')
    pdf.cell(0,5,'R.G.:', 0,1 , 'C')
    pdf.cell(0,5,'__________________________________________________', 0,1 , 'C')
    pdf.cell(0,5,'TESTEMUNHA:', 0,1 , 'C')
    pdf.cell(0,5,'__________________________________________________', 0,1 , 'C')
    pdf.cell(0,5,'R.G.:', 0,1 , 'C')
    pdf.cell(0,5,'__________________________________________________', 0,1 , 'C')

    pdf.output('numero%s.pdf'%(registro),'F')



