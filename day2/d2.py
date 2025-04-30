# fructe=["mere","pere","nuci"]
# fructe.append("banane")
# fructe.remove("pere")
# print(fructe)
# print(fructe[0],fructe[2])
#
# profil={
#     "nume":"Medeea",
#     "oras": "Cluj",
#     "varsta":24
# }
# print(profil["oras"])

cumparaturi=["apa","ciocolata","suc"]
a=input("Ce produs vrei?")
cumparaturi.append(a)
b = input("Ce produs vrei să elimini?")


if b in cumparaturi:
    cumparaturi.remove(b)
else:
    print("nu exista")
print(cumparaturi)