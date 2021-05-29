# TUPLES

ejemplo = ("Pastel",'Panqué',"Muffin")
# Siempre se usan comas, un tuple con solo 1 elemento debe llevar coma forzosamente

vertigo_data = ("Vertigo", 1958, "A. Hitchcock")

#SE PUEDEN GUARDAR TUPLES DENTRO DE LISTAS

scores = [("mia", 75), ("Lee", 90)] #Contiene dos elementos
print(scores[0]) #---- para imprimir un elemento en específico

for user_scores in scores:
	print(f"Result: {user_scores}")


def get_scores_data(score_list):
  highest_score = max(score_list)
  lowest_score = min(score_list)
  return highest_score, lowest_score

scores = [31, 748, 96, 2, 9]
data = get_scores_data(scores)


def form_team(players):
  team=[]
  team.append(players[0])
  team.append(players[2])
  return team

players = ["Sue", "Ed", "Ann", "Ty"]
team = form_team(players)
team[0] = 'Robert'


# DICTIONARIES

locations = {"Headquarters": "New Zeland", "Flagship": "Indonesia"}

# SE PUEDE GUARDAR CUALQUIER TIPO DE DATO DENTRO DE UN DICCIONARIO
# SOLAMENTE SE PUEDE USAR LA ETIQUETA UNA SOLA VEZ, NO SE PUEDEN REPETIR
# SOLAMENTE SE PUEDE ASIGNAR UN VALOR A UNA SOLA ETIQUETA

car_data = {"Brand": "Cadillac", "Year": 1960, "Restoration": ["1990", "2018"], "Rented": False}

winner = {"Firsr": ("Ted", 50),
          "Second": ("Sara", 79)
        }
actor_bio = {"name": "Bill Murray",
             "Known for": ["Lost in Translation", "Rushmore"]
             }
# PARA IMPRIMIR UN SOLO DATO DEL DICCIONARIO
# print(actor_bio["name"]) 
# O SE PUEDE CREAR UNA VARIABLE actor_name = actor_bio["name"]

players_scores = {"Ann": 13, "Michael": 20, "Ava":34}
for player in players_scores:
    print(players_scores[player])


ticket = {"Seat no.": 25, "first class": False}
# UPDATE A VALUE
ticket["first class"] = True

# AGREGAR VALORES A LOS DICCIONARIOS

boletos = {"seat no.": 66}
boletos["Window"]=True

# PARA BUSCAR UNA KEYWORD EN UN DICCIONARIO SE USA 'in'
# IMORIME UN BOOLEANO

print("name" in actor_bio)

ejemplo_2 = "Brand" in car_data

# PODEMOS ELIMINAR UN ELEMENTO DE UN DICCIONARIO USANDO .pop()


cochinita = {"Tacos": 40, "Panuchos": 30, "Tortas con queso": 2, "Agua de jamaica": 0}

if "Agua de jamaica" in cochinita:
    cochinita.pop("Agua de jamaica")


# Creating Sets
# DENTRO DE LOS SETS NO SE PUEDEN REPETIR VALORES
# SI SE REPITE ALGÚN ELEMENTO SE IMPRIME EL PRIMERO Y LOS SE OMITEN

postcodes = {"2",2}
postcodes.add(56)

T = {18,0.9,48,20,94,7,9,2,8}
# SETS no tienen orden, no se puede imprimir pr index
# Se busca elementos en los SETS con la ayuda de 'in'
print(45 in T)

#  for number in T:
#	print(f"Los números son: {number}")

# PARA ELIMINAR UN ELEMENTO
T.remove(94)
'''
EJ 1:
if 20 in T:
	T.remove(20)
'''
'''
EJ 2:
if 5 not in T:
	print("sacate, no está")
'''
'''
EJ 3:
 if 69 not in T:
	postcodes.add("Saluton mondo")
print(postcodes)
'''

# PODEMOS TRANSFORMAR UNA 'LISTA' EN 'SET' CON EL COMANDO
# print(set(Ej_4))

Ej_4 = ["Todos", "comen", "pastel", "pastel", 66,66, 82]

# SE PUEDE CREAR UNA VARIABLE PARA GUARDAR EL CAMBIO 'LIST -> SET'

# SE PUEDEN TENER SUBSETS cuando tiene info que el SET contiene

Friends = {"Fadil", "Karlos", "Jorge", "Mariano"}
Apex = {"Mariano", "Karlos"}

# PARA SABER SI ES UN 'SUBSET' SE USA EL COMANDO 'print(Apex.issubset(Friends))

print(f"{len(Friends)}, los necesarios para un squad de Warzone")

# Se pueden unir dos SETS usando 'print(Warzone.union(Apex))

Warzone = {"Barri", "Guarda", "Mariano", "Miguel"} 
Apex = {"Barri", "Mariano", "Italo"}

# PARA SABER QUE ELEMENTOS SE REPITEN EN AMBOS SETS USAMOS .intersection()

Apezone = Apex.union(Warzone)
Warpex = Warzone.intersection(Apex)

# PARA CONOCER LOS ELEMENTOS QUE SON UNICOS EN DOS SETS SE USA .difference()
# ES DE SUMA IMPORTANCIA EL ORDEN DE CUAL SET VA PRIMERO QUE EL OTRO

# Apezone.difference(Warpex) != Warpex.difference(Apezone)
