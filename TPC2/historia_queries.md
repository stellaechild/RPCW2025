# Queries com SPARQL - GraphDB"

A ontologia utilizada como foco de estudo contém todos os detalhes sobre a História de Portugal."

## Alínea A - Quantos triplos existem na Ontologia?

```(sparql)
PREFIX owl: <http://www.w3.org/2002/07/owl#>
prefix : <http://www.semanticweb.org/andre/ontologies/2015/6/historia#>
SELECT (COUNT(*) AS ?totalTriplos) WHERE { 
    ?s ?p ?o 
}
```

Output: 4587


## Alínea B - Que classes estão definidas?

```(sparql)
PREFIX owl: <http://www.w3.org/2002/07/owl#>
prefix : <http://www.semanticweb.org/andre/ontologies/2015/6/historia#>
select ?class where {
    ?class a owl:Class .
}
```

Output: 
:Rainha
:Monarca
_:node1

:Casa
:Individuo
:Regime
:Batalha
:Acontecimento
:Partido
:Dinastia
:Descobrimento
:Local
:Reinado
_:node12

:Conquista
:Mandato
:Rei
_:node16

:Presidente
_:node20