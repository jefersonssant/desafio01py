# 1: Restaurando as Regras Escolares 
# O vírus apagou os critérios de aprovação dos alunos! Para ajudar o Professor Byte a organizar o sistema, sua tarefa é criar um programa que verifique se um aluno foi aprovado (nota maior ou igual à 6) ou reprovado (nota menor ou igual à 5).

media = 6
nota = int(input("Digige sua nota para saber o resultado: "))

if nota >= media:
  print(f"Você foi APROVADO, a média para aprovação é {media} e sua nota é {nota}")
else:
  print(f"Você foi REPROVADO, a média para a aprovação é {media} e sua nota é {nota}")
