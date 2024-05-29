'''Faça um algoritmo em Python que leia de cem (100) alunos de um curso EAD da UVV:

LER DO USUÁRIO: Nota [0, 1] na AOP1: Atividade Online Pontuada 1;
LER DO USUÁRIO: Nota [0, 2] na AOP2: Atividade Online Pontuada 2;
LER DO USUÁRIO: Nota [0, 1] na AOP3: Atividade Online Pontuada 3;
LER DO USUÁRIO: Nota [0, 6] da PROVA REGULAR;
LER DO USUÁRIO: Nota [0, 10] da PROVA DE RECUPERAÇÃO: Somente se o aluno não obteve Soma do Módulo (AOP1 + AOP2 + AOP3 + Prova Regular) >=7
E, calcule e mostre na tela: as informações a seguir:
Soma do Módulo (SM) = AOP1 + APO2 + AOP3 + PROVA REGULAR
Aluno = float (input("Nota Aop1: "))

print (type (Aluno))
Média do Módulo (MM) = (AOP1 + APO2 + AOP3 + PROVA REGULAR + PROVA DE RECUPERAÇÃO)/2'''
aprovado = 0
reprovado = 0
i = 0
while i < 5:
    print("\n"*2)
    print(f"---- Aluno {i+1}----")
    aop1 = float(input("Insira uma nota AOP1: "))
    if aop1 <=1 and aop1>=0:
        aop2 = float(input("Insira uma nota AOP2: "))
        if aop2 <=2 and aop2 >=0:
            aop3 = float(input("Insira uma nota AOP3: "))
            if aop3 <=1 and aop3>=0:
                prova = float(input("Insira uma nota da PROVA: "))
                if prova <=6 and prova >=0:
                    sm = aop1 + aop2 + aop3 + prova
                    if sm >=7:
                        print("APROVADO")
                        aprovado = aprovado + 1
                        i += 1
                    else:
                        print("PROVA DE RECUPERACAO")
                        recuperacao = float(input("Nota prova de recuperação: "))
                        if recuperacao <=10 and recuperacao >=0:
                            if (sm + recuperacao) / 2 >=5:
                                print("APROVADO")
                                aprovado = aprovado + 1
                                i += 1
                            else:
                                print("REPROVADO")
                                reprovado = reprovado + 1
                                i += 1
                        else:
                            print("\nDigite um numero valido")
                        
                    
                else:
                    print("\nDigite um numero valido")
                
            else:
                print("\nDigite um numero valido")
        
            
        else:
            print("\nDigite um numero valido")
    else:
        print("\nDigite um numero valido")
print(f"Aprovado: {(aprovado / (aprovado + reprovado)):.0%}")
print(f"Reprovado: {(reprovado / (aprovado + reprovado)):.0%}")