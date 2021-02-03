students = []

def addStudents():
    while True:
        students.append(input("Insira o nome do " + str(len(students)+1) + "º estudante: "))

        addNewStudent = input("Deseja inserir o nome de um novo aluno na lista? Responda com sim ou não.\n")

        if addNewStudent != "sim":
            break

def searchForStudent(array, searchedName):
    found = False
    
    i = 0

    while i < len(array) and found == False:
        if searchedName == array[i]:
            found = True
        else:
            i += 1

    return found,i

addStudents()

keepGoing = "sim"

while keepGoing == "sim":
    search = input("Insira o nome do aluno que deseja buscar: ")

    x = searchForStudent(students, search)

    if x[0] == True:
        print("O(A) aluno(a) " + search + " foi encontrado(a) na " + str(x[1]+1) + "º posição da lista.")
    else:
        print("O(A) aluno(a) " + search + " não foi encontrado(a) na lista.")

    keepGoing = input("Deseja pesquisar o nome de outro aluno? Responda com sim ou não.\n")
