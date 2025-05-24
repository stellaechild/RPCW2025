import json 

f = open("./ex2/doentes.json")
doentes = json.load(f)
output = ""
sintomas = {}
patients = {}
tratamentos = {}

for i,e in enumerate(doentes):
    if e['nome'] not in patients:
            patients[e['nome']] = "P" + str(len(patients))
            output += f"""
    ###  http://mirtilo/rpcw.di.uminho.pt/2025/#{patients[e['nome']]}
    :{patients[e['nome']]} rdf:type owl:NamedIndividual ,
                :Patient ;
        :name "{e['nome']}"
            """
    idPatient = patients[e['nome']]

    for sintoma in e['sintomas']:
         if sintoma not in sintomas:
              sintomas[sintoma] = "S" + str(len(sintomas))
              output+= f"""
              ###  http://mirtilo/rpcw.di.uminho.pt/2025/#Symptom
    :{sintoma} rdf:type owl:NamedIndividual ,
             :{sintoma} a :Symptom .
              """
    
with open("./ex2/medical_populado.ttl", "w", encoding="utf-8") as output_file:
    output_file.write(output)



print("Conteúdo guardado.")