import json

fc = open("conceitos.json")
con = json.load(fc)
fc.close()
fd = open("disciplinas.json")
dis = json.load(fd)
fd.close()
fm = open("mestres.json")
mes = json.load(fd)
fm.close()
fo = open("obras.json")
obr = json.load(fo)
fo.close()
fa= open("pg54042.json") #aprendizes
apre = json.load(fa)
fa.close()

ttl = ""

for c in con['conceitos']:
    conceitos_listados += f"{c['nome']}"

for d in dis['disciplinas']:
    disciplinas_listadas += f"{d['nome']}"

for m in mes['mestres']:
    mestres_listados += f"{m['nome']}"

for o in obr['obras']:
    obras_listadas += f"{o['nome']}"

aps_listadas = []
periodos_listados = []
tipos_listados = []

for mestre in mes['mestres']:
   # campos : nome aplicações períodoHistórico 
    # propriedades a inserir na ontologia; 
    idMestre = mestre['nome']
    registo = f"""
###  http://www.semanticweb.org/mirtilo/ontologies/2025/untitled-ontology-18#Mestre_{idMestre}
:Mestre_{idMestre} rdf:type owl:Class .
""" 
    # data properties
    registo += f"""                :nome "{idMestre}" ;
      """   
    for p in mestre['períodoHistórico']:
        registo += f"""                :ensinou "{p}" ;
      """
        # criar registo de aplicacao
        if p not in periodos_listados:
            registo = f"""
    ###  http://www.semanticweb.org/mirtilo/ontologies/2025/untitled-ontology-18#PeríodoHistorico_{p}
    :PeríodoHistorico_{p} rdf:type owl:Class .
    """
            #data properties
            registo += f"""                :nome "{p}" ;

        """
            # object properties
            registo += f"""                :teveMestres "{idMestre}" ;
        """
            periodos_listados.append(p)
        else:
            # object properties
            registo += f"""                :teveMestres "{idMestre}" ;
        """
    for d in mestre['disciplinas']:
        registo += f"""                :ensinada "{d}" ;
      """
        if d not in disciplinas_listadas:
            registo = f"""
###  http://www.semanticweb.org/mirtilo/ontologies/2025/untitled-ontology-18#Conceito_{d}
:Disciplina_{d} rdf:type owl:Class .
"""
            # data properties
            registo += f"""                :nome "{d}" ;
            """
            registo += f"""                :ensinadaPor "{idMestre}" ;"""



for conceito in con['conceitos']:
    # campos : nome aplicações períodoHistórico 
    # propriedades a inserir na ontologia; 
    idConceito = conceito['nome']
    registo = f"""
###  http://www.semanticweb.org/mirtilo/ontologies/2025/untitled-ontology-18#Conceito_{idConceito}
:Conceito_{idConceito} rdf:type owl:Class .
"""
    # data properties
    registo += f"""                :nome "{conceito['nome']}" ;
      """
    # object properties
    for c in conceito['conceitosRelacionados']:
        registo+=f"                :estaRelacionadoCom :{c} ;\n"
        if c not in conceitos_listados:
            # criar registo de conceito
            registo = f"""
###  http://www.semanticweb.org/mirtilo/ontologies/2025/untitled-ontology-18#Conceito_{c}
:Conceito_{c} rdf:type owl:Class .
"""
            # data properties
            registo += f"""                :nome "{c}" ;"""
            #object properties
            registo+=f"                :estaRelacionadoCom :{idConceito} ;\n"
            conceitos_listados.append(c)
    
    for a in conceito['aplicações']:
            
        #object properties com aplicacao
        registo += f"""                :temAplicacaoEm "{a}" ;
      """
        # criar registo de aplicacao
        if a not in aps_listadas:
            registo = f"""
    ###  http://www.semanticweb.org/mirtilo/ontologies/2025/untitled-ontology-18#Aplicação_{a}
    :Aplicação_{a} rdf:type owl:Class .
    """
            # data properties
            registo += f"""                :nome "{a}" ;

        """
            #object properties
            registo += f"""                :usaConceito "{idConceito}" ;
        """
            aps_listadas.append(a)


    for p in conceito['períodoHistórico']:
        registo += f"""                :descobriu "{p}" ;
      """
        # criar registo de periodo
        if p not in periodos_listados:
            registo = f"""
    ###  http://www.semanticweb.org/mirtilo/ontologies/2025/untitled-ontology-18#PeríodoHistorico_{p}
    :PeríodoHistorico_{p} rdf:type owl:Class .
    """
            #data properties
            registo += f"""                :nome "{p}" ;

        """
            # object properties
            registo += f"""                :surge em "{idConceito}" ;
        """
            periodos_listados.append(p)
        
for obras in obr['obras']:
    idObra= obr['nome']
    registo = f"""###  http://www.semanticweb.org/mirtilo/ontologies/2025/untitled-ontology-18#Obra_{idObra}
:Obra_{idObra} rdf:type owl:Class ."""
    registo += f"""                :nome "{p}" ;

        """
    for c in obr['conceitos']:
        registo+=f"                :explica :{c} ;\n"
        if c not in conceitos_listados:
            # criar registo de conceito
            registo = f"""
###  http://www.semanticweb.org/mirtilo/ontologies/2025/untitled-ontology-18#Conceito_{c}
:Conceito_{c} rdf:type owl:Class .
"""
            # data properties
            registo += f"""                :nome "{c}" ;
      """
            registo+=f"                :explicadoEm :{idObra} ;\n"
            conceitos_listados.append(c)
    for at in obr['autor']:
        registo+=f"                :escritoPor :{at} ;\n"
        if at not in mestres_listados:
            # criar registo de conceito
            registo = f"""
###  http://www.semanticweb.org/mirtilo/ontologies/2025/untitled-ontology-18#Mestre_{at}
:Conceito_{at} rdf:type owl:Class .
"""
            # data properties
            registo += f"""                :nome "{c}" ;
      """
            registo+=f"                :escreveu :{idObra} ;\n"
            conceitos_listados.append(c)
    


for disciplina in dis['disciplinas']: 
    idDisciplina= dis['nome']
    registo = f"""
###  http://www.semanticweb.org/mirtilo/ontologies/2025/untitled-ontology-18#Conceito_{idDisciplina}
:Disciplina_{idDisciplina} rdf:type owl:Class .
"""
    # data properties
    registo += f"""                :nome "{disciplina['nome']}" ;
      """
    # object properties
    for c in disciplina['conceitos']:
        registo+=f"                :aborda :{c} ;\n"
        if c not in conceitos_listados:
            # criar registo de conceito
            registo = f"""
###  http://www.semanticweb.org/mirtilo/ontologies/2025/untitled-ontology-18#Conceito_{c}
:Conceito_{c} rdf:type owl:Class .
"""
            # data properties
            registo += f"""                :nome "{c}" ;
      """
            registo+=f"                :eEstudadoEm :{idDisciplina} ;\n"
    
    for t in disciplina['tiposDeConhecimento']:
        registo+=f"                :pertenceA :{t} ;\n"
        if t not in tipos_listados:
            # criar registo de conceito
            registo = f"""
###  http://www.semanticweb.org/mirtilo/ontologies/2025/untitled-ontology-18#TiposDeConhecimento_{t}
:TiposDeConhecimento_{t} rdf:type owl:Class .
"""
            # data properties
            registo += f"""                :nome "{t}" ;
      """
            registo+=f"                :pertencenteA :{idDisciplina} ;\n"
       
for aprendiz in apre:
    idAprendiz = aprendiz['nome']
    registo = f"""
    ###  http://www.semanticweb.org/mirtilo/ontologies/2025/untitled-ontology-18#TiposDeConhecimento_{idAprendiz}
:Aprendiz_{idAprendiz} rdf:type owl:Class .
"""
    registo += f"""                :nome "{idAprendiz}" ;
                                   :idade "{aprendiz["idade"]}";
      """
    for d in aprendiz['disciplinas']:
        registo += f"""                :aprende "{d}" ;
      """
        if d not in disciplinas_listadas:

            registo = f"""
        ###  http://www.semanticweb.org/mirtilo/ontologies/2025/untitled-ontology-18#Conceito_{idDisciplina}
        :Disciplina_{d} rdf:type owl:Class .
        """
            # data properties
            registo += f"""                :nome "{d}" ; 
                                           :aprendidaPor"{idAprendiz}"""
            disciplinas_listadas.append(d)
        

f = open("sapienta_base.ttl", "r")
f2 = open("sapienta_ind.ttl", "w")
f2.write(f.read())
f.close()
f2.write(ttl)
f2.close()