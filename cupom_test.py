import cupom;

cupom.nome_loja = "Arcos Dourados Com. de Alimentos LTDA"
cupom.logradouro = "Av. Projetada Leste"
cupom.numero = 500
cupom.complemento = "EUC F32/33/34"
cupom.bairro = "Br. Sta Genebra"
cupom.municipio = "Campinas"
cupom.estado = "SP"
cupom.cep = "13080-395"
cupom.telefone = "(19) 3756-7408"
cupom.observacao = "Loja 1317 (PDP)"
cupom.cnpj = "42.591.651/0797-34"
cupom.inscricao_estadual = "244.898.500.113"

def test_exercicio1():
    assert cupom.imprime_dados_loja() == '''Arcos Dourados Com. de Alimentos LTDA
Av. Projetada Leste, 500 EUC F32/33/34
Br. Sta Genebra - Campinas - SP
CEP:13080-395 Tel (19) 3756-7408
Loja 1317 (PDP)
CNPJ: 42.591.651/0797-34
IE: 244.898.500.113
'''

def test_exercicio2_tudo_vazio():
    global nome_loja
    global logradouro
    global numero
    global complemento
    global bairro
    global municipio
    global estado
    global cep
    global telefone
    global observacao
    global cnpj
    global inscricao_estadual
    
    cupom.nome_loja = ""
    cupom.logradouro = ""
    cupom.numero = 0
    cupom.complemento = ""
    cupom.bairro = ""
    cupom.municipio = ""
    cupom.estado = ""
    cupom.cep = ""
    cupom.telefone = ""
    cupom.observacao = ""
    cupom.cnpj = ""
    cupom.inscricao_estadual = ""

    assert cupom.imprime_dados_loja() == '''
, 0 
 -  - 
CEP: Tel 

CNPJ: 
IE: 
'''

def test_exercicio2_customizado():
    global nome_loja
    global logradouro
    global numero
    global complemento
    global bairro
    global municipio
    global estado
    global cep
    global telefone
    global observacao
    global cnpj
    global inscricao_estadual
    
    # Defina seus próprios valores para as variáveis a seguir
    cupom.nome_loja = "LOJAS AMERICANAS S.A."
    cupom.logradouro = "R SACADURA CABRAL"
    cupom.numero = 102
    cupom.complemento = ""
    cupom.bairro = "GAMBOA"
    cupom.municipio = "RIO DE JANEIRO"
    cupom.estado = "RJ"
    cupom.cep = "20.221-160"
    cupom.telefone = "(21) 2206-6708"
    cupom.observacao = "47.11-3-02 Comercio varejista de mercadorias em geral"
    cupom.cnpj = "33.014.556/0001-96"
    cupom.inscricao_estadual = "85.687.08-5"

    #E atualize o texto esperado abaixo
    assert cupom.imprime_dados_loja() == '''LOJAS AMERICANAS S.A.
R SACADURA CABRAL, 102 
GAMBOA - RIO DE JANEIRO - RJ
CEP:20.221-160 Tel (21) 2206-6708
47.11-3-02 Comercio varejista de mercadorias em geral
CNPJ: 33.014.556/0001-96
IE: 85.687.08-5
'''
