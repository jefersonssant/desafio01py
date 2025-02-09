# O Sistema Eleitoral Secreto
# O grêmio estudantil da escola realiza votações para decidir melhorias e inovações, mas o vírus desativou a verificação de elegibilidade para votar! Sua tarefa é criar um programa que pergunte a idade do usuário e informe se ele pode votar (mínimo: 16 anos).

idade_minima = 16
idade = int(input("Informe a sua idade: "))

if idade >= idade_minima:
  print(f"Você PODE votar, sua idade é {idade} anos e a idade mínima permitida é {idade_minima} anos")
else:
  print(f"Você NÃO PODE votar, sua idade é {idade} anos e a idade mínima permitida é {idade_minima} anos")
