# -*- coding: utf-8 -*-

from fpdf import FPDF

pdf=FPDF()
#Adicionando página
pdf.add_page()
#Adicionando configurações de Fonte
pdf.set_font('Arial','B',11)
#Inserindo linhas cell by cell.
pdf.cell(0,10,'CONTRATO DE LOCAÇÃO RESIDENCIAL', 0,1 , 'C')
pdf.set_font('Arial','',8)
pdf.cell(0,10,'(SUGESTÃO DE MINUTA BÁSICA)', 0,1 ,'C')
pdf.ln(10)
#Locador
pdf.set_font('Arial','I',9)
pdf.cell(0,5,'LOCADOR(A):	..................................., brasileiro, solteiro, comerciante,', 0,1 , 'J')
pdf.cell(0,5,'portador da cédula de identidade RG ....................../SSP.SP e inscrito no CPFMF sob nº ...................', 0,1 , 'J')
#Locatario
pdf.cell(0,5,'LOCATÁRIO(A): ................................................, brasileiro, casado, autônomo,', 0,1 , 'J')
pdf.cell(0,5,', portador da cédula de identidade RG .................SSP/SP e inscrito no CPFMF sob nº ................... ', 0,1 , 'J')
pdf.ln(5)
#Objeto
pdf.set_font('Arial','B',9)
pdf.cell(0,5,'OBJETO:', 0,1 , 'C')
pdf.set_font('Arial','',9)
pdf.cell(0,5,'A CASA SOB Nº ....., DA RUA ................................, ou A UNIDADE RESIDENCIAL SOB N ....., ', 0,1 ,'')
pdf.cell(0,5,'SITO NA RUA ............. N ..., na cidade de ..................., SP, com suas benfeitorias e instalações',0,1,'')
pdf.ln(5)
#--
pdf.set_font('Arial','I',8)
pdf.cell(0,5,'Por este particular instrumento, as partes supraqualificadas resolvem, de comum acordo e de livre e espontânea vontade,',0,1,'L')
pdf.cell(0,5,'firmar um Contrato de Locação, tendo por objeto o imóvel declinado no preâmbulo, a reger-se pelas seguintes cláusulas e condições',0,1,'L')
pdf.ln(1)
#Primeira
pdf.set_font('Arial','',8)
pdf.cell(33,5,'PRIMEIRA:',1,1 , 'L')
pdf.ln(1)
pdf.cell(0,5,'prazo da locação é de trinta (30) meses, iniciando-se no dia 00.....2003 e findando-se em 00.....2005,', 0,1, 'J')
pdf.cell(0,5,'quando então será considerada finda, independentemente de notificação judicial ou extrajudicial,', 0,1, 'J')
pdf.cell(0,5,' obrigando-se o(a) LOCATÁRIO(A) a restituir o imóvel, completamente livre e desocupado. (vide observação 01)', 0,1, 'J')
pdf.ln(1)
#Segunda
pdf.cell(33,5,'SEGUNDA:', 1,1, 'L')
pdf.ln(1)
pdf.cell(0,5,'O aluguel convencionado é de R$ ........ (....................... reais) mensais,',0,1,'J')
pdf.cell(0,5,'diretamente à .............(nome do(a) administrador(a)), estabelecido(a) na rua .........., ou a quem vier o(a) LOCADOR(A) a indicar,',0,1,'J')
pdf.cell(0,5,'sempre porém na cidade de ............... (a mesma do local de pagamento contratual). (vide observação 02)', 0,1, 'J')
pdf.ln(1)
#Terceira
pdf.cell(33,5,'TERCEIRA:', 1,1, 'L')
pdf.ln(1)
pdf.cell(0,5,'O valor do locativo mensal será anualmente reajustado, segundo os índices do .......(escolher um índice principal)', 0,1, 'J')
pdf.cell(0,5,'acumulados no período e, no caso de sua extinção, de forma alternativa e subsidiária, pelos do .......(declinar outros dois).', 0,1 , 'J')
pdf.ln(1)
#Quarta
pdf.cell(33,5,'QUARTA:', 1,1, 'L')
pdf.ln(1)
pdf.cell(0,5,'A não observância do prazo estabelecido na cláusula segunda,implicará na incidência de multa diária de 1% sobre o valor ,', 0,1 , 'J')
pdf.cell(0,5,' do aluguel até o limite de 20%, acrescido de juros de mora de ......... ao mês ou fração e atualização monetária. (vide observação 03 e 04)', 0,1 , 'J')
pdf.ln(1)
#Quinta
pdf.cell(33,5,'QUINTA:', 1,1, 'L')
pdf.ln(1)
pdf.cell(0,5,'Além do aluguel, obriga se o(a) LOCATÁRIO(A) a efetuar o pagamento dos seguintes encargos,:',0,1,'J')
pdf.cell(0,5,'que poderão ser exigidos juntamente com o aluguel', 0,1 , 'J')
pdf.cell(0,5,'a.	o imposto predial e territorial;',0,1,'J')
pdf.cell(0,5,'b.	o consumo de água e energia elétrica;',0,1,'J')
pdf.cell(0,5,'c. o prêmio de seguro contra incêndio, que deverá ser feito pelo valor venal do imóvel, nele figurando o(a) LOCADOR(A) como beneficiário(a);',0,1,'J')
pdf.cell(0,5,'d.	as taxas de condomínio, se houverem;',0,1,'J')
pdf.cell(0,5,'e.	os demais encargos e tributos que normalmente incidem ou venham a incidir sobre o imóvel. (vide observação 05) ',0,1,'J')
pdf.cell(0,5,'ÚNICO:	O não pagamento desses encargos nas épocas próprias, facultará ao(a) LOCADOR(A) a justa recusa ao recebimento dos alugueres,',0,1,'J')
pdf.cell(0,5,'sujeitando-se o(a) LOCATÁRIO(A) ao pagamento dos ônus decorrentes do inadimplemento,',0,1,'J')
pdf.cell(0,5,', previstos para cada débito, independentemente de eventual ação de despejo. ',0,1,'J')
pdf.ln(1)
#Sexta
pdf.cell(33,5,'SEXTA:', 1,1, 'L')
pdf.ln(1)
pdf.cell(0,5,'O imóvel objeto deste instrumento é locado exclusivamente para servir de residência ao(à) LOCATÁRIO(A) e sua família,',0,1,'J')
pdf.cell(0,5,' não podendo sua destinação ser alterada, ou acrescida de qualquer outra, sem prévia e expressa anuência do(a) LOCADOR(A).',0,1,'J')
pdf.cell(0,5,'Fica vedado, outrossim, a sublocação, cessão ou transferência deste contrato, bem como o empréstimo,', 0,1 , 'J')
pdf.cell(0,5,'parcial ou total do imóvel locado, que dependerão também, de prévia e expressa anuência do(a) LOCADOR(A).', 0,1 , 'J')
pdf.ln(1)
#Setima
pdf.cell(33,5,'SÉTIMA:', 1,1, 'L')
pdf.ln(1)
pdf.cell(0,5,'O imóvel objeto deste, foi ......(vide observação 06)...(1) - entregue ao(a) LOCATÁRIO(A)', 0,1 , 'J')
pdf.cell(0,5,' nas condições descritas no “Termo de Vistoria” devidamente assinado pelas partes, integrando o presente,', 0,1 ,'J')
pdf.cell(0,5,', obrigando-se a devolvê-lo, uma vez finda a locação, nas mesmas condições em que o recebeu,', 0,1 , 'J')
pdf.cell(0,5,'razão pela qual, no momento da restituição das chaves, proceder-se-á a uma nova vistoria.', 0,1 , 'J')
pdf.cell(0,5,'..(2) - devidamente vistoriado pelo(a) LOCATÁRIO(A), que constatou encontrar-se em perfeitas condições de habitabilidade, ', 0,1 , 'J')
pdf.cell(0,5,'com pintura nova, portas com fechaduras em funcionamento e munidas das correspondentes chaves,', 0,1 , 'J')
pdf.cell(0,5,'azulejos e porcelanas da cozinha e banheiro inteiros, aberturas com ferragens em condições e vidros inteiros, ', 0,1 , 'J')
pdf.cell(0,5,'instalação elétrica e hidráulica em condições, obrigando-se a devolvê-lo, uma vez finda a locação, nas mesmas condições em que o recebeu, ', 0,1 , 'J')
pdf.cell(0,5,', razão pela qual, no momento da restituição das chaves, proceder-se-á a uma nova vistoria.', 0,1 , '')
pdf.cell(0,5,'ÚNICO: Constatadas eventuais irregularidades e a necessidade de reparos no imóvel em decorrência de uso indevido,', 0,1 , '')
pdf.cell(0,5,'fará o(a) LOCADOR(A) apresentar de imediato ao(à) LOCATÁRIO(A), um orçamento prévio assinado por profissional do ramo,', 0,1 , '')
pdf.cell(0,5,', sendo-lhe facultado pagar o valor nele declinado, liberando-se assim de eventuais ônus em razão de demora e/ou imperfeições nos serviços.', 0,1 , 'J')
pdf.cell(0,5,'Caso contrário, poderá contratar por sua própria conta e risco mão-de-obra especializada, ', 0,1 , 'J')
pdf.cell(0,5,'arcando nessa condição com os riscos de eventuais imperfeições dos serviços e pelo pagamento do aluguel dos dias despendidos para a sua execução,', 0,1 , 'J')
pdf.cell(0,5,'cessando a locação unicamente com o “Termo de Entrega de Chaves e Vistoria”, firmado pelo(a) LOCADOR(A) ou seu(sua) administrador(a).', 0,1 , 'J')
pdf.ln(1)
#Oitava
pdf.cell(33,5,'OITAVA:', 1,1, 'L')
pdf.ln(1)
pdf.cell(0,5,'Obriga-se o(a) LOCATÁRIO(A) a manter o imóvel sempre limpo e bem cuidado na vigência da locação,', 0,1 , 'J')
pdf.cell(0,5,', correndo por sua conta e risco, não só os pequenos reparos tendentes a sua conservação, mas também as multas a que der causa, ', 0,1 , 'J')
pdf.cell(0,5,', por inobservância de quaisquer leis, decretos e/ou regulamentos.', 0,1 , 'J')
pdf.ln(1)
#Nona
pdf.cell(33,5,'NONA:', 1,1, 'L')
pdf.ln(1)
pdf.cell(0,5,'O(A) LOCATÁRIO(A) não poderá fazer no imóvel ou em suas dependências, ', 0,1 , 'J')
pdf.cell(0,5,'quaisquer obras ou benfeitorias, sem prévia e expressa anuência do(a) LOCADOR(A),', 0,1 , 'J')
pdf.cell(0,5,'não lhe cabendo direito de retenção, por aquelas que, mesmo necessárias ou consentidas, venham a ser realizadas.', 0,1 , 'J')
pdf.cell(0,5,'§ ÚNICO: Caso não convenha ao(à) LOCADOR(A) a permanência de quaisquer obras ou benfeitorias', 0,1 , 'J')
pdf.cell(0,5,'benfeitorias realizadas pelo(a) LOCATÁRIO(A), mesmo necessárias ou consentidas, deverá este(a), ', 0,1 , 'J')
pdf.cell(0,5,'uma vez finda a locação, removê-las às suas expensas, de modo a devolver o imóvel nas mesmas condições em que o recebeu. ', 0,1 , 'J')
pdf.ln(1)
#Decima
pdf.cell(33,5,'DÉCIMA:', 1,1, 'L')
pdf.ln(1)
pdf.cell(0,5,'Obriga-se desde já o(a) LOCATÁRIO(A), a respeitar os regulamentos e as leis vigentes,', 0,1 , 'J')
pdf.cell(0,5,'bem como o direito de vizinhança, evitando a prática de quaisquer atos que possam perturbar a tranqüilidade ou ameaçar a saúde pública.', 0,1 , 'J')
pdf.ln(1)
#Decima-Primeira
pdf.cell(33,5,'DÉCIMA-PRIMEIRA:', 1,1, 'L')
pdf.ln(1)
pdf.cell(0,5,'Como fiadores e principais pagadores de todas as obrigações que incumbem ao(a) LOCATÁRIO(A),', 0,1 , 'J')
pdf.cell(0,5,'por força de lei ou do presente contrato e até a efetiva desocupação do imóvel, nas condições previstas pela cláusula sétima deste, ', 0,1 , 'J')
pdf.cell(0,5,'assinam ..................... e sua mulher ........................., ele servidor público, portador da cédula de identidade RG ......./SSP.SP', 0,1 , 'J')
pdf.cell(0,5,'e inscrito no CPFMF sob nº .................. e ela do lar, portadora da cédula de identidade RG ................./SSP.SP ', 0,1 , 'J')
pdf.cell(0,5,'e inscrita no CPFMF sob nº ......................., ambos brasileiros, casados pelo regime da comunhão universal de bens,', 0,1 , 'J')
pdf.cell(0,5,'antes da vigência da Lei 6.515/77, residentes e domiciliados na rua ................................ nº ....., na cidade de ..................,', 0,1 , 'J')
pdf.cell(0,5,'que neste ato renunciam ao benefício de ordem, estabelecido pelo artigo 827, do Código Civil. (vide observação 07)', 0,1 , 'J')
pdf.cell(0,5,' ÚNICO: Fica convencionado que os fiadores supramencionados não se eximirão da obrigação ora assumida', 0,1, 'J')
pdf.cell(0,5,', caso a locação, seja por força de lei, de contrato ou por ajuste feito entre LOCADOR(A) e LOCATÁRIO(A), ', 0,1, 'J')
pdf.cell(0,5,'se prorrogue por prazo superior ao convencionado. (vide observação 08)', 0,1, '')
pdf.ln(1)
#Decima-Segunda
pdf.cell(33,5,'DÉCIMA-SEGUNDA:', 1,1, 'L')
pdf.ln(1)
pdf.cell(0,5,'	Qualquer tolerância ou concessão, com o fito de resolver extrajudicialmente questão legal ou contratual,', 0,1, 'J')
pdf.cell(0,5,'não se constituirá em precedente invocável pelo(a) LOCATÁRIO(A) e nem modificará quaisquer das condições estabelecidas neste instrumento. ', 0,1, 'J')
pdf.ln(1)
#Decima-Terceira
pdf.cell(33,5,'DÉCIMA-TERCEIRA:', 1,1, 'L')
pdf.ln(1)
pdf.cell(0,5,'Em caso de morte, exoneração, falência ou insolvência de quaisquer dos fiadores, obriga-se o(a) LOCATÁRIO(A),', 0,1, 'J')
pdf.cell(0,5,'num prazo de quinze (15) dias, contados da verificação do fato, a apresentar substituto idôneo ao(à) LOCADOR(A), ', 0,1, 'J')
pdf.cell(0,5,'à juízo deste(a) (apenas se a garantia for através de fiança). ', 0,1, '')
pdf.ln(1)
#Decima-Quarta
pdf.cell(33,5,'DÉCIMA-QUARTA:', 1,1, 'L')
pdf.ln(1)
pdf.cell(0,5,'Obriga-se o(a) LOCATÁRIO(A) a efetuar a ligação de energia elétrica em seu nome, providenciando no seu desligamento,', 0,1, 'J')
pdf.cell(0,5,'por ocasião da devolução do imóvel, quando então deverá apresentar as últimas contas de seu consumo. (vide observação 09)', 0,1, 'J')
pdf.ln(1)
#Decima-Quinta
pdf.cell(33,5,'DÉCIMA-QUINTA:', 1,1, 'L')
pdf.ln(1)
pdf.cell(0,5,'A falta de cumprimento de qualquer cláusula ou condição deste instrumento, implicará na sua imediata rescisão,', 0,1, 'J')
pdf.cell(0,5,'ficando a parte infratora, sujeita ao pagamento de uma multa, equivalente a três meses de aluguel, ', 0,1, 'J')
pdf.cell(0,5,'pelo valor vigente à época da infração, além de perdas e danos.  (vide observação 10)', 0,1, 'J')
pdf.ln(1)
#Decima-Sexta
pdf.cell(33,5,'DÉCIMA-SEXTA:', 1,1, 'L')
pdf.ln(1)
pdf.cell(0,5,'Sempre que as partes forem obrigadas a se valer de medidas judiciais para a defesa de direitos e obrigações ', 0,1, 'J')
pdf.cell(0,5,'decorrentes deste instrumento, o valor devido a título de honorários, será de 20% (vinte por cento) sobre o valor da causa, ', 0,1, 'J')
pdf.cell(0,5,'elegendo, desde já, o foro da cidade de ....... (o mesmo da situação do imóvel), para a solução das questões dele emergentes.', 0,1, 'J')
pdf.ln(1)
#Inicio-Obs
pdf.set_font('Arial','I',8)
pdf.cell(0,10,'E por estarem assim justas e contratadas, assinam o presente, em três (03) vias, de igual teor e forma, na presença das testemunhas retro, ', 0,1, 'J')
pdf.cell(0,10,'para que surta seus legais e jurídicos efeitos, obrigando-se por si, seus herdeiros e/ou sucessores,', 0,1, 'J')
pdf.cell(0,10,'ao fiel cumprimento de todas as suas cláusulas e condições.', 0,1 , 'J')
pdf.ln(10)
#Locadores
pdf.set_font('Arial', '', 9)
pdf.cell(0,5,'_____ , _____ , _________', 0,1 , 'C')
pdf.ln(10)
pdf.cell(0,5,'__________________________________________________',0,1,'J')
pdf.cell(0,5,'                    Locador(a)                   ', 0,1, 'J')
pdf.cell(0,5,'__________________________________________________', 0,1, 'J')
pdf.cell(0,5,'                    Locatário(a)                  ',0,1, 'J')
pdf.cell(0,5,'__________________________________________________', 0,1, 'J')
pdf.cell(0,5,'                      Fiador                   ', 0,1, 'J')
pdf.cell(0,5,'__________________________________________________', 0,1, 'J')
pdf.cell(0,5,'                     Fiadora                    ', 0,1 , 'J')
pdf.cell(0,5,'TESTEMUNHAS',0,1,'')
pdf.cell(0,5,'__________________________________________________', 0,1, 'J')
pdf.cell(0,5,'__________________________________________________', 0,1, 'J')
#Observacoes
pdf.set_font('Arial', 'B' , 7)
pdf.cell(0,5,'OBSERVAÇÕES IMPORTANTES',1,1, 'C')
pdf.cell(0,5,'INTEGRANTES DA MINUTA DE CONTRATO DE LOCAÇÃO RESIDENCIAL ',1,1,'C')
pdf.ln(1)
#Observacao01
pdf.set_font('Arial', 'I', 6)
pdf.cell(0,5,'Observação 01: Muito embora o artigo 565, do novo Código Civil não tenha mais estabelecido o prazo mínimo de 30 meses ',0,1,'J')
pdf.cell(0,5,'previsto na legislação locatícia, ainda não existe manifestação de nossos Tribunais sobre eventual revogação dessa regra. ',0,1,'J')
pdf.cell(0,5,'Como pela legislação locatícia, o prazo inferior a 30 meses implicava na prorrogação automática do contrato',0,1,'')
pdf.cell(0,5,'e exigia para a retomada circunstâncias especiais ou o decurso de 5 anos, o aconselhável é ainda se utilizar esse prazo (30 meses). ',0,1,'J')
pdf.ln(1)
#Observacao02
pdf.cell(0,5,'Observação 02: Normalmente, no primeiro mês de locação ocorre a cobrança do aluguel “pro-rata”,',0,1,'J')
pdf.cell(0,5,'seja, os dias ocupados decorridos desde o início da locação até o final do mês.',0,1,'J')
pdf.cell(0,5,'Somente a partir do segundo mês é que é feita a cobrança do valor locatício integral. ',0,1,'J')
pdf.ln(1)
#Observacao03
pdf.cell(0,5,'Observação 03: Muitos administradores criam aquilo que se chama de “abono de pontualidade”, ',0,1,'J')
pdf.cell(0,5,'reduzindo o valor do aluguel em determinado percentual, caso seja pago até a data do vencimento. ',0,1,'J')
pdf.cell(0,5,'Essa prática é reconhecida pelos Tribunais como mora disfarçada e muitos a consideram ilegal, não ',0,1,'J')
pdf.cell(0,5,'podendo jamais ser cumulada com multa de mora. O mais salutar é convencionar o valor real do ',0,1,'J')
pdf.cell(0,5,'aluguel e fazer incidir uma mora diária no caso de inadimplemento, até o limite de 20% (máximo ',0,1,'J')
pdf.cell(0,5,'permitido pelos Tribunais). Ao contrário da multa integral desde o primeiro dia de atraso, a multa ',0,1,'J')
pdf.cell(0,5,'escalonada estimula o locatário a resgatar o débito, mesmo após o primeiro dia de vencimento, ',0,1,'J')
pdf.cell(0,5,' pois ela é progressiva até o vigésimo dia de atraso.',0,1,'J')
pdf.ln(1)
#Observacao04
pdf.cell(0,5,'Observação 04: O artigo 406, do novo Código Civil, aparentemente teria revogado de forma expressa o artigo 1, do Decreto 22.626/33, ',0,1,'J')
pdf.cell(0,5,'que estabelecia vedação de juros superiores a 1% ao mês. Pelo citado artigo, eles poderiam ser convencionados acima desse limite.',0,1,'J')
pdf.cell(0,5,'Como a lei não estabelece o limite máximo, a idéia lógica seria a de que o limite máximo ficaria ao arbítrio das partes. ',0,1,'J')
pdf.cell(0,5,'Só que esse entendimento, com toda certeza, será objeto de questionamento pelos Tribunais, que no devido tempo,',0,1,'J')
pdf.cell(0,5,' deverão estabelecer os percentuais máximos a serem aplicados. ',0,1,'')
pdf.cell(0,5,'A única certeza, é de que o limite permitido é o das taxas da Fazenda Nacional (taxa SELIC). Por isso, recomenda-se prudência e coerência.',0,1,'J')
pdf.ln(1)
#Observacao05
pdf.cell(0,5,'Observação 05: Nunca entregar para o(a) locatário(a) o carnê do IPTU e nunca permitir que .',0,1,'J')
pdf.cell(0,5,'as taxas condominiais sejam remetidas diretamente ao mesmo',0,1,'J')
pdf.cell(0,5,'Sempre cuidar para que esses pagamentos sejam realizados pelo(a) administrador(a),',0,1,'J')
pdf.cell(0,5,'pois é dele a responsabilidade pelo inadimplemento. Todos esses valores são normalmente cobrados juntamente com o aluguel.',0,1,'J')
pdf.cell(0,5,'Não se descuidar da contratação de seguro-incêndio,',0,1,'')
pdf.cell(0,5,'pois se algum sinistro ocorrer no imóvel e este não tiver seguro, o(a) administrador(a) será responsável pelo prejuízo.  ',0,1,'J')
pdf.ln(1)
#Observacao06
pdf.cell(0,5,'Observação 06:  Duas opções são informadas. A mais correta é a primeira, com a realização de vistoria, através de termo,',0,1,'J')
pdf.cell(0,5,'sendo uma dias vias entregue ao locatário, com o seguinte texto, transcrito em destaque,',0,1,'J')
pdf.cell(0,5,' após os dados da vistoria e no canto direito do formulário: ',0,1,'J')
pdf.set_font('Arial','', 7)
pdf.cell(0,5,'“Recebi a primeira via deste, ciente de que disponho do prazo de quarenta e oito (48) ',0,1,'J')
pdf.cell(0,5,'horas para encaminhar ao(à) administrador(a) reclamação escrita de qualquer ',0,1,'J')
pdf.cell(0,5,'anormalidade encontrada no imóvel, ou de condições que estejam em desacordo com os ',0,1,'J')
pdf.cell(0,5,'termos da presente vistoria, ciente também de que meu silêncio, fará presumir o aceite ',0,1,'J')
pdf.cell(0,5,'das condições aqui mencionadas.',0,1,'')
pdf.cell(0,5,'.............., .... de ................... de ...........',0,1,'J')
pdf.cell(0,5,'Locatário',0,1,'C')
pdf.ln(1)
#Observacao07
pdf.set_font('Arial', 'I', 7)
pdf.cell(0,5,'Observação 07: (a) A garantia locatícia é um dos maiores problemas do contrato. Existem três tipos: ',0,1,'J')
pdf.cell(0,5,'caução, fiança e seguro-fiança, só podendo ser exigida uma delas. A caução, normalmente em ',0,1,'J')
pdf.cell(0,5,'dinheiro e equivalente a três meses de aluguel, não deve ser entregue ao(a) locador(a), mas sim ',0,1,'J')
pdf.cell(0,5,'depositada em conta poupança de instituição oficial, aberta em nome do(a) administrador(a), onde ',0,1,'J')
pdf.cell(0,5,'deverá permanecer até a rescisão do contrato, oportunidade em que deverá ser devolvida ao(à) ',0,1,'J')
pdf.cell(0,5,'locatário(a), com os acréscimos percebidos. Como os débitos de inadimplência e reparos costumam ',0,1,'J')
pdf.cell(0,5,'ser muito superiores a três meses de aluguel, não se recomenda esse tipo de garantia. (b) A caução ',0,1,'J')
pdf.cell(0,5,'imobiliária (que deve ser objeto de  averbação à margem da matrícula do imóvel, a vista de escritura ',0,1,'J')
pdf.cell(0,5,'pública específica de caução ou do próprio contrato elaborado com as formalidades legais) pode ser ',0,1,'J')
pdf.cell(0,5,'utilizada com segurança, pois o imóvel permanecerá como garantia até o final do prazo ajustado e ',0,1,'J')
pdf.cell(0,5,'como se encontra registrada no Ofício Predial, mesmo no caso de sua alienação a terceiros, ',0,1,'J')
pdf.cell(0,5,'permanecerá intacta. (c) O seguro-fiança é boa garantia. Entretanto, como depende do pagamento do ',0,1,'J')
pdf.cell(0,5,'prêmio, o(a) administrador(a) corre o risco de ser obrigado(a) a arcar com o seu pagamento, caso ',0,1,'J')
pdf.cell(0,5,'o(a) locatário(a) não venha a fazê-lo, sob pena de ser responsabilizado pelos prejuízos. Deve, pois, o ',0,1,'J')
pdf.cell(0,5,'administrador estar atento para o pagamento pontual do prêmio. (d) A fiança envolve valores que ',0,1,'J')
pdf.cell(0,5,'asseguram indenização integral no caso de inadimplemento e ressarcimento dos reparos. Cuidados ',0,1,'J')
pdf.cell(0,5,'se fazem necessários na completa busca dos dados cadastrais e antecedentes dos fiadores, que ',0,1,'J')
pdf.cell(0,5,'necessariamente deverão residir e ser proprietários exclusivos de, pelo menos um imóvel além ',0,1,'J')
pdf.cell(0,5,'daquele onde residem (precavendo-se assim dos efeitos da decisão do STF nos autos do RE 352940, ',0,1,'J')
pdf.cell(0,5,'que entendeu ser impenhorável o imóvel onde reside o fiador), no mesmo local de situação do imóvel ',0,1,'J')
pdf.cell(0,5,'locado, para evitar dificuldades processuais no caso de execução, ',0,1,'J')
pdf.cell(0,5,' cuidando para que não seja um terreno sem valor comercial.',0,1,'J')
pdf.ln(1)
#Observacao08
pdf.cell(0,5,'Observação 08: A fiança não permite interpretação extensiva. Desta forma, por exemplo, reajustes ',0,1,'J')
pdf.cell(0,5,'de alugueres acima dos índices pactuados, não terão validade para os fiadores, se não anuírem de ',0,1,'J')
pdf.cell(0,5,'forma expressa com esses reajustes. Por isso, sempre que houver qualquer alteração não prevista no ',0,1,'J')
pdf.cell(0,5,'contrato, tomar a providência de exigir a concordância dos fiadores. Nos termos do atual inciso X, do ',0,1,'J')
pdf.cell(0,5,'artigo 40, da Lei do Inquilinato alterada, uma vez prorrogado o contrato por prazo indeterminado, o ',0,1,'J')
pdf.cell(0,5,'fiador poderá se desonerar do encargo, por via de notificação ao locador, permanecendo responsável ',0,1,'J')
pdf.cell(0,5,'por todos os efeitos, pelo prazo de 120 dias, cabendo ao locador notificar o locatário para apresentar ',0,1,'J')
pdf.cell(0,5,'novo fiador no prazo de 30 dias, sob pena de despejo. ',0,1,'J')
pdf.ln(1)
#Observacao09
pdf.cell(0,5,'Observação 09: Cuidar para que a ligação de energia elétrica seja sempre realizada (ou transferida) ',0,1,'J')
pdf.cell(0,5,'para o nome do locatário, a fim de que a eventual cobrança e a inclusão em cadastro de ',0,1,'J')
pdf.cell(0,5,'inadimplentes não seja feita em nome do(a) locador(a). ',0,1,'J')
pdf.ln(1)
#Observacao10
pdf.cell(0,5,'Observação 10: A multa indenizatória sempre será proporcional ao prazo restante do contrato. ',0,1,'J')
pdf.ln(1)
#ObservacaoFinal
pdf.set_font('Arial', 'B', 7)
pdf.cell(0,5,'OBSERVAÇÃO FINAL: A presente minuta é apenas uma sugestão, nela informadas as ',0,1,'J')
pdf.cell(0,5,'cláusulas básicas de um contrato de locação residencial, às quais deverão ser adicionadas ',0,1,'J')
pdf.cell(0,5,'outras que vierem a ser necessárias, em face das características particulares de cada negócio. ',0,1,'J')

pdf.output('Locar.pdf','F')
pdf=FPDF('P','mm','A4')
