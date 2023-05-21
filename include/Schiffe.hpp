#pragma once
#include <iostream>
#include <vector>

using namespace std;
namespace SchiffeVersenken
{
    class Schiffe
    {
    public:
        Schiffe();
        void schiffe_platzieren();
        void koordinaten_einfügen();

    private:
        vector<int> Schiffgrößen;
        vector<int> Koordinaten;
        vector<int> Schiffgrößen2;
    };
}