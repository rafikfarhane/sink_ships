#pragma once
#include <string>
#include <iostream>
#include <vector>

using namespace std;

namespace SchiffeVersenken
{

    class SpielBrett
    {

    public:
        SpielBrett(); // Konstruktor
        std::string Feld[10][10];

        void druckeSpielbrett();
        void set_value(int x, int y, string s);
        void setzeSchiff(std::tuple<int,int> tupel);
        void set_hit(std::tuple<int,int> tupel);
        void set_miss(std::tuple<int,int> tupel);
    };
}