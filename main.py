import re

#FUNÇÃO PARA EXPANDIR O INCLUDE
def expand(linha, newArq):
  includes = ""
  if ("#include" in linha):
    indice = linha.find("<") 
    if (indice != -1):
      includes = linha[indice + 1:len(linha.strip()) - 1]
    indice = linha.find("\"")
    if (indice != -1):
      includes = linha[indice + 1:len(linha.strip()) - 1]

    PreProcessador(includes, newArq)

#FUNÇÃO QUE SIMULA O PRÉ-PROCESSADOR
def PreProcessador(arqC,ArqAlterado): 
  with open(arqC,'r') as file: 
    arq = file.readlines() 
    file.close() 

  listaArq=[] 

  #FOR PARA TIRAR QUEBRA DE LINHAS
  for linha in arq: 
    if '\n' in linha: 
      linha = linha.replace('\n','') 
    listaArq.append(linha) 

  newList=[] 
  
  #FOR PARA TIRAR COMENTÁRIOS 
  for linha in listaArq: 
    if ' ' in linha:
      linha=re.sub("^\s+",'', linha)  
    if '#include' in linha:
      listaArq = expand(linha,ArqAlterado) 
      linha = ''
    if '//' in linha: 
      linha = '' 
    newList.append(linha) 

  editArq=''.join(newList) 

  
  for linha in editArq:
    ArqAlterado.write(linha)
    
  return editArq 

#MAIN
arqC = 'exemplo.c' 
ArqAlterado = open('arqAlterado.c','w') 
editArq = PreProcessador(arqC,ArqAlterado)

#Imprimindo Arqs antes
with open(arqC,'r') as file:
  LerArq=file.read()
print(LerArq) 
print('##########################################')
print("\n")

#Imprimindo Arqs depois
print(editArq)

ArqAlterado.close() 