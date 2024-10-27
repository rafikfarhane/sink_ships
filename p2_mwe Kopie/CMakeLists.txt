## Konfiguration des Buildsystems CMake ##

# Minimale Version des Buildsystems
cmake_minimum_required(VERSION 3.14)
# Name des Projekts
project(SchiffeVersenken)

## Optionen ##

# Setzte verwendeten C++-Standard auf C++17
set(CMAKE_CXX_STANDARD 17)


# Füge selbsgeschriebene Includes hinzu
include_directories(include)
# Füge externe Includes hinzu
include_directories(external)


find_package(pybind11 REQUIRED)

## Baue Programme ##

set(SRC_FILES 
    src/Schiffe.cpp
    src/Spiel.cpp
    src/Lobby.cpp
    src/Spieler.cpp
    src/Spielbrett.cpp
)

pybind11_add_module(schiffeversenken
  examples/versenken_pybind.cpp
  ${SRC_FILES}
)

## Installiere die Bibliothek
install(TARGETS schiffeversenken
  COMPONENT python
  LIBRARY DESTINATION ${PROJECT_SOURCE_DIR}/extra)
