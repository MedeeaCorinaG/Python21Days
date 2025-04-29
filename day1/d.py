a = input("Care e numele tau? ")
b = input("Din ce oraș ești? ")
c = int(input("Câți ani ai? "))

# Calculăm vârsta peste 10 ani
c_peste_10_ani = c + 10

# Afișăm mesajul complet
print("Salut, " + a + "! Locuiești în " + b + " și ai " + str(c) + " ani. Peste 10 ani vei avea " + str(c_peste_10_ani) + " ani!")
