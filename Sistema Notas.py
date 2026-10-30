#Pojeto de algoritmo: Notas

n1=0
n2=0
ap=0
rep=0
rec=0
ac=0
m=0
re=0

while re!=6:
    print('Bem-vindo ao controle de notas!\n')

    print(f'1 - Cadastrar Notas')
    print(f'2 - Qtd. Alunos Cadastrados')
    print(f'3 - Qtd. de Aprovados')
    print(f'4 - Qtd. de Recuperação')
    print(f'5 - Qtd. de Reprovados')
    print(f'6 - Finalizar\n')

    re = int(input('Escolha uma opção: \n'))

    if re==1:
        n1=int(input(f'Digite a primeira nota: '))
        n2=int(input(f'Digite a segunda nota: '))
        m=(n1+n2)/2
        ac+=1
        if m < 5:
            print('Esse aluno foi reprovado!')
            rep+=1
        elif m>=5 and m<=6.9:
            print('Esse aluno está de recuperação!')
            rec+=1
        else:
            print('Esse aluno foi aprovado!')
            ap+=1

    elif re==2:
        print(f'O número de alunos cadastrados até o momento é {ac}.')

    elif re==3:
        print(f'A quantidade de alunos aprovados até o momento é {ap}.')

    elif re==4:
        print(f'A quantidade de alunos em recuperação até o momento é de {rec}.')

    elif re==5:
        print(f'A quantidade de alunos reprovados até o momento é de {rep}')

    elif re==6:
        print(f'Obrigado por cadastrar conosco! Você cadastrou {ac} alunos, sendo: {ap} aprovados, {rec} de recuperação e {rep} reprovados. Encerrando programa...')

    else:
        print('Esse número não está listado! Escolha um listado!')






