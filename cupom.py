nome_loja = "Arco Dourados Com. de Alimentos LTDA"
logradouro = "Av. Projetada Leste"
numero = 500
complemento = "EUC F32/33/34"
bairro = "Br. Sta Genebra"
municipio = "Campinas"
estado = "SP"
cep = "13080-395"
telefone = "(19) 3756-7408"
observacao = "Loja 1317 (PDP)"
cnpj = "42.591.651/0797-34"
inscricao_estadual = "244.898.500.113"

def imprime_dados_loja():
  show = "%s\n%s, %d %s\n%s - %s - %s\nCEP:%s Tel %s\n%s\nCNPJ: %s\nIE: %s\n" %(nome_loja,logradouro,numero,complemento,bairro,municipio,estado,cep,telefone,observacao,cnpj,inscricao_estadual)
  return show
