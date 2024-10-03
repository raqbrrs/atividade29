# Crie um programa que receba uma lista com os nomes dos alunos presentes em uma aula e exiba quantos alunos estão presentes e a lista dos nomes. Se o total de alunos presentes for menor que 5, exiba uma mensagem sugerindo uma revisão da lista de chamada.

# Exemplo de entrada:
# Alunos presentes: ['Ana', 'Bruno', 'Carlos', 'Daniela']

# Exemplo de saída:
# Alunos presentes: 4
# Lista de alunos presentes: Ana, Bruno, Carlos, Daniela
# Aviso: Poucos alunos presentes. Revisar lista de chamada.

def lista_presenca(alunos_presentes):
    total_presentes = len(alunos_presentes)
    print(f"alunos que estão presentes: {total_presentes}")
    print("lista de alunos presentes:", ', '.join(alunos_presentes))
    
    if total_presentes < 5:
        print("aviso: Poucos alunos presentes. revisar lista de chamada.")

# Exemplo
alunos_presentes = ["raquel", "livia", "thayane", "camila",]
lista_presenca(alunos_presentes)

    