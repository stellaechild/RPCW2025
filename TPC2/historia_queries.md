# Queries com SPARQL - GraphDB"

A ontologia utilizada como foco de estudo contém todos os detalhes sobre a História de Portugal."

## Alínea A - Quantos triplos existem na Ontologia?

```(sparql)
prefix owl: <http://www.w3.org/2002/07/owl#>
prefix : <http://www.semanticweb.org/andre/ontologies/2015/6/historia#>
SELECT (COUNT(*) AS ?totalTriplos) WHERE { 
    ?s ?p ?o 
}
```

### Output

```(txt)
4587 
```


## Alínea B - Que classes estão definidas?

```(sparql)
prefix owl: <http://www.w3.org/2002/07/owl#>
prefix : <http://www.semanticweb.org/andre/ontologies/2015/6/historia#>
select ?class where {
    ?class a owl:Class .
}
```

### Output

```(txt)
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
```

## Alínea C - Que propriedades tem a classe "Rei"?

```(sparql)
prefix : <http://www.semanticweb.org/andre/ontologies/2015/6/historia#>
SELECT DISTINCT ?p WHERE { 
    ?s ?p ?o .
    ?s a :Rei .
}
```

### Output

```(txt)
rdf:type
:sexo
:casa
:enterro
:nascimento
:morte
:localNascimento
:nome
:temReinado
owl:topObjectProperty
:predecessor
:sucessor
:descendente
:notas
:cognomes
:posicao
:ascendente
```

## Alínea D - Quantos reis aparecem na ontologia?

```(sparql)
prefix owl: <http://www.w3.org/2002/07/owl#>
prefix : <http://www.semanticweb.org/andre/ontologies/2015/6/historia#>
SELECT DISTINCT (COUNT(?rei) AS ?totalReis) WHERE { 
    ?rei a :Rei .
}
```

### Output

```(txt)
32
```

## Alínea E - Calcula uma tabela com o seu nome, data de nascimento e cognome.

```(sparql)
prefix owl: <http://www.w3.org/2002/07/owl#>
prefix : <http://www.semanticweb.org/andre/ontologies/2015/6/historia#>

SELECT ?rei ?nome ?dataNascimento ?cognomes WHERE { 
    ?rei a :Rei .
    ?rei :nome ?nome . 
    ?rei :nascimento ?dataNascimento . 
    ?rei :cognomes ?cognomes .
}
```

### Output

| Rei      | Nome                          | Data de Nascimento      | Cognomes                                                                 |
|----------|-------------------------------|-------------------------|--------------------------------------------------------------------------|
| :rei14   | D. Manuel I                    | 31 de maio de 1469      | O Venturoso, O Bem-Aventurado, O Pomposo                                |
| :rei10   | D. João I                      | 11 de abril de 1357     | O da Boa Memória                                                         |
| :rei8    | D. Pedro I                     | 8 de abril de 1320      | O Justiceiro, O Cruel, O Cru, O Vingativo, O Tartamudo, O Até-ao-Fim-do-Mundo-Apaixonado |
| :rei7    | D. Afonso IV                   | 8 de fevereiro de 1291  | O Bravo                                                                  |
| :rei6    | D. Dinis I                     | 9 de outubro de 1261    | O Lavrador, O Rei-Trovador, O Rei-Poeta, O Rei-Agricultor               |
| :rei5    | D. Afonso III                  | 5 de maio de 1210       | O Bolonhês                                                               |
| :rei3    | D. Afonso II                   | 23 de abril de 1185     | O Gordo, O Crasso, O Gafo, O Legislador                                  |
| :rei2    | D. Sancho I                    | 11 de novembro de 1154  | O Povoador                                                              |
| :rei1    | D. Afonso I                    | 1109                    | O Conquistador, O Fundador, O Grande                                     |
| :rei4    | D. Sancho II                   | 8 de setembro de 1209   | O Capelo, O Piedoso, O Pio                                               |
| :rei9    | D. Fernando I                  | 31 de outubro de 1345   | O Formoso, O Belo, O Inconstante, O Inconsciente                         |
| :rei11   | D. Duarte I                    | 31 de outubro de 1391   | O Eloquente, O Rei-Filósofo                                              |
| :rei12   | D. Afonso V                    | 15 de janeiro de 1432   | O Africano                                                               |
| :rei13   | D. João II                     | 3 de março de 1455      | O Príncipe Perfeito, O Tirano                                           |
| :rei15   | D. João III                    | 7 de junho de 1502      | O Piedoso, O Pio                                                         |
| :rei16   | D. Sebastião I                 | 20 de janeiro de 1554   | O Desejado, O Encoberto, O Adormecido                                    |
| :rei17   | D. Henrique I                  | 31 de janeiro de 1512   | O Casto, O Cardeal-Rei, O Eborense/O de Évora                           |
| :rei18   | Filipe I                        | 21 de maio de 1527      | O Prudente                                                               |
| :rei19   | Filipe II                       | 14 de abril de 1578     | O Pio, O Piedoso                                                         |
| :rei20   | Filipe III                      | 8 de abril de 1605      | O Grande                                                                 |
| :rei21   | D. João IV                      | 19 de março de 1604     | O Restaurador, O Afortunado                                              |
| :rei22   | D. Afonso VI                    | 21 de agosto de 1643    | O Vitorioso, O Prisioneiro                                               |
| :rei23   | D. Pedro II                     | 26 de abril de 1648     | O Pacífico                                                               |
| :rei24   | D. João V                       | 22 de outubro de 1689   | O Magnânimo, O Magnífico, O Rei-Sol Português, O Freirático              |
| :rei25   | D. José I                       | 6 de junho de 1714      | O Reformador                                                             |
| :rei27   | D. João VI                      | 13 de maio de 1767      | O Clemente                                                               |
| :rei28   | D. Pedro IV                     | 12 de outubro de 1798   | O Rei-Soldado, O Rei-Imperador, O Libertador                             |
| :rei31   | D. Pedro V                      | 16 de setembro de 1837  | O Esperançoso, O Bem-Amado, O Muito Amado                                |
| :rei30   | D. Miguel I                     | 26 de outubro de 1802   | O Rei Absoluto, O Absolutista, O Tradicionalista, O Usurpador            |
| :rei32   | D. Luís I                       | 31 de outubro de 1838   | O Popular, O Bom, O Rei-Marinheiro                                       |
| :rei33   | D. Carlos I                     | 28 de setembro de 1863  | O Diplomata, O Martirizado, O Mártir, O Oceanógrafo, O Rei-Pintor       |
| :rei34   | D. Manuel II                    | 15 de novembro de 1889  | O Patriota, O Desventurado, O Estudioso, O Bibliófilo, O Rei-Saudade    |


### Alínea F - Acrescenta à tabela anterior a dinastia em que cada rei reinou.

```(sparql)
prefix owl: <http://www.w3.org/2002/07/owl#>
prefix : <http://www.semanticweb.org/andre/ontologies/2015/6/historia#>

SELECT ?rei ?nome ?dataNascimento ?cognomes ?dinastia ?name WHERE { 
    ?rei a :Rei .
    ?rei :nome ?nome . 
    ?rei :nascimento ?dataNascimento . 
    ?rei :cognomes ?cognomes .
    ?rei :temReinado ?reinado .  
    ?reinado :dinastia ?dinastia .
    ?dinastia :nome ?name
}
```

### Ouput 

| Rei        | Nome                        | Data de Nascimento    | Cognomes                                                       | Dinastia                                |
|------------|-----------------------------|-----------------------|----------------------------------------------------------------|-----------------------------------------|
| :rei14     | D. Manuel I                  | 31 de maio de 1469    | O Venturoso, O Bem-Aventurado, O Pomposo                      | :dinastia2 - Dinastia de Avis / Dinastia Joanina    |
| :rei10     | D. João I                    | 11 de abril de 1357   | O da Boa Memória                                               | :dinastia2 - Dinastia de Avis / Dinastia Joanina    |
| :rei8      | D. Pedro I                   | 8 de abril de 1320    | O Justiceiro, O Cruel, O Cru, O Vingativo, O Tartamudo, O Até-ao-Fim-do-Mundo-Apaixonado | :dinastia1 - Dinastia de Borgonha / Dinastia Afonsina |
| :rei7      | D. Afonso IV                 | 8 de fevereiro de 1291| O Bravo                                                        | :dinastia1 - Dinastia de Borgonha / Dinastia Afonsina |
| :rei6      | D. Dinis I                   | 9 de outubro de 1261  | O Lavrador, O Rei-Trovador, O Rei-Poeta, O Rei-Agricultor     | :dinastia1 - Dinastia de Borgonha / Dinastia Afonsina |
| :rei5      | D. Afonso III                | 5 de maio de 1210     | O Bolonhês                                                     | :dinastia1 - Dinastia de Borgonha / Dinastia Afonsina |
| :rei3      | D. Afonso II                 | 23 de abril de 1185   | O Gordo, O Crasso, O Gafo, O Legislador                        | :dinastia1 - Dinastia de Borgonha / Dinastia Afonsina |
| :rei2      | D. Sancho I                  | 11 de novembro de 1154| O Povoador                                                     | :dinastia1 - Dinastia de Borgonha / Dinastia Afonsina |
| :rei1      | D. Afonso I                  | 1109                  | O Conquistador, O Fundador, O Grande                           | :dinastia1 - Dinastia de Borgonha / Dinastia Afonsina |
| :rei4      | D. Sancho II                 | 8 de setembro de 1209 | O Capelo, O Piedoso, O Pio                                     | :dinastia1 - Dinastia de Borgonha / Dinastia Afonsina |
| :rei9      | D. Fernando I                | 31 de outubro de 1345 | O Formoso, O Belo, O Inconstante, O Inconsciente               | :dinastia1 - Dinastia de Borgonha / Dinastia Afonsina |
| :rei11     | D. Duarte I                   | 31 de outubro de 1391 | O Eloquente, O Rei-Filósofo                                    | :dinastia2 - Dinastia de Avis / Dinastia Joanina    |
| :rei12     | D. Afonso V                   | 15 de janeiro de 1432 | O Africano                                                     | :dinastia2 - Dinastia de Avis / Dinastia Joanina    |
| :rei13     | D. João II                   | 3 de março de 1455    | O Príncipe Perfeito, O Tirano                                  | :dinastia2 - Dinastia de Avis / Dinastia Joanina    |
| :rei15     | D. João III                  | 7 de junho de 1502    | O Piedoso, O Pio                                               | :dinastia2 - Dinastia de Avis / Dinastia Joanina    |
| :rei16     | D. Sebastião I               | 20 de janeiro de 1554 | O Desejado, O Encoberto, O Adormecido                         | :dinastia2 - Dinastia de Avis / Dinastia Joanina    |
| :rei17     | D. Henrique I                | 31 de janeiro de 1512 | O Casto, O Cardeal-Rei, O Eborense/O de Évora                 | :dinastia2 - Dinastia de Avis / Dinastia Joanina    |
| :rei18     | Filipe I                      | 21 de maio de 1527    | O Prudente                                                     | :dinastia3 - Dinastia Filipina                      |
| :rei19     | Filipe II                     | 14 de abril de 1578   | O Pio, O Piedoso                                               | :dinastia3 - Dinastia Filipina                      |
| :rei20     | Filipe III                    | 8 de abril de 1605    | O Grande                                                       | :dinastia3 - Dinastia Filipina                      |
| :rei21     | D. João IV                    | 19 de março de 1604   | O Restaurador, O Afortunado                                    | :dinastia4 - Dinastia de Bragança / Dinastia Brigantina |
| :rei22     | D. Afonso VI                  | 21 de agosto de 1643  | O Vitorioso, O Prisioneiro                                     | :dinastia4 - Dinastia de Bragança / Dinastia Brigantina |
| :rei23     | D. Pedro II                   | 26 de abril de 1648   | O Pacífico                                                     | :dinastia4 - Dinastia de Bragança / Dinastia Brigantina |
| :rei24     | D. João V                     | 22 de outubro de 1689 | O Magnânimo, O Magnífico, O Rei-Sol Português, O Freirático   | :dinastia4 - Dinastia de Bragança / Dinastia Brigantina |
| :rei25     | D. José I                     | 6 de junho de 1714    | O Reformador                                                   | :dinastia4 - Dinastia de Bragança / Dinastia Brigantina |
| :rei27     | D. João VI                    | 13 de maio de 1767    | O Clemente                                                     | :dinastia4 - Dinastia de Bragança / Dinastia Brigantina |
| :rei28     | D. Pedro IV                   | 12 de outubro de 1798 | O Rei-Soldado, O Rei-Imperador, O Libertador                   | :dinastia4 - Dinastia de Bragança / Dinastia Brigantina |
| :rei31     | D. Pedro V                    | 16 de setembro de 1837| O Esperançoso, O Bem-Amado, O Muito Amado                     | :dinastia4 - Dinastia de Bragança / Dinastia Brigantina |
| :rei30     | D. Miguel I                   | 26 de outubro de 1802 | O Rei Absoluto, O Absolutista, O Tradicionalista, O Usurpador | :dinastia4 - Dinastia de Bragança / Dinastia Brigantina |
| :rei32     | D. Luís I                     | 31 de outubro de 1838 | O Popular, O Bom, O Rei-Marinheiro                            | :dinastia4 - Dinastia de Bragança / Dinastia Brigantina |
| :rei33     | D. Carlos I                   | 28 de setembro de 1863| O Diplomata, O Martirizado, O Mártir, O Oceanógrafo, O Rei-Pintor | :dinastia4 - Dinastia de Bragança / Dinastia Brigantina |
| :rei34     | D. Manuel II                  | 15 de novembro de 1889| O Patriota, O Desventurado, O Estudioso, O Bibliófilo, O Rei-Saudade | :dinastia4 - Dinastia de Bragança / Dinastia Brigantina |


## Alínea 