# Recuperando o Cofre de Segurança
# O cofre da biblioteca guarda códigos raros de programação, mas o vírus resetou a senha! Agora, apenas quem souber a combinação correta poderá acessá-lo.
# Crie um programa que solicite ao usuário uma senha e verifique se ela está correta. A senha correta é "Python123".

senha_correta = "Python123"
senha_solicitada = input("Digite a senha correta para acessar o cofre: ")

if senha_solicitada == senha_correta:
  print(f"Senha correta, acesso permitido!")
else:
  print(f"Senha incorreta, acesso negado!")
