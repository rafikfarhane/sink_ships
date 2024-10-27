#include "../include/Schiffe.hpp"
#include "../include/Spielbrett.hpp"
#include <iostream>
#include <vector>
#include <algorithm>
#include <tuple>

using namespace std;
namespace SchiffeVersenken
{
    Schiffe::Schiffe() {}

    void Schiffe::koordinaten_einfügen(int a, int x, int y, string direction)
    {
        if (direction == "h")
        {
            for (int i = 0; i < a; i++)
            {
                std::tuple<int, int> schiff(x + i, y);
                Koordinaten.push_back(schiff);
            }
        }

        else if (direction == "v")
        {
            for (int i = 0; i < a; i++)
            {
                std::tuple<int, int> schiff(x, y + i);
                Koordinaten.push_back(schiff);
            }
        }
    }

    std::tuple<int,int> Schiffe::get_tupel(int index)
    {
        return Koordinaten[index];
    }

    int Schiffe::get_size()
    {
        return Koordinaten.size();
    }

    std::vector<std::tuple<int,int>> Schiffe::get_koordinaten()
    {
        return Koordinaten;
    }

    void Schiffe::koordinaten_löschen()
    {
        Koordinaten.clear();
    }
}