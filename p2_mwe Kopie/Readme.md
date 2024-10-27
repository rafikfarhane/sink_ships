# Projekt Beta

## Projekt bauen
Um das Projekt zu bauen, soll einer der folgenden Befehlsketten im Projektverzeichnis ausgeführt werden.
In Linux Mint verwendet man
```
cmake -S . -B build && cmake --build build && cmake --install build
```
Auf den Rechnern der CIP Pools ist der Aufruf leider ein wenig länger
```
export PROJ_PATH=`pwd` && cmake -S $PROJ_PATH -B $PROJ_PATH/build && cmake --build $PROJ_PATH/build && cmake --install $PROJ_PATH/build
```
Falls das Projekt so nicht baut, liegen entweder Implementierungsfehler vor oder es fehlen externe Softwarepakete.
