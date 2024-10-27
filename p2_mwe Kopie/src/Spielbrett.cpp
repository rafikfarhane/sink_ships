#include <vector>
#include <tuple>
#include <string>
#include <iostream>
#include "../include/Spielbrett.hpp"
#include "../include/Schiffe.hpp"

using namespace std;

namespace SchiffeVersenken
{
    SpielBrett::SpielBrett()
    {
        for (int i = 0; i < 10; i++)
            for (int j = 0; j < 10; j++)
                Feld[i][j] = "-";
    }

    void SpielBrett::druckeSpielbrett()
    {
        cout << "  ";

        for (int i = 0; i < 10; i++)
            cout << i << " ";

        cout << endl;
        
        for (int i = 0; i < 10; i++)
        {
            cout << i << " ";
            for (int j = 0; j < 10; j++)
            {
                std::cout << Feld[i][j] << " ";
            }
            std::cout << std::endl;
        }
    }

    void SpielBrett::set_value(int x, int y, string s)
    {
        Feld[x][y] = s;
    }

    void SpielBrett::setzeSchiff(std::tuple<int,int> tupel)
    {
        int y = std::get<0>(tupel);
        int x = std::get<1>(tupel);
        set_value(x,y,"S");
    }

    void SpielBrett::set_hit(std::tuple<int,int> tupel)
    {
        int y = std::get<0>(tupel);
        int x = std::get<1>(tupel);
        set_value(x,y,"X");
    }

    void SpielBrett::set_miss(std::tuple<int,int> tupel)
    {
        int y = std::get<0>(tupel);
        int x = std::get<1>(tupel);
        set_value(x,y,"O");
    }
}