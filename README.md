SPUIS 
=======================================
### *Toepassing* <br/>
Het programma SPUIS berekent waterstanden en profiel-gemiddelde stroomsnelheden in spuisluizen of andere constructies met vrije waterspiegel. Het bovenstroomse deel, bijvoorbeeld een toeleidingskanaal met vernauwing naar de sluis, en het benedenstroomse deel, bijvoorbeeld een diffusor, worden meegenomen in de berekening. Er kunnen ook berekeningen worden gemaakt voor leidingen, kokers, e.d. zonder vrije waterspiegel. In de watergang mogen zich regelconstructies bevinden (bijvoorbeeld over- of onderstroomde schuiven, overlaten, deuren en kleppen). De gebruiker dient wel zelf de stroomvoerende doorsnede aan te geven (eerst stroombeelden schetsen!). Steeds wordt uitgegaan van stationaire stroming. Het water kan stromen of schieten. In situaties met een vrije waterspiegel kunnen overgangen van stromend water naar schietend water (op de overgang bevindt zich de kritische, afvoerbepalende doorsnede) en van schietend water naar stromend water (overgang door middel van een watersprong, al dan niet verdronken) worden doorgerekend. 

De watergang wordt door middel van een aantal achter elkaar gelegen raaien opgedeeld in takken. Tussen de raaien worden verhanglijnen berekend met behulp van de stepmethode of back-water curves in geval van een vrije waterspiegel. De ruwheid van bodem en wanden is hierbij de maatgevende variabele. Veranderingen in het watervoerende profiel worden doorgerekend met Bernoulli-, impuls- en continuiteits-vergelijkingen. Splitsing van een tak in meerdere parallelle takken, zoals dit zich voordoet bij spuisluizen met meerdere naast elkaar gelegen kokers, is niet mogelijk.

Stromend-water situaties worden in stroomopwaartse richting doorgerekend (back-water curves); schietend-water situaties worden in stroomafwaartse richting doorgerekend. In situaties met vrije waterspiegel, waarbij zowel stromend als schietend water aanwezig is, wordt de rekenrichting aangepast aan de stromingstoestand en deze kan daarom tijdens de berekening omkeren. In feite wordt er dan overgegaan van SPUIS4 naar SPUIS4a of omgekeerd. In versie 4.01 van SPUIS (maart 1995) is een automatische switch aanwezig. In dit programma wordt ervan uitgegaan dat de stroming sub-kritisch is. De berekening vindt daarom in eerste instantie in stroomopwaartse richting plaats. Zodra tijdens de berekening een kritische doorsnede wordt gevonden, wordt de rekenrichting omgekeerd en wordt het super-kritische watertraject doorgerekend tot de overgang naar sub-kritische stroming (de watersprong) wordt gevonden.

### *Achtergrond* <br/>
De achtergronden, formules en opzet van de programma’s worden volledig gegeven in [1] en [2]. Het programma is getest voor een beperkt aantal sluizen; deze tests betroffen een vergelijking met enkele beschikbare modelmetingen en een beoordeling van het effect van variaties in diverse parameters. De testresultaten zijn niet gerapporteerd! In rapport Q1952 [3] wordt advies gegeven voor het aflaatwerk en gemaal te Oosterhout. Hierbij wordt gebruik gemaakt van het programma SPUIS. 

<pre>
[1]   Waterloopkundig Laboratorium, E.A. van Kleef. ‘Berekening van de afvoer van spuisluizen met behulp van een rekenmodel.’ Rapport R2125/Q331, november 1986.
[2]   Waterloopkundig Laboratorium, E.A. van Kleef. ‘Berekening van de afvoer van spuisluizen bij schietend water situaties.’ Rapport Q331-II, juli 1989.
[3]   Waterloopkundig Laboratorium, A. Vrijburcht. ‘Aflaatwerk en gemaal te Oosterhout.’ Rapport Q1952, maart 1995
</pre>

### *Installeren requirements Python packages* <br/>
Om de juiste packages te hebben voor Python om de som te draaien, vul de volgende commando in in de command window:
<pre>
pip install -r ./docs/requirements.txt
</pre>

### *Uitvoeren simulatie* <br/>
De simulatie kan uitgevoerd worden door 'runSpuis.py' (./SPUIS) uit te voeren. Dit is een Python code die de postprocessing bevat. Hier in kan de postprocessing eventueel verandert worden. De python file voert de executable uit en gebruikt de resultaten om figuren te maken. Deze figuren worden opgeslagen in de folder waar de input file is gemaakt. De input file eindigt op ".in". Voorbeelden zijn opgeslagen in folder "Tests". De code kan het best lokaal opgeslagen worden (en niet op een server) om sneller resultaten te krijgen.

### *Nieuwe executable maken* <br/>
Wanneer er ontwikkelt wordt aan de code (./SPUIS/SPUIS401/) veranderd is moet er een nieuwe executable gemaakt worden.
Hiervoor kan EXE.py gebruikt worden. Hierbij is het van belang om aan te geven in EXE.py wat de veranderingen zijn en wat de nieuwe versienummer wordt. Benodigde package is pyInstaller

<pre>
pip3 install pyInstaller
</pre>

Na het uitvoeren van EXE.py wordt er in de folder 'dist' de onafhankelijke executable gemaakt. Deze wordt gekopieerd naast de SPUIS401.py file.

### *Documentatie* <br/>
Documentatie van de code is te vinden "./docs" en is gemaakt met behulp van 'readthedocs' en 'sphinx'.