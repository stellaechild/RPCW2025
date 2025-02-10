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

###  http://www.semanticweb.org/uminho/mirtilo/rpcw/2025/tpc1#Clube
:Clube rdf:type owl:Class .

#################################################################
#    Object Properties
#################################################################

###  http://www.semanticweb.org/uminho/mirtilo/rpcw/2025/tpc1#temExame
:temExame rdf:type owl:ObjectProperty ;
        rdfs:domain :Atleta ;
        rdfs:range :Exame .

###  http://www.semanticweb.org/uminho/mirtilo/rpcw/2025/tpc1#pertenceAClube
:pertenceAClube rdf:type owl:ObjectProperty ;
        rdfs:domain :Atleta ;
        rdfs:range :Clube .

#################################################################
#    Data Properties
#################################################################

:temId rdf:type owl:DatatypeProperty ;
      rdfs:domain :Atleta ;
      rdfs:range xsd:string .

:temIndex rdf:type owl:DatatypeProperty ;
          rdfs:domain :Atleta ;
          rdfs:range xsd:int .

:temDataEMD rdf:type owl:DatatypeProperty ;
         rdfs:domain :Exame ;
         rdfs:range xsd:date .

:temPrimeiroNome rdf:type owl:DatatypeProperty ;
                 rdfs:domain :Atleta ;
                 rdfs:range xsd:string .

:temApelido rdf:type owl:DatatypeProperty ;
            rdfs:domain :Atleta ;
            rdfs:range xsd:string .

:temNome rdf:type owl:DatatypeProperty ;
         rdfs:domain :Atleta ;
         rdfs:range xsd:string .

:temIdade rdf:type owl:DatatypeProperty ;
         rdfs:domain :Atleta ;
         rdfs:range xsd:int .

:temGenero rdf:type owl:DatatypeProperty ;
         rdfs:domain :Atleta ;
         rdfs:range xsd:string .

:temMorada rdf:type owl:DatatypeProperty ;
         rdfs:domain :Atleta ;
         rdfs:range xsd:string .

:temModalidade rdf:type owl:DatatypeProperty ;
         rdfs:domain :Atleta ;
         rdfs:range xsd:string .

:temClube rdf:type owl:DatatypeProperty ;
         rdfs:domain :Clube ;
         rdfs:range xsd:string .

:temEmail rdf:type owl:DatatypeProperty ;
         rdfs:domain :Atleta ;
         rdfs:range xsd:string .

:eFederado rdf:type owl:DatatypeProperty ;
         rdfs:domain :Atleta ;
         rdfs:range xsd:boolean .

:temResultado rdf:type owl:DatatypeProperty ;
         rdfs:domain :Exame ;
         rdfs:range xsd:boolean .

#################################################################
#    Individuals
#################################################################
"""

# Criar os indivíduos para cada atleta
for atleta in bd:
    atleta_id = f"a_{atleta['_id']}"
    exame_id = f"e_{atleta['_id']}"
    clube_id = f"c_{atleta['clube'].replace(' ', '_')}"

    registo = f"""
###  {atleta_id}
:{atleta_id} rdf:type owl:NamedIndividual ,
             :Atleta ;
             :temId "{atleta['_id']}" ;
             :temIndex {atleta['index']} ;
             :temPrimeiroNome "{atleta['nome']['primeiro']}" ;
             :temApelido "{atleta['nome']['último']}" ;
             :temNome "{atleta['nome']['primeiro']} {atleta['nome']['último']}" ;
             :temIdade {atleta['idade']} ;
             :temGenero "{atleta['género']}" ;
             :temMorada "{atleta['morada']}" ;
             :temModalidade "{atleta['modalidade']}" ;
             :temEmail "{atleta['email']}" ;
             :eFederado "{str(atleta['federado']).lower()}" ;
             :temExame :{exame_id} ;
             :pertenceAClube :{clube_id} .

###  {exame_id}
:{exame_id} rdf:type owl:NamedIndividual ,
            :Exame ;
            :temDataEMD "{atleta['dataEMD']}" ;
            :temResultado "{str(atleta['resultado']).lower()}" .

###  {clube_id}
:{clube_id} rdf:type owl:NamedIndividual ,
            :Clube ;
            :temClube "{atleta['clube']}" .
"""
    ttl += registo

# Gerar o ficheiro TTL
with open("atletas.ttl", "w", encoding="utf-8") as output_file:
    output_file.write(ttl)

print("Conteúdo guardado.")
