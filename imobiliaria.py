#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
# MOB SYSTEM
# Ferramentas do Ambiente de Desenvolvimento:
# - Interface: pyGtk
# - Banco de Dados: Postgree SQL
# - Construtor de interface XML: Glade
# - Sistema Operacional: Windows 7/8 - 32/64 bits
#  


#Importando as bibliotecas que serão utilizadas
import pygtk
pygtk.require('2.0')
import gtk
import gtk.glade 
import psycopg2
from datetime import date
from fpdf import FPDF
#importando os arquivos .py para formatação de PDFs.
import contratovenda
import ATUALIZARVENDA
import contratoaluguel
import atualizaraluguel

# URL de conexão com o banco de dados
connection = psycopg2.connect('host=localhost user=postgres password=1234 dbname= imobsystem')
# Faz a transação entre o banco de dados e o código do Python
cursor = connection.cursor()

# Faz a validação do login para Funcionario e Administrador do sistema
class Login(object):
    #Método contrutor da classe.
    def __init__ (self):
        #Carrega o arquivo XML do Glade.
        self.xml = gtk.glade.XML('ImobSystem.glade')
        #Carrega os widgets da janela login
        self.window = self.xml.get_widget('Login')
        self.login = self.xml.get_widget("entryLogin")
        self.password = self.xml.get_widget("entryPassword")
        self.statusbar = self.xml.get_widget("statusbarLogin")
        self.context = self.statusbar.get_context_id("")    
        
        #Criando um Dicionario para conectar os sinais dos botões.
        dic = {"on_Login_destroy" : self.cancel,
	      "on_btnLogin_clicked" : self.loginValidate,
              "on_btnCancel_clicked" : self.cancel,
               }
        
        #Conecta os sinais do dicionário à janela login. 
        self.xml.signal_autoconnect(dic)
        #Torna visÍveis os widgets da janela Login.
        self.window.show_all()
       
    def loginValidate(self ,widget):
        #Faz uma seleção no banco de dados na tabela de login, cria um contador para saber o numero de linhas de cada coluna.
        cursor.execute("SELECT * FROM login WHERE login='"+self.login.get_text()+"'")
        result = cursor.fetchall()
        existUser = cursor.rowcount
        #atribue numero de erro a variável correspondente a cada erro para a validação do login.
        self.error = 1
        if(self.login.get_text() == ""):
            self.error = 2
        elif(existUser < 1):
            self.error = 3
        #Realiza uma iteração nas colunas do banco de dados
        for row in result:
            user = row[1]
            password = row[2]
            function = str(row[3])
            #Se a senha não corresponder ao usuario salvo no banco de dados.
            if(self.login.get_text() == user) and (self.password.get_text() != password):
                self.error = 4
            #se a senha corresponder aos usuario e corresponder a função Funcionario, fechar a página de login e abrir a pagina Funcionario. 
            elif(self.login.get_text() == user) and (self.password.get_text() == password) and (function == "Funcionario"):
                self.window.hide()
                Office()
            else:
                # se o login corresponder com a senha e função, fecha a página de login, abre pagina Administrador.
                self.window.hide() 
                Manager()
        #Chama as mensagens de erro do statusbar
        self.statusBar()
        
    def statusBar(self):
        #Define as mensagens de erros que aparecerão na statusbar para o numero correspondente ao erro.
        if(self.error == 2):
            self.statusbar.push(self.context, "Preencha o campo Longin!")   
        elif(self.error == 3):
            self.statusbar.push(self.context, " Usuario invalido!")   
        elif(self.error == 4):
            self.statusbar.push(self.context, "Senha invalida!")

    def cancel(self, widget):
        #Fecha a janela Loign
        self.window.hide()
    
class Office(object):
    def __init__(self):
        #Carrega o arquivo XML do glade.
        self.xml = gtk.glade.XML('ImobSystem.glade')
        #carregar a janela Funcionário.
        self.windowOffice = self.xml.get_widget('Office')
        #Carregando os widgets da janela Funcionário
        self.officeStatusbar = self.xml.get_widget("statusbarOffice")
        self.context = self.officeStatusbar.get_context_id("")
        self.officeStatusbar.push(self.context, "Funcionario")
        self.categoria = self.xml.get_widget("entrycategoria")
        self.nome = self.xml.get_widget("entryname")
        self.cpf = self.xml.get_widget("entrycpf")
        self.rg = self.xml.get_widget("entryrg")
        self.orgaoEmissor = self.xml.get_widget("entryOrgao")
        self.naturalidade = self.xml.get_widget("entryNaturalidade")
        self.dataNascimento = self.xml.get_widget("entryDtnascimento")
        self.nomeMae = self.xml.get_widget("entrymae")
        self.nomePai = self.xml.get_widget("entrypai")
        self.estadoCivil = self.xml.get_widget("entryEstadocivil")
        self.regimeCasamento = self.xml.get_widget("entryRegimeCasamento")
        self.telefone = self.xml.get_widget("entryTelefoneResidencial")
        self.celular = self.xml.get_widget("entryCelular")
        self.email = self.xml.get_widget("entryEmail")
        self.endereco = self.xml.get_widget("entryEndereco")
        self.profissao = self.xml.get_widget("entryProfissao")
        self.empresa = self.xml.get_widget("entryEmpresa")
        self.cargo = self.xml.get_widget("entryCargo")
        self.enderecoEmpresa = self.xml.get_widget("entryEnderecoEmpresa")
        self.telefoneEmpresa = self.xml.get_widget("entryTelefoneEmpresa")
        self.emailFuncional = self.xml.get_widget("entryEmailFuncional")
        self.pesquisarImv = self.xml.get_widget("entryPesquisarImv")
        self.pesquisarCli = self.xml.get_widget("entryPesquisarCli")
        
        #Criando dicionário para conectar os sinais dos botões.
        dic = {"on_buttonSalvar_clicked" : self.ValidarCliente,
               "on_buttonCancel_destroy" : self.CancelSystem,
               "on_buttonCancel_clicked" : self.CancelSystem,
               "on_btnPesquisar_clicked" : self.PesqImovel,
               "on_btnPesquisarCli_clicked" : self.PesqCliente,
               "on_btnEditar_clicked" : self.Seleciona_Cliente,
               "on_btnExcluir_clicked" : self.DeletarCliente,   
            }

        #Define o Modelo do TreeView
        self.liststore = gtk.ListStore(str, str, str, str, str,str,str,str, str, str, str, str,str,str,str, str, str, str, str,str,str,str,str)#numero de colunas
        #Carrega o TreeView do Arquivo Interface.glade
        self.listaImoveis = self.xml.get_widget('listaImovel')
        #Adiciona o Modelo ao Widget TreeView
        self.listaImoveis.set_model(self.liststore)
        
	#Criando as colunas no treeWiew as colunas
        colunaProprietario     = gtk.TreeViewColumn("Proprietario",gtk.CellRendererText(), text=0)
        colunaEscritura     = gtk.TreeViewColumn("Num. Escritura",gtk.CellRendererText(), text=1)
        colunaCartorio     = gtk.TreeViewColumn("Cartorio",gtk.CellRendererText(), text=2)
        colunaCidade     = gtk.TreeViewColumn("Cidade",gtk.CellRendererText(), text=3)
        colunaRua     = gtk.TreeViewColumn("Rua",gtk.CellRendererText(), text=4)
        colunaNumero     = gtk.TreeViewColumn("Numero",gtk.CellRendererText(), text=5)
        colunaCep     = gtk.TreeViewColumn("CEP",gtk.CellRendererText(), text=6)
        colunaBairro     = gtk.TreeViewColumn("Bairro",gtk.CellRendererText(), text=7)
        colunaComplemento     = gtk.TreeViewColumn("Complemento",gtk.CellRendererText(), text=8)
        colunaCidadeImovel     = gtk.TreeViewColumn("Cidade",gtk.CellRendererText(), text=9)
        colunaUf     = gtk.TreeViewColumn("Estado",gtk.CellRendererText(), text=10)
        colunaDescricao     = gtk.TreeViewColumn("Descricao",gtk.CellRendererText(), text=11)
        colunaCategoria     = gtk.TreeViewColumn("Categoria",gtk.CellRendererText(), text=12)
        colunaDormitorio     = gtk.TreeViewColumn("Dormitorio",gtk.CellRendererText(), text=13)
        colunaSuite     = gtk.TreeViewColumn("Suite",gtk.CellRendererText(), text=14)
        colunaCopa     = gtk.TreeViewColumn("Copa",gtk.CellRendererText(), text=15)
        colunaGaragem     = gtk.TreeViewColumn("Garagem",gtk.CellRendererText(), text=16)
        colunaSalaJantar     = gtk.TreeViewColumn("Sala de Jantar",gtk.CellRendererText(), text=17)
        colunaSalaEstar  = gtk.TreeViewColumn("Sala de Estar",gtk.CellRendererText(), text=18)
        colunaBanheiro     = gtk.TreeViewColumn("Banheiro",gtk.CellRendererText(), text=19)
        colunaAreaTotal     = gtk.TreeViewColumn("Area Total",gtk.CellRendererText(), text=20)
        colunaOutrosDados     = gtk.TreeViewColumn("Outros dados",gtk.CellRendererText(), text=21)
        colunaValor     = gtk.TreeViewColumn("Valor",gtk.CellRendererText(), text=22)
        
        #Adicionando as colunas no treeWiew 
        self.listaImoveis.append_column(colunaProprietario)
        self.listaImoveis.append_column(colunaEscritura)
        self.listaImoveis.append_column(colunaCartorio)
        self.listaImoveis.append_column(colunaCidade)
        self.listaImoveis.append_column(colunaRua)
        self.listaImoveis.append_column(colunaNumero)
        self.listaImoveis.append_column(colunaCep)
        self.listaImoveis.append_column(colunaBairro)
        self.listaImoveis.append_column(colunaComplemento)
        self.listaImoveis.append_column(colunaCidadeImovel)
        self.listaImoveis.append_column(colunaUf)
        self.listaImoveis.append_column(colunaDescricao)
        self.listaImoveis.append_column(colunaCategoria)
        self.listaImoveis.append_column(colunaDormitorio)
        self.listaImoveis.append_column(colunaSuite)
        self.listaImoveis.append_column(colunaCopa)
        self.listaImoveis.append_column(colunaGaragem)
        self.listaImoveis.append_column(colunaSalaJantar)
        self.listaImoveis.append_column(colunaSalaEstar)
        self.listaImoveis.append_column(colunaBanheiro)
        self.listaImoveis.append_column(colunaAreaTotal)
        self.listaImoveis.append_column(colunaOutrosDados)
        self.listaImoveis.append_column(colunaValor)

        #Seleciona os dados da tabela imoveis, realiza a iteração nas colunas do banco e adiciona os valores em um liststore  
        cursor.execute("SELECT * FROM imoveis")
        resultado1 = cursor.fetchall() 
        for row in resultado1:
            imovelProprietario = row[1]
            escritura = row[2]
            cartorio = row[3]
            cidadeCartorio = row[4]
            rua = row[5]
            num = row[6]
            cep = row[7]
            bairro = row[8]
            complemento = row[9]
            cidadeImovel = row[10]
            uf = row[11]
            descrissao = row[12]
            categoriaImovel = row[13] 
            dormitorio = row[14]
            suite = row[15]
            copa = row[16]
            garagem = row[17]
            salaJantar = row[18]
            salaEstar = row[19]
            banheiro = row[20]
            areaTotal = row[21]
            outrosDados = row[22]
            valor = row[23]
            self.liststore.append([imovelProprietario,escritura,cartorio,cidadeCartorio,rua,num,cep,bairro,complemento,cidadeImovel,uf,descrissao,categoriaImovel,dormitorio,suite,copa,garagem,salaJantar,salaEstar,banheiro,areaTotal,outrosDados,valor])
        
        #Define o modelo do treeview
        self.listStore2 = gtk.ListStore(str,str,str,str,str,str,str,str,str,str,str,str,str,str,str,str,str,str,str,str,str)#numero de colunas
        #Carregando o treeWiew2 do arquivo xml realState.glade
        self.listaClientes = self.xml.get_widget('listaClientes')
        #Adiciona o Modelo ao Widget TreeView
        self.listaClientes.set_model(self.listStore2)

        #Criando as colunas de clientes.
        colunaCategoria = gtk.TreeViewColumn("Categoria",gtk.CellRendererText(), text=0)
        colunaNome = gtk.TreeViewColumn("Nome",gtk.CellRendererText(), text=1)
        colunaCpf = gtk.TreeViewColumn("CPF",gtk.CellRendererText(), text=2)
        colunaRg = gtk.TreeViewColumn("RG",gtk.CellRendererText(), text=3)
        colunaOrgaoEmissor = gtk.TreeViewColumn("Orgao Emissor",gtk.CellRendererText(), text=4)
        colunaNaturalidade = gtk.TreeViewColumn("Naturalidade",gtk.CellRendererText(), text=5)
        colunaDtNascimento = gtk.TreeViewColumn("Data de Nascimento",gtk.CellRendererText(), text=6)
        colunaNomeMae = gtk.TreeViewColumn("Nome da Mae",gtk.CellRendererText(), text=7)
        colunaNomePai = gtk.TreeViewColumn("Nome do Pai",gtk.CellRendererText(), text=8)
        colunaEstadoCivil = gtk.TreeViewColumn("Estado Civil",gtk.CellRendererText(), text=9)
        colunaRegimeCasamento = gtk.TreeViewColumn("Regime Casamento",gtk.CellRendererText(), text=10)
        colunaTelefone = gtk.TreeViewColumn("Telefone",gtk.CellRendererText(), text=11)
        colunaCelular = gtk.TreeViewColumn("Celular",gtk.CellRendererText(), text=12)
        colunaEmail = gtk.TreeViewColumn("Email",gtk.CellRendererText(), text=13)
        colunaEndereco = gtk.TreeViewColumn("Endereco",gtk.CellRendererText(), text=14)
        colunaProfissao = gtk.TreeViewColumn("Profissao",gtk.CellRendererText(), text=15)
        colunaEmpresa = gtk.TreeViewColumn("Empresa",gtk.CellRendererText(), text=16)
        colunaCargo = gtk.TreeViewColumn("Cargo",gtk.CellRendererText(), text=17)
        colunaEnderecoEmpresa = gtk.TreeViewColumn("Endereco da Empresa",gtk.CellRendererText(), text=18)
        colunaTelefoneEmpresa = gtk.TreeViewColumn("Telefone da Empresa",gtk.CellRendererText(), text=19)
        colunaEmailFuncional = gtk.TreeViewColumn("Email ou Site",gtk.CellRendererText(), text=20)

        #Adicionando as colunas ao widget listaClientes
        self.listaClientes.append_column(colunaCategoria)
        self.listaClientes.append_column(colunaNome)
        self.listaClientes.append_column(colunaCpf)
        self.listaClientes.append_column(colunaRg)
        self.listaClientes.append_column(colunaOrgaoEmissor)
        self.listaClientes.append_column(colunaNaturalidade)
        self.listaClientes.append_column(colunaDtNascimento)
        self.listaClientes.append_column(colunaNomeMae)
        self.listaClientes.append_column(colunaNomePai)
        self.listaClientes.append_column(colunaEstadoCivil)
        self.listaClientes.append_column(colunaRegimeCasamento)
        self.listaClientes.append_column(colunaTelefone)
        self.listaClientes.append_column(colunaCelular)
        self.listaClientes.append_column(colunaEmail)
        self.listaClientes.append_column(colunaEndereco)
        self.listaClientes.append_column(colunaProfissao)
        self.listaClientes.append_column(colunaEmpresa)
        self.listaClientes.append_column(colunaCargo)
        self.listaClientes.append_column(colunaEnderecoEmpresa)
        self.listaClientes.append_column(colunaTelefoneEmpresa)
        self.listaClientes.append_column(colunaEmailFuncional)
        self.leClientes()
        
        #Conecta os sinai da classe Office 
        self.xml.signal_autoconnect(dic)
        # Torna visivel a janela Office 
        self.windowOffice.show_all()
        
    def leClientes(self):
        ##Seleciona os dados da tabela clientes, realiza a iteração nas colunas do banco e adiciona os valores em um liststore 
        cursor.execute("SELECT * FROM clientes")
        resultado2 = cursor.fetchall()
        self.listStore2.clear()#Apaga os dados anteriores
        for row in resultado2:
            clienteCategoria = row[1]
            nome = row[2]
            cpf = row[3]
            rg = row[4]
            orgaoEmisso = row[5]
            naturalidade = row[6]
            dtNascimento = row[7]
            nomeMae = row[8]
            nomePai = row[9]
            estadoCivil = row[10]
            regimeCasamento = row[11]
            telefone = row[12]
            celular = row[13]
            email = row[14]
            endereco = row[15]
            profissao = row[16]
            empresa = row[17]
            cargo = row[18]
            enderecoEmpresa = row[19]
            telefoneEmpresa = row[20]
            emailFuncional = row[21]
            self.listStore2.append([clienteCategoria,nome,cpf,rg,orgaoEmisso,naturalidade,dtNascimento,nomeMae,nomePai,estadoCivil,regimeCasamento,telefone,celular,email,endereco,profissao,empresa,cargo,enderecoEmpresa,telefoneEmpresa,emailFuncional])

    def ValidarCliente(self,widget):
        #Carregando a barra de estatus
        self.statusbarCliente = self.xml.get_widget("statusbarCliente")
        self.context = self.statusbarCliente.get_context_id("")
        #Validar se todos os campos da aba clientes estão preenchidos e inserir no banco de dados, retornar uma mensagem de erro caso não estejar.
        if(self.categoria.get_text() == "" or self.nome.get_text() == "" or self.cpf.get_text() == "" or self.rg.get_text() == "" or self.orgaoEmissor.get_text() == ""\
           or self.naturalidade.get_text() == "" or self.dataNascimento.get_text() == "" or self.nomeMae.get_text() == "" or self.nomePai.get_text() == "" or self.estadoCivil.get_text() == ""\
           or self.regimeCasamento.get_text() == "" or self.telefone.get_text() == "" or self.celular.get_text() == "" or self.email.get_text() == "" or self.endereco.get_text() == ""\
           or self.profissao.get_text() == "" or self.empresa.get_text() == "" or self.cargo.get_text() == "" or self.enderecoEmpresa.get_text() == "" or self.telefoneEmpresa.get_text() == "" or self.emailFuncional.get_text() == ""):
            self.statusbarCliente.push(self.context, "Todos os campos devem ser preenchidos!")
        else:
            cursor.execute("INSERT INTO clientes(categoria,nome,cpf,rg,orgaoemissor,naturalidade,datanascimento,nomemae,nomepai,estadocivil,regimecasamento,telefone,celular,email,endereco,profissao,empresa,cargo,enderecoempresa,telefoneempresa,emailsite)\
                           VALUES ('"+self.categoria.get_text()+"','"+self.nome.get_text()+"','"+self.cpf.get_text()+"','"+self.rg.get_text()+"','"+self.orgaoEmissor.get_text()+"','"+self.naturalidade.get_text()+"','"+self.dataNascimento.get_text()+"','"+self.nomeMae.get_text()+"','"+self.nomePai.get_text()+"','"+self.estadoCivil.get_text()+"','"+self.regimeCasamento.get_text()+"','"+self.telefone.get_text()+"','"+self.celular.get_text()+"','"+self.email.get_text()+"','"+self.endereco.get_text()+"','"+self.profissao.get_text()+"','"+self.empresa.get_text()+"','"+self.cargo.get_text()+"','"+self.enderecoEmpresa.get_text()+"','"+self.telefoneEmpresa.get_text()+"','"+self.emailFuncional.get_text()+"')")
            connection.commit()
            self.leClientes() # chama a função que faz seleção no banco de dados para atualizar o treeview
            msg = gtk.MessageDialog(None, 0, gtk.MESSAGE_INFO, gtk.BUTTONS_OK, 'Cadastrado realizado com sucesso!!!')
            msg.run()
            msg.destroy()
            
            #Esvasiar os campos
            self.categoria.props.text = ""
            self.nome.props.text = ""
            self.cpf.props.text = ""
            self.rg.props.text = ""
            self.orgaoEmissor.props.text = ""
            self.naturalidade.props.text = ""
            self.dataNascimento.props.text = ""
            self.nomeMae.props.text = ""
            self.nomePai.props.text = ""
            self.estadoCivil.props.text = ""
            self.regimeCasamento.props.text = ""
            self.telefone.props.text = ""
            self.celular.props.text = ""
            self.email.props.text = ""
            self.endereco.props.text = ""
            self.profissao.props.text = ""
            self.empresa.props.text = ""
            self.cargo.props.text = ""
            self.enderecoEmpresa.props.text = ""
            self.telefoneEmpresa.props.text = ""
            self.emailFuncional.props.text = ""
            
    def CancelSystem(self, widget):
        #Fecha a janela Office
        self.windowOffice.hide()    

    def PesqImovel(self,widget):
        #Faz uma seleção no banco de dados a partir do que foi digitado pelo usuário no campo de texto.
        cursor.execute("SELECT * FROM imoveis WHERE proprietario like '"+self.pesquisarImv.get_text()+"%'")
        pesqImovel = cursor.fetchall()
        self.liststore.clear()#Limpa todos os dados do liststore
        for row in pesqImovel:
            pesqProprietario = row[1]
            pesqEscritura = row[2]
            pesqCartorio = row[3]
            pesqCidade = row[4]
            pesqRua = row[5]
            pesqNumero = row[6]
            pesqCep = row[7]
            pesqBairro = row[8]
            pesqComplemento = row[9]
            pesqCidade = row[10]
            pesqUf = row[11]
            pesqDescricao = row[12]
            pesqCategoria = row[13]
            pesqDormitorio = row[14]
            pesqSuite = row[15]
            pesqCopa = row[16]
            pesqGaragem = row[17]
            pesqSalaJantar = row[18]
            pesqSalaEstar = row[19]
            pesqBanheiro = row[20]
            pesqArea = row[21]
            pesqOutros = row[22]
            pesqValor = row[23]
            #Adiciona os dados no liststore da pesquisa no liststore, retornando-os na tela.
            self.liststore.append([pesqProprietario,pesqEscritura,pesqCartorio,pesqCidade,pesqRua,pesqNumero,pesqCep,pesqBairro,pesqComplemento,pesqCidade,pesqUf,pesqDescricao,pesqCategoria,pesqDormitorio,pesqSuite,pesqCopa,pesqGaragem,pesqSalaJantar,pesqSalaEstar,pesqBanheiro,pesqArea,pesqOutros,pesqValor])

    def PesqCliente(self,widget):
        #Faz uma seleção no banco de dados a partir do que foi digitado pelo usuário no campo de texto.
        cursor.execute("SELECT * FROM clientes WHERE nome like '"+self.pesquisarCli.get_text()+"%'")
        pesquisacliente = cursor.fetchall()
        self.listStore2.clear()#Limpa todos os dados da liststore
        for row in pesquisacliente:
            pesqCategoria = row[1]
            pesqNome = row[2]
            pesqCpf = row[3]
            pesqRg = row[4]
            pesqOrgEmissor = row[5]
            pesqNaturalidade = row[6]
            pesqDtNascimento = row[7]
            pesqMae = row[8]
            pesqPai = row[9]
            pesqEstCivil = row[10]
            pesqRegimeCasamento = row[11]
            pesqTelefone = row[12]
            pesqCelular = row[13]
            pesqEmail = row[14]
            pesqEndereco = row[15]
            pesqProfissao = row[16]
            pesqEmpresa = row[17]
            pesqCargo= row[18]
            pesqEndEmpresa = row[19]
            pesqTelEmpresa = row[20]
            pesqEmailEmpresa = row[21]
            #Adiciona os dados no liststore da pesquisa no liststore, retornando-os na tela.
            self.listStore2.append([pesqCategoria,pesqNome,pesqCpf,pesqRg,pesqOrgEmissor,pesqNaturalidade,pesqDtNascimento,pesqMae,pesqPai,pesqEstCivil,pesqRegimeCasamento,pesqTelefone,pesqCelular,pesqEmail,pesqEndereco,pesqProfissao,pesqEmpresa,pesqCargo,pesqEndEmpresa,pesqTelEmpresa,pesqEmailEmpresa])
            
    def Seleciona_Cliente(self,widget):
        #Posiciona o cursor na linha do treeview que deseja editar  
        self.valorCliente = self.listaClientes.get_cursor()
        #Carrega a interface, a janela e os widgets de edição de clientes.
        self.xml = gtk.glade.XML('ImobSystem.glade')
        self.janelaCliente = self.xml.get_widget('EditarCliente')
        self.edtCategoria_Cli = self.xml.get_widget("entrycategoriaAdm1EDT")
        self.edtNome_Cli = self.xml.get_widget("entrynomeAdm1EDT")
        self.edtCpf_Cli = self.xml.get_widget("entrycpfAdm1EDT")
        self.edtRg_Cli = self.xml.get_widget("entryrgAdm1EDT")
        self.edtOrgEmissor_Cli = self.xml.get_widget("entryorgaoemissorAdm1EDT")
        self.edtNaturalidade_Cli = self.xml.get_widget("entrynaturalidadeAdm1EDT")
        self.edtDtNascimento_Cli = self.xml.get_widget("entrydtnascimentoAdm1EDT")
        self.edtMae_Cli = self.xml.get_widget("entrymaeAdm1EDT")
        self.edtPai_Cli = self.xml.get_widget("entrypaiAdm1EDT")
        self.edtEstCivil_Cli = self.xml.get_widget("entryestcivilAdm1EDT")
        self.edtRegimeCasamento_Cli = self.xml.get_widget("entryregcasamentoAdm1EDT")
        self.edtTelefone_Cli = self.xml.get_widget("entrytelefoneAdm1EDT")
        self.edtCelular_Cli = self.xml.get_widget("entrycelularAdm1EDT")
        self.edtEmail_Cli = self.xml.get_widget("entryemailAdm1EDT")
        self.edtEndereco_Cli = self.xml.get_widget("entryenderecoAdm1EDT")
        self.edtProfissao_Cli = self.xml.get_widget("entryprofissaoAdm1EDT")
        self.edtEmpresa_Cli = self.xml.get_widget("entryempresaAdm1EDT")
        self.edtCargo_Cli = self.xml.get_widget("entrycargoAdm1EDT")
        self.edtEndEmpresa_Cli = self.xml.get_widget("entryendempresaAdm1EDT")
        self.edtTelEmpresa_Cli = self.xml.get_widget("entrytelempresaAdm1EDT")
        self.edtEmailEmpresa_Cli = self.xml.get_widget("entryemailempresaAdm1EDT")
        #Torna visível a janela de edição de clientes 
        self.janelaCliente.show_all()
        #cria dicionário para conectar os sinais da janela clientes
        dic_cli = {"on_btnCancelarCli_clicked" : self.Cancelar_Cliente,
                   "on_btnEDTCliAdm1_clicked" : self.EditarCliente,
            }
        #Conecta os sinais do dicionario à janela de ediçao de clientes.
        self.xml.signal_autoconnect(dic_cli)
        self.valorCliente = self.listaClientes.get_selection()#seleciona a linha onde cursor está posicionado.
        self.valorCliente.set_mode(gtk.SELECTION_MULTIPLE)#Define que vários itens podem ser selecionadas de cada vez.
        modelo, caminhos = self.valorCliente.get_selected_rows()# recupera a seleção dependendo do modo de seleção atual.
        for caminho in caminhos:
            #Aponta o caminho
            kiter = modelo.get_iter(caminho) 
            categoriaEDT = modelo.get_value(kiter, 0)
            nomeEDT = modelo.get_value(kiter, 1)
            cpfEDT = modelo.get_value(kiter, 2)
            rgEDT = modelo.get_value(kiter, 3)
            orgEmissorEDT = modelo.get_value(kiter, 4)
            naturalidadeEDT = modelo.get_value(kiter, 5)
            dtNascimentoEDT = modelo.get_value(kiter, 6)
            maeEDT = modelo.get_value(kiter, 7)
            paiEDT = modelo.get_value(kiter, 8)
            estCivilEDT = modelo.get_value(kiter, 9)
            regimeCasamentoEDT = modelo.get_value(kiter, 10)
            telefoneEDT = modelo.get_value(kiter, 11)
            celularEDT = modelo.get_value(kiter, 12)
            emailEDT = modelo.get_value(kiter, 13)
            enderecoEDT = modelo.get_value(kiter, 14)
            profissaoEDT = modelo.get_value(kiter, 15)
            empresaEDT = modelo.get_value(kiter, 16)
            cargoEDT = modelo.get_value(kiter, 17)
            endEmpresaEDT = modelo.get_value(kiter, 18)
            telEmpresaEDT = modelo.get_value(kiter, 19)
            emailEmpresaEDT = modelo.get_value(kiter, 20)
            #Substitui as variáveis pelos dados apontados pelo caminho
            self.edtCategoria_Cli.props.text = categoriaEDT
            self.edtNome_Cli.props.text = nomeEDT
            self.edtCpf_Cli.props.text = cpfEDT
            self.edtRg_Cli.props.text = rgEDT
            self.edtOrgEmissor_Cli.props.text = orgEmissorEDT
            self.edtNaturalidade_Cli.props.text = naturalidadeEDT
            self.edtDtNascimento_Cli.props.text = dtNascimentoEDT
            self.edtMae_Cli.props.text = maeEDT
            self.edtPai_Cli.props.text = paiEDT
            self.edtEstCivil_Cli.props.text = estCivilEDT
            self.edtRegimeCasamento_Cli.props.text = regimeCasamentoEDT
            self.edtTelefone_Cli.props.text = telefoneEDT
            self.edtCelular_Cli.props.text = celularEDT
            self.edtEmail_Cli.props.text = emailEDT
            self.edtEndereco_Cli.props.text = enderecoEDT
            self.edtProfissao_Cli.props.text = profissaoEDT
            self.edtEmpresa_Cli.props.text = empresaEDT
            self.edtCargo_Cli.props.text = cargoEDT
            self.edtEndEmpresa_Cli.props.text = endEmpresaEDT
            self.edtTelEmpresa_Cli.props.text = telEmpresaEDT
            self.edtEmailEmpresa_Cli.props.text = emailEmpresaEDT
            
    def EditarCliente(self, widget):
        print "a"
        #Selecina na tabela clientes os dados que estão digitados no campo de texto. Faz uma iteração, e atualiza o banco de dados com os novos
        #valores digitados pelo usuário, em seguida chama a função leClientes para atualizar os dados no treeview
        cursor.execute("SELECT * FROM clientes WHERE cpf='"+self.edtCpf_Cli.get_text()+"'")
        print "b"
        selectCli = cursor.fetchall()
        for linha in selectCli:
            cursor.execute("UPDATE clientes SET categoria='"+self.edtCategoria_Cli.get_text()+"',cpf='"+self.edtCpf_Cli.get_text()+"',rg= '"+self.edtRg_Cli.get_text()+"',orgaoemissor='"+self.edtOrgEmissor_Cli.get_text()+"',naturalidade='"+self.edtNaturalidade_Cli.get_text()+"',datanascimento='"+self.edtDtNascimento_Cli.get_text()+"',nomemae='"+self.edtMae_Cli.get_text()+"',nomepai='"+self.edtPai_Cli.get_text()+"',estadocivil='"+self.edtEstCivil_Cli.get_text()+"',regimecasamento= '"+self.edtRegimeCasamento_Cli.get_text()+"',telefone='"+self.edtTelefone_Cli.get_text()+"',celular='"+self.edtCelular_Cli.get_text()+"',email='"+self.edtEmail_Cli.get_text()+"',endereco='"+self.edtEndereco_Cli.get_text()+"',profissao='"+self.edtProfissao_Cli.get_text()+"',empresa='"+self.edtEmpresa_Cli.get_text()+"',cargo='"+self.edtCargo_Cli.get_text()+"',enderecoempresa='"+self.edtEndEmpresa_Cli.get_text()+"',telefoneempresa='"+self.edtTelEmpresa_Cli.get_text()+"',emailsite='"+self.edtEmailEmpresa_Cli.get_text()+"' WHERE nome='"+self.edtNome_Cli.get_text()+"'" )
            connection.commit()
            print "c"
            msg = gtk.MessageDialog(None, 0, gtk.MESSAGE_INFO, gtk.BUTTONS_OK, 'Atualizado Com Sucesso')
            msg.run()
            msg.destroy()
            self.janelaCliente.hide()#fecha a janela de edição de clientes
            self.leClientes()
            
    def Cancelar_Cliente(self,widget):
        #fecha a janela de edição de clientes
        self.janelaCliente.hide()
         
    def DeletarCliente(self, widget):
        #Posiciona o cursor na linha selecionada. Envia uma mensagem de validação para que o usuário escolha se deseja ou não exluir aqueles dados.
        self.valor_DelCli = self.listaClientes.get_cursor()
        msg = gtk.MessageDialog(None, 0, gtk.MESSAGE_QUESTION, gtk.BUTTONS_YES_NO, 'Deseja excluir o registro ?')
        resposta = msg.run()
        msg.destroy()
        if resposta == gtk.RESPONSE_YES:
            #Caso a resposta seja sim, o cursor seleciona a linha que ele estava posicionado 
            self.valor_DelCli = self.listaClientes.get_selection()
            self.valor_DelCli.set_mode(gtk.SELECTION_MULTIPLE) #Define que vários itens podem ser selecionados de cada vez 
            modelo, caminhos = self.valor_DelCli.get_selected_rows() #recupera a seleção dependendo do modo de seleção atual.
            for caminho in caminhos:
                kiter = modelo.get_iter(caminho)
                #Aponta o caminho
                self.delCli = modelo.get_value(kiter,3)
            #Seleciona os valores da tabela clientes e deleta os valores se a linha escolhida for igual ao caminho apontado pelo cursor.        
            cursor.execute("SELECT * FROM clientes")
            removeCli = cursor.fetchall()
            for linha in removeCli: 
                if self.delCli == linha[4]:
                    print "a"
                    cursor.execute("DELETE FROM clientes WHERE cpf='%s'" % (linha[4]))
                    connection.commit()
                    self.leClientes()#Chama a função para atualizar os dados no treeview     
            msg = gtk.MessageDialog(None, 0, gtk.MESSAGE_INFO, gtk.BUTTONS_OK, 'Deletado com Sucesso!')
            msg.run()
            msg.destroy()
            
class Manager(object):
    def __init__(self):
        #Carrega o Arquivo XML do glade
        self.xml = gtk.glade.XML('ImobSystem.glade')
        #Carrega a janela de Administrador e os widgets
        self.windowManager = self.xml.get_widget('Manager')
        self.managerStatusbar = self.xml.get_widget("statusbarManager")
        self.contexto = self.managerStatusbar.get_context_id("")
        self.managerStatusbar.push(self.contexto, "Administrador")#Define o contexto da statusbar
        self.proprietario= self.xml.get_widget("entryProp")
        self.escritura = self.xml.get_widget("entryEscritura")
        self.cartorio = self.xml.get_widget("entryCartorio")
        self.cidadeCartorio = self.xml.get_widget("entryCidadeCartorio")
        self.rua = self.xml.get_widget("entryRua")
        self.num = self.xml.get_widget("entryNum")
        self.cep = self.xml.get_widget("entryCep")
        self.bairro = self.xml.get_widget("entryBairro")
        self.complemento = self.xml.get_widget("entryComplem")
        self.cidadeImovel = self.xml.get_widget("entryCidade")
        self.uf = self.xml.get_widget("entryUf")
        self.descrissao = self.xml.get_widget("entryDescrissao")
        self.categoria = self.xml.get_widget("entryCateg")
        self.dormitorio = self.xml.get_widget("entryDorm")
        self.suite = self.xml.get_widget("entrySuite")
        self.copa = self.xml.get_widget("entryCopa")
        self.garagem = self.xml.get_widget("entryGaragem")
        self.salaJantar = self.xml.get_widget("entrySala")
        self.salaEstar = self.xml.get_widget("entrySalaEstar")
        self.banheiro = self.xml.get_widget("entryBanheiro")
        self.areaTotal = self.xml.get_widget("entryArea")
        self.outrosDados = self.xml.get_widget("entryOutrosDados")
        self.valor = self.xml.get_widget("entryValor")
        #Aba Aluguel.
        self.locador = self.xml.get_widget("entryLocador")#Informações referentes ao imovel.
        self.locatario = self.xml.get_widget("entryLocatario")
        self.numeroIMV = self.xml.get_widget("entryNumIMV")
        self.finalidadeIMV = self.xml.get_widget("entryFinalidadeIMV")
        self.prazoIMV = self.xml.get_widget("entryPrazoIMV")
        self.valorIMV = self.xml.get_widget("entryValorAluguel")
        self.inicioIMV = self.xml.get_widget("entryInicioAluguel")
        self.terminoIMV = self.xml.get_widget("entryTerminoAluguel")
        self.vencimentoIMV = self.xml.get_widget("entryVencimentoAluguel")
        self.fiador1 = self.xml.get_widget("entryFiador1")#Informações referentes ao fiador 01
        self.cpf1 = self.xml.get_widget("entryCPF1")
        self.rg1 = self.xml.get_widget("entryRG1")
        self.dtnascimento1 = self.xml.get_widget("entryDT1")
        self.estCivil1 = self.xml.get_widget("entryEC1")
        self.regCivil1 = self.xml.get_widget("entryRC1")
        self.esposa1 = self.xml.get_widget("entryConjugueAluguel")
        self.dtEsposa1 = self.xml.get_widget("entryDTE1")
        self.cpfEsposa1 = self.xml.get_widget("entryCPFE1")
        self.rgEsposa1 = self.xml.get_widget("entryRGE1") 
        self.endereco1 = self.xml.get_widget("entryEnd1")
        self.numero1 = self.xml.get_widget("entryNum1")
        self.bairro1 = self.xml.get_widget("entryBairro1")
        self.cidade1 = self.xml.get_widget("entryCidade1")
        self.estado1 = self.xml.get_widget("entryEstado1")
        self.profissao1 = self.xml.get_widget("entryProf1")
        self.renda1 = self.xml.get_widget("entryRM1")
        self.adiciais1 = self.xml.get_widget("entryAdc1")
        self.fiador2 = self.xml.get_widget("entryFiador")##Informações referentes ao fiador 02
        self.cpf2 = self.xml.get_widget("entryCPF2")
        self.rg2 = self.xml.get_widget("entryRG2")
        self.dtnascimento2 = self.xml.get_widget("entryDT2")
        self.estCivil2 = self.xml.get_widget("entryEC2")
        self.regCivil2 = self.xml.get_widget("entryRC2")
        self.esposa2 = self.xml.get_widget("entryESP2")
        self.dtEsposa2 = self.xml.get_widget("entryDTE2")
        self.cpfEsposa2 = self.xml.get_widget("entryCPFE2")
        self.rgEsposa2 = self.xml.get_widget("entryRGE2")
        self.endereco2 = self.xml.get_widget("entryEnd2")
        self.numero2 = self.xml.get_widget("entryNum2")
        self.bairro2 = self.xml.get_widget("entryBairro2")
        self.cidade2 = self.xml.get_widget("entryCidade2") 
        self.estado2 = self.xml.get_widget("entryEstado2")
        self.profissao2 = self.xml.get_widget("entryProf2")
        self.renda2 = self.xml.get_widget("entryRM2") 
        self.adicionais2 = self.xml.get_widget("entryAdc2")
        #Aba Venda
        self.vendedor = self.xml.get_widget("entryNomevenda")
        self.cpfvendedor = self.xml.get_widget("entrycpfvenda")
        self.rgvenderdor = self.xml.get_widget("entryrgvenda")
        self.naturalidadevendedor = self.xml.get_widget("entrynaturalidadevenda")
        self.ecvendedor = self.xml.get_widget("entryEstcivilvenda")
        self.profissaovend = self.xml.get_widget("entryProfVendedor")
        self.enderecovendedor = self.xml.get_widget("entryEnderecovenda")
        self.numerovendedor = self.xml.get_widget("entryNumvenda")
        self.bairrovendedor =  self.xml.get_widget("entryBairroVendedor")
        self.cepvendedor = self.xml.get_widget("entryCepvenda")
        self.cidadevendedor = self.xml.get_widget("entryCidadevenda")
        self.estadovendedor = self.xml.get_widget("entryEstadoVendedor")
        self.comprador = self.xml.get_widget("entryCompradorvenda")
        self.cpfcomprador = self.xml.get_widget("entryCpfCompradorvenda")
        self.rgcomprador = self.xml.get_widget("entryRGComprador")
        self.naturalidadecomprador = self.xml.get_widget("entryNatCompradorvenda")
        self.eccomprador = self.xml.get_widget("entryECcompradorvenda")
        self.profissaocomprador = self.xml.get_widget("entryProfComprador")
        self.enderecocomprador = self.xml.get_widget("entryEndCompradorvenda")
        self.numerocomprador = self.xml.get_widget("entryNumcompradorvenda")
        self.bairrocomprador = self.xml.get_widget("entryBairroComprador")
        self.cepcomprador = self.xml.get_widget("entrycepCompradorvenda")
        self.cidadecomprador = self.xml.get_widget("entryCidadeCompvenda")
        self.estadocomprador = self.xml.get_widget("entryEstadoComprador")
        self.areavenda = self.xml.get_widget("entryareavenda")
        self.registovenda = self.xml.get_widget("entryRegistrovenda")
        self.valorvenda = self.xml.get_widget("entryValorVenda")
        #Aba clientes.
        self.categoriaAdm = self.xml.get_widget("entrycategoriaAdm")
        self.nomeAdm = self.xml.get_widget("entrynomeAdm")
        self.cpfAdm = self.xml.get_widget("entrycpfAdm")
        self.rgAdm = self.xml.get_widget("entryrgAdm")
        self.orgaoemissorAdm = self.xml.get_widget("entryorgaoemissorAdm")
        self.naturalidadeAdm = self.xml.get_widget("entrynaturalidadeAdm")
        self.dtnascimentoAdm = self.xml.get_widget("entrydtnascimentoAdm")
        self.maeAdm = self.xml.get_widget("entrymaeAdm")
        self.paiAdm = self.xml.get_widget("entrypaiAdm")
        self.estcivilAdm = self.xml.get_widget("entryestcivilAdm")
        self.regcasamentoAdm = self.xml.get_widget("entryregcasamentoAdm")
        self.telefoneAdm = self.xml.get_widget("entrytelefoneAdm")
        self.celularAdm = self.xml.get_widget("entrycelularAdm")
        self.emailAdm = self.xml.get_widget("entryemailAdm")
        self.enderecoAdm = self.xml.get_widget("entryenderecoAdm")
        self.profissaoAdm = self.xml.get_widget("entryprofissaoAdm")
        self.empresaAdm = self.xml.get_widget("entryempresaAdm")
        self.cargoAdm = self.xml.get_widget("entrycargoAdm")
        self.endempresaAdm = self.xml.get_widget("entryendempresaAdm")
        self.telempresaAdm = self.xml.get_widget("entrytelempresaAdm")
        self.emailempresaAdm = self.xml.get_widget("entryemailempresaAdm")
        #Aba Funcionário
        self.nomeFuncionario = self.xml.get_widget("entryNomeFuncionario")
        self.dtnFuncionario = self.xml.get_widget("entryDtNascFuncionario")
        self.cpfFuncionario = self.xml.get_widget("entryCPFFuncionario")
        self.rgFuncionario = self.xml.get_widget("entryRgFuncionario")
        self.etdcvlFuncionario = self.xml.get_widget("entryEstCicilFuncionario")
        self.filhosFuncionario = self.xml.get_widget("entryFilhosFuncionario")
        self.grauInstFuncionario = self.xml.get_widget("entryGInstrucao")
        self.telefoneFuncionario = self.xml.get_widget("entryTelefoneFuncionario")
        self.emailFuncionario = self.xml.get_widget("entryEmailFuncionario")
        self.ruaFuncionario = self.xml.get_widget("entryRuaFuncionario")
        self.numeroFuncionario = self.xml.get_widget("entryNumFuncionario")
        self.bairroFuncionario = self.xml.get_widget("entryBairroFuncionario")
        self.complementoFuncionario = self.xml.get_widget("entryComplementoFuncionario")
        self.informacoesFuncionario = self.xml.get_widget("entryOutrasFuncionario")
        #Aba Login
        self.login_CD = self.xml.get_widget("entryLoginCD")
        self.senha_CD = self.xml.get_widget("entrySenhaCD")
        self.funcao_CD = self.xml.get_widget("entryFuncaoCD")
        # Pesquisa #
        self.pequisaImovel = self.xml.get_widget("entryPesquisarImovel")
        self.pequisaCliente = self.xml.get_widget("entryPesquisarCliente")
        self.pequisaFuncionario = self.xml.get_widget("entryPesquisarFuncionario")
        self.pesquisaAluguel = self.xml.get_widget("entryPesquisarAluguel")
        self.pesquisaVenda = self.xml.get_widget("entryPesquisarVenda")
        self.pesquisaLogin = self.xml.get_widget("entryPesquisarLogin")
        
        #Define o Modelo do TreeView Imóveis 
        self.liststore3 = gtk.ListStore(str, str, str, str, str,str,str,str, str, str, str, str,str,str,str, str, str, str, str,str,str,str,str)#número de colunas
        #Carrega o TreeView do Arquivo Interface.glade
        self.listaImoveis1 = self.xml.get_widget('treeviewImovel')
        #Adiciona o Modelo ao Widget TreeView
        self.listaImoveis1.set_model(self.liststore3)

	#Criando as colunas no treeWiew as colunas
        colunaProprietario1     = gtk.TreeViewColumn("Proprietario",gtk.CellRendererText(), text=0)
        colunaEscritura1     = gtk.TreeViewColumn("Num. Escritura",gtk.CellRendererText(), text=1)
        colunaCartorio1     = gtk.TreeViewColumn("Cartorio",gtk.CellRendererText(), text=2)
        colunaCidade1     = gtk.TreeViewColumn("Cidade",gtk.CellRendererText(), text=3)
        colunaRua1     = gtk.TreeViewColumn("Rua",gtk.CellRendererText(), text=4)
        colunaNumero1     = gtk.TreeViewColumn("Numero",gtk.CellRendererText(), text=5)
        colunaCep1     = gtk.TreeViewColumn("CEP",gtk.CellRendererText(), text=6)
        colunaBairro1     = gtk.TreeViewColumn("Bairro",gtk.CellRendererText(), text=7)
        colunaComplemento1     = gtk.TreeViewColumn("Complemento",gtk.CellRendererText(), text=8)
        colunaCidadeImovel1     = gtk.TreeViewColumn("Cidade",gtk.CellRendererText(), text=9)
        colunaUf1     = gtk.TreeViewColumn("Estado",gtk.CellRendererText(), text=10)
        colunaDescricao1     = gtk.TreeViewColumn("Descricao",gtk.CellRendererText(), text=11)
        colunaCategoria1     = gtk.TreeViewColumn("Categoria",gtk.CellRendererText(), text=12)
        colunaDormitorio1     = gtk.TreeViewColumn("Dormitorio",gtk.CellRendererText(), text=13)
        colunaSuite1     = gtk.TreeViewColumn("Suite",gtk.CellRendererText(), text=14)
        colunaCopa1     = gtk.TreeViewColumn("Copa",gtk.CellRendererText(), text=15)
        colunaGaragem1     = gtk.TreeViewColumn("Garagem",gtk.CellRendererText(), text=16)
        colunaSalaJantar1     = gtk.TreeViewColumn("Sala de Jantar",gtk.CellRendererText(), text=17)
        colunaSalaEstar1  = gtk.TreeViewColumn("Sala de Estar",gtk.CellRendererText(), text=18)
        colunaBanheiro1     = gtk.TreeViewColumn("Banheiro",gtk.CellRendererText(), text=19)
        colunaAreaTotal1     = gtk.TreeViewColumn("Area Total",gtk.CellRendererText(), text=20)
        colunaOutrosDados1     = gtk.TreeViewColumn("Outros dados",gtk.CellRendererText(), text=21)
        colunaValor1     = gtk.TreeViewColumn("Valor",gtk.CellRendererText(), text=22)

        #Adicionando as colunas no treeWiew as colunas
        self.listaImoveis1.append_column(colunaProprietario1)
        self.listaImoveis1.append_column(colunaEscritura1)
        self.listaImoveis1.append_column(colunaCartorio1)
        self.listaImoveis1.append_column(colunaCidade1)
        self.listaImoveis1.append_column(colunaRua1)
        self.listaImoveis1.append_column(colunaNumero1)
        self.listaImoveis1.append_column(colunaCep1)
        self.listaImoveis1.append_column(colunaBairro1)
        self.listaImoveis1.append_column(colunaComplemento1)
        self.listaImoveis1.append_column(colunaCidadeImovel1)
        self.listaImoveis1.append_column(colunaUf1)
        self.listaImoveis1.append_column(colunaDescricao1)
        self.listaImoveis1.append_column(colunaCategoria1)
        self.listaImoveis1.append_column(colunaDormitorio1)
        self.listaImoveis1.append_column(colunaSuite1)
        self.listaImoveis1.append_column(colunaCopa1)
        self.listaImoveis1.append_column(colunaGaragem1)
        self.listaImoveis1.append_column(colunaSalaJantar1)
        self.listaImoveis1.append_column(colunaSalaEstar1)
        self.listaImoveis1.append_column(colunaBanheiro1)
        self.listaImoveis1.append_column(colunaAreaTotal1)
        self.listaImoveis1.append_column(colunaOutrosDados1)
        self.listaImoveis1.append_column(colunaValor1)
        self.le_Imovel()
                    
        #Criando a aba de pesquisa a clientes do Notebook1.
        self.listStore4 = gtk.ListStore(str,str,str,str,str,str,str,str,str,str,str,str,str,str,str,str,str,str,str,str,str)#número de tabelas
        #Carregando o treeWiew2 do arquivo xml realState.glade
        self.listaClientes1 = self.xml.get_widget('treeviewCliente')
        #Adiciona o Modelo ao Widget TreeView
        self.listaClientes1.set_model(self.listStore4)
        
        #Criando as colunas para pesquisa de clientes.
        colunaCategoria1 = gtk.TreeViewColumn("Categoria",gtk.CellRendererText(), text=0)
        colunaNome1 = gtk.TreeViewColumn("Nome",gtk.CellRendererText(), text=1)
        colunaCpf1 = gtk.TreeViewColumn("CPF",gtk.CellRendererText(), text=2)
        colunaRg1 = gtk.TreeViewColumn("RG",gtk.CellRendererText(), text=3)
        colunaOrgaoEmissor1 = gtk.TreeViewColumn("Orgao Emissor",gtk.CellRendererText(), text=4)
        colunaNaturalidade1 = gtk.TreeViewColumn("Naturalidade",gtk.CellRendererText(), text=5)
        colunaDtNascimento1 = gtk.TreeViewColumn("Data de Nascimento",gtk.CellRendererText(), text=6)
        colunaNomeMae1 = gtk.TreeViewColumn("Nome da Mae",gtk.CellRendererText(), text=7)
        colunaNomePai1 = gtk.TreeViewColumn("Nome do Pai",gtk.CellRendererText(), text=8)
        colunaEstadoCivil1 = gtk.TreeViewColumn("Estado Civil",gtk.CellRendererText(), text=9)
        colunaRegimeCasamento1 = gtk.TreeViewColumn("Regime Casamento",gtk.CellRendererText(), text=10)
        colunaTelefone1 = gtk.TreeViewColumn("Telefone",gtk.CellRendererText(), text=11)
        colunaCelular1 = gtk.TreeViewColumn("Celular",gtk.CellRendererText(), text=12)
        colunaEmail1 = gtk.TreeViewColumn("Email",gtk.CellRendererText(), text=13)
        colunaEndereco1 = gtk.TreeViewColumn("Endereco",gtk.CellRendererText(), text=14)
        colunaProfissao1 = gtk.TreeViewColumn("Profissao",gtk.CellRendererText(), text=15)
        colunaEmpresa1 = gtk.TreeViewColumn("Empresa",gtk.CellRendererText(), text=16)
        colunaCargo1 = gtk.TreeViewColumn("Cargo",gtk.CellRendererText(), text=17)
        colunaEnderecoEmpresa1 = gtk.TreeViewColumn("Endereco da Empresa",gtk.CellRendererText(), text=18)
        colunaTelefoneEmpresa1 = gtk.TreeViewColumn("Telefone da Empresa",gtk.CellRendererText(), text=19)
        colunaEmailFuncional1 = gtk.TreeViewColumn("Email ou Site",gtk.CellRendererText(), text=20)
        
        #Adicionando as colunas ao widget listaClientes
        self.listaClientes1.append_column(colunaCategoria1)
        self.listaClientes1.append_column(colunaNome1)
        self.listaClientes1.append_column(colunaCpf1)
        self.listaClientes1.append_column(colunaRg1)
        self.listaClientes1.append_column(colunaOrgaoEmissor1)
        self.listaClientes1.append_column(colunaNaturalidade1)
        self.listaClientes1.append_column(colunaDtNascimento1)
        self.listaClientes1.append_column(colunaNomeMae1)
        self.listaClientes1.append_column(colunaNomePai1)
        self.listaClientes1.append_column(colunaEstadoCivil1)
        self.listaClientes1.append_column(colunaRegimeCasamento1)
        self.listaClientes1.append_column(colunaTelefone1)
        self.listaClientes1.append_column(colunaCelular1)
        self.listaClientes1.append_column(colunaEmail1)
        self.listaClientes1.append_column(colunaEndereco1)
        self.listaClientes1.append_column(colunaProfissao1)
        self.listaClientes1.append_column(colunaEmpresa1)
        self.listaClientes1.append_column(colunaCargo1)
        self.listaClientes1.append_column(colunaEnderecoEmpresa1)
        self.listaClientes1.append_column(colunaTelefoneEmpresa1)
        self.listaClientes1.append_column(colunaEmailFuncional1)
        self.le_Cliente()
    
        #Definindo o TreeView para Funcionários
        self.listfun = gtk.ListStore(str, str, str, str, str,str,str,str, str, str, str, str,str, str)#número de colunas
        #Carrega o TreeView do Arquivo Interface.glade
        self.listaFuncionario = self.xml.get_widget('treeviewFuncionario')
        #Adiciona o Modelo ao Widget TreeView
        self.listaFuncionario.set_model(self.listfun)
        
        #Criando as colunas para pesquisa de funcionários.
        colunaNome2 = gtk.TreeViewColumn("Nome",gtk.CellRendererText(), text=0)
        colunaDataNascimento2 = gtk.TreeViewColumn("Data de Nascimento",gtk.CellRendererText(), text=1)
        colunaCpf2 = gtk.TreeViewColumn("CPF",gtk.CellRendererText(), text=2)
        colunaRg2 = gtk.TreeViewColumn("RG",gtk.CellRendererText(), text=3)
        colunaEstadoCicil2 = gtk.TreeViewColumn("Estado Civil",gtk.CellRendererText(), text=4)
        colunaFilhos2 = gtk.TreeViewColumn("N. de filhos",gtk.CellRendererText(), text=5)
        colunaGrauInstrucao2 = gtk.TreeViewColumn("Grau de Instrucao",gtk.CellRendererText(), text=6)
        colunaTelefone2 = gtk.TreeViewColumn("Telefone",gtk.CellRendererText(), text=7)
        colunaEmail2 = gtk.TreeViewColumn("Email",gtk.CellRendererText(), text=8)
        colunaRua2 = gtk.TreeViewColumn("Rua",gtk.CellRendererText(), text=9)
        colunaNum2 = gtk.TreeViewColumn("Numero",gtk.CellRendererText(), text=10)
        colunaBairro2 = gtk.TreeViewColumn("Bairro",gtk.CellRendererText(), text=11)
        colunaComplento2 = gtk.TreeViewColumn("Complemento",gtk.CellRendererText(), text=12)
        colunaOutras = gtk.TreeViewColumn("Outros",gtk.CellRendererText(), text=13)
        
        #Adicionando as colunas ao widget lista funcionários
        self.listaFuncionario.append_column(colunaNome2)
        self.listaFuncionario.append_column(colunaDataNascimento2)
        self.listaFuncionario.append_column(colunaCpf2)
        self.listaFuncionario.append_column(colunaRg2)
        self.listaFuncionario.append_column(colunaEstadoCicil2)
        self.listaFuncionario.append_column(colunaFilhos2)
        self.listaFuncionario.append_column(colunaGrauInstrucao2)
        self.listaFuncionario.append_column(colunaTelefone2)
        self.listaFuncionario.append_column(colunaEmail2)
        self.listaFuncionario.append_column(colunaRua2)
        self.listaFuncionario.append_column(colunaNum2)
        self.listaFuncionario.append_column(colunaBairro2)
        self.listaFuncionario.append_column(colunaComplento2)
        self.listaFuncionario.append_column(colunaOutras)
        self.le_Funcionario()
        
        #Definindo treeview para aluguel
        self.listAluguel = gtk.ListStore(str, str, str, str, str,str,str,str, str, str, str, str,str,str,str,str, str, str, str, str,str,str,str, str, str, str, str,str,str,str,str, str, str, str, str,str,str,str, str, str, str, str,str,str,str)#número de colunas
        self.listaAluguel = self.xml.get_widget('treeviewAluguel')
        self.listaAluguel.set_model(self.listAluguel)
        
        #Criando as colunas para pesquisa de aluguel aluguel 
        colunaLocador = gtk.TreeViewColumn("Locador",gtk.CellRendererText(), text=0)
        colunaLocatario = gtk.TreeViewColumn("Locatario",gtk.CellRendererText(), text=1)
        colunanumeroIMV = gtk.TreeViewColumn("Registro do Imovel",gtk.CellRendererText(), text=2)
        colunafinalidadeIMV = gtk.TreeViewColumn("Finalidade",gtk.CellRendererText(), text=3)
        colunaprazoIMV = gtk.TreeViewColumn("Prazp de locacao",gtk.CellRendererText(), text=4)
        colunainicioIMV = gtk.TreeViewColumn("Inicio",gtk.CellRendererText(), text=5)
        colunaterminoIMV = gtk.TreeViewColumn("Termino",gtk.CellRendererText(), text=6)
        colunavencimentoIMV = gtk.TreeViewColumn("Data de vencimento",gtk.CellRendererText(), text=7)
        colunavalorIMV = gtk.TreeViewColumn("Valor",gtk.CellRendererText(), text=8)
        colunafiador1 = gtk.TreeViewColumn("Fiado 1",gtk.CellRendererText(), text=9)
        colunacpf1 = gtk.TreeViewColumn("CPF",gtk.CellRendererText(), text=10)
        colunarg1 = gtk.TreeViewColumn("RG",gtk.CellRendererText(), text=11)
        colunadtnascimento1 = gtk.TreeViewColumn("Data de Nascimento",gtk.CellRendererText(), text=12)
        colunaestCivil1 = gtk.TreeViewColumn("Estado Cívil",gtk.CellRendererText(), text=13)
        colunaregCasamento1 = gtk.TreeViewColumn("Regime de Casamento",gtk.CellRendererText(), text=14)
        colunaesposa1 = gtk.TreeViewColumn("Nome do conjugue",gtk.CellRendererText(), text=15)
        colunadtEsposa1 = gtk.TreeViewColumn("Data de nascimento",gtk.CellRendererText(), text=16)
        colunacpfEsposa1 = gtk.TreeViewColumn("CPF",gtk.CellRendererText(), text=17)
        colunargEsposa1 = gtk.TreeViewColumn("RG",gtk.CellRendererText(), text=18)
        colunaendereco1 = gtk.TreeViewColumn("Endereço",gtk.CellRendererText(), text=19)
        colunanumero1 = gtk.TreeViewColumn("Numero",gtk.CellRendererText(), text=20)
        colunabairro1 = gtk.TreeViewColumn("Bairro",gtk.CellRendererText(), text=21)
        colunacidade1 = gtk.TreeViewColumn("Cidade",gtk.CellRendererText(), text=22)
        colunaestado1 = gtk.TreeViewColumn("Estado",gtk.CellRendererText(), text=23)
        colunaprofissao1 = gtk.TreeViewColumn("Profissao",gtk.CellRendererText(), text=24)
        colunarenda1 = gtk.TreeViewColumn("Renda",gtk.CellRendererText(), text=25)
        colunaadiciais1 = gtk.TreeViewColumn("Outras Informacoes",gtk.CellRendererText(), text=26)
        colunafiador2 = gtk.TreeViewColumn("Fiador 2",gtk.CellRendererText(), text=27)
        colunacpf2 = gtk.TreeViewColumn("CPF",gtk.CellRendererText(), text=28)
        colunarg2 = gtk.TreeViewColumn("RG",gtk.CellRendererText(), text=29)
        colunadtnascimento2 = gtk.TreeViewColumn("Data de Nascimento",gtk.CellRendererText(), text=30) 
        colunaestCivil2 = gtk.TreeViewColumn("Estado Civil",gtk.CellRendererText(), text=31)
        colunaregCivil2 = gtk.TreeViewColumn("Regime de Casamento",gtk.CellRendererText(), text=32)
        colunaesposa2 = gtk.TreeViewColumn("Nome do Conjugue",gtk.CellRendererText(), text=33)
        colunadtEsposa2 = gtk.TreeViewColumn("Data de Nascimento",gtk.CellRendererText(), text=34)
        colunacpfEsposa2 = gtk.TreeViewColumn("CPF",gtk.CellRendererText(), text=35)
        colunargEsposa2 = gtk.TreeViewColumn("RG",gtk.CellRendererText(), text=36)
        colunaendereco2 = gtk.TreeViewColumn("Endereco",gtk.CellRendererText(), text=37)
        colunanumero2 = gtk.TreeViewColumn("Numero",gtk.CellRendererText(), text=38)
        colunabairro2 = gtk.TreeViewColumn("Bairro",gtk.CellRendererText(), text=39)
        colunacidade2 = gtk.TreeViewColumn("Cidade",gtk.CellRendererText(), text=40)
        colunaestado2 = gtk.TreeViewColumn("Estado",gtk.CellRendererText(), text=41)
        colunaprofissao2 = gtk.TreeViewColumn("Profissao",gtk.CellRendererText(), text=42)
        colunarenda2 = gtk.TreeViewColumn("Renda",gtk.CellRendererText(), text=43)
        colunaadiciais2 = gtk.TreeViewColumn("Outras Informaçoes",gtk.CellRendererText(), text=44)
        
        #Adicionando as colunas ao treeview
        self.listaAluguel.append_column(colunaLocador)
        self.listaAluguel.append_column(colunaLocatario)
        self.listaAluguel.append_column(colunanumeroIMV)
        self.listaAluguel.append_column(colunafinalidadeIMV)
        self.listaAluguel.append_column(colunaprazoIMV)
        self.listaAluguel.append_column(colunainicioIMV)
        self.listaAluguel.append_column(colunaterminoIMV)
        self.listaAluguel.append_column(colunavencimentoIMV)
        self.listaAluguel.append_column(colunavalorIMV)
        self.listaAluguel.append_column(colunafiador1)
        self.listaAluguel.append_column(colunacpf1)
        self.listaAluguel.append_column(colunarg1)
        self.listaAluguel.append_column(colunadtnascimento1)
        self.listaAluguel.append_column(colunaestCivil1)
        self.listaAluguel.append_column(colunaregCasamento1)
        self.listaAluguel.append_column(colunaesposa1)
        self.listaAluguel.append_column(colunadtEsposa1)
        self.listaAluguel.append_column(colunacpfEsposa1)
        self.listaAluguel.append_column(colunargEsposa1)
        self.listaAluguel.append_column(colunaendereco1)
        self.listaAluguel.append_column(colunanumero1)
        self.listaAluguel.append_column(colunabairro1)
        self.listaAluguel.append_column(colunacidade1)
        self.listaAluguel.append_column(colunaestado1)
        self.listaAluguel.append_column(colunaprofissao1)
        self.listaAluguel.append_column(colunarenda1)
        self.listaAluguel.append_column(colunaadiciais1)
        self.listaAluguel.append_column(colunafiador2)
        self.listaAluguel.append_column(colunacpf2)
        self.listaAluguel.append_column(colunarg2)
        self.listaAluguel.append_column(colunadtnascimento2)
        self.listaAluguel.append_column(colunaestCivil2)
        self.listaAluguel.append_column(colunaregCivil2)
        self.listaAluguel.append_column(colunaesposa2)
        self.listaAluguel.append_column(colunadtEsposa2)
        self.listaAluguel.append_column(colunacpfEsposa2)
        self.listaAluguel.append_column(colunargEsposa2)
        self.listaAluguel.append_column(colunaendereco2)
        self.listaAluguel.append_column(colunanumero2)
        self.listaAluguel.append_column(colunabairro2)
        self.listaAluguel.append_column(colunacidade2)
        self.listaAluguel.append_column(colunaestado2)
        self.listaAluguel.append_column(colunaprofissao2)
        self.listaAluguel.append_column(colunarenda2)
        self.listaAluguel.append_column(colunaadiciais2)
        self.le_Aluguel()
                    
        #Treeview Vendas
        self.listVenda = gtk.ListStore(str,str,str,str,str,str,str,str,str,str,str,str,str,str,str,str,str,str,str,str,str,str,str,str,str,str,str)
        self.listaVenda = self.xml.get_widget('treeviewVendas')
        self.listaVenda.set_model(self.listVenda)
        #Criando as colunas para pesquisar Venda
        colunavendedor = gtk.TreeViewColumn("Nome: Vendedor",gtk.CellRendererText(), text=0)
        colunacpfvendedor = gtk.TreeViewColumn("CPF",gtk.CellRendererText(), text=1)
        colunargvenderdor = gtk.TreeViewColumn("RG",gtk.CellRendererText(), text=2)
        colunanaturalidadevendedor = gtk.TreeViewColumn("Naturalidade",gtk.CellRendererText(), text=3)
        colunaecvendedor = gtk.TreeViewColumn("Estado civil",gtk.CellRendererText(), text=4)
        colunaprofissaovend = gtk.TreeViewColumn("Profissao",gtk.CellRendererText(), text=5)
        colunaenderecovendedor = gtk.TreeViewColumn("Endereco",gtk.CellRendererText(), text=6)
        colunanumerovendedor = gtk.TreeViewColumn("Numero",gtk.CellRendererText(), text=7)
        colunabairrovendedor = gtk.TreeViewColumn("Bairro",gtk.CellRendererText(), text=8)
        colunacepvendedor = gtk.TreeViewColumn("CEP",gtk.CellRendererText(), text=9)
        colunacidadevendedor = gtk.TreeViewColumn("Cidade",gtk.CellRendererText(), text=10)
        colunaestadovendedor = gtk.TreeViewColumn("Estado",gtk.CellRendererText(), text=11)
        colunacomprador = gtk.TreeViewColumn("Nome: Comprador",gtk.CellRendererText(), text=12)
        colunacpfcomprador = gtk.TreeViewColumn("CPF",gtk.CellRendererText(), text=13)
        colunargcomprador = gtk.TreeViewColumn("RG",gtk.CellRendererText(), text=14)
        colunanaturalidadecomprador = gtk.TreeViewColumn("Naturalidade",gtk.CellRendererText(), text=15)
        colunaeccomprador = gtk.TreeViewColumn("Estado Civil",gtk.CellRendererText(), text=16)
        colunaprofissaocomprador = gtk.TreeViewColumn("Profissao",gtk.CellRendererText(), text=17)
        colunaenderecocomprador = gtk.TreeViewColumn("Endereco",gtk.CellRendererText(), text=18)
        colunanumerocomprador = gtk.TreeViewColumn("Numero",gtk.CellRendererText(), text=19)
        colunabairrocomprador = gtk.TreeViewColumn("Bairro",gtk.CellRendererText(), text=20)
        colunacepcomprador = gtk.TreeViewColumn("CEP",gtk.CellRendererText(), text=21)
        colunacidadecomprador = gtk.TreeViewColumn("Cidade",gtk.CellRendererText(), text=22)
        colunaestadocomprador = gtk.TreeViewColumn("Estado",gtk.CellRendererText(), text=23)
        colunaareavenda = gtk.TreeViewColumn("Area do Imovel",gtk.CellRendererText(), text=24)
        colunaregistovenda = gtk.TreeViewColumn("Registro de venda",gtk.CellRendererText(), text=25)
        colunavalorvenda = gtk.TreeViewColumn("Valor",gtk.CellRendererText(), text=26)

        #Adicionando as colunas ao lista ventas
        self.listaVenda.append_column(colunavendedor)
        self.listaVenda.append_column(colunacpfvendedor)
        self.listaVenda.append_column(colunargvenderdor)
        self.listaVenda.append_column(colunanaturalidadevendedor)
        self.listaVenda.append_column(colunaecvendedor)
        self.listaVenda.append_column(colunaprofissaovend)
        self.listaVenda.append_column(colunaenderecovendedor)
        self.listaVenda.append_column(colunanumerovendedor)
        self.listaVenda.append_column(colunabairrovendedor)
        self.listaVenda.append_column(colunacepvendedor)
        self.listaVenda.append_column(colunacidadevendedor)
        self.listaVenda.append_column(colunaestadovendedor)
        self.listaVenda.append_column(colunacomprador)
        self.listaVenda.append_column(colunacpfcomprador)
        self.listaVenda.append_column(colunargcomprador)
        self.listaVenda.append_column(colunanaturalidadecomprador)
        self.listaVenda.append_column(colunaeccomprador)
        self.listaVenda.append_column(colunaprofissaocomprador)
        self.listaVenda.append_column(colunaenderecocomprador)
        self.listaVenda.append_column(colunanumerocomprador)
        self.listaVenda.append_column(colunabairrocomprador)
        self.listaVenda.append_column(colunacepcomprador)
        self.listaVenda.append_column(colunacidadecomprador)
        self.listaVenda.append_column(colunaestadocomprador)
        self.listaVenda.append_column(colunaareavenda)
        self.listaVenda.append_column(colunaregistovenda)
        self.listaVenda.append_column(colunavalorvenda)  
        self.le_Venda()
        
        #Definindo TreeView Login
        self.listLogin = gtk.ListStore(str,str,str)
        self.listaLogin = self.xml.get_widget('treeviewPesquisaLogin')
        self.listaLogin.set_model(self.listLogin)
        #Criando as colunas de clientes.
        colunaLogin = gtk.TreeViewColumn("Login",gtk.CellRendererText(), text=0)
        colunaSenha = gtk.TreeViewColumn("Senha",gtk.CellRendererText(), text=1)
        colunaFuncao = gtk.TreeViewColumn("Funçao",gtk.CellRendererText(), text=2)
        #adicionando as colunas ao treeview de login
        self.listaLogin.append_column(colunaLogin)
        self.listaLogin.append_column(colunaSenha)
        self.listaLogin.append_column(colunaFuncao)
        self.le_Login()
        
        #Criando dicionário para conectar os sinais dos botões.
        dic = {"on_btnSalvarImovel_clicked" : self.ValidarImovel,
               "on_btnSalvarAluguel_clicked" : self.ValidarAluguel,
               "on_btnSalvarFuncionario_clicked" : self.ValidarFuncionario,
               "on_btnSalvarCliAdm_clicked" : self.ValidarClientes,
               "on_btnSalvarVenda_clicked" : self.ValidarVenda,
               "on_btnSalvarLogin_clicked":self.ValidarLogin,
               "on_btnPesquisarImovel_clicked" : self.PesquisarImovel,
               "on_btnPesquisarFuncionario_clicked" : self.PesquisarFuncionario,
               "on_btnPesquisarCliente_clicked" : self.PesquisarCliente,
               "on_btnPesquisarAluguel_clicked" : self.PesquisarAluguel,
               "on_btnPesquisarVenda_clicked" : self.PesquisarVenda,
               "on_btnPesquisarLogin_clicked" : self.PesquisarLogin,
               "on_btnEditarFun_clicked" : self.SelecionarFuncionario,
               "on_btnEditarImovel_clicked" : self.SelecionarImovel,
               "on_btnEditarCliente_clicked" : self.SelecionarCliente,
               "on_btnEditarAluguel_clicked" : self.SelecionarAluguel,
               "on_btnEditarVenda_clicked" : self.SelecionarVenda, 
               "on_btnEditarLogin_clicked" : self.SelecionarLogin,
               "on_btnExcluirImovel_clicked" : self.RemoverImovel,
               "on_btnExcluirCliente_clicked" : self.RemoverCliente,
               "on_btnExcluirAluguel_clicked" : self.RemoverAluguel,
               "on_btnExcluirVenda_clicked" : self.RemoverVenda,
               "on_btnExcluirFunc_clicked" : self.RemoverFuncionario,
               "on_btnExcluirLogin_clicked" : self.RemoverLogin,
               "on_btnContratoVenda_clicked" : self.novoContratoVenda,
               "on_btnGerarPDF_clicked" : self.novoContratoAluguel,
               
            }
        
        #Conecta os sinais aos elementos da janela Manager
        self.xml.signal_autoconnect(dic)
        #Torna a janela Manaer visível
        self.windowManager.show_all()
        
    def le_Imovel(self):
        #Seleciona os dados da tabela imóveis, faz uma iteração na lista de dados e adiciona ao liststore de imóveis  
        cursor.execute("SELECT * FROM imoveis")
        resultado3 = cursor.fetchall()
        self.liststore3.clear()#Limpa os dados antigos do liststore
        for row in resultado3:
            imovelProprietario = row[1]
            escritura = row[2]
            cartorio = row[3]
            cidadeCartorio = row[4]
            rua = row[5]
            num = row[6]
            cep = row[7]
            bairro = row[8]
            complemento = row[9]
            cidadeImovel = row[10]
            uf = row[11]
            descricao = row[12]
            categoriaImovel = row[13]
            dormitorio = row[14]
            suite = row[15]
            copa = row[16]
            garagem = row[17]
            salaJantar = row[18]
            salaEstar = row[19]
            banheiro = row[20]
            areaTotal = row[21]
            outrosDados = row[22]
            valor = row[23]
            self.liststore3.append([imovelProprietario,escritura,cartorio,cidadeCartorio,rua,num,cep,bairro,complemento,cidadeImovel,uf,descricao,categoriaImovel,dormitorio,suite,copa,garagem,salaJantar,salaEstar,banheiro,areaTotal,outrosDados,valor])

    def le_Aluguel(self):
        #Seleciona os dados da tabela alugue, faz uma iteração na lista de dados e adiciona ao liststore de aluguel  
        cursor.execute("SELECT * FROM alugue")
        resultado7 = cursor.fetchall()
        self.listAluguel.clear()#Limpa os dados antigos do liststore
        for row in resultado7:
            locador_row = row[1]
            locatario_row = row[2]
            registro_row = row[3]
            finalidade_row = row[4]
            prazo_row = row[5]
            inicio_row = row[6]
            termino_row = row[7]
            vencimento_row = row[8]
            valor_row = row[9]
            fiador1_row = row[10]
            cpf1_row = row[11]
            rg1_row = row[12]
            dtnascimento1_row = row[13]
            estcivil1_row = row[14]
            regcasamento1_row = row[15]
            conjugue1_row = row[16]
            dtconjugue1_row = row[17]
            cpfconjugue1_row = row[18]
            rgconjugue1_row = row[19]
            endereco1_row = row[20]
            num1_row = row[21]
            bairro1_row = row[22]
            cidade1_row = row[23]
            estado1_row = row[24]
            prof1_row = row[25]
            renda1_row = row[26]
            out1_row = row[27]
            fiador2_row = row[28]
            cpf2_row = row[29]
            rg2_row = row[30]
            dtnascimento2_row = row[31]
            estcivil2_row = row[32]
            regcasamento2_row = row[33]
            conjugue2_row = row[34]
            dtconjugue2_row = row[35]
            cpfconjugue2_row = row[36]
            regconjugue2_row =  row[37]
            endereco2_row = row[38]
            num2_row = row[39]
            bairro2_row = row[40]
            cidade2_row = row[41]
            estado2_row = row[42]
            prof2_row = row[43]
            renda2_row = row[44]
            out2_row = row[45]
            self.listAluguel.append([locador_row,locatario_row,registro_row,finalidade_row,prazo_row,inicio_row,termino_row,vencimento_row,valor_row,fiador1_row,cpf1_row,rg1_row,dtnascimento1_row,estcivil1_row,regcasamento1_row,conjugue1_row,dtconjugue1_row,cpfconjugue1_row,rgconjugue1_row,endereco1_row,num1_row,bairro1_row,cidade1_row,estado1_row,prof1_row,renda1_row,out1_row,fiador2_row,cpf2_row,rg2_row,dtnascimento2_row,estcivil2_row,regcasamento2_row,conjugue2_row,dtconjugue2_row,cpfconjugue2_row,regconjugue2_row,endereco2_row,num2_row,bairro2_row,cidade2_row,estado2_row,prof2_row,renda2_row,out2_row])

    def le_Venda(self):
        #Seleciona os dados da tabela Venda, faz uma iteração na lista de dados e adiciona ao liststore de venda
        cursor.execute("SELECT * FROM venda")
        resultado8 = cursor.fetchall()
        self.listVenda.clear()#Limpa todos os dados antigos do liststore.
        for row in resultado8:
            vendedor_vend = row[1]
            cpf_vend = row[2]
            rg_vend = row[3]
            naturalidade_vend = row[4]
            estcivil_vend = row[5]
            profissao_vend = row[6]
            endereco_vend = row[7]
            numero_vend = row[8]
            bairro_vend = row[9]
            cepvend_vend = row[10]
            cidade_vend = row[11]
            estado_vend = row[12]
            comprador_vend = row[13]
            cpfCP_vend = row[14]
            rgCP_vend = row[15]
            naturalidadeCP_vend = row[16]
            estcivilCP_vend = row[17]
            profCP_vend = row[18]
            enderecoCP_vend = row[19]
            numeroCP_vend = row[20]
            bairroCP_vend = row[21]
            cepCP_vend = row[22]
            cidadeCP_vend = row[23]
            estadoCP_vend = row[24]
            area_vend = row[25]
            registro_vend = row[26]
            valor_vend = row[27]
            self.listVenda.append([vendedor_vend,cpf_vend,rg_vend,naturalidade_vend,estcivil_vend,profissao_vend,endereco_vend,numero_vend,bairro_vend,cepvend_vend,cidade_vend,estado_vend,comprador_vend,cpfCP_vend,rgCP_vend,naturalidadeCP_vend,estcivilCP_vend,profCP_vend,enderecoCP_vend,numeroCP_vend,bairroCP_vend,cepCP_vend,cidadeCP_vend,estadoCP_vend,area_vend,registro_vend,valor_vend])

    def le_Cliente(self):
        #Seleciona os dados da tabela Cliente, faz uma iteração na lista de dados e adiciona ao liststore de Cliente
        cursor.execute("SELECT * FROM clientes")
        resultado4 = cursor.fetchall()
        self.listStore4.clear()#Limpa os dados antigos do liststore
        for row in resultado4:
            clienteCategoria = row[1]
            nome = row[2]
            cpf = row[3]
            rg = row[4]
            orgaoEmisso = row[4]
            naturalidade = row[6]
            dtNascimento = row[7]
            nomeMae = row[8]
            nomePai = row[9]
            estadoCivil = row[10]
            regimeCasamento = row[11]
            telefone = row[12]
            celular = row[13]
            email = row[14]
            endereco = row[15]
            profissao = row[16]
            empresa = row[17]
            cargo = row[18]
            enderecoEmpresa = row[19]
            telefoneEmpresa = row[20]
            emailFuncional = row[21]
            self.listStore4.append([clienteCategoria,nome,cpf,rg,orgaoEmisso,naturalidade,dtNascimento,nomeMae,nomePai,estadoCivil,regimeCasamento,telefone,celular,email,endereco,profissao,empresa,cargo,enderecoEmpresa,telefoneEmpresa,emailFuncional])

    def le_Funcionario(self):
        #Seleciona os dados da tabela funcionarios, faz uma iteração na lista de dados e adiciona ao liststore de funcionarios 
        cursor.execute("SELECT * FROM funcionarios")
        resultado6 = cursor.fetchall()
        self.listfun.clear()#Limpa todos os dados antigos do liststore
        for row in resultado6:
            nome2 = row[1]
            dataNascimento2 = row[2]
            cpf2 = row[3]
            rg2 = row[4]
            estadoCivil2 = row[5]
            filhos2 = row[6]
            grauInstrucao2 = row[7]
            telefone2 = row[8]
            email2 = row[9]
            rua2 = row[10]
            num2 = row[11]
            bairro2 = row[12]
            complemento2 = row[13]
            outras2 = row[14]
            self.listfun.append([nome2,dataNascimento2,cpf2,rg2,estadoCivil2,filhos2,grauInstrucao2,telefone2,email2,rua2,num2,bairro2,complemento2,outras2])

    def le_Login(self):
        #Seleciona os dados da tabela login, faz uma iteração na lista de dados e adiciona ao liststore de login
        cursor.execute("SELECT * FROM login")
        resultado9 = cursor.fetchall()
        self.listLogin.clear()#Limpa todos os dados antigos do liststore
        for row in resultado9:
            login_row = row[1]
            senha_row = row[2]
            funcao_row = row[3]
            self.listLogin.append([login_row,senha_row,funcao_row])

    def ValidarImovel(self, widget):
        #Carrega a statusbar  
        self.statusbarImovel = self.xml.get_widget("statusbarImovel")
        self.context = self.statusbarImovel.get_context_id("")
        ##Validar se todos os campos da aba imoveis estão preenchidos e inserir no banco de dados, retornar uma mensagem de erro caso não estejar.
        if(self.proprietario.get_text() == "" or self.escritura.get_text() == "" or self.cartorio.get_text() == "" or self.cidadeCartorio.get_text() == "" or self.rua.get_text() == ""\
        or self.num.get_text() == "" or self.cep.get_text() == "" or self.bairro.get_text() == "" or self.complemento.get_text() == "" or self.cidadeImovel.get_text() == "" or self.uf.get_text() == ""\
        or self.descrissao.get_text() == "" or self.categoria.get_text() == "" or self.dormitorio.get_text() == "" or self.suite.get_text() == "" or self.copa.get_text() == "" or self.garagem.get_text() == ""\
        or self.salaJantar.get_text() == "" or self.salaEstar.get_text() == "" or self.banheiro.get_text() == "" or self.areaTotal.get_text() == "" or self.outrosDados.get_text() == "" or self.valor.get_text() == ""):
            self.statusbarImovel.push(self.context,"Todos os campos devem ser preenchidos!")
        else:
            cursor.execute("INSERT INTO imoveis(proprietario,numeroescritura,cartorio,cidade,rua,numero,cep,bairro,complemento,cidadeimovel,uf,descrissao,categoria,domitorio,suite,copa,garagem,salajantar,salaestar,banheiro,areatotal,outrosdados,valorproprietario)\
                    VALUES ('"+self.proprietario.get_text()+"','"+self.escritura.get_text()+"','"+self.cartorio.get_text()+"','"+self.cidadeCartorio.get_text()+"','"+self.rua.get_text()+"','"+self.num.get_text()+"','"+self.cep.get_text()+"','"+self.bairro.get_text()+"','"+self.complemento.get_text()+"','"+self.cidadeImovel.get_text()+"','"+self.uf.get_text()+"','"+self.descrissao.get_text()+"','"+self.categoria.get_text()+"','"+self.dormitorio.get_text()+"','"+self.suite.get_text()+"','"+self.copa.get_text()+"','"+self.garagem.get_text()+"','"+self.salaJantar.get_text()+"','"+self.salaEstar.get_text()+"','"+self.banheiro.get_text()+"','"+self.areaTotal.get_text()+"','"+self.outrosDados.get_text()+"','"+self.valor.get_text()+"')")
            connection.commit()
            self.le_Imovel() #Chama função para atualizar o treeview
            msg = gtk.MessageDialog(None, 0, gtk.MESSAGE_INFO, gtk.BUTTONS_OK, 'Cadastro realizado com Sucesso!!!')
            msg.run()
            msg.destroy()

            #Limpar os campos
            self.proprietario.props.text = ""
            self.escritura.props.text = ""
            self.cartorio.props.text = ""
            self.cidadeCartorio.props.text = ""
            self.rua.props.text = ""
            self.num.props.text = ""
            self.cep.props.text = ""
            self.bairro.props.text = ""
            self.complemento.props.text = ""
            self.cidadeImovel.props.text = ""
            self.uf.props.text = ""
            self.descrissao.props.text = ""
            self.categoria.props.text = ""
            self.dormitorio.props.text = ""
            self.suite.props.text = ""
            self.copa.props.text = ""
            self.garagem.props.text = ""
            self.salaJantar.props.text = ""
            self.salaEstar.props.text = ""
            self.banheiro.props.text = ""
            self.areaTotal.props.text = ""
            self.outrosDados.props.text = ""
            self.valor.props.text = ""

    def ValidarAluguel(self, widget):
        #Carrega a statusbar
        self.statusbarAluguel = self.xml.get_widget("statusbarAluguel")
        self.contextoo = self.statusbarAluguel.get_context_id("")
        #Validar se todos os campos da aba aluguel estão preenchidos e inserir no banco de dados, retornar uma mensagem de erro caso não estejar.
        if(self.locador.get_text() == "" or self.locatario.get_text() == "" or self.numeroIMV.get_text() == "" or self.finalidadeIMV.get_text() == "" or self.prazoIMV.get_text() == "" \
           or self.valorIMV.get_text() == "" or self.inicioIMV.get_text() == "" or self.terminoIMV.get_text() == "" or self.vencimentoIMV.get_text() == "" or self.fiador1.get_text() == "" \
           or self.cpf1.get_text() == "" or self.rg1.get_text() == "" or self.dtnascimento1.get_text() == "" or self.estCivil1.get_text() == "" or self.regCivil1.get_text() == "" \
           or self.esposa1.get_text() == "" or self.dtEsposa1.get_text() == "" or self.cpfEsposa1.get_text() == "" or self.rgEsposa1.get_text() == "" or self.endereco1.get_text() == "" \
           or self.numero1.get_text() == "" or self.bairro1.get_text() == "" or self.cidade1.get_text() == "" or self.estado1.get_text() == "" or self.profissao1.get_text() == "" \
           or self.renda1.get_text() == "" or self.adiciais1.get_text() == "" or self.fiador2.get_text() == "" or self.cpf2.get_text() == "" or self.rg2.get_text() == "" \
           or self.dtnascimento2.get_text() == "" or self.estCivil2.get_text() == "" or self.regCivil2.get_text() == "" or self.esposa2.get_text() == "" or self.dtEsposa2.get_text() == "" \
           or self.cpfEsposa2.get_text() == "" or self.rgEsposa2.get_text() == "" or self.endereco2.get_text() == "" or self.numero2.get_text() == "" or self.bairro2.get_text() == "" \
           or self.cidade2.get_text() == "" or self.estado2.get_text() == "" or self.profissao2.get_text() == "" or self.renda2.get_text() == "" or self.adicionais2.get_text() == "" ):
            self.statusbarAluguel.push(self.contextoo, "Todos os campos devem ser preenchidos!")
            
        else:
            cursor.execute("INSERT INTO alugue(locador,locatario,numeroimv,finalidadeimv,prazoimv,inicioimv,terminoimv,vencimentoimv,valorimv,fiador1,cpf1,rg1,dtnascimento1,estcivil1,regcivil1,esposa1,dtesposa1,cpfesposa1,rgesposa1,endereco1,numero1,bairro1,cidade1,estado1,profissao1,renda1,adiciais1,fiador2,cpf2,rg2,dtnascimento2,estcivil2,regcivil2,esposa2,dtesposa2,cpfesposa2,rgesposa2,endereco2,numero2,bairro2,cidade2,estado2,profissao2,renda2,adicionais2)\
            VALUES ('"+self.locador.get_text()+"','"+self.locatario.get_text()+"','"+self.numeroIMV.get_text()+"','"+self.finalidadeIMV.get_text()+"','"+self.prazoIMV.get_text()+"','"+self.valorIMV.get_text()+"','"+self.inicioIMV.get_text()+"','"+self.terminoIMV.get_text()+"','"+self.vencimentoIMV.get_text()+"','"+self.fiador1.get_text()+"','"+self.cpf1.get_text()+"','"+self.rg1.get_text()+"','"+self.dtnascimento1.get_text()+"','"+self.estCivil1.get_text()+"','"+self.regCivil1.get_text()+"','"+self.esposa1.get_text()+"','"+self.dtEsposa1.get_text()+"','"+self.cpfEsposa1.get_text()+"','"+self.rgEsposa1.get_text()+"','"+self.endereco1.get_text()+"','"+self.numero1.get_text()+"','"+self.bairro1.get_text()+"','"+self.cidade1.get_text()+"','"+self.estado1.get_text()+"','"+self.profissao1.get_text()+"','"+self.renda1.get_text()+"','"+self.adiciais1.get_text()+"','"+self.fiador2.get_text()+"','"+self.cpf2.get_text()+"','"+self.rg2.get_text()+"','"+self.dtnascimento2.get_text()+"','"+self.estCivil2.get_text()+"','"+self.regCivil2.get_text()+"','"+self.esposa2.get_text()+"','"+self.cpfEsposa2.get_text()+"','"+self.rgEsposa2.get_text()+"','"+self.dtEsposa1.get_text()+"','"+self.endereco2.get_text()+"','"+self.numero2.get_text()+"','"+self.bairro2.get_text()+"','"+self.cidade2.get_text()+"','"+self.estado2.get_text()+"','"+self.profissao2.get_text()+"','"+self.renda2.get_text()+"','"+self.adicionais2.get_text()+"')")
            connection.commit()
            self.le_Aluguel()#chama função para atualizar o treeview
            msg = gtk.MessageDialog(None, 0, gtk.MESSAGE_INFO, gtk.BUTTONS_OK, 'Cadastro realizado com Sucesso!!!')
            msg.run()
            msg.destroy()

            #Limpando os campos 
            self.locador.props.text = ""
            self.locatario.props.text = ""
            self.numeroIMV.props.text = ""
            self.finalidadeIMV.props.text = ""
            self.prazoIMV.props.text = ""
            self.inicioIMV.props.text = ""
            self.terminoIMV.props.text = ""
            self.vencimentoIMV.props.text = ""
            self.valorIMV.props.text = ""
            self.fiador1.props.text = ""
            self.cpf1.props.text = ""
            self.rg1.props.text = ""
            self.dtnascimento1.props.text = ""
            self.estCivil1.props.text = ""
            self.regCivil1.props.text = ""
            self.esposa1.props.text = ""
            self.dtEsposa1.props.text = ""
            self.cpfEsposa1.props.text = ""
            self.rgEsposa1.props.text = ""
            self.endereco1.props.text = ""
            self.numero1.props.text = ""
            self.bairro1.props.text = ""
            self.cidade1.props.text = ""
            self.estado1.props.text = ""
            self.profissao1.props.text = ""
            self.renda1.props.text = ""
            self.adiciais1.props.text = ""
            self.fiador2.props.text = ""
            self.cpf2.props.text = ""
            self.rg2.props.text = ""
            self.dtnascimento2.props.text = ""
            self.estCivil2.props.text = ""
            self.regCivil2.props.text = ""
            self.esposa2.props.text = ""
            self.dtEsposa2.props.text = ""
            self.cpfEsposa2.props.text = ""
            self.rgEsposa2.props.text = ""
            self.endereco2.props.text = ""
            self.numero2.props.text = ""
            self.bairro2.props.text = ""
            self.cidade2.props.text = ""
            self.estado2.props.text = ""
            self.profissao2.props.text = ""
            self.renda2.props.text = ""
            self.adicionais2.props.text = "" 

    def ValidarVenda(self, widget):
        #Carregando a statusbar venda
        self.statusbarVenda = self.xml.get_widget("statusbarvenda")
        self.contextt = self.statusbarVenda.get_context_id("")
        #Validar se todos os campos da aba venda estão preenchidos e inserir no banco de dados, retornar uma mensagem de erro caso não estejar.
        if(self.vendedor.get_text() == "" or self.cpfvendedor.get_text() == "" or self.rgvenderdor.get_text() == "" or self.naturalidadevendedor.get_text() == "" \
           or self.ecvendedor.get_text() == "" or self.profissaovend.get_text() == "" or self.enderecovendedor.get_text() == "" or self.numerovendedor.get_text() == "" \
           or self.bairrovendedor.get_text() == "" or self.cepvendedor.get_text() == "" or self.cidadevendedor.get_text() == "" or self.estadovendedor.get_text() == "" \
           or self.comprador.get_text() == "" or self.cpfcomprador.get_text() == "" or self.rgcomprador.get_text() == "" or self.naturalidadecomprador.get_text() == "" \
           or self.eccomprador.get_text() == "" or self.profissaocomprador.get_text() == "" or self.enderecocomprador.get_text() == "" or self.numerocomprador.get_text() == "" \
           or self.bairrocomprador.get_text() == "" or self.cepcomprador.get_text() == "" or self.cidadecomprador.get_text() == "" or self.estadocomprador.get_text() == "" \
           or self.areavenda.get_text() == "" or self.registovenda.get_text() == "" or self.valorvenda.get_text() == ""):
            self.statusbarVenda.push(self.contextt, "Todos os campos devem ser preenchidos!")
        else:
            cursor.execute("INSERT INTO venda (vendedor,cpfvendedor,rgvendedor,naturalidadevendedor,ecvendedor,profissaovend,enderecovendedor,numerovendedor,bairrovendedor,cepvendedor,cidadevendedor,estadovendedor,comprador,cpfcomprador,rgcomprador,naturalidadecomprador,eccomprador,profissaocomprador,enderecocomprador,numerocomprador,bairrocomprador,cepcomprador,cidadecomprador,estadocomprador,areavenda,registovenda,valorvenda)VALUES('"+self.vendedor.get_text()+"','"+self.cpfvendedor.get_text()+"','"+self.rgvenderdor.get_text()+"','"+self.naturalidadevendedor.get_text()+"','"+self.ecvendedor.get_text()+"','"+self.profissaovend.get_text()+"','"+self.enderecovendedor.get_text()+"','"+self.numerovendedor.get_text()+"','"+self.bairrovendedor.get_text()+"','"+self.cepvendedor.get_text()+"','"+self.cidadevendedor.get_text()+"','"+self.estadovendedor.get_text()+"','"+self.comprador.get_text()+"','"+self.cpfcomprador.get_text()+"','"+self.rgcomprador.get_text()+"','"+self.naturalidadecomprador.get_text()+"','"+self.eccomprador.get_text()+"','"+self.profissaocomprador.get_text()+"','"+self.enderecocomprador.get_text()+"','"+self.numerocomprador.get_text()+"','"+self.bairrocomprador.get_text()+"','"+self.cepcomprador.get_text()+"','"+self.cidadecomprador.get_text()+"','"+self.estadocomprador.get_text()+"','"+self.areavenda.get_text()+"','"+self.registovenda.get_text()+"','"+self.valorvenda.get_text()+"')")
            connection.commit()
            self.le_Venda()#Chama função para atualizar o treeview
            msg = gtk.MessageDialog(None, 0, gtk.MESSAGE_INFO, gtk.BUTTONS_OK, 'Cadastro realizado com sucesso!!!')
            msg.run()
            msg.destroy()
            
            #Limpando os campos
            self.vendedor.props.text = ""
            self.cpfvendedor.props.text = ""
            self.rgvenderdor.props.text = ""
            self.naturalidadevendedor.props.text = ""
            self.ecvendedor.props.text = ""
            self.profissaovend.props.text = ""
            self.enderecovendedor.props.text = ""
            self.numerovendedor.props.text = ""
            self.bairrovendedor.props.text = "" 
            self.cepvendedor.props.text = ""
            self.cidadevendedor.props.text = ""
            self.estadovendedor.props.text = ""
            self.comprador.props.text = ""
            self.cpfcomprador.props.text = ""
            self.rgcomprador.props.text = ""
            self.naturalidadecomprador.props.text = ""
            self.eccomprador.props.text = ""
            self.profissaocomprador.props.text = ""
            self.enderecocomprador.props.text = ""
            self.numerocomprador.props.text = ""
            self.bairrocomprador.props.text = ""
            self.cepcomprador.props.text = ""
            self.cidadecomprador.props.text = ""
            self.estadocomprador.props.text = ""
            self.areavenda.props.text = ""
            self.registovenda.props.text = ""
            self.valorvenda.props.text = ""
        
    def ValidarClientes(self, widget):
        #Cria statusbar para clientes
        self.statusbarCliAdm = self.xml.get_widget("statusbarCliAdm")
        #Validar se todos os campos da aba Clientes estão preenchidos e inserir no banco de dados, retornar uma mensagem de erro caso não estejar.
        self.contex = self.statusbarCliAdm.get_context_id("")
        if (self.categoriaAdm.get_text() == "" or self.nomeAdm.get_text() == "" or self.cpfAdm.get_text() == "" or self.rgAdm.get_text() == "" or self.orgaoemissorAdm.get_text() == "" \
            or self.naturalidadeAdm.get_text() == "" or self.dtnascimentoAdm.get_text() == "" or self.maeAdm.get_text() == "" or self.paiAdm.get_text() == "" or self.estcivilAdm.get_text() == "" \
            or self.regcasamentoAdm.get_text() == "" or self.telefoneAdm.get_text() == "" or self.celularAdm.get_text() == "" or self.emailAdm.get_text() == "" or self.enderecoAdm.get_text() == "" \
            or self.profissaoAdm.get_text() == "" or self.empresaAdm.get_text() == "" or self.cargoAdm.get_text() == "" or self.endempresaAdm.get_text() == "" or self.telempresaAdm.get_text() == "" or \
            self.emailempresaAdm.get_text() == ""):
            self.statusbarCliAdm.push(self.contex, "Todos os campos devem ser preenchidos!")
            
        else:
            #Caso nenhum dos campos estiverem vazios, inserir dados na tabela.
            cursor.execute("INSERT INTO clientes(categoria,nome,cpf,rg,orgaoemissor,naturalidade,datanascimento,nomemae,nomepai,estadocivil,regimecasamento,telefone,celular,email,endereco,profissao,empresa,cargo,enderecoempresa,telefoneempresa,emailsite)\
                            VALUES ('"+self.categoriaAdm.get_text()+"','"+self.nomeAdm.get_text()+"','"+self.cpfAdm.get_text()+"','"+self.rgAdm.get_text()+"','"+self.orgaoemissorAdm.get_text()+"','"+self.naturalidadeAdm.get_text()+"','"+self.dtnascimentoAdm.get_text()+"','"+self.maeAdm.get_text()+"','"+self.paiAdm.get_text()+"','"+self.estcivilAdm.get_text()+"','"+self.regcasamentoAdm.get_text()+"','"+self.telefoneAdm.get_text()+"','"+self.celularAdm.get_text()+"','"+self.emailAdm.get_text()+"','"+self.enderecoAdm.get_text()+"','"+self.profissaoAdm.get_text()+"','"+self.empresaAdm.get_text()+"','"+self.cargoAdm.get_text()+"','"+self.endempresaAdm.get_text()+"','"+self.telempresaAdm.get_text()+"','"+self.emailempresaAdm.get_text()+"')")
            connection.commit()
            self.le_Cliente()
            msg = gtk.MessageDialog(None, 0, gtk.MESSAGE_INFO, gtk.BUTTONS_OK, 'Cadastro realizado com Sucesso!!!')
            msg.run()
            msg.destroy()

            #Limpando os campos
            self.categoriaAdm.props.text = ""
            self.nomeAdm.props.text = ""
            self.cpfAdm.props.text = ""
            self.rgAdm.props.text = ""
            self.orgaoemissorAdm.props.text = ""
            self.naturalidadeAdm.props.text = ""
            self.dtnascimentoAdm.props.text = ""
            self.maeAdm.props.text = ""
            self.paiAdm.props.text = ""
            self.estcivilAdm.props.text = ""
            self.regcasamentoAdm.props.text = ""
            self.telefoneAdm.props.text = ""
            self.celularAdm.props.text = ""
            self.emailAdm.props.text = ""
            self.enderecoAdm.props.text = ""
            self.profissaoAdm.props.text = ""
            self.empresaAdm.props.text = ""
            self.cargoAdm.props.text = ""
            self.endempresaAdm.props.text = ""
            self.telempresaAdm.props.text = ""
            self.emailempresaAdm.props.text = ""
        
    def ValidarFuncionario(self, widget):
        #Carregar as statusbar de funcionario
        self.statusbarFuncionario = self.xml.get_widget("statusbarFuncionario")
        self.coontexto = self.statusbarFuncionario.get_context_id("")
        #Validar se todos os campos da aba Funcionários estão preenchidos e inserir no banco de dados, retornar uma mensagem de erro caso não estejar.
        if (self.nomeFuncionario.get_text() == "" or self.dtnFuncionario.get_text() == "" or self.cpfFuncionario.get_text() == "" or self.rgFuncionario.get_text() == "" \
            or self.etdcvlFuncionario.get_text() == "" or self.filhosFuncionario.get_text() == "" or self.grauInstFuncionario.get_text() == "" or self.telefoneFuncionario.get_text() == ""\
            or self.emailFuncionario.get_text() == "" or self.ruaFuncionario.get_text() == "" or self.numeroFuncionario.get_text() == "" or self.bairroFuncionario.get_text() == "" \
            or self.complementoFuncionario.get_text() == "" or self.informacoesFuncionario.get_text() == ""):
            self.statusbarFuncionario.push(self.coontexto, "Todos os campos devem ser preenchidos!")
        else: 
            cursor.execute("INSERT INTO funcionarios (nome,datanascimento,cpf,rg,estadocivil,filhos,graudeinstrucao,telefone,email,rua,numero,bairro,complemento,informacoesextras)\
            VALUES ('"+self.nomeFuncionario.get_text()+"','"+self.dtnFuncionario.get_text()+"','"+self.cpfFuncionario.get_text()+"','"+self.rgFuncionario.get_text()+"','"+self.etdcvlFuncionario.get_text()+"','"+self.filhosFuncionario.get_text()+"','"+self.grauInstFuncionario.get_text()+"','"+self.telefoneFuncionario.get_text()+"','"+self.emailFuncionario.get_text()+"','"+self.ruaFuncionario.get_text()+"','"+self.numeroFuncionario.get_text()+"','"+self.bairroFuncionario.get_text()+"','"+self.complementoFuncionario.get_text()+"','"+self.informacoesFuncionario.get_text()+"')")
            connection.commit()
            self.le_Funcionario()#Chama funcção que atualiza os treviews
            msg = gtk.MessageDialog(None, 0, gtk.MESSAGE_INFO, gtk.BUTTONS_OK, 'Cadastrado realizado com sucesso!!!')
            msg.run()
            msg.destroy()
            
            #Limpando os campos
            self.nomeFuncionario.props.text = ""
            self.dtnFuncionario.props.text = ""
            self.cpfFuncionario.props.text = ""
            self.rgFuncionario.props.text = ""
            self.etdcvlFuncionario.props.text = ""
            self.filhosFuncionario.props.text = ""
            self.grauInstFuncionario.props.text = ""
            self.telefoneFuncionario.props.text = ""
            self.emailFuncionario.props.text = ""
            self.ruaFuncionario.props.text = ""
            self.numeroFuncionario.props.text = ""
            self.bairroFuncionario.props.text = ""
            self.complementoFuncionario.props.text = ""
            self.informacoesFuncionario.props.text = ""

    def ValidarLogin(self,widget):
        #Carrega o statusbar
        self.statusbar_Login = self.xml.get_widget("statusbarCadastroLogin")
        self.contextol = self.statusbar_Login.get_context_id("")
        #Validar se todos os campos da aba aluguel estão preenchidos e inserir no banco de dados, retornar uma mensagem de erro caso não estejar.
        if(self.login_CD.get_text() == "" or self.senha_CD.get_text() == "" or self.funcao_CD.get_text() == ""):
            self.statusbar_Login.push(self.contextol, "Todos os campos devem ser preenchidos!")
        else:
            cursor.execute("INSERT INTO login (login, password, function) VALUES('"+self.login_CD.get_text()+"','"+self.senha_CD.get_text()+"','"+self.funcao_CD.get_text()+"')")
            connection.commit()
            self.le_Login()#chama função que atualiza o treeview
            msg = gtk.MessageDialog(None, 0, gtk.MESSAGE_INFO, gtk.BUTTONS_OK, 'Cadastro realizado com sucesso!!!')
            msg.run()
            msg.destroy()
            
            #Limpando os campos
            self.login_CD.props.text = ""
            self.senha_CD.props.text = ""
            self.funcao_CD.props.text = ""

    def PesquisarImovel(self,widget):
        #seleciona no banco de dados as tuplas que campo nome é igual ao que foi informado no campo pesquisar imóvel. Faz uma iteração nos dados e adiciona os valores em um liststore.
        cursor.execute("SELECT * FROM imoveis WHERE proprietario like '"+self.pequisaImovel.get_text()+"%'")
        pesquisaImovel = cursor.fetchall()
        self.liststore3.clear()#Apaga todos os dados do liststore
        for row in pesquisaImovel:
            pesqProprietario = row[1]
            pesqEscritura = row[2]
            pesqCartorio = row[3]
            pesqCidadeProp = row[4]
            pesqRua = row[5]
            pesqNumero = row[6]
            pesqCep = row[7]
            pesqBairro = row[8]
            pesqComplemento = row[9]
            pesqCidade = row[10]
            pesqUf = row[11]
            pesqDescricao = row[12]
            pesqCategoria = row[13]
            pesqDormitorio = row[14]
            pesqSuite = row[15]
            pesqCopa = row[16]
            pesqGaragem = row[17]
            pesqSalaJantar = row[18]
            pesqSalaEstar = row[19]
            pesqBanheiro = row[20]
            pesqArea = row[21]
            pesqOutros = row[22]
            pesqValor = row[23]
            #Adiciona os valores no liststore
            self.liststore3.append([pesqProprietario,pesqEscritura,pesqCartorio,pesqCidadeProp,pesqRua,pesqNumero,pesqCep,pesqBairro,pesqComplemento,pesqCidade,pesqUf,pesqDescricao,pesqCategoria,pesqDormitorio,pesqSuite,pesqCopa,pesqGaragem,pesqSalaJantar,pesqSalaEstar,pesqBanheiro,pesqArea,pesqOutros,pesqValor])

    def PesquisarCliente(self,widget):
        #seleciona no banco de dados as tuplas cujo campo nome é igual ao que foi informado no campo pesquisar cliente. Faz uma iteração nos dados e adiciona no liststore
        cursor.execute("SELECT * FROM clientes WHERE nome like '"+self.pequisaCliente.get_text()+"%'")
        pesquisaCliente = cursor.fetchall()
        self.listStore4.clear()#Apaga todos os dados do liststore
        for row in pesquisaCliente:
            pesqCategoria = row[1]
            pesqNome = row[2]
            pesqCpf = row[3]
            pesqRg = row[4]
            pesqOrgEmissor = row[5]
            pesqNaturalidade = row[6]
            pesqDtNascimento = row[7]
            pesqMae = row[8]
            pesqPai = row[9]
            pesqEstCivil = row[10]
            pesqRegimeCasamento = row[11]
            pesqTelefone = row[12]
            pesqCelular = row[13]
            pesqEmail = row[14]
            pesqEndereco = row[15]
            pesqProfissao = row[16]
            pesqEmpresa = row[17]
            pesqCargo= row[18]
            pesqEndEmpresa = row[19]
            pesqTelEmpresa = row[20]
            pesqEmailEmpresa = row[21]
            self.listStore4.append([pesqCategoria,pesqNome,pesqCpf,pesqRg,pesqOrgEmissor,pesqNaturalidade,pesqDtNascimento,pesqMae,pesqPai,pesqEstCivil,pesqRegimeCasamento,pesqTelefone,pesqCelular,pesqEmail,pesqEndereco,pesqProfissao,pesqEmpresa,pesqCargo,pesqEndEmpresa,pesqTelEmpresa,pesqEmailEmpresa])

    def PesquisarFuncionario(self,widget):
        #seleciona no banco de dados as tuplas cujo campo nome é igual ao que foi informado no campo pesquisar funcionário.Faz uma iteração nos dados e adiciona no liststore
        cursor.execute("SELECT * FROM funcionarios WHERE nome like '"+self.pequisaFuncionario.get_text()+"%'")
        pesquisa_Funcionario = cursor.fetchall()
        self.listfun.clear()#Apaga tudo que tiver no liststore
        for row in pesquisa_Funcionario:
            PesqFunNome = row[1]
            PesqFunDtNascimento = row[2]
            PesqFunCpf = row[3]
            PesqFunRg = row[4]
            PesqFunEstCivil = row[5]
            PesqFunFilhos = row[6]
            PesqFunGrauInstrucao = row[7]
            PesqFunTelefone = row[8]
            PesqFunEmail = row[9]
            PesqFunRua = row[10]
            PesqFunNumero = row[11]
            PesqFunBairro = row[12]
            PesqFunComplemento = row[13]
            PesqFunOutros = row[14]
            self.listfun.append([PesqFunNome,PesqFunDtNascimento,PesqFunCpf,PesqFunRg,PesqFunEstCivil,PesqFunFilhos,PesqFunGrauInstrucao,PesqFunTelefone,PesqFunEmail,PesqFunRua,PesqFunNumero,PesqFunBairro,PesqFunComplemento,PesqFunOutros])

    def PesquisarAluguel(self, widget):
        #seleciona no banco de dados as tuplas cujo campo nome é igual ao que foi informado no campo pesquisar funcionário.Faz uma iteração nos dados e adiciona no liststore
        cursor.execute("SELECT * FROM alugue WHERE numeroimv like '"+self.pesquisaAluguel.get_text()+"%'")
        pesquisa_Aluguel = cursor.fetchall()
        self.listAluguel.clear()#Apaga todos os dados do liststore
        for row in pesquisa_Aluguel:
            pesqLocador = row[1]
            pesqLocatario = row[2]
            pesqRegistro = row[3]
            pesqFinalidade = row[4]
            pesqPrazo = row[5]
            pesqInicio = row[6]
            pesqTermino = row[7]
            pesqVencimento = row[8]
            pesqValor = row[9]
            pesqFiador_1 = row[10]
            pesqCPF_1 = row[11]
            pesqRG_1 = row[12]
            pesqDtNascimento_1 = row[13]
            pesqEstCivil_1 = row[14]
            pesqRegimeCasamento_1 = row[15]
            pesqConjugue_1 = row[16]
            pesqDTNConjugue_1 = row[17]
            pesqCPFConjugue_1 = row[18]
            pesqRGConjugue_1 = row[19]
            pesqEndereco_1 = row[20]
            pesqNumero_1 = row[21]
            pesqBairro_1 = row[22]
            pesqCidade_1 = row[23]
            pesqEstado_1 = row[24]
            pesqProfissao_1 = row[25]
            pesqRenda_1 = row[26]
            pesqOutros_1 = row[27]
            pesqFiador_2 = row[28]
            pesqCPF_2 = row[29]
            pesqRG_2 = row[30]
            pesqDtNascimento_2 = row[31]
            pesqEstCivil_2 = row[32]
            pesqRegimeCasamento_2 = row[33]
            pesqConjugue_2 = row[34]
            pesqDTNConjugue_2 = row[35]
            pesqCPFConjugue_2 = row[36]
            pesqRGConjugue_2 = row[37]
            pesqEndereco_2 = row[38]
            pesqNumero_2 = row[39]
            pesqBairro_2 = row[40]
            pesqCidade_2 = row[41]
            pesqEstado_2 = row[42]
            pesqProfissao_2 = row[43]
            pesqRenda_2 = row[44]
            pesqOutros_2 = row[45]
            self.listAluguel.append([pesqLocador,pesqLocatario,pesqRegistro,pesqFinalidade,pesqPrazo,pesqInicio,pesqTermino,pesqVencimento,pesqValor,pesqFiador_1,pesqCPF_1,pesqRG_1,pesqDtNascimento_1,pesqEstCivil_1,pesqRegimeCasamento_1,pesqConjugue_1,pesqDTNConjugue_1,pesqCPFConjugue_1,pesqRGConjugue_1,pesqEndereco_1,pesqNumero_1,pesqBairro_1,pesqCidade_1,pesqEstado_1,pesqProfissao_1,pesqRenda_1,pesqOutros_1,pesqFiador_2,pesqCPF_2,pesqRG_2,pesqDtNascimento_2,pesqEstCivil_2,pesqRegimeCasamento_2,pesqConjugue_2,pesqDTNConjugue_2,pesqCPFConjugue_2,pesqRGConjugue_2,pesqEndereco_2,pesqNumero_2,pesqBairro_2,pesqCidade_2,pesqEstado_2,pesqProfissao_2,pesqRenda_2,pesqOutros_2])  
        
    def PesquisarVenda(self, widget):
        #seleciona no banco de dados as tuplas cujo campo nome é igual ao que foi informado no campo pesquisar funcionário.Faz uma iteração nos dados e adiciona no liststore
        cursor.execute("SELECT * FROM venda WHERE registovenda like '"+self.pesquisaVenda.get_text()+"%'")
        pesquisa_Venda = cursor.fetchall()
        self.listVenda.clear()#Apaga todos os dados do liststore
        for row in pesquisa_Venda:
            pesq_Vendedor = row[1]
            pesqCPF_Vendedor = row[2]
            pesqRG_Vendedor = row[3]
            pesqNat_Vendedor = row[4]
            pesqEC_Vendedor = row[5]
            pesqProf_Vendedor = row[6]
            pesqEnd_Vendedor = row[7]
            pesqNum_Vendedor = row[8]
            pesqBairro_Vendedor = row[9]
            pesqCep_Vendedor = row[10]
            pesqCidade_Vendedor = row[11]
            pesqEstado_Vendedor = row[12]
            pesq_Comprador = row[13]
            pesqCPF_Comprador = row[14]
            pesqRG_Comprador = row[15]
            pesqNat_Comprador = row[16]
            pesqEC_Comprador = row[17]
            pesqProf_Comprador = row[18]
            pesqEnd_Comprador = row[19]
            pesqNum_Comprador = row[20]
            pesqBairro_Comprador = row[21]
            pesqCep_Comprador = row[22]
            pesqCidade_Comprador = row[23]
            pesqEstado_Comprador = row[24]
            pesqArea_Venda = row[25]
            pesqRegistro_Venda = row[26]
            pesqValor_Venda = row[27]
            self.listVenda.append([pesq_Vendedor,pesqCPF_Vendedor,pesqRG_Vendedor,pesqNat_Vendedor,pesqEC_Vendedor,pesqProf_Vendedor,pesqEnd_Vendedor,pesqNum_Vendedor,pesqBairro_Vendedor,pesqCep_Vendedor,pesqCidade_Vendedor,pesqEstado_Vendedor,pesq_Comprador,pesqCPF_Comprador,pesqRG_Comprador,pesqNat_Comprador,pesqEC_Comprador,pesqProf_Comprador,pesqEnd_Comprador,pesqNum_Comprador,pesqBairro_Comprador,pesqCep_Comprador,pesqCidade_Comprador,pesqEstado_Comprador,pesqArea_Venda,pesqRegistro_Venda,pesqValor_Venda])
            
    def PesquisarLogin(self, widget):
        #seleciona no banco de dados as tuplas cujo campo nome é igual ao que foi informado no campo pesquisar funcionário.Faz uma iteração nos dados e adiciona no liststore
        cursor.execute("SELECT * FROM login WHERE login like '"+self.pesquisaLogin.get_text()+"%'")
        pesquisa_Login = cursor.fetchall()
        self.listLogin.clear()#Apaga todos os dados do liststore
        for row in pesquisa_Login:
            pesqLogin = row[1]
            pesqSenha = row[2]
            pesqFuncao = row[3]
            self.listLogin.append([pesqLogin,pesqSenha,pesqFuncao])
        
    def SelecionarImovel(self, widget): 
        #Posiciona o cursor na linha que deseja editar
        self.valor_imovel = self.listaImoveis1.get_cursor()
        #Carrega a interface, a janela e os widgets da janela de edição de imovels
        self.xml = gtk.glade.XML('ImobSystem.glade')
        self.windowImovel = self.xml.get_widget('EditarImovel')
        self.edtProprietario = self.xml.get_widget("entryProp1EDT")
        self.edtEscritura = self.xml.get_widget("entryEscritura1EDT")
        self.edtCartorio = self.xml.get_widget("entryCartorio1EDT")
        self.edtCidadeProp = self.xml.get_widget("entryCidadeCartorio1EDT")
        self.edtRua = self.xml.get_widget("entryRua1EDT")
        self.edtNumero = self.xml.get_widget("entryNum3EDT")
        self.edtCep = self.xml.get_widget("entryCep1EDT")
        self.edtBairro = self.xml.get_widget("entryBairro3EDT")
        self.edtComp = self.xml.get_widget("entryComplem1EDT")
        self.edtCidadeImv = self.xml.get_widget("entryCidade3EDT")
        self.edtUf = self.xml.get_widget("entryUf1EDT")
        self.edtDescricao = self.xml.get_widget("entryDescrissao1EDT")
        self.edtCategoria = self.xml.get_widget("entryCateg1EDT")
        self.edtDorm = self.xml.get_widget("entryDorm1EDT")
        self.edtSuite = self.xml.get_widget("entrySuite1EDT")
        self.edtCopa = self.xml.get_widget("entryCopa1EDT")
        self.edtGaragem = self.xml.get_widget("entryGaragem1EDT")
        self.edtSlJantar = self.xml.get_widget("entrySala1EDT")
        self.edtSlEstar = self.xml.get_widget("entrySalaEstar1EDT")
        self.edtBanheiro = self.xml.get_widget("entryBanheiro1EDT")
        self.edtArea = self.xml.get_widget("entryArea1EDT")
        self.edtOut = self.xml.get_widget("entryOutrosDados1EDT")
        self.edtValor = self.xml.get_widget("entryValor1EDT")
        #Cria um dicionário para conectar os sinais 
        dic_imv = {"on_btnSalvarImovel1EDT_clicked" : self.AtualizarImovel,
                   "on_btnCancelarImovel_clicked" : self.CancelarImovel,
                   }
        
        self.windowImovel.show_all()#Tona visivel a janela de edição de imóveis 
        self.xml.signal_autoconnect(dic_imv)#Conecta os sinais à janela de edição de imóveis 
        self.valor_imovel = self.listaImoveis1.get_selection()#seleciona a linha onde cursor está posicionado.
        self.valor_imovel.set_mode(gtk.SELECTION_MULTIPLE)#Define que vários itens podem ser selecionadas de cada vez.
        modelo, caminhos = self.valor_imovel.get_selected_rows()# recupera a seleção dependendo do modo de seleção atual.
        for caminho in caminhos:
            #Define o caminho
            kiter = modelo.get_iter(caminho)
            proprietarioEDT = modelo.get_value(kiter, 0)
            escrituraEDT = modelo.get_value(kiter,1)
            cartorioEDT = modelo.get_value(kiter,2)
            cidadePropEDT = modelo.get_value(kiter,3)
            ruaEDT = modelo.get_value(kiter,4)
            numeroEDT = modelo.get_value(kiter,5)
            cepEDT = modelo.get_value(kiter,6)
            bairroEDT = modelo.get_value(kiter,7)
            complementoEDT = modelo.get_value(kiter,8) 
            cidadeEDT = modelo.get_value(kiter,9)
            ufEDT = modelo.get_value(kiter,10)
            descricaoEDT = modelo.get_value(kiter,11)
            categoriaEDT = modelo.get_value(kiter,12)
            dormitorioEDT = modelo.get_value(kiter,13)
            suiteEDT = modelo.get_value(kiter,14)
            copaEDT = modelo.get_value(kiter,15)
            garagemEDT = modelo.get_value(kiter,16)
            salaJantarEDT = modelo.get_value(kiter,17)
            salaEstarEDT = modelo.get_value(kiter,18)
            banheiroEDT = modelo.get_value(kiter,19)
            areaEDT = modelo.get_value(kiter,20)
            outrosEDT = modelo.get_value(kiter,21)
            valorEDT = modelo.get_value(kiter,22)
            #Substitui os campos de texto pelos dados selecionados pelo caminho
            self.edtProprietario.props.text = proprietarioEDT
            self.edtEscritura.props.text = escrituraEDT
            self.edtCartorio.props.text = cartorioEDT
            self.edtCidadeProp.props.text = cidadePropEDT
            self.edtRua.props.text = ruaEDT
            self.edtNumero.props.text = numeroEDT
            self.edtCep.props.text = cepEDT
            self.edtBairro.props.text = bairroEDT
            self.edtComp.props.text = complementoEDT
            self.edtCidadeImv.props.text = cidadeEDT
            self.edtUf.props.text = ufEDT
            self.edtDescricao.props.text = descricaoEDT
            self.edtCategoria.props.text = categoriaEDT
            self.edtDorm.props.text = dormitorioEDT
            self.edtSuite.props.text = suiteEDT
            self.edtCopa.props.text = copaEDT
            self.edtGaragem.props.text = garagemEDT
            self.edtSlJantar.props.text = salaJantarEDT
            self.edtSlEstar.props.text = salaEstarEDT
            self.edtBanheiro.props.text = banheiroEDT
            self.edtArea.props.text = areaEDT
            self.edtOut.props.text = outrosEDT
            self.edtValor.props.text = valorEDT

        
    def SelecionarCliente(self, widget):
        #Posiciona o cursor na linha que deseja editar
        self.valor_cliente = self.listaClientes1.get_cursor()
        #Carrega interface, janela e widgets de edição
        self.xml = gtk.glade.XML('ImobSystem.glade')
        self.windowCliente = self.xml.get_widget('EditarCliente')
        self.edtCategoriaCli = self.xml.get_widget("entrycategoriaAdm1EDT")
        self.edtNomeCli = self.xml.get_widget("entrynomeAdm1EDT")
        self.edtCpfCli = self.xml.get_widget("entrycpfAdm1EDT")
        self.edtRgCli = self.xml.get_widget("entryrgAdm1EDT")
        self.edtOrgEmissorCli = self.xml.get_widget("entryorgaoemissorAdm1EDT")
        self.edtNaturalidadeCli = self.xml.get_widget("entrynaturalidadeAdm1EDT")
        self.edtDtNascimentoCli = self.xml.get_widget("entrydtnascimentoAdm1EDT")
        self.edtMaeCli = self.xml.get_widget("entrymaeAdm1EDT")
        self.edtPaiCli = self.xml.get_widget("entrypaiAdm1EDT")
        self.edtEstCivilCli = self.xml.get_widget("entryestcivilAdm1EDT")
        self.edtRegimeCasamentoCli = self.xml.get_widget("entryregcasamentoAdm1EDT")
        self.edtTelefoneCli = self.xml.get_widget("entrytelefoneAdm1EDT")
        self.edtCelularCli = self.xml.get_widget("entrycelularAdm1EDT")
        self.edtEmailCli = self.xml.get_widget("entryemailAdm1EDT")
        self.edtEnderecoCli = self.xml.get_widget("entryenderecoAdm1EDT")
        self.edtProfissaoCli = self.xml.get_widget("entryprofissaoAdm1EDT")
        self.edtEmpresaCli = self.xml.get_widget("entryempresaAdm1EDT")
        self.edtCargoCli = self.xml.get_widget("entrycargoAdm1EDT")
        self.edtEndEmpresaCli = self.xml.get_widget("entryendempresaAdm1EDT")
        self.edtTelEmpresaCli = self.xml.get_widget("entrytelempresaAdm1EDT")
        self.edtEmailEmpresaCli = self.xml.get_widget("entryemailempresaAdm1EDT")
        #Cria dicionário para conetar os sinais
        dic_cli = {"on_btnCancelarCli_clicked" : self.CancelarCliente,
                   "on_btnEDTCliAdm1_clicked" : self.AtualizarCliente, 
            }
        #Torna visível a janela de edição de clientes
        self.windowCliente.show_all()
        #coneta os sinais a janela de edição de clientes
        self.xml.signal_autoconnect(dic_cli)
        self.valor_cliente = self.listaClientes1.get_selection()#seleciona a linha onde cursor está posicionado.
        self.valor_cliente.set_mode(gtk.SELECTION_MULTIPLE)#Define que vários itens podem ser selecionadas de cada vez.
        modelo, caminhos = self.valor_cliente.get_selected_rows()# recupera a seleção dependendo do modo de seleção atual.
        for caminho in caminhos:
            #Define o caminho
            kiter = modelo.get_iter(caminho)
            categoriaEDT = modelo.get_value(kiter, 0)
            nomeEDT = modelo.get_value(kiter, 1)
            cpfEDT = modelo.get_value(kiter, 2)
            rgEDT = modelo.get_value(kiter, 3)
            orgEmissorEDT = modelo.get_value(kiter, 4)
            naturalidadeEDT = modelo.get_value(kiter, 5)
            dtNascimentoEDT = modelo.get_value(kiter, 6)
            maeEDT = modelo.get_value(kiter, 7)
            paiEDT = modelo.get_value(kiter, 8)
            estCivilEDT = modelo.get_value(kiter, 9)
            regimeCasamentoEDT = modelo.get_value(kiter, 10)
            telefoneEDT = modelo.get_value(kiter, 11)
            celularEDT = modelo.get_value(kiter, 12)
            emailEDT = modelo.get_value(kiter, 13)
            enderecoEDT = modelo.get_value(kiter, 14)
            profissaoEDT = modelo.get_value(kiter, 15)
            empresaEDT = modelo.get_value(kiter, 16)
            cargoEDT = modelo.get_value(kiter, 17)
            endEmpresaEDT = modelo.get_value(kiter, 18)
            telEmpresaEDT = modelo.get_value(kiter, 19)
            emailEmpresaEDT = modelo.get_value(kiter, 20)
            #Substitui os campos de texto pelos dados selecionados pelo caminho
            self.edtCategoriaCli.props.text = categoriaEDT
            self.edtNomeCli.props.text = nomeEDT
            self.edtCpfCli.props.text = cpfEDT
            self.edtRgCli.props.text = rgEDT
            self.edtOrgEmissorCli.props.text = orgEmissorEDT
            self.edtNaturalidadeCli.props.text = naturalidadeEDT
            self.edtDtNascimentoCli.props.text = dtNascimentoEDT
            self.edtMaeCli.props.text = maeEDT
            self.edtPaiCli.props.text = paiEDT
            self.edtEstCivilCli.props.text = estCivilEDT
            self.edtRegimeCasamentoCli.props.text = regimeCasamentoEDT
            self.edtTelefoneCli.props.text = telefoneEDT
            self.edtCelularCli.props.text = celularEDT
            self.edtEmailCli.props.text = emailEDT
            self.edtEnderecoCli.props.text = enderecoEDT
            self.edtProfissaoCli.props.text = profissaoEDT
            self.edtEmpresaCli.props.text = empresaEDT
            self.edtCargoCli.props.text = cargoEDT
            self.edtEndEmpresaCli.props.text = endEmpresaEDT
            self.edtTelEmpresaCli.props.text = telEmpresaEDT
            self.edtEmailEmpresaCli.props.text = emailEmpresaEDT

    def SelecionarFuncionario(self,widget):
        #Posiciona o cursor na linha que deseja editar
        self.valor = self.listaFuncionario.get_cursor()
        #carrega a interface, a janela e os widgets para edição de funcionario
        self.xml = gtk.glade.XML('ImobSystem.glade')
        self.windowFunc = self.xml.get_widget('EditarFuncionario')
        self.nomeEDT = self.xml.get_widget("entry2")
        self.dataNascEDT = self.xml.get_widget("entry3")
        self.cpfEDT = self.xml.get_widget("entry4")
        self.rgEDT = self.xml.get_widget("entry5")
        self.estadocivilEDT = self.xml.get_widget("entry6")
        self.filhoEDT = self.xml.get_widget("entry7")
        self.grauInstucaoEDT = self.xml.get_widget("entry8")
        self.emailEDT = self.xml.get_widget("entry9")
        self.telefoneEDT = self.xml.get_widget("entry10")
        self.ruaEDT = self.xml.get_widget("entry11")
        self.numEDT = self.xml.get_widget("entry12")
        self.bairroEDT = self.xml.get_widget("entry13")
        self.compEDT = self.xml.get_widget("entry14")
        self.outrosEDT = self.xml.get_widget("entry1")
        #Cria dicionário para conectar os sinais
        dic_fun = {"on_btnSalvarEdtFuncionario_clicked" : self.AtualizarFuncionario,
                   "on_btnCancelarFun_clicked" : self.CancelarFuncionario,   
                 }
        #Torna visiveis os elementos da janela de edição de funcionários  
        self.windowFunc.show_all()
        #conecta os sinaos a janela funcionario
        self.xml.signal_autoconnect(dic_fun)
        self.valor = self.listaFuncionario.get_selection()#seleciona a linha onde cursor está posicionado.
        self.valor.set_mode(gtk.SELECTION_MULTIPLE)#Define que vários itens podem ser selecionadas de cada vez.
        modelo, caminhos = self.valor.get_selected_rows()# recupera a seleção dependendo do modo de seleção atual.
        for caminho in caminhos:
            #Define o caminho
            kiter = modelo.get_iter(caminho)
            nome_EDT = modelo.get_value(kiter, 0)
            dataNasc_EDT = modelo.get_value(kiter, 1)
            cpf_EDT = modelo.get_value(kiter, 2)
            rg_EDT = modelo.get_value(kiter, 3)
            estadocivil_EDT = modelo.get_value(kiter, 4)
            filhos_EDT = modelo.get_value(kiter, 5)
            grauInstucao_EDT = modelo.get_value(kiter, 6)
            telefone_EDT = modelo.get_value(kiter, 7)
            email_EDT = modelo.get_value(kiter, 8)
            rua_EDT = modelo.get_value(kiter, 9)
            num_EDT = modelo.get_value(kiter, 10)
            bairro_EDT = modelo.get_value(kiter, 11)
            comp_EDT = modelo.get_value(kiter, 12)
            outros_EDT = modelo.get_value(kiter, 13)
            #Substitui os campos de texto pelos dados selecionados pelo caminho
            self.nomeEDT.props.text = nome_EDT
            self.dataNascEDT.props.text = dataNasc_EDT
            self.cpfEDT.props.text = cpf_EDT
            self.rgEDT.props.text = rg_EDT
            self.estadocivilEDT.props.text = estadocivil_EDT
            self.filhoEDT.props.text = filhos_EDT
            self.grauInstucaoEDT.props.text = grauInstucao_EDT
            self.telefoneEDT.props.text = telefone_EDT
            self.emailEDT.props.text = email_EDT
            self.ruaEDT.props.text = rua_EDT
            self.numEDT.props.text = num_EDT
            self.bairroEDT.props.text = bairro_EDT
            self.compEDT.props.text = comp_EDT
            self.outrosEDT.props.text = outros_EDT

    def SelecionarAluguel(self, widget):
        #Posiciona o cursor na linha que deseja editar
        self.valor_aluguel = self.listaAluguel.get_cursor()
        #Carregar a interface, janela e widgets
        self.xml = gtk.glade.XML('ImobSystem.glade')
        self.windowAlug = self.xml.get_widget('EditarAluguel')
        self.locador_SLC = self.xml.get_widget("entryEdtLocador")
        self.locatario_SLC = self.xml.get_widget("entryEdtLocatario")
        self.numeroIMV_SLC = self.xml.get_widget("entryEdtRegistro")
        self.finalidadeIMV_SLC = self.xml.get_widget("entryEdtFinalidade")
        self.prazoIMV_SLC = self.xml.get_widget("entryEdtPrazo")
        self.valorIMV_SLC = self.xml.get_widget("entryEdtValor")#AJEITAR NO RESTO DO CÓDIGO E DO CADASTRO
        self.inicioIMV_SLC = self.xml.get_widget("entryEdtInicio")
        self.terminoIMV_SLC = self.xml.get_widget("entryEdtTermino")
        self.vencimentoIMV_SLC = self.xml.get_widget("entryEdtVencimento")
        self.fiador1_SLC = self.xml.get_widget("entryEdtNome")
        self.cpf1_SLC = self.xml.get_widget("entryEdtCPF")
        self.rg1_SLC = self.xml.get_widget("entryEdtRG")
        self.dtnascimento1_SLC = self.xml.get_widget("entryEdtDtNascimento")
        self.estCivil1_SLC = self.xml.get_widget("entryEdtEC")
        self.regCivil1_SLC = self.xml.get_widget("entryEdtRC")
        self.esposa1_SLC = self.xml.get_widget("entryEdtConjugue")
        self.dtEsposa1_SLC = self.xml.get_widget("entryEdtDtConjugue")
        self.cpfEsposa1_SLC = self.xml.get_widget("entryEdtCPFC")
        self.rgEsposa1_SLC = self.xml.get_widget("entryEdtRGC")
        self.endereco1_SLC = self.xml.get_widget("entryEdtEndereco")
        self.numero1_SLC = self.xml.get_widget("entryEdtNumero")
        self.bairro1_SLC = self.xml.get_widget("entryEdtBairro")
        self.cidade1_SLC = self.xml.get_widget("entryEdtCidade")
        self.estado1_SLC = self.xml.get_widget("entryEdtEstado")
        self.profissao1_SLC = self.xml.get_widget("entryEdtProfissao")
        self.renda1_SLC = self.xml.get_widget("entryEdtRenda")
        self.adiciais1_SLC = self.xml.get_widget("entryEdtOutros")
        self.fiador2_SLC = self.xml.get_widget("entryEdtFiador")
        self.cpf2_SLC = self.xml.get_widget("entryEdtFiadorCPF")
        self.rg2_SLC = self.xml.get_widget("entryEdtFiadorRG")
        self.dtnascimento2_SLC = self.xml.get_widget("entryEdtFiadorDTN")
        self.estCivil2_SLC = self.xml.get_widget("entryEdtFiadorEC")
        self.regCivil2_SLC = self.xml.get_widget("entryEdtFiadorRC")
        self.esposa2_SLC = self.xml.get_widget("entryEdtFiadorConjugue")
        self.dtEsposa2_SLC = self.xml.get_widget("entryEdtFiadorDTNConjugue")
        self.cpfEsposa2_SLC = self.xml.get_widget("entryEdtFiadorCPFConjugue")
        self.rgEsposa2_SLC = self.xml.get_widget("entryEdtFiadorRGConjugue")
        self.endereco2_SLC = self.xml.get_widget("entryEdtFiadorEndereco")
        self.numero2_SLC = self.xml.get_widget("entryEdtFiadorNum")
        self.bairro2_SLC = self.xml.get_widget("entryEdtFiadorBairro")
        self.cidade2_SLC = self.xml.get_widget("entryEdtFiadorCidade")
        self.estado2_SLC = self.xml.get_widget("entryEdtFiadorEstado")
        self.profissao2_SLC = self.xml.get_widget("entryEdtFiadorProfissao")
        self.renda2_SLC = self.xml.get_widget("entryEdtFiadorRM")
        self.adicionais2_SLC = self.xml.get_widget("entryEdtFiadorOutros")
        #Criar dicionário para conectar os sinais
        dic_alg = { "on_btnNovo_clicked" : self.atualizarContratoAluguel,
                    "on_btnAtualizar_clicked" : self.AtualizarAluguel,
                    "on_btnCancelarEDT_clicked" : self.CancelarAluguel,
            }
        #Tornar visivel a janela de edição de alugel
        self.windowAlug.show_all()
        #conectar os sinais a janela de edição de aluguel
        self.xml.signal_autoconnect(dic_alg)
        self.valor_aluguel = self.listaAluguel.get_selection()#seleciona a linha onde cursor está posicionado
        self.valor_aluguel.set_mode(gtk.SELECTION_MULTIPLE)#Define que vários itens podem ser selecionadas de cada vez.
        modelo, caminhos = self.valor_aluguel.get_selected_rows()# recupera a seleção dependendo do modo de seleção atual.
        for caminho in caminhos:
            #Define o caminho
            kiter = modelo.get_iter(caminho)
            locador_SLCEDT = modelo.get_value(kiter, 0)
            locatario_SLCEDT = modelo.get_value(kiter, 1)
            numeroIMV_SLCEDT = modelo.get_value(kiter, 2)
            finalidadeIMV_SLCEDT = modelo.get_value(kiter, 3)
            prazoIMV_SLCEDT = modelo.get_value(kiter, 4)
            valorIMV_SLCEDT = modelo.get_value(kiter, 5)
            terminoIMV_SLCEDT = modelo.get_value(kiter, 6)
            vencimentoIMV_SLCEDT = modelo.get_value(kiter, 7)
            inicioIMV_SLCEDT = modelo.get_value(kiter, 8)
            fiador1_SLCEDT = modelo.get_value(kiter, 9)
            cpf1_SLCEDT = modelo.get_value(kiter, 10)
            rg1_SLCEDT = modelo.get_value(kiter, 11)
            dtnascimento1_SLCEDT = modelo.get_value(kiter, 12)
            estCivil1_SLCEDT = modelo.get_value(kiter, 13)
            regCivil1_SLCEDT = modelo.get_value(kiter, 14)
            esposa1_SLCEDT = modelo.get_value(kiter, 15)
            dtEsposa1_SLCEDT = modelo.get_value(kiter, 16)
            cpfEsposa1_SLCEDT = modelo.get_value(kiter, 17)
            rgEsposa1_SLCEDT =  modelo.get_value(kiter, 18)
            endereco1_SLCEDT = modelo.get_value(kiter, 19)
            numero1_SLCEDT = modelo.get_value(kiter, 20)
            bairro1_SLCEDT = modelo.get_value(kiter, 21)
            cidade1_SLCEDT = modelo.get_value(kiter, 22)
            estado1_SLCEDT = modelo.get_value(kiter, 23)
            profissao1_SLCEDT = modelo.get_value(kiter, 24)
            renda1_SLCEDT = modelo.get_value(kiter, 25)
            adiciais1_SLCEDT = modelo.get_value(kiter, 26)
            fiador2_SLCEDT = modelo.get_value(kiter, 27)
            cpf2_SLCEDT = modelo.get_value(kiter, 28)
            rg2_SLCEDT = modelo.get_value(kiter, 29)
            dtnascimento2_SLCEDT = modelo.get_value(kiter, 30)
            estCivil2_SLCEDT = modelo.get_value(kiter, 31)
            regCivil2_SLCEDT = modelo.get_value(kiter, 32)
            esposa2_SLCEDT = modelo.get_value(kiter, 33)
            dtEsposa2_SLCEDT = modelo.get_value(kiter, 34)
            cpfEsposa2_SLCEDT = modelo.get_value(kiter, 35)
            rgEsposa2_SLCEDT = modelo.get_value(kiter, 36)
            endereco2_SLCEDT = modelo.get_value(kiter, 37)
            numero2_SLCEDT = modelo.get_value(kiter, 38)
            bairro2_SLCEDT = modelo.get_value(kiter, 39)
            cidade2_SLCEDT = modelo.get_value(kiter, 40)
            estado2_SLCEDT = modelo.get_value(kiter, 41)
            profissao2_SLCEDT = modelo.get_value(kiter, 42)
            renda2_SLCEDT = modelo.get_value(kiter, 43) 
            adicionais2_SLCEDT = modelo.get_value(kiter, 44)
            #Substitui os campos de texto pelos dados selecionados pelo caminho
            self.locador_SLC.props.text = locador_SLCEDT
            self.locatario_SLC.props.text = locatario_SLCEDT
            self.numeroIMV_SLC.props.text = numeroIMV_SLCEDT
            self.finalidadeIMV_SLC.props.text = finalidadeIMV_SLCEDT
            self.prazoIMV_SLC.props.text = prazoIMV_SLCEDT
            self.valorIMV_SLC.props.text = valorIMV_SLCEDT
            self.inicioIMV_SLC.props.text = inicioIMV_SLCEDT
            self.terminoIMV_SLC.props.text = terminoIMV_SLCEDT
            self.vencimentoIMV_SLC.props.text = vencimentoIMV_SLCEDT
            self.fiador1_SLC.props.text = fiador1_SLCEDT
            self.cpf1_SLC.props.text = cpf1_SLCEDT
            self.rg1_SLC.props.text = rg1_SLCEDT 
            self.dtnascimento1_SLC.props.text = dtnascimento1_SLCEDT
            self.estCivil1_SLC.props.text = estCivil1_SLCEDT
            self.regCivil1_SLC.props.text = regCivil1_SLCEDT
            self.esposa1_SLC.props.text = esposa1_SLCEDT
            self.dtEsposa1_SLC.props.text = dtEsposa1_SLCEDT
            self.cpfEsposa1_SLC.props.text = cpfEsposa1_SLCEDT
            self.rgEsposa1_SLC.props.text = rgEsposa1_SLCEDT
            self.endereco1_SLC.props.text = endereco1_SLCEDT
            self.numero1_SLC.props.text = numero1_SLCEDT
            self.bairro1_SLC.props.text = bairro1_SLCEDT
            self.cidade1_SLC.props.text = cidade1_SLCEDT
            self.estado1_SLC.props.text = estado1_SLCEDT
            self.profissao1_SLC.props.text = profissao1_SLCEDT
            self.renda1_SLC.props.text = renda1_SLCEDT
            self.adiciais1_SLC.props.text = adiciais1_SLCEDT
            self.fiador2_SLC.props.text = fiador2_SLCEDT
            self.cpf2_SLC.props.text = cpf2_SLCEDT
            self.rg2_SLC.props.text = rg2_SLCEDT
            self.dtnascimento2_SLC.props.text = dtnascimento2_SLCEDT
            self.estCivil2_SLC.props.text = estCivil2_SLCEDT
            self.regCivil2_SLC.props.text = regCivil2_SLCEDT
            self.esposa2_SLC.props.text = esposa2_SLCEDT
            self.dtEsposa2_SLC.props.text = dtEsposa2_SLCEDT
            self.cpfEsposa2_SLC.props.text = cpfEsposa2_SLCEDT
            self.rgEsposa2_SLC.props.text = rgEsposa2_SLCEDT
            self.endereco2_SLC.props.text = endereco2_SLCEDT
            self.numero2_SLC.props.text = numero2_SLCEDT
            self.bairro2_SLC.props.text = bairro2_SLCEDT
            self.cidade2_SLC.props.text = cidade2_SLCEDT
            self.estado2_SLC.props.text = estado2_SLCEDT
            self.profissao2_SLC.props.text = profissao2_SLCEDT
            self.renda2_SLC.props.text = renda2_SLCEDT
            self.adicionais2_SLC.props.text = adicionais2_SLCEDT
        
    def SelecionarVenda(self, widget):
        #Posiciona o cursor na linha que deseja editar
        self.valor_venda = self.listaVenda.get_cursor()
        #Carrega a interface a janela e os widgets
        self.xml = gtk.glade.XML('ImobSystem.glade')
        self.window_Venda = self.xml.get_widget('EditarVenda')
        self.vendedor_EDTVENDA = self.xml.get_widget("entrynomevendaEDT")
        self.cpf_EDTVENDA = self.xml.get_widget("entrycpfvenda1EDT")
        self.rg_EDTVENDA = self.xml.get_widget("entryRGEDT")
        self.naturalidade_EDTVENDA = self.xml.get_widget("entrynaturalidadevenda1EDT")
        self.estcivil_EDTVENDA = self.xml.get_widget("entryEstcivilvenda1EDT")
        self.prof_EDTVENDA = self.xml.get_widget("entryProfissaoEDT")
        self.end_EDTVENDA = self.xml.get_widget("entryEnderecovenda1EDT")
        self.numero_EDTVENDA = self.xml.get_widget("entryNumvenda1EDT")
        self.bairro_EDTVENDA = self.xml.get_widget("entryBairroEDT")
        self.cep_EDTVENDA = self.xml.get_widget("entryCepvenda1EDT")
        self.cidade_EDTVENDA = self.xml.get_widget("entryCidadevenda1EDT")
        self.estado_EDTVENDA = self.xml.get_widget("entryEstadoEDT")
        self.comprador_EDTCOMPRA = self.xml.get_widget("entryCompradorvenda1EDT")
        self.cpf_EDTCOMPRA = self.xml.get_widget("entryCpfCompradorvenda1EDT")
        self.rg_EDTCOMPRA = self.xml.get_widget("entryRGCompradorEDT")
        self.naturalidade_EDTCOMPRA = self.xml.get_widget("entryNatCompradorvenda1EDT")
        self.estcivil_EDTCOMPRA = self.xml.get_widget("entryECcompradorvenda1EDT")
        self.prof_EDTCOMPRA = self.xml.get_widget("entryProfissaoCompradorEDT")
        self.end_EDTCOMPRA = self.xml.get_widget("entryEndCompradorvenda1EDT")
        self.numero_EDTCOMPRA = self.xml.get_widget("entryNumcompradorvenda1EDT")
        self.bairro_EDTCOMPRA = self.xml.get_widget("entryBairroCompradorEDT")
        self.cep_EDTCOMPRA = self.xml.get_widget("entrycepCompradorvenda1EDT")
        self.cidade_EDTCOMPRA = self.xml.get_widget("entryCidadeCompvenda1EDT")
        self.estado_EDTCOMPRA = self.xml.get_widget("entryEstadoVendaEDT")
        self.area_EDTVENDA = self.xml.get_widget("entryareavenda1EDT")
        self.registro_EDTVENDA = self.xml.get_widget("entryRegistrovenda1EDT")
        self.valor_EDTVENDA = self.xml.get_widget("entryValorEDT")
        #Cria um dicionário para conectar os sinais
        dic_vend = {"on_btnGerarNovo_clicked" : self.atualizarContratoVenda,
                    "on_btnSalvarVenda1EDT_clicked" : self.AtualizarVenda,
                    "on_btnExcluirVendaEDT_clicked" : self.CancelarVenda,
            }
        
        self.window_Venda.show_all()
        #Conecta os sinais à janela venda
        self.xml.signal_autoconnect(dic_vend) 
        self.valor_venda = self.listaVenda.get_selection()#seleciona a linha onde cursor está posicionado.
        self.valor_venda.set_mode(gtk.SELECTION_MULTIPLE)#Define que vários itens podem ser selecionadas de cada vez.
        modelo, caminhos = self.valor_venda.get_selected_rows()# recupera a seleção dependendo do modo de seleção atual.
        for caminho in caminhos:
            #Define o caminho
            kiter = modelo.get_iter(caminho)
            vendedor_SLCVENDA = modelo.get_value(kiter, 0)
            cpf_SLCVENDA = modelo.get_value(kiter, 1)
            rg_SLCVENDA = modelo.get_value(kiter, 2)
            naturalidade_SLCVENDA = modelo.get_value(kiter, 3)
            estcivil_SLCVENDA = modelo.get_value(kiter, 4)
            prof_SLCVENDA = modelo.get_value(kiter, 5)
            end_SLCVENDA = modelo.get_value(kiter, 6)
            numero_SLCVENDA = modelo.get_value(kiter, 7)
            bairro_SLCVENDA = modelo.get_value(kiter, 8)
            cep_SLCVENDA = modelo.get_value(kiter, 9)
            cidade_SLCVENDA = modelo.get_value(kiter, 10)
            estado_SLCVENDA = modelo.get_value(kiter, 11)
            comprador_SLCCOMPRA  = modelo.get_value(kiter, 12)
            cpf_SLCCOMPRA = modelo.get_value(kiter, 13)
            rg_SLCCOMPRA = modelo.get_value(kiter, 14)
            naturalidade_SLCCOMPRA = modelo.get_value(kiter, 15)
            estcivil_SLCCOMPRA = modelo.get_value(kiter, 16)
            prof_SLCCOMPRA = modelo.get_value(kiter, 17)
            end_SLCCOMPRA = modelo.get_value(kiter, 18)
            numero_SLCCOMPRA = modelo.get_value(kiter, 19)
            bairro_SLCCOMPRA = modelo.get_value(kiter, 20)
            cep_SLCCOMPRA = modelo.get_value(kiter, 21)
            cidade_SLCCOMPRA = modelo.get_value(kiter, 22)
            estado_SLCCOMPRA = modelo.get_value(kiter, 23)
            area_SLCVENDA = modelo.get_value(kiter, 24)
            registro_SLCVENDA = modelo.get_value(kiter, 25)
            valor_SLCVENDA = modelo.get_value(kiter, 26)
            #Substitui os campos de texto pelos dados selecionados pelo caminho
            self.vendedor_EDTVENDA.props.text = vendedor_SLCVENDA
            self.cpf_EDTVENDA.props.text = cpf_SLCVENDA
            self.rg_EDTVENDA.props.text = rg_SLCVENDA
            self.naturalidade_EDTVENDA.props.text = naturalidade_SLCVENDA
            self.estcivil_EDTVENDA.props.text = estcivil_SLCVENDA
            self.prof_EDTVENDA.props.text = prof_SLCVENDA
            self.end_EDTVENDA.props.text = end_SLCVENDA
            self.numero_EDTVENDA.props.text = numero_SLCVENDA
            self.bairro_EDTVENDA.props.text = bairro_SLCVENDA
            self.cep_EDTVENDA.props.text = cep_SLCVENDA
            self.cidade_EDTVENDA.props.text = cidade_SLCVENDA
            self.estado_EDTVENDA.props.text = estado_SLCVENDA
            self.comprador_EDTCOMPRA.props.text = comprador_SLCCOMPRA
            self.cpf_EDTCOMPRA.props.text = cpf_SLCCOMPRA
            self.rg_EDTCOMPRA.props.text = rg_SLCCOMPRA
            self.naturalidade_EDTCOMPRA.props.text = naturalidade_SLCCOMPRA
            self.estcivil_EDTCOMPRA.props.text = estcivil_SLCCOMPRA
            self.prof_EDTCOMPRA.props.text = prof_SLCCOMPRA
            self.end_EDTCOMPRA.props.text = end_SLCCOMPRA
            self.numero_EDTCOMPRA.props.text = numero_SLCCOMPRA
            self.bairro_EDTCOMPRA.props.text = bairro_SLCCOMPRA
            self.cep_EDTCOMPRA.props.text = cep_SLCCOMPRA
            self.cidade_EDTCOMPRA.props.text = cidade_SLCCOMPRA
            self.estado_EDTCOMPRA.props.text = estado_SLCCOMPRA
            self.area_EDTVENDA.props.text = area_SLCVENDA
            self.registro_EDTVENDA.props.text = registro_SLCVENDA
            self.valor_EDTVENDA.props.text = valor_SLCVENDA

    def SelecionarLogin(self, widget):
        #Posiciona o cursor na linha que deseja editar
        self.valor_log = self.listaLogin.get_cursor()
        #Carrega a interface, a janela e os widgets para edição de login
        self.xml = gtk.glade.XML('ImobSystem.glade')
        self.windowlog = self.xml.get_widget('EditarLogin')
        self.login_EDT = self.xml.get_widget("entryEditarlogin")
        self.senha_EDT = self.xml.get_widget("entryEditarSenha")
        self.funcao_EDT = self.xml.get_widget("entryEditarFuncao")
        #Cria dicionário para conectar os sinais
        dic_log = {"on_btnAtualizarLogin_clicked" : self.AtualizarLogin,
            }
        #Trona visivel a janela de edição de login
        self.windowlog.show_all()
        #Conecta os sinais à janela login
        self.xml.signal_autoconnect(dic_log)
        self.valor_log = self.listaLogin.get_selection()#seleciona a linha onde cursor está posicionado.
        self.valor_log.set_mode(gtk.SELECTION_MULTIPLE)#Define que vários itens podem ser selecionadas de cada vez.
        modelo, caminhos = self.valor_log.get_selected_rows()# recupera a seleção dependendo do modo de seleção atual.
        for caminho in caminhos:
            #Define o caminho
            kiter = modelo.get_iter(caminho)
            login_SLC = modelo.get_value(kiter, 0)
            senha_SLC = modelo.get_value(kiter, 1)
            funcao_SLC = modelo.get_value(kiter, 2)
            #Substitui os campos de texto pelos dados selecionados pelo caminho
            self.login_EDT.props.text = login_SLC
            self.senha_EDT.props.text = senha_SLC
            self.funcao_EDT.props.text = funcao_SLC

    def AtualizarImovel(self,widget):
        #Seleciona no banco de dados a coluna que for igual ao que está digitado no campo de texto
        cursor.execute("SELECT * FROM imoveis WHERE numeroescritura='"+self.edtEscritura.get_text()+"'")
        selectImovel = cursor.fetchall()
        for linha in selectImovel:
            #Faz uma iteração no valores selecionado e atualiza no banco de dados os novos valores digitado.
            cursor.execute("UPDATE imoveis SET proprietario='"+self.edtProprietario.get_text()+"',numeroescritura='"+self.edtEscritura.get_text()+"',cartorio='"+self.edtCartorio.get_text()+"',cidade='"+self.edtCidadeProp.get_text()+"',rua='"+self.edtRua.get_text()+"',numero='"+self.edtNumero.get_text()+"',cep='"+self.edtCep.get_text()+"',bairro='"+self.edtBairro.get_text()+"',complemento='"+self.edtComp.get_text()+"',cidadeimovel='"+self.edtCidadeImv.get_text()+"',uf='"+self.edtUf.get_text()+"',descrissao='"+self.edtDescricao.get_text()+"',categoria='"+self.edtCategoria.get_text()+"',domitorio='"+self.edtDorm.get_text()+"',suite='"+self.edtSuite.get_text()+"',copa='"+self.edtCopa.get_text()+"',garagem='"+self.edtGaragem.get_text()+"',salajantar='"+self.edtSlJantar.get_text()+"',salaestar='"+self.edtSlEstar.get_text()+"',banheiro='"+self.edtBanheiro.get_text()+"',areatotal='"+self.edtArea.get_text()+"',outrosdados='"+self.edtOut.get_text()+"',valorproprietario='"+self.edtValor.get_text()+"' WHERE proprietario='"+self.edtProprietario.get_text()+"'")
            connection.commit()
            msg = gtk.MessageDialog(None, 0, gtk.MESSAGE_INFO, gtk.BUTTONS_OK, 'Atualizado Com Sucesso')
            msg.run()
            msg.destroy()
            self.windowImovel.hide()
            self.le_Imovel()#Atualiza o treeview
            
    def AtualizarCliente(self,widget):
        print "a"
        #Seleciona no banco de dados a coluna que for igual ao que está digitado no campo de texto
        cursor.execute("SELECT * FROM clientes WHERE cpf='"+self.edtCpfCli.get_text()+"'")
        print "b"
        selectCli = cursor.fetchall()
        for linha in selectCli:
            #Faz uma iteração no valores selecionado e atualiza no banco de dados os novos valores digitado.
            cursor.execute("UPDATE clientes SET categoria='"+self.edtCategoriaCli.get_text()+"',cpf='"+self.edtCpfCli.get_text()+"',rg= '"+self.edtRgCli.get_text()+"',orgaoemissor='"+self.edtOrgEmissorCli.get_text()+"',naturalidade='"+self.edtNaturalidadeCli.get_text()+"',datanascimento='"+self.edtDtNascimentoCli.get_text()+"',nomemae='"+self.edtMaeCli.get_text()+"',nomepai='"+self.edtPaiCli.get_text()+"',estadocivil='"+self.edtEstCivilCli.get_text()+"',regimecasamento= '"+self.edtRegimeCasamentoCli.get_text()+"',telefone='"+self.edtTelefoneCli.get_text()+"',celular='"+self.edtCelularCli.get_text()+"',email='"+self.edtEmailCli.get_text()+"',endereco='"+self.edtEnderecoCli.get_text()+"',profissao='"+self.edtProfissaoCli.get_text()+"',empresa='"+self.edtEmpresaCli.get_text()+"',cargo='"+self.edtCargoCli.get_text()+"',enderecoempresa='"+self.edtEndEmpresaCli.get_text()+"',telefoneempresa='"+self.edtTelEmpresaCli.get_text()+"',emailsite='"+self.edtEmailEmpresaCli.get_text()+"' WHERE nome='"+self.edtNomeCli.get_text()+"'" )
            connection.commit()
            print "c"
            msg = gtk.MessageDialog(None, 0, gtk.MESSAGE_INFO, gtk.BUTTONS_OK, 'Atualizado Com Sucesso')
            msg.run()
            msg.destroy()
            self.windowCliente.hide()
            self.le_Cliente()#Atualiza o treeview
        
    def AtualizarFuncionario(self,widget):
        cursor.execute("SELECT * FROM funcionarios WHERE cpf='"+self.cpfEDT.get_text()+"'")
        #Seleciona no banco de dados a coluna que for igual ao que está digitado no campo de texto
        selectFuncionario = cursor.fetchall()
        for linha in selectFuncionario:
            #Faz uma iteração no valores selecionado e atualiza no banco de dados os novos valores digitado.
            cursor.execute("UPDATE funcionarios SET datanascimento='"+self.dataNascEDT.get_text()+"',cpf='"+self.cpfEDT.get_text()+"',rg='"+self.rgEDT.get_text()+"',estadocivil='"+self.estadocivilEDT.get_text()+"',filhos='"+self.filhoEDT.get_text()+"',graudeinstrucao='"+self.grauInstucaoEDT.get_text()+"',telefone='"+self.telefoneEDT.get_text()+"',email='"+self.emailEDT.get_text()+"',rua='"+self.ruaEDT.get_text()+"',numero='"+self.numEDT.get_text()+"',bairro='"+self.bairroEDT.get_text()+"',complemento='"+self.compEDT.get_text()+"',informacoesextras='"+self.outrosEDT.get_text()+"' WHERE nome='"+self.nomeEDT.get_text()+"'")
            connection.commit()
            msg = gtk.MessageDialog(None, 0, gtk.MESSAGE_INFO, gtk.BUTTONS_OK, 'Atualizado Com Sucesso')
            msg.run()
            msg.destroy()
            self.windowFunc.hide()
            self.le_Funcionario()#Atualiza o treeview
        
    def AtualizarAluguel(self, widget):
        cursor.execute("SELECT * FROM alugue WHERE numeroimv='"+self.numeroIMV_SLC.get_text()+"'")
        selectAluguel = cursor.fetchall()
        #Seleciona no banco de dados a coluna que for igual ao que está digitado no campo de texto
        for linha in selectAluguel:
            cursor.execute("UPDATE alugue SET locador='"+self.locador_SLC.get_text()+"', locatario='"+self.locatario_SLC.get_text()+"', finalidadeimv='"+self.finalidadeIMV_SLC.get_text()+"', prazoimv='"+self.prazoIMV_SLC.get_text()+"', valorimv='"+self.valorIMV_SLC.get_text()+"', inicioimv='"+self.inicioIMV_SLC.get_text()+"', terminoimv='"+self.terminoIMV_SLC.get_text()+"', vencimentoimv='"+self.vencimentoIMV_SLC.get_text()+"', fiador1='"+self.fiador1_SLC.get_text()+"', cpf1='"+self.cpf1_SLC.get_text()+"', rg1='"+self.rg1_SLC.get_text()+"', dtnascimento1='"+self.dtnascimento1_SLC.get_text()+"', estcivil1='"+self.estCivil1_SLC.get_text()+"', regcivil1='"+self.regCivil1_SLC.get_text()+"', esposa1='"+self.esposa1_SLC.get_text()+"', dtesposa1='"+self.dtEsposa1_SLC.get_text()+"', cpfesposa1='"+self.cpfEsposa1_SLC.get_text()+"', rgesposa1='"+self.rgEsposa1_SLC.get_text()+"', endereco1='"+self.endereco1_SLC.get_text()+"', numero1='"+self.numero1_SLC.get_text()+"', bairro1='"+self.bairro1_SLC.get_text()+"', cidade1='"+self.cidade1_SLC.get_text()+"', estado1='"+self.estado1_SLC.get_text()+"', profissao1='"+self.profissao1_SLC.get_text()+"', renda1='"+self.renda1_SLC.get_text()+"', adiciais1='"+self.adiciais1_SLC.get_text()+"', fiador2='"+self.fiador2_SLC.get_text()+"', cpf2='"+self.cpf2_SLC.get_text()+"',rg2='"+self.rg2_SLC.get_text()+"', dtnascimento2='"+self.dtnascimento2_SLC.get_text()+"', estcivil2='"+self.estCivil2_SLC.get_text()+"', regcivil2='"+self.regCivil2_SLC.get_text()+"', esposa2='"+self.esposa2_SLC.get_text()+"', dtesposa2='"+self.dtEsposa2_SLC.get_text()+"', cpfesposa2='"+self.cpfEsposa2_SLC.get_text()+"', rgesposa2='"+self.rgEsposa2_SLC.get_text()+"', endereco2='"+self.endereco2_SLC.get_text()+"', numero2='"+self.numero2_SLC.get_text()+"', bairro2='"+self.bairro2_SLC.get_text()+"', cidade2='"+self.cidade2_SLC.get_text()+"', estado2='"+self.estado2_SLC.get_text()+"', profissao2='"+self.profissao2_SLC.get_text()+"', renda2='"+self.renda2_SLC.get_text()+"', adicionais2='"+self.adicionais2_SLC.get_text()+"' WHERE numeroimv='"+self.numeroIMV_SLC.get_text()+"'")
            connection.commit()
            msg = gtk.MessageDialog(None, 0, gtk.MESSAGE_INFO, gtk.BUTTONS_OK, 'Atualizado Com Sucesso')
            msg.run()
            msg.destroy()
            self.windowAlug.hide()
            self.le_Aluguel()

    def AtualizarVenda(self, widget):
        cursor.execute("SELECT * FROM venda WHERE cpfvendedor='"+self.cpf_EDTVENDA.get_text()+"'")
        selectVenda = cursor.fetchall()
        #Seleciona no banco de dados a coluna que for igual ao que está digitado no campo de texto
        for linha in selectVenda:
            cursor.execute("UPDATE venda SET vendedor='"+self.vendedor_EDTVENDA.get_text()+"',rgvendedor='"+self.rg_EDTVENDA.get_text()+"',naturalidadevendedor='"+self.naturalidade_EDTVENDA.get_text()+"',ecvendedor='"+self.estcivil_EDTVENDA.get_text()+"',profissaovend='"+self.prof_EDTVENDA.get_text()+"',enderecovendedor='"+self.end_EDTVENDA.get_text()+"',numerovendedor='"+self.numero_EDTVENDA.get_text()+"',bairrovendedor='"+self.bairro_EDTVENDA.get_text()+"',cepvendedor='"+self.cep_EDTVENDA.get_text()+"',cidadevendedor='"+self.cidade_EDTVENDA.get_text()+"',estadovendedor='"+self.estado_EDTVENDA.get_text()+"',comprador='"+self.comprador_EDTCOMPRA.get_text()+"',cpfcomprador='"+self.cpf_EDTCOMPRA.get_text()+"',rgcomprador='"+self.rg_EDTCOMPRA.get_text()+"', naturalidadecomprador='"+self.naturalidade_EDTCOMPRA.get_text()+"',eccomprador='"+ self.estcivil_EDTCOMPRA.get_text()+"',profissaocomprador='"+self.prof_EDTCOMPRA.get_text()+"',enderecocomprador='"+self.end_EDTCOMPRA.get_text()+"',numerocomprador='"+self.numero_EDTCOMPRA.get_text()+"',bairrocomprador='"+self.bairro_EDTCOMPRA.get_text()+"',cepcomprador='"+self.cep_EDTCOMPRA.get_text()+"',cidadecomprador='"+self.cidade_EDTCOMPRA.get_text()+"',estadocomprador='"+self.estado_EDTCOMPRA.get_text()+"',areavenda='"+self.area_EDTVENDA.get_text()+"',registovenda='"+self.registro_EDTVENDA.get_text()+"',valorvenda='"+self.valor_EDTVENDA.get_text()+"' WHERE cpfvendedor='"+self.cpf_EDTVENDA.get_text()+"'")
            connection.commit()
            msg = gtk.MessageDialog(None, 0, gtk.MESSAGE_INFO, gtk.BUTTONS_OK, 'Atualizado Com Sucesso')
            msg.run()
            msg.destroy()
            self.window_Venda.hide()
            self.le_Venda()
        
    def AtualizarLogin(self, widget):
        #Seleciona no banco de dados a coluna que for igual ao que está digitado no campo de texto
        cursor.execute("SELECT * FROM login WHERE login='"+self.login_EDT.get_text()+"'")
        selectLogin = cursor.fetchall()
        for row in selectLogin:
            #Faz uma iteração no valores selecionado e atualiza no banco de dados os novos valores digitado.
            cursor.execute("UPDATE login SET password='%s', function='%s' WHERE login='"+self.login_EDT.get_text()+"'"%(self.senha_EDT.props.text,self.funcao_EDT.props.text))
            connection.commit()
            msg = gtk.MessageDialog(None, 0, gtk.MESSAGE_INFO, gtk.BUTTONS_OK, 'Atualizado Com Sucesso')
            msg.run()
            msg.destroy()
            self.windowAlug.hide()
            self.le_Login()#Atualiza o treeview
            
    def CancelarImovel(self, widget):
        self.windowImovel.hide()#Fechar a janela de edição de imóvel   
    def CancelarCliente(self, widget):
        self.windowCliente.hide() #Fechar a janela de edição de clientes
    def CancelarFuncionario(self, widget):
        self.windowFunc.hide()   #Fechar a janela de edição de  funcionário
    def CancelarAluguel(self, widget):
        self.windowAlug.hide()   #Fechar a janela de edição de  aluguel 
    def CancelarVenda(self, widget):
        self.window_Venda.hide()#Fechar a janela de edição de venda

    def RemoverImovel(self, widget):
        ##Posiciona o cursor na linha que deseja editar
        self.valor_RmvImovel = self.listaImoveis1.get_cursor()
        #Envia uma mensagem para o usuário decidir se deseja ou não excluir
        msg = gtk.MessageDialog(None, 0, gtk.MESSAGE_QUESTION, gtk.BUTTONS_YES_NO, 'Deseja excluir o registro ?')
        resposta = msg.run()
        msg.destroy()
        #Se a resposta for sim, seleciona no banco de dados os valores que vão se excluidos.
        if resposta == gtk.RESPONSE_YES:
            self.valor_RmvImovel = self.listaImoveis1.get_selection()#seleciona a linha onde cursor está posicionado.
            self.valor_RmvImovel.set_mode(gtk.SELECTION_MULTIPLE)#Define que vários itens podem ser selecionadas de cada vez.
            modelo, caminhos = self.valor_RmvImovel.get_selected_rows()# recupera a seleção dependendo do modo de seleção atual.
            for caminho in caminhos:
                kiter = modelo.get_iter(caminho)
                #Define o caminho
                self.delImv = modelo.get_value(kiter,2)
            #Faz uma iteração, se o caminho for igual a linha escolhida, exclui os valores no banco de dados
            cursor.execute("SELECT * FROM imoveis")
            removeCli = cursor.fetchall()
            for linha in removeCli:
                if self.delImv == linha[3]:
                    print "a"
                    cursor.execute("DELETE FROM imoveis WHERE numeroescritura='%s'" % (linha[3]))
                    connection.commit()
                    self.le_Imovel()         
            msg = gtk.MessageDialog(None, 0, gtk.MESSAGE_INFO, gtk.BUTTONS_OK, 'Deletado com Sucesso!')
            msg.run()
            msg.destroy()
            
    def RemoverCliente(self, widget):
        ##Posiciona o cursor na linha que deseja editar
        self.valor_RemCli = self.listaClientes1.get_cursor()
        #Envia uma mensagem para o usuário decidir se deseja ou não excluir
        msg = gtk.MessageDialog(None, 0, gtk.MESSAGE_QUESTION, gtk.BUTTONS_YES_NO, 'Deseja excluir o registro ?')
        resposta = msg.run()
        msg.destroy()
        #Se a resposta for sim, seleciona no banco de dados os valores que vão se excluidos.
        if resposta == gtk.RESPONSE_YES:
            self.valor_RemCli = self.listaClientes1.get_selection()#seleciona a linha onde cursor está posicionado.
            self.valor_RemCli.set_mode(gtk.SELECTION_MULTIPLE)#Define que vários itens podem ser selecionadas de cada vez.
            modelo, caminhos = self.valor_RemCli.get_selected_rows()# recupera a seleção dependendo do modo de seleção atual.
            for caminho in caminhos:
                #Define o caminho
                kiter = modelo.get_iter(caminho)
                self.delFun = modelo.get_value(kiter,3)
             #Faz uma iteração, se o caminho for igual a linha escolhida, exclui os valores no banco de dados        
            cursor.execute("SELECT * FROM clientes")
            removeCli = cursor.fetchall()
            for linha in removeCli:
                if self.delFun == linha[4]:
                    print "a"
                    cursor.execute("DELETE FROM clientes WHERE cpf='%s'" % (linha[4]))
                    connection.commit()
                    
            msg = gtk.MessageDialog(None, 0, gtk.MESSAGE_INFO, gtk.BUTTONS_OK, 'Deletado com Sucesso!')
            msg.run()
            self.le_Cliente()
            msg.destroy()
            
    def RemoverFuncionario(self, widget):
        #Posiciona o cursor na linha que deseja editar
        self.valor_RemFun = self.listaFuncionario.get_cursor()
        #Envia uma mensagem para o usuário decidir se deseja ou não excluir
        msg = gtk.MessageDialog(None, 0, gtk.MESSAGE_QUESTION, gtk.BUTTONS_YES_NO, 'Deseja excluir o registro ?')
        resposta = msg.run()
        msg.destroy()
        #Se a resposta for sim, seleciona no banco de dados os valores que vão se excluidos.
        if resposta == gtk.RESPONSE_YES:
            self.valor_RemFun = self.listaFuncionario.get_selection()#seleciona a linha onde cursor está posicionado.
            self.valor_RemFun.set_mode(gtk.SELECTION_MULTIPLE)#Define que vários itens podem ser selecionadas de cada vez.
            modelo, caminhos = self.valor_RemFun.get_selected_rows()# recupera a seleção dependendo do modo de seleção atual.
            for caminho in caminhos:
                #Define o caminho
                kiter = modelo.get_iter(caminho)
                self.delFun = modelo.get_value(kiter,3)
                #Faz uma iteração, se o caminho for igual a linha escolhida, exclui os valores no banco de dados 
            cursor.execute("SELECT * FROM funcionarios")
            removeFun = cursor.fetchall()
            for linha in removeFun: 
                if self.delFun == linha[4]:
                    print "a"
                    cursor.execute("DELETE FROM funcionarios WHERE cpf='%s'" % (linha[4]))
                    connection.commit()
                    self.le_Funcionario()
            msg = gtk.MessageDialog(None, 0, gtk.MESSAGE_INFO, gtk.BUTTONS_OK, 'Deletado com Sucesso!')
            msg.run()
            msg.destroy()
    
    def RemoverAluguel(self, widget):
        #Posiciona o cursor na linha que deseja editar
        self.valor_RemAluguel = self.listaAluguel.get_cursor()
        #Envia uma mensagem para o usuário decidir se deseja ou não excluir
        msg = gtk.MessageDialog(None, 0, gtk.MESSAGE_QUESTION, gtk.BUTTONS_YES_NO, 'Deseja excluir o registro ?')
        resposta = msg.run()
        msg.destroy()
        #Se a resposta for sim, seleciona no banco de dados os valores que vão se excluidos.
        if resposta == gtk.RESPONSE_YES:
            self.valor_RemAluguel = self.listaAluguel.get_selection()#seleciona a linha onde cursor está posicionado.
            self.valor_RemAluguel.set_mode(gtk.SELECTION_MULTIPLE)#Define que vários itens podem ser selecionadas de cada vez.
            modelo, caminhos = self.valor_RemAluguel.get_selected_rows()# recupera a seleção dependendo do modo de seleção atual.
            for caminho in caminhos:
                #Define o caminho
                kiter = modelo.get_iter(caminho)
                self.delAluguel = modelo.get_value(kiter,3)
                #Faz uma iteração, se o caminho for igual a linha escolhida, exclui os valores no banco de dados 
            cursor.execute("SELECT * FROM alugue")
            removeAluguel = cursor.fetchall()
            for linha in removeAluguel: 
                if self.delAluguel == linha[4]:
                    print "a"
                    cursor.execute("DELETE FROM alugue WHERE numeroimv='%s'" % (linha[4]))
                    connection.commit()
                    self.le_Aluguel()
            msg = gtk.MessageDialog(None, 0, gtk.MESSAGE_INFO, gtk.BUTTONS_OK, 'Deletado com Sucesso!')
            msg.run()
            msg.destroy()
                
    def RemoverVenda(self, widget):
        #Posiciona o cursor na linha que deseja editar
        self.valor_RemVenda = self.listaVenda.get_cursor()
        #Envia uma mensagem para o usuário decidir se deseja ou não excluir
        msg = gtk.MessageDialog(None, 0, gtk.MESSAGE_QUESTION, gtk.BUTTONS_YES_NO, 'Deseja excluir o registro ?')
        resposta = msg.run()
        msg.destroy()
        #Se a resposta for sim, seleciona no banco de dados os valores que vão se excluidos.
        if resposta == gtk.RESPONSE_YES:
            self.valor_RemVenda = self.listaVenda.get_selection()#seleciona a linha onde cursor está posicionado.
            self.valor_RemVenda.set_mode(gtk.SELECTION_MULTIPLE)#Define que vários itens podem ser selecionadas de cada vez.
            modelo, caminhos = self.valor_RemVenda.get_selected_rows()# recupera a seleção dependendo do modo de seleção atual.
            for caminho in caminhos:
                #Define o caminho
                kiter = modelo.get_iter(caminho)
                self.delVenda = modelo.get_value(kiter,1)
            #Faz uma iteração, se o caminho for igual a linha escolhida, exclui os valores no banco de dados        
            cursor.execute("SELECT * FROM venda")
            removeVenda = cursor.fetchall()
            for linha in removeVenda: 
                if self.delVenda == linha[2]:
                    print "a"
                    cursor.execute("DELETE FROM venda WHERE cpfvendedor='%s'" % (linha[2]))
                    connection.commit()
                    self.le_Venda()
            msg = gtk.MessageDialog(None, 0, gtk.MESSAGE_INFO, gtk.BUTTONS_OK, 'Deletado com Sucesso!')
            msg.run()
            msg.destroy()
        
    def RemoverLogin(self, widget):
        print "a"
        #Posiciona o cursor na linha que deseja editar
        self.valor_RemLog = self.listaLogin.get_cursor()
        #Envia uma mensagem para o usuário decidir se deseja ou não excluir
        msg = gtk.MessageDialog(None, 0, gtk.MESSAGE_QUESTION, gtk.BUTTONS_YES_NO, 'Deseja excluir o registro ?')
        resposta = msg.run()
        msg.destroy()
        #Se a resposta for sim, seleciona no banco de dados os valores que vão se excluidos.
        if resposta == gtk.RESPONSE_YES: 
            self.valor_RemLog = self.listaLogin.get_selection()#seleciona a linha onde cursor está posicionado.
            self.valor_RemLog.set_mode(gtk.SELECTION_MULTIPLE)#Define que vários itens podem ser selecionadas de cada vez.
            modelo, caminhos = self.valor_RemLog.get_selected_rows()# recupera a seleção dependendo do modo de seleção atual.
            for caminho in caminhos:
                    kiter = modelo.get_iter(caminho)
                    #coloquei o self para poer pegar esse valor em outro lugar
                    self.codigo = modelo.get_value(kiter, 0)
            #Faz uma iteração, se o caminho for igual a linha escolhida, exclui os valores no banco de dados               
            cursor.execute("SELECT * FROM login")
            removeLogin = cursor.fetchall()
            for linha in removeLogin: 
                if self.codigo == linha[1]:
                    print "a"
                    cursor.execute("DELETE FROM login WHERE login ='%s'" % (linha[1]))
                    connection.commit()
                    self.le_Login()
            msg = gtk.MessageDialog(None, 0, gtk.MESSAGE_INFO, gtk.BUTTONS_OK, 'Deletado com Sucesso!')
            msg.run()
            msg.destroy()
            
    def novoContratoVenda(self, widget):
        #Se algum campo necessário para o preenchimento do Contrato estiver vazio retorna uma mensagem de erro 
        if (self.vendedor.get_text() == "" or self.naturalidadevendedor.get_text() == "" or self.ecvendedor.get_text() == "" or self.profissaovend.get_text() == ""\
            or self.rgvenderdor.get_text() == "" or self.cpfvendedor.get_text() == "" or self.enderecovendedor.get_text() == "" or self.numerovendedor.get_text() == ""\
            or self.bairrovendedor.get_text() == "" or self.cepvendedor.get_text() == "" or self.cidadevendedor.get_text() == "" or self.estadovendedor.get_text() == ""\
            or self.comprador.get_text() == "" or self.naturalidadecomprador.get_text() == "" or self.eccomprador.get_text() == "" or self.profissaocomprador.get_text() == ""\
            or self.rgcomprador.get_text() == "" or self.cpfcomprador.get_text() == "" or self.enderecocomprador.get_text() == "" or self.numerocomprador.get_text() == ""\
            or self.bairrocomprador.get_text() == "" or self.cepcomprador.get_text() == "" or self.cidadecomprador.get_text() == "" or self.estadocomprador.get_text() == ""\
            or self.areavenda.get_text() == "" or self.registovenda.get_text() == "" or self.valorvenda.get_text() == ""):
            msg = gtk.MessageDialog(None, 0, gtk.MESSAGE_INFO, gtk.BUTTONS_OK, 'Preencha todos os campos!')
            msg.run()
            msg.destroy()
        else:
        
            nomeVend = self.vendedor.get_text()
            naturalidadeVend = self.naturalidadevendedor.get_text()
            estadoCivilVend = self.ecvendedor.get_text()
            profissaoVend = self.profissaovend.get_text()
            rgVend = self.rgvenderdor.get_text()
            cpfVend = self.cpfvendedor.get_text()
            ruaVend = self.enderecovendedor.get_text()
            numVend = self.numerovendedor.get_text()
            bairroVend = self.bairrovendedor.get_text()
            cepVend = self.cepvendedor.get_text()
            cidadeVend = self.cidadevendedor.get_text()
            estadoVend = self.estadovendedor.get_text()
            nomeComp = self.comprador.get_text()
            naturalidadeComp = self.naturalidadecomprador.get_text()
            estadoCivilComp = self.eccomprador.get_text()
            profissaoComp = self.profissaocomprador.get_text()
            rgComp = self.rgcomprador.get_text()
            cpfComp = self.cpfcomprador.get_text()
            ruaComp = self.enderecocomprador.get_text()
            numComp = self.numerocomprador.get_text()
            bairroComp = self.bairrocomprador.get_text()
            cepComp = self.cepcomprador.get_text()
            cidadeComp = self.cidadecomprador.get_text()
            estado = self.estadocomprador.get_text()
            area = self.areavenda.get_text()
            registro = self.registovenda.get_text()
            valor = self.valorvenda.get_text()
            #Define os parametros para substituíção na função de novo venda do arquivo de atualizar contrato de venda
            contratovenda.novoVenda(nomeVend, naturalidadeVend,estadoCivilVend,profissaoVend,rgVend,cpfVend,ruaVend,numVend,bairroVend,cepVend,cidadeVend,estadoVend,nomeComp,naturalidadeComp,estadoCivilComp,profissaoComp,rgComp,cpfComp,ruaComp,numComp,bairroComp,cepComp,cidadeComp, estado, area, registro, valor)
            msg = gtk.MessageDialog(None, 0, gtk.MESSAGE_INFO, gtk.BUTTONS_OK, 'Contrato salvo com sucesso!')
            msg.run()
            msg.destroy()

    def atualizarContratoVenda(self, widget):
        #Se algum campo necessário para o preenchimento do Contrato estiver vazio retorna uma mensagem de erro 
        if(self.vendedor_EDTVENDA.get_text() == "" or self.naturalidade_EDTVENDA.get_text() == "" or self.estcivil_EDTVENDA.get_text() == "" or self.prof_EDTVENDA.get_text() == ""\
           or self.rg_EDTVENDA.get_text() == "" or self.cpf_EDTVENDA.get_text() == "" or self.end_EDTVENDA.get_text() == "" or self.numero_EDTVENDA.get_text() == ""\
           or self.bairro_EDTVENDA.get_text() == "" or self.cep_EDTVENDA.get_text() == "" or self.cidade_EDTVENDA.get_text() == "" or self.estado_EDTVENDA.get_text() == ""\
           or self.comprador_EDTCOMPRA.get_text() == "" or self.naturalidade_EDTCOMPRA.get_text() == "" or self.estcivil_EDTCOMPRA.get_text() == "" or self.prof_EDTCOMPRA.get_text() == ""
           or self.rg_EDTCOMPRA.get_text() == "" or self.cpf_EDTCOMPRA.get_text() == "" or self.end_EDTCOMPRA.get_text() == "" or self.numero_EDTCOMPRA.get_text() == ""\
           or self.bairro_EDTCOMPRA.get_text() == "" or self.cep_EDTCOMPRA.get_text() == "" or self.cidade_EDTCOMPRA.get_text() == "" or self.estado_EDTCOMPRA.get_text() == ""\
           or self.area_EDTVENDA.get_text() == "" or self.registro_EDTVENDA.get_text() == "" or self.valor_EDTVENDA.get_text() == ""):
            msg = gtk.MessageDialog(None, 0, gtk.MESSAGE_INFO, gtk.BUTTONS_OK, 'Preencha todos os campos!')
            msg.run()
            msg.destroy()

        else:   
            nomeVend = self.vendedor_EDTVENDA.get_text()
            naturalidadeVend = self.naturalidade_EDTVENDA.get_text()
            estadoCivilVend = self.estcivil_EDTVENDA.get_text()
            profissaoVend = self.prof_EDTVENDA.get_text()
            rgVend = self.rg_EDTVENDA.get_text()
            cpfVend = self.cpf_EDTVENDA.get_text()
            ruaVend = self.end_EDTVENDA.get_text()
            numVend = self.numero_EDTVENDA.get_text()
            bairroVend = self.bairro_EDTVENDA.get_text()
            cepVend = self.cep_EDTVENDA.get_text()
            cidadeVend = self.cidade_EDTVENDA.get_text()
            estadoVend = self.estado_EDTVENDA.get_text()
            nomeComp = self.comprador_EDTCOMPRA.get_text()
            naturalidadeComp = self.naturalidade_EDTCOMPRA.get_text()
            estadoCivilComp = self.estcivil_EDTCOMPRA.get_text()
            profissaoComp = self.prof_EDTCOMPRA.get_text()
            rgComp = self.rg_EDTCOMPRA.get_text()
            cpfComp = self.cpf_EDTCOMPRA.get_text()
            ruaComp = self.end_EDTCOMPRA.get_text()
            numComp = self.numero_EDTCOMPRA.get_text()
            bairroComp = self.bairro_EDTCOMPRA.get_text()
            cepComp = self.cep_EDTCOMPRA.get_text()
            cidadeComp = self.cidade_EDTCOMPRA.get_text()
            estado = self.estado_EDTCOMPRA.get_text()
            area = self.area_EDTVENDA.get_text()
            registro = self.registro_EDTVENDA.get_text()
            valor = self.valor_EDTVENDA.get_text()
            #Define os parametros para substituíção na função de atualizar venda do arquivo de atualizar contrato de venda
            ATUALIZARVENDA.atualizarVenda(nomeVend, naturalidadeVend,estadoCivilVend,profissaoVend,rgVend,cpfVend,ruaVend,numVend,bairroVend,cepVend,cidadeVend,estadoVend,nomeComp,naturalidadeComp,estadoCivilComp,profissaoComp,rgComp,cpfComp,ruaComp,numComp,bairroComp,cepComp,cidadeComp, estado, area, registro, valor)
            msg = gtk.MessageDialog(None, 0, gtk.MESSAGE_INFO, gtk.BUTTONS_OK, 'Contrato salvo com sucesso!')
            msg.run()
            msg.destroy()

    def novoContratoAluguel(self, widget):
        #Se algum campo necessário para o preenchimento do Contrato estiver vazio retorna uma mensagem de erro 
        if (self.locador.get_text() == "" or self.locatario.get_text() == "" or self.fiador1.get_text() == "" or self.estCivil1.gets_text() == "" or self.profissao1.get_text() == ""\
            or self.rg1.get_text() == "" or self.cpf1.get_text() == "" or self.endereco1.get_text() == "" or self.numero1.get_text() == "" or self.bairro1.get_text() == ""\
            or self.cidade1.get_text() == "" or self.estado1.get_text() == "" or self.esposa1.get_text() == "" or self.rgEsposa1.get_text() == "" or self.cpfEsposa1.get_text() == ""\
            or self.fiador2.get_text() == "" or self.estCivil2.get_text() == "" or self.profissao2.get_text() == "" or self.rg2.get_text() == "" or self.cpf2.get_text() == ""\
            or self.endereco2.get_text() == "" or self.numero2.get_text() == "" or self.bairro2.get_text() == "" or self.cidade2.get_text() == "" or self.estado2.get_text() == ""\
            or self.esposa2.get_text() == "" or self.rgEsposa2.get_text() == "" or self.cpfEsposa2.get_text() == "" or self.numeroIMV.get_text() == "" or self.prazoIMV.get_text() == ""\
            or self.inicioIMV.get_text() == "" or self.terminoIMV.get_text() == "" or self.valorIMV.get_text() == "" or self.vencimentoIMV.get_text() == ""):
            msg = gtk.MessageDialog(None, 0, gtk.MESSAGE_INFO, gtk.BUTTONS_OK, 'Preencha todos os campos necessários para preencher o contrato!')
            msg.run()
            msg.destroy()
            
        else:
            #Substitui as variáveis pelo nome dos campo 
            nomelocador = self.locador.get_text()
            nomelocatario = self.locatario.get_text()
            fiadorI = self.fiador1.get_text()
            ecI = self.estCivil1.get_text()
            profI = self.profissao1.get_text()
            rgI = self.rg1.get_text()
            cpfI = self.cpf1.get_text()
            ruaI = self.endereco1.get_text()
            numI = self.numero1.get_text()
            bairroI = self.bairro1.get_text()
            cidadeI = self.cidade1.get_text()
            ufI = self.estado1.get_text()
            conjugueI = self.esposa1.get_text()
            rgconjugueI = self.rgEsposa1.get_text()
            cpfconjugueI = self.cpfEsposa1.get_text()
            fiadorII = self.fiador2.get_text()
            ecII = self.estCivil2.get_text()
            profII = self.profissao2.get_text()
            rgII = self.rg2.get_text()
            cpfII = self.cpf2.get_text()
            ruaII = self.endereco2.get_text()
            numII = self.numero2.get_text()
            bairroII = self.bairro2.get_text()
            cidadeII = self.cidade2.get_text()
            ufII = self.estado2.get_text()
            conjugueII = self.esposa2.get_text()
            rgconjugueII = self.rgEsposa2.get_text()
            cpfconjugueII = self.cpfEsposa2.get_text()
            registro = self.numeroIMV.get_text()
            prazo = self.prazoIMV.get_text()
            inicio = self.inicioIMV.get_text()
            fim = self.terminoIMV.get_text()
            valor = self.valorIMV.get_text()
            vencimento = self.vencimentoIMV.get_text()
            #Define os parametros para substituíção na função de novo aluguel do arquivo de atualizar contrato de aluguel
            contratoaluguel.novoAluguel(nomelocador, nomelocatario, fiadorI, ecI, profI, rgI, cpfI, ruaI, numI, bairroI, cidadeI, ufI, conjugueI, rgconjugueI, cpfconjugueI, fiadorII, ecII, profII, rgII, cpfII, ruaII, numII, bairroII, cidadeII, ufII, conjugueII, rgconjugueII, cpfconjugueII ,registro, prazo, inicio, fim, valor, vencimento)
            msg = gtk.MessageDialog(None, 0, gtk.MESSAGE_INFO, gtk.BUTTONS_OK, 'Contrato salvo com sucesso!')
            msg.run()
            msg.destroy()
             
    def atualizarContratoAluguel(self, widget):
        #Se algum campo necessário para o preenchimento do Contrato estiver vazio retorna uma mensagem de erro 
        if (self.locador_SLC.get_text() == "" or self.locatario_SLC.get_text() == "" or self.fiador1_SLC.get_text() == "" or self.estCivil1_SLC.get_text() == ""\
            or self.profissao1_SLC.get_text() == "" or self.rg1_SLC.get_text() == "" or self.cpf1_SLC.get_text() == "" or self.endereco1_SLC.get_text() == ""\
            or self.numero1_SLC.get_text() == "" or self.bairro1_SLC.get_text() == "" or self.cidade1_SLC.get_text() == "" or self.estado1_SLC.get_text() == ""\
            or self.esposa1_SLC.get_text() == "" or self.rgEsposa1_SLC.get_text() == "" or self.cpfEsposa1_SLC.get_text() == "" or self.fiador2_SLC.get_text() == ""\
            or self.estCivil2_SLC.get_text() == "" or self.profissao2_SLC.get_text() == "" or self.rg2_SLC.get_text() == "" or self.cpf2_SLC.get_text() == ""\
            or self.endereco2_SLC.get_text() == "" or self.numero2_SLC.get_text() == "" or self.bairro2_SLC.get_text() == "" or self.cidade2_SLC.get_text() == ""\
            or self.estado2_SLC.get_text() == "" or self.esposa2_SLC.get_text() == "" or self.rgEsposa2_SLC.get_text() == "" or self.cpfEsposa2_SLC.get_text() == ""\
            or self.numeroIMV_SLC.get_text() == "" or self.prazoIMV_SLC.get_text() == "" or self.inicioIMV_SLC.get_text() == "" or self.terminoIMV_SLC.get_text() == ""\
            or self.valorIMV_SLC.get_text() == "" or self.vencimentoIMV_SLC.get_text() == ""):
            msg = gtk.MessageDialog(None, 0, gtk.MESSAGE_INFO, gtk.BUTTONS_OK, 'Preencha todos os campos necessários para preencher o contrato!')
            msg.run()
            msg.destroy()
            
        else:
            #Substitui as variáveis pelos nomes dos campos
            nomelocador = self.locador_SLC.get_text()
            nomelocatario = self.locatario_SLC.get_text()
            fiadorI = self.fiador1_SLC.get_text()
            ecI = self.estCivil1_SLC.get_text()
            profI = self.profissao1_SLC.get_text()
            rgI = self.rg1_SLC.get_text()
            cpfI = self.cpf1_SLC.get_text()
            ruaI = self.endereco1_SLC.get_text()
            numI = self.numero1_SLC.get_text()
            bairroI = self.bairro1_SLC.get_text()
            cidadeI = self.cidade1_SLC.get_text()
            ufI = self.estado1_SLC.get_text()
            conjugueI = self.esposa1_SLC.get_text()
            rgconjugueI = self.rgEsposa1_SLC.get_text()
            cpfconjugueI = self.cpfEsposa1_SLC.get_text()
            fiadorII = self.fiador2_SLC.get_text()
            ecII = self.estCivil2_SLC.get_text()
            profII = self.profissao2_SLC.get_text()
            rgII = self.rg2_SLC.get_text()
            cpfII = self.cpf2_SLC.get_text()
            ruaII = self.endereco2_SLC.get_text()
            numII = self.numero2_SLC.get_text()
            bairroII = self.bairro2_SLC.get_text()
            cidadeII = self.cidade2_SLC.get_text()
            ufII = self.estado2_SLC.get_text()
            conjugueII = self.esposa2_SLC.get_text()
            rgconjugueII = self.rgEsposa2_SLC.get_text()
            cpfconjugueII = self.cpfEsposa2_SLC.get_text()
            registro = self.numeroIMV_SLC.get_text()
            prazo = self.prazoIMV_SLC.get_text()
            inicio = self.inicioIMV_SLC.get_text()
            fim = self.terminoIMV_SLC.get_text()
            valor = self.valorIMV_SLC.get_text()
            vencimento = self.vencimentoIMV_SLC.get_text()
            #Define os parametros para substituíção na função de atualizar aluguel do arquivo de atualizar contrato de aluguel
            atualizaraluguel.atualizarAluguel(nomelocador, nomelocatario, fiadorI, ecI, profI, rgI, cpfI, ruaI, numI, bairroI, cidadeI, ufI, conjugueI, rgconjugueI, cpfconjugueI, fiadorII, ecII, profII, rgII, cpfII, ruaII, numII, bairroII, cidadeII, ufII, conjugueII, rgconjugueII, cpfconjugueII ,registro,prazo, inicio, fim, valor, vencimento)
            msg = gtk.MessageDialog(None, 0, gtk.MESSAGE_INFO, gtk.BUTTONS_OK, 'Contrato salvo com sucesso!')
            msg.run()
            msg.destroy()

m = Login()
gtk.main()
