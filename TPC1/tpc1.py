import json

# Abrir o ficheiro JSON
with open("emd.json", encoding="utf-8") as f:
    try:
        bd = json.load(f)
    except json.JSONDecodeError as e:
        print(f"Erro ao decodificar JSON: {e}")
        raise

# Cabeçalho TTL
ttl = """@prefix : <http://www.semanticweb.org/uminho/mirtilo/rpcw/2025/tpc1#> .
@prefix owl: <http://www.w3.org/2002/07/owl#> .
@prefix rdf: <http://www.w3.org/1999/02/22-rdf-syntax-ns#> .
@prefix xml: <http://www.w3.org/XML/1998/namespace> .
@prefix xsd: <http://www.w3.org/2001/XMLSchema#> .
@prefix rdfs: <http://www.w3.org/2000/01/rdf-schema#> .
@base <http://www.semanticweb.org/uminho/mirtilo/rpcw/2025/tpc1> .

<http://www.semanticweb.org/uminho/mirtilo/rpcw/2025/tpc1> rdf:type owl:Ontology .

#################################################################
#    Classes
#################################################################

###  http://www.semanticweb.org/uminho/mirtilo/rpcw/2025/tpc1#Atleta
:Atleta rdf:type owl:Class .

###  http://www.semanticweb.org/uminho/mirtilo/rpcw/2025/tpc1#Exame
:Exame rdf:type owl:Class .

#################################################################
#    Object Properties
#################################################################

###  http://www.semanticweb.org/uminho/mirtilo/rpcw/2025/tpc1#temExame
:temExame rdf:type owl:ObjectProperty ;
        rdfs:domain :Atleta ;
        rdfs:range :Exame .

#################################################################
#    Data Properties
#################################################################

:temId rdf:type owl:DatatypeProperty ;
      rdfs:domain :Atleta ;
      rdfs:range xsd:string .

:temIndex rdf:type owl:DatatypeProperty ;
          rdfs:domain :Atleta ;
          rdfs:range xsd:int .

:temData rdf:type owl:DatatypeProperty ;
         rdfs:domain :Atleta ;
         rdfs:range xsd:dateTime .

:temApelido rdf:type owl:DatatypeProperty ;
            rdfs:domain :Atleta ;
            rdfs:range xsd:string .

:temPrimeiroNome rdf:type owl:DatatypeProperty ;
                 rdfs:domain :Atleta ;
                 rdfs:range xsd:string .

:temNome rdf:type owl:DatatypeProperty ;
         rdfs:domain :Atleta ;
         rdfs:range xsd:string .


#################################################################
#    Individuals
#################################################################
"""

# Criar os indivíduos para cada atleta
for atleta in bd:
    atleta_id = f"a_{atleta['_id']}"
    exame_id = f"e_{atleta['_id']}"

    registo = f"""
###  {atleta_id}
:{atleta_id} rdf:type owl:NamedIndividual ,
             :Atleta ;
             :temId "{atleta['_id']}";
             :temIndex "{atleta['index']}";
             :temData "{atleta['dataEMD']}";
             :temApelido "{atleta['nome']['último']}" ;
             :temPrimeiroNome "{atleta['nome']['primeiro']}" ;
             :temNome "{atleta['nome']['primeiro']} {atleta['nome']['último']}";
             :temExame :{exame_id} .

###  {exame_id}
:{exame_id} rdf:type owl:NamedIndividual ,
            :Exame ;
            :temData "{atleta['dataEMD']}" .
"""
    ttl += registo

# Guardar o conteúdo TTL num ficheiro
with open("atletas.ttl", "w", encoding="utf-8") as output_file:
    output_file.write(ttl)

print("Conteúdo guardado.")
