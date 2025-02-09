# Recuperando o Sistema de Notas
# As classificações das provas desapareceram! Agora os alunos não sabem se tiraram um não sabem se tiraram um A, B, C, D ou F . Antes que o pânico se espalhe, sua tarefa é criar um programa que peça a nota do aluno e imprima sua classificação conforme a escala:
# - A (90-100) – "Parabéns, você tirou A!"
# - B (80-89) – "Muito bem, você tirou B."
# - C (70-79) – "Bom trabalho, você tirou C."
# - D (60-69) – "Fique atento, você tirou D."
# - F (menos de 60) – "Estude um pouco mais, você tirou F."

nota_para_classificacao = int(input("Digite a sua nota para saber sua classificação: "))

if nota_para_classificacao >= 90 or nota_para_classificacao == 100:
  print(f"Parabéns, você tirou um A!")
elif nota_para_classificacao >= 80:
  print(f"Muito bem, você tirou B.")
elif nota_para_classificacao >= 70:
  print(f"Bom trabalho, você tirou C.")
elif nota_para_classificacao >= 60:
  print(f"Fique atento, você tirou D.")
else:
  print(f"Estude um pouco mais, você tirou F.")
