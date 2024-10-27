// clang++ -std=c++17 -I/include examples/SchiffeTest.cpp -o schiffe
#include "../include/Schiffe.hpp"
#include "../src/Schiffe.cpp"
#include "../include/Spielbrett.hpp"
#include <iostream>

using namespace SchiffeVersenken;

int main() 
{ 
    Schiffe s;
    try
    {
    s.schiffe_platzieren();
    }
    catch (const std::invalid_argument e)
    {
        cout << "ERROR: '" << e.what() << "'" << endl;
    }
}