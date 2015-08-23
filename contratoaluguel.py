#!/usr/bin/env python
# -*- coding: utf-8 -*-
from fpdf import FPDF

def novoAluguel(nomelocador, nomelocatario, fiadorI, ecI, profI, rgI, cpfI, ruaI, numI, bairroI, cidadeI, ufI, conjugueI, rgconjugueI, cpfconjugueI, fiadorII, ecII, profII, rgII, cpfII, ruaII, numII, bairroII, cidadeII, ufII, conjugueII, rgconjugueII, cpfconjugueII ,registro,prazo, inicio, fim, valor, vencimento):
    pdf=FPDF()
    pdf=FPDF('P','mm','A4')
    pdf.set_margins(10, 10, 10)
    #Adicionando página
    pdf.add_page()
    #Adicionando configurações de Fonte
    pdf.set_font('Arial','B',16)
    #Inserindo linhas cell by cell.
    contrato = 'CONTRATO DE LOCAÇÃO RESIDENCIAL'
    utxt1 = unicode (contrato, 'UTF-8')
    stxt1 = utxt1.encode ('iso-8859-1')
    pdf.cell(0,10,stxt1, 1,1 , 'C')
    pdf.ln(10)

    pdf.set_font('Arial','B',8)

    locador = 'LOCADOR(A):'+nomelocador+''
    utxt2 = unicode (locador, 'UTF-8')
    stxt2 = utxt2.encode ('iso-8859-1') 
    pdf.multi_cell(0,5,stxt2, 0,'J')
    pdf.ln(1)

    locatario = 'LOCATÁRIO(A):'+nomelocatario+''
    utxt3 = unicode (locatario, 'UTF-8')
    stxt3 = utxt3.encode ('iso-8859-1') 
    pdf.multi_cell(0,5,stxt3, 0,'J')
    pdf.ln(1)
    
    pdf.set_font('Arial','',8)
    fiadoresI = 'FIADOR I: '+fiadorI+', brasileiro(a), '+ecI+', '+profI+', portador(a) do R.G. nº '+rgI+', e inscrito(a) no CPF/MF sob nº '+cpfI+', residente e'
    fiadoresI +=' domiciliado(a) à '+ruaI+', '+numI+', '+bairroI+', '+cidadeI+', '+ufI+', e conjugue '+conjugueI+', brasileiro(a), portador(a) do R.G. nº '+rgconjugueI+' e CPF/MF nº '+cpfconjugueI+''
    utxt4 = unicode (fiadoresI, 'UTF-8')
    stxt4 = utxt4.encode ('iso-8859-1') 
    pdf.multi_cell(0,5,stxt4, 0,'J')
    pdf.ln(1)

    fiadoresII = 'FIADOR II: '+fiadorII+', brasileiro(a), '+ecII+', '+profII+', portador(a) do R.G. nº '+rgII+', e inscrito(a) no CPF/MF sob nº '+cpfII+', residente e'
    fiadoresII +=' domiciliado(a) à '+ruaII+', '+numII+', '+bairroII+', '+cidadeII+', '+ufII+', e conjugue '+conjugueII+', brasileiro(a), portador(a) do R.G. nº '+rgconjugueII+' e CPF/MF nº '+cpfconjugueII+''
    utxt5 = unicode (fiadoresII, 'UTF-8')
    stxt5 = utxt5.encode ('iso-8859-1') 
    pdf.cell(33,5,stxt5, 1,1 , 'L')
    pdf.ln(5)

    pdf.set_font('Arial','B',8)
    objeto = 'O IMÓVEL SOB Nº '+registro+' com suas benfeitorias e instalações vontade,'
    objeto +='Por este particular instrumento, as partes supraqualificadas resolvem, de comum acordo e de livre e espontânea'
    objeto +='firmar um Contrato de Locação, tendo por objeto o imóvel declinado no preâmbulo, a reger-se pelas seguintes cláusulas e condições'
    utxt6 = unicode (objeto, 'UTF-8')
    stxt6 = utxt6.encode ('iso-8859-1') 
    pdf.multi_cell(0,5,stxt6, 0,'J')
    pdf.ln(3)

    pdf.set_font('Arial','',8)
    primeira = 'CLÁUSULA PRIMEIRA:'
    utxt7 = unicode (primeira, 'UTF-8')
    stxt7 = utxt7.encode ('iso-8859-1') 
    pdf.cell(33,5,stxt7, 1,1 , 'L')
    pdf.ln(1)
    
    clausulaPrimeira ='O prazo da locação é de '+prazo+', iniciando-se '+inicio+' e findando-se em '+fim+',quando e será considerada finda, independentemente ' 
    clausulaPrimeira +='de notificação judicial ou extrajudicial, obrigando-se o(a) LOCATÁRIO(A) a restituir o imóvel, completamente livre e desocupado.'
    utxt8 = unicode (clausulaPrimeira, 'UTF-8')
    stxt8 = utxt8.encode ('iso-8859-1') 
    pdf.multi_cell(0,5,stxt8, 0,'J')
    pdf.ln(3)
    
    segunda = 'CLÁUSULA SEGUNDA:'
    utxt9 = unicode (segunda, 'UTF-8')
    stxt9 = utxt9.encode ('iso-8859-1') 
    pdf.cell(33,5,stxt9, 1,1 , 'L')
    pdf.ln(1)
    
    clausulaSegunda = 'O aluguel convencionado é de R$ '+valor+' mensais, que deverão ser pagos até o dia '+vencimento+', do mês subseqüente ao vencimento,com depósito'
    clausulaSegunda += 'em conta corrente do Locador(a), com recibo, devendo, o(a) Locatário(a), fazer prova de quitação do mesmo, se for o caso, e das parcelas de I.P.T.U,' 
    clausulaSegunda += 'sob pena de não o fazendo, não considera-se integralmente pago o aluguel, ensejando ação de despejo por falta de pagamento.'
    utxt10 = unicode (clausulaSegunda, 'UTF-8')
    stxt10 = utxt10.encode ('iso-8859-1') 
    pdf.multi_cell(0,5,stxt10, 0,'J')
    pdf.ln(3)
    
    terceira = 'CLÁUSULA TERCEIRA:'
    utxt11 = unicode (terceira, 'UTF-8')
    stxt11 = utxt11.encode ('iso-8859-1') 
    pdf.cell(33,5,stxt11, 1,1 , 'L')
    pdf.ln(1)
    
    clausulaTerceira = 'A não observância do prazo estabelecido na cláusula segunda,implicará na incidência de multa diária de 1% sobre o valor ,do aluguel'
    clausulaTerceira += 'até o limite de 20%, acrescido de juros de mora de 10% ao mês além da correção monetária monetária.'
    utxt12 = unicode (clausulaTerceira, 'UTF-8')
    stxt12 = utxt12.encode ('iso-8859-1') 
    pdf.multi_cell(0,5,stxt12, 0,'J')
    pdf.ln(3)
    
    quarta = 'CLÁUSULA QUARTA:'
    utxt13 = unicode (quarta, 'UTF-8')
    stxt13 = utxt13.encode ('iso-8859-1') 
    pdf.cell(33,5,stxt13, 1,1 , 'L')
    pdf.ln(1)
    
    clausulaQuarta = 'O imóvel objeto deste instrumento é locado exclusivamente para servir de residência ao(à) LOCATÁRIO(A) e sua família,'
    clausulaQuarta +='não podendo sua destinação ser alterada, ou acrescida de qualquer outra, sem prévia e expressa anuência do(a) LOCADOR(A).'
    clausulaQuarta +='Fica vedado, outrossim, a sublocação, cessão ou transferência deste contrato, bem como o empréstimo,'
    clausulaQuarta +='parcial ou total do imóvel locado, que dependerão também, de prévia e expressa anuência do(a) LOCADOR(A).'
    utxt14 = unicode (clausulaQuarta, 'UTF-8')
    stxt14 = utxt14.encode ('iso-8859-1') 
    pdf.multi_cell(0,5,stxt14, 0,'J')
    pdf.ln(3)

    quinta = 'CLÁUSULA QUINTA:'
    utxt15 = unicode (quinta, 'UTF-8')
    stxt15 = utxt15.encode ('iso-8859-1') 
    pdf.cell(33,5,stxt15, 1,1 , 'L')
    pdf.ln(1)
    
    clausulaQuinta = '(1) O imóvel objeto deste, foi entregue ao(a) LOCATÁRIO(A)nas condições descritas no Termo de Vistoria, obrigando-se a devolvê-lo, uma vez '
    clausulaQuinta += 'finda a locação, nas mesmas condições em que o recebeu, razão pela qual, no momento da restituição das chaves, proceder-se-á a uma nova, vistoria.'
    dois = '(2) devidamente vistoriado pelo(a) LOCATÁRIO(A), que constatou encontrar-se em perfeitas condições de habitabilidade, com pintura nova, portas '
    dois += 'com fechaduras em funcionamento e munidas das correspondentes chaves,azulejos e porcelanas da cozinha e banheiro inteiros, aberturas com  '
    dois += 'ferragens em condições e vidros inteiros, instalação elétrica e hidráulica em condições, obrigando-se a devolvê-lo, uma vez finda a locação, '
    dois += 'nas mesmas condições em que o recebeu, razão pela qual, no momento da restituição das chaves, proceder-se-á a uma nova vistoria.'
    unico = 'ÚNICO: Constatadas eventuais irregularidades e a necessidade de reparos no imóvel em decorrência de uso indevido, fará o(a) LOCADOR(A) '
    unico += 'apresentar de imediato ao(à) LOCATÁRIO(A), um orçamento prévio assinado por profissional do ramo, sendo-lhe facultado pagar o valor nele declinado,'
    cont = 'liberando-se assim de eventuais ônus em razão de demora e/ou imperfeições nos serviços.Caso contrário, poderá contratar por sua própria'
    cont += 'conta e risco mão-de-obra especializada, arcando nessa condição com os riscos de eventuais imperfeições dos serviços e pelo pagamento do '
    cont1 = 'aluguel dos dias despendidos para a sua execução, cessando a locação unicamente com o Termo de Entrega de Chaves e Vistoria,  firmado pelo(a) LOCADOR(A)ou seu(sua) administrador(a)'
    utxt161 = unicode (clausulaQuinta, 'UTF-8')
    stxt161 = utxt161.encode ('iso-8859-1') 
    pdf.multi_cell(0,5,stxt161, 0,'J')
    utxt162 = unicode (dois, 'UTF-8')
    stxt162 = utxt162.encode ('iso-8859-1') 
    pdf.multi_cell(0,5,stxt162, 0,'J')
    utxt163 = unicode (unico, 'UTF-8')
    stxt163 = utxt163.encode ('iso-8859-1') 
    pdf.multi_cell(0,5,stxt163, 0,'J') 
    utxt164 = unicode (cont, 'UTF-8')
    stxt164 = utxt164.encode ('iso-8859-1') 
    pdf.multi_cell(0,5,stxt164, 0,'J')
    utxt165 = unicode (cont1, 'UTF-8')
    stxt165 = utxt165.encode ('iso-8859-1') 
    pdf.multi_cell(0,5,stxt165, 0,'J')
    pdf.ln(3)
    
    sexta = 'CLÁUSULA SEXTA:'
    utxt17 = unicode (sexta, 'UTF-8')
    stxt17 = utxt17.encode ('iso-8859-1') 
    pdf.cell(33,5,stxt17, 1,1 , 'L')
    pdf.ln(1)
    
    clausulaSexta = 'Obriga-se o(a) LOCATÁRIO(A) a manter o imóvel sempre limpo e bem cuidado na vigência da locação,, correndo por sua conta e risco,não só os pequenos'
    clausulaSexta += 'reparos tendentes a sua conservação, mas também as multas a que der causa, por inobservância de quaisquer leis, decretos e/ou regulamentos. '
    utxt18 = unicode (clausulaSexta, 'UTF-8')
    stxt18 = utxt18.encode ('iso-8859-1') 
    pdf.multi_cell(0,5,stxt18, 0,'J')
    pdf.ln(3)
    
    setima = 'CLÁUSULA SÉTIMA:'
    utxt19 = unicode (setima, 'UTF-8')
    stxt19 = utxt19.encode ('iso-8859-1') 
    pdf.cell(33,5,stxt19, 1,1 , 'L')
    pdf.ln(1)
    
    clausulaSetima ='O(A) LOCATÁRIO(A) não poderá fazer no imóvel ou em suas dependências, quaisquer obras ou benfeitorias, sem prévia e expressa anuência do(a) LOCADOR(A),'
    clausulaSetima += 'não lhe cabendo direito de retenção, por aquelas que, mesmo necessárias ou consentidas, venham a ser realizadas.'
    paragrafo = '§ ÚNICO: Caso não convenha ao(à) LOCADOR(A) a permanência de quaisquer obras ou benfeitorias benfeitorias realizadas pelo(a) LOCATÁRIO(A),'
    paragrafo += 'mesmo necessárias ou consentidas, deverá este(a), uma vez finda a locação, removê-las às suas expensas, de modo a devolver o imóvel nas mesmas condições em que o recebeu. '
    utxt20 = unicode (clausulaSetima, 'UTF-8')
    stxt20 = utxt20.encode ('iso-8859-1') 
    pdf.multi_cell(0,5,stxt20, 0,'J')
    utxt21 = unicode (paragrafo, 'UTF-8')
    stxt21 = utxt21.encode ('iso-8859-1') 
    pdf.multi_cell(0,5,stxt21, 0,'J')
    pdf.ln(3)
    
    oitava = 'CLÁUSULA OITAVA:'
    utxt22 = unicode (oitava, 'UTF-8')
    stxt22 = utxt22.encode ('iso-8859-1') 
    pdf.cell(33,5,stxt22, 1,1 , 'L')
    pdf.ln(1)
    
    clausulaOitava = 'Obriga-se desde já o(a) LOCATÁRIO(A), a respeitar os regulamentos e as leis vigentes, bem como o direito de vizinhança, evitando a prática de quaisquer atos que possam'
    clausulaOitava +=' perturbar a tranqüilidade ou ameaçar a saúde pública.'
    utxt23 = unicode (clausulaOitava, 'UTF-8')
    stxt23 = utxt23.encode ('iso-8859-1') 
    pdf.multi_cell(0,5,stxt23, 0,'J')
    pdf.ln(3)

    nona = 'CLÁUSULA NONA:'
    utxt24 = unicode (nona, 'UTF-8')
    stxt24 = utxt24.encode ('iso-8859-1') 
    pdf.cell(33,5,stxt24, 1,1 , 'L')
    pdf.ln(1)
    
    clausulaNona = 'Qualquer tolerância ou concessão, com o fito de resolver extrajudicialmente questão legal ou contratual, não se constituirá em precedente invocável pelo(a)'
    clausulaNona += ' LOCATÁRIO(A) e nem modificará quaisquer das condições estabelecidas neste instrumento. '
    utxt25 = unicode (clausulaNona, 'UTF-8')
    stxt25 = utxt25.encode ('iso-8859-1') 
    pdf.multi_cell(0,5,stxt25, 0,'J')
    pdf.ln(3)
    
    decima = 'CLÁUSULA DÉCIMA:'
    utxt26 = unicode (decima, 'UTF-8')
    stxt26 = utxt26.encode ('iso-8859-1') 
    pdf.cell(33,5,stxt26, 1,1 , 'L')
    pdf.ln(1)
    
    clausulaDecima = 'Em caso de morte, exoneração, falência ou insolvência de quaisquer dos fiadores, obriga-se o(a) LOCATÁRIO(A)num prazo de quinze (15) dias, contados,'
    clausulaDecima += ' da verificação do fato, a apresentar substituto idôneo ao(à) LOCADOR(A), à juízo deste(a) (apenas se a garantia for através de fiança).'
    utxt27 = unicode (clausulaDecima, 'UTF-8')
    stxt27 = utxt27.encode ('iso-8859-1') 
    pdf.multi_cell(0,5,stxt27, 0,'J')
    pdf.ln(3)

    decima1 = 'CLÁUSULA DÉCIMA PRIMEIRA:'
    utxt28 = unicode (decima1, 'UTF-8')
    stxt28 = utxt28.encode ('iso-8859-1') 
    pdf.cell(45,5,stxt28, 1,1 , 'L')
    pdf.ln(1)
    
    decimaPrimeira = 'Obriga-se o(a) LOCATÁRIO(A) a efetuar a ligação de energia elétrica em seu nome, providenciando no seu desligamento, por ocasião da devolução do '
    decimaPrimeira += 'imóvel, quando então deverá apresentar as últimas contas de seu consumo. '
    utxt29 = unicode (decimaPrimeira, 'UTF-8')
    stxt29 = utxt29.encode ('iso-8859-1') 
    pdf.multi_cell(0,5,stxt29, 0,'J')
    pdf.ln(3)

    decima2 = 'CLÁUSULA DÉCIMA SEGUNDA:'
    utxt30 = unicode (decima2, 'UTF-8')
    stxt30 = utxt30.encode ('iso-8859-1') 
    pdf.cell(45,5,stxt30, 1,1 , 'L')
    pdf.ln(1)
    
    decimaSegunda = 'A falta de cumprimento de qualquer cláusula ou condição deste instrumento, implicará na sua imediata rescisão, ficando a parte infratora , sujeita'
    decimaSegunda +='ao pagamento de uma multa, equivalente a três meses de aluguel, pelo valor vigente à época da infração, além de perdas e danos.'
    utxt31 = unicode (decimaSegunda, 'UTF-8')
    stxt31 = utxt31.encode ('iso-8859-1') 
    pdf.multi_cell(0,5,stxt31, 0,'J')
    pdf.ln(3)

    decima3 = 'CLÁUSULA DÉCIMA TERCEIRA:'
    utxt32 = unicode (decima3, 'UTF-8')
    stxt32 = utxt32.encode ('iso-8859-1') 
    pdf.cell(45,5,stxt32, 1,1 , 'L')
    pdf.ln(1)
    
    decimaTerceira = 'Sempre que as partes forem obrigadas a se valer de medidas judiciais para a defesa de direitos e obrigações decorrentes deste instrumento,'
    decimaTerceira +='o valor devido a título de honorários, será de 20% (vinte por cento) sobre o valor da causa, elegendo, desde já, o foro da cidade de (cidade)'
    decimaTerceira +='para a solução das questões dele emergentes.'
    utxt33 = unicode (decimaTerceira, 'UTF-8')
    stxt33 = utxt33.encode ('iso-8859-1') 
    pdf.multi_cell(0,5,stxt33, 0,'J')
    pdf.ln(3)

    pdf.cell(0,5,'_________________________________________________  _______ , _______ , __________', 0,1 , 'C')
    pdf.ln(10)
    pdf.cell(0,5,'__________________________________________________',0,1,'C')
    pdf.cell(0,5,'Locador(a)', 0,1, 'C')
    pdf.cell(0,5,'__________________________________________________', 0,1, 'C')
    pdf.cell(0,5,'Locatario(a)',0,1, 'C')
    pdf.cell(0,5,'__________________________________________________', 0,1, 'C')
    pdf.cell(0,5,'Fiador(a)', 0,1, 'C')
    pdf.cell(0,5,'__________________________________________________', 0,1, 'C')
    pdf.cell(0,5,'Fiador(a)', 0,1 , 'C')

    pdf.add_page()
    pdf.set_font('Arial','B',14)
    importante = 'OBSERVAÇÕES IMPORTANTES '
    utxtim = unicode (importante, 'UTF-8')
    stxtim = utxtim.encode ('iso-8859-1')
    pdf.cell(0,10,stxtim,1,1, 'C')
    pdf.ln(3)
    integrantes = 'INTEGRANTES DA MINUTA DE CONTRATO DE LOCAÇÃO RESIDENCIAL '
    utxtin = unicode (integrantes, 'UTF-8')
    stxtin = utxtin.encode ('iso-8859-1')
    pdf.cell(0,10,stxtin,0,1, 'C')
    pdf.ln(10)


    pdf.set_font('Arial', '', 8)
    
    obs1 = 'OBSERVAÇÃO(01)'
    utxt34 = unicode (obs1, 'UTF-8')
    stxt34 = utxt34.encode ('iso-8859-1') 
    pdf.cell(45,5,stxt34, 1,1 , 'L')
    pdf.ln(2)
    
    observacao1 = ' Muito embora o artigo 565, do novo Código Civil não tenha mais estabelecido o prazo mínimo de 30 meses previsto na legislação locatícia,'
    observacao1 += 'ainda não existe manifestação de nossos Tribunais sobre eventual revogação dessa regra. Como pela legislação locatícia, o prazo inferior a 30 meses implicava'
    observacao1 += 'na prorrogação automática do contratoe exigia para a retomada circunstâncias especiais ou o decurso de 5 anos, o aconselhável é ainda se utilizar esse prazo (30 meses).'
    utxt35 = unicode (observacao1, 'UTF-8')
    stxt35 = utxt35.encode ('iso-8859-1') 
    pdf.multi_cell(0,5,stxt35, 0,'J')
    pdf.ln(1)
    
    obs2 = 'OBSERVAÇÃO(02)'
    utxt36 = unicode (obs2, 'UTF-8')
    stxt36 = utxt36.encode ('iso-8859-1') 
    pdf.cell(45,5,stxt36, 1,1 , 'L')
    pdf.ln(2)
    
    observacao2 = ' Normalmente, no primeiro mês de locação ocorre a cobrança do aluguel,seja os dias ocupados decorridos desde o início da locação até o final do mês.'
    observacao2 +='seja, os dias ocupados decorridos desde o início da locação até o final do mês. Somente a partir do segundo mês é que é feita a cobrança do valor locatício integral.'
    utxt37 = unicode (observacao2, 'UTF-8')
    stxt37 = utxt37.encode ('iso-8859-1') 
    pdf.multi_cell(0,5,stxt37, 0,'J')
    pdf.ln(1)
    
    obs3 = 'OBSERVAÇÃO(03)'
    utxt38 = unicode (obs3, 'UTF-8')
    stxt38 = utxt38.encode ('iso-8859-1') 
    pdf.cell(45,5,stxt38, 1,1 , 'L')
    pdf.ln(2)
    
    observacao3 = ' O artigo 406, do novo Código Civil, aparentemente teria revogado de forma expressa o artigo 10, do Decreto 22.626/33, que estabelecia '
    observacao3 += ' vedação de juros superiores a 1% ao mês. Pelo citado artigo, eles poderiam ser convencionados acima desse limite. Como a lei não estabelece o limitemáximo,'
    observacao3 += '  a idéia lógica seria a de que o limite máximo ficaria ao arbítrio das partes. Só que esse entendimento, com toda certeza, será objeto de questionamento pelos Tribunais,'
    observacao3 += ' que no devido tempo, deverão estabelecer os percentuais máximos a serem aplicados.A única certeza, é de que o limite permitido é o das taxas da Fazenda Nacional. Por isso, recomenda-se prudência e coerência. '
    utxt39 = unicode (observacao3, 'UTF-8')
    stxt39 = utxt39.encode ('iso-8859-1') 
    pdf.multi_cell(0,5,stxt39, 0,'J')
    pdf.ln(1)
    
    obs4 = 'OBSERVAÇÃO(04)'
    utxt40 = unicode (obs4, 'UTF-8')
    stxt40 = utxt40.encode ('iso-8859-1') 
    pdf.cell(45,5,stxt40, 1,1 , 'L')
    pdf.ln(2)
    
    observacao4 = 'Nunca entregar para o(a) locatário(a) o carnê do IPTU e nunca permitir que as taxas condominiais sejam remetidas diretamente ao mesmo. Sempre cuidar para'
    observacao4 +=' que esses pagamentos sejam realizados pelo(a) administrador(a), pois é dele a responsabilidade pelo inadimplemento. Todos esses valores são normalmente cobrados '
    observacao4 +='juntamente com o aluguel.Não se descuidar da contratação de seguro-incêndio, pois se algum sinistro ocorrer no imóvel e este não tiver seguro, o(a) administrador(a) será responsável pelo prejuízo.'
    utxt41 = unicode (observacao4, 'UTF-8')
    stxt41 = utxt41.encode ('iso-8859-1') 
    pdf.multi_cell(0,5,stxt41, 0,'J')
    pdf.ln(1)
    
    obs5 = 'OBSERVAÇÃO(05)'
    utxt42 = unicode (obs5, 'UTF-8')
    stxt42 = utxt42.encode ('iso-8859-1') 
    pdf.cell(45,5,stxt42, 1,1 , 'L')
    pdf.ln(2)
    
    observacao5 = 'A fiança não permite interpretação extensiva. Desta forma, por exemplo, reajustes de alugueres acima dos índices pactuados, não terão validade para'
    observacao5 +=' os fiadores, se não anuírem de forma expressa com esses reajustes. Por isso, sempre que houver qualquer alteração não prevista no contrato, tomar'
    observacao5 +=' a providência de exigir a concordância dos fiadores. Nos termos do atual inciso X, do artigo 40, da Lei do Inquilinato alterada, uma vez prorrogado '
    observacao5 +='o contrato por prazo indeterminado, o fiador poderá se desonerar do encargo, por via de notificação ao locador, permanecendo responsável'
    observacao5 +='por todos os efeitos, pelo prazo de 120 dias, cabendo ao locador notificar o locatário para apresentar novo fiador no prazo de 30 dias, sob pena de despejo.'
    utxt43 = unicode (observacao5, 'UTF-8')
    stxt43 = utxt43.encode ('iso-8859-1') 
    pdf.multi_cell(0,5,stxt43, 0,'J')
    pdf.ln(1)

    obs6 = 'OBSERVAÇÃO(06)'
    utxt44 = unicode (obs6, 'UTF-8')
    stxt44 = utxt44.encode ('iso-8859-1') 
    pdf.cell(45,5,stxt44, 1,1 , 'L')
    pdf.ln(2)
    
    observacao6 = 'Cuidar para que a ligação de energia elétrica seja sempre realizada (ou transferida) para o nome do locatário, a fim de que a eventual cobrança e a '
    observacao6 += ' inclusão em cadastro de inadimplentes não seja feita em nome do(a) locador(a).'
    utxt45 = unicode (observacao6, 'UTF-8')
    stxt45 = utxt45.encode ('iso-8859-1') 
    pdf.multi_cell(0,5,stxt45, 0,'J')
    pdf.ln(1)

    obs7 = 'OBSERVAÇÃO(07)'
    utxt46 = unicode (obs7, 'UTF-8')
    stxt46 = utxt46.encode ('iso-8859-1') 
    pdf.cell(45,5,stxt46, 1,1 , 'L')
    pdf.ln(2)
    
    observacao7 = 'A multa indenizatória sempre será proporcional ao prazo restante do contrato.'
    utxt47 = unicode (observacao7, 'UTF-8')
    stxt47 = utxt47.encode ('iso-8859-1') 
    pdf.multi_cell(0,5,stxt47, 0,'J')
    pdf.ln(1)

    obs8 = 'OBSERVAÇÃO FINAL:'
    utxt48 = unicode (obs8, 'UTF-8')
    stxt48 = utxt48.encode ('iso-8859-1') 
    pdf.cell(45,5,stxt48, 1,1 , 'L')
    pdf.ln(2)
    
    observacao8 = 'A presente minuta é apenas uma sugestão, nela informadas as cláusulas básicas de um contrato de locação residencial,'
    observacao8 +=' às quais deverão ser adicionadas outras que vierem a ser necessárias, em face das características particulares de cada negócio.'
    utxt49 = unicode (observacao8, 'UTF-8')
    stxt49 = utxt49.encode ('iso-8859-1') 
    pdf.multi_cell(0,5,stxt49, 0,'J')
    pdf.ln(1)

    pdf.ln(10)
    pdf.cell(0,5,'__________________________________________________',0,1,'C')
    pdf.cell(0,5,'Locador(a)', 0,1, 'C')
    pdf.cell(0,5,'__________________________________________________', 0,1, 'C')
    pdf.cell(0,5,'Locatario(a)',0,1, 'C')
    pdf.cell(0,5,'__________________________________________________', 0,1, 'C')
    pdf.cell(0,5,'Fiador(a)', 0,1, 'C')
    pdf.cell(0,5,'__________________________________________________', 0,1, 'C')
    pdf.cell(0,5,'Fiador(a)', 0,1 , 'C')


    pdf.output('aluguel%s.pdf'%(registro),'F')


