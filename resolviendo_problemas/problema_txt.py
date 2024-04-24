#creando lista, una con nombres otra con apellidos

nombres = ["Lucas", "mate", "camila", "Kiko", "Roberto"]
apellidos = ["Dalto", "Arse", "Dalto", "Maste", "Tarado"]

#registrar esta informacion en un txt de forma optima

with open("resolviendo_problemas\\nombres_y_apellidos.txt","w") as arch:
    arch.writelines("Los datos son:\n")
    [arch.writelines(f"Nombre: {n}\nApellido: {a} \n-----------------\n") for n, a in zip(nombres,apellidos)]
    
