n1, n2, n3, n4 = map(float, input().split())
media = ((n1 * 2) + (n2 * 3) + (n3 * 4) + (n4 * 1)) / 10
print(f'Media: {media:.1f}')
if media >= 7.0:
    print('Aluno aprovado.')
if media < 5.0:
    print('Aluno reprovado.')
if 5.0 <= media <= 6.9:
    print('Aluno em exame.')
    notaExame = float(input())
    print(f'Nota do exame: {notaExame:.1f}')
    mediaFinal = (media + notaExame) / 2
    if mediaFinal >= 5:
        print('Aluno aprovado.')
        print(f'Media final: {mediaFinal:.1f}')
    else:
        print(f'Aluno reprovado.')
        print(f'Media final: {mediaFinal:.1f}')
