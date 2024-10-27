#pragma once
#include <iostream>
#include "../include/Spieler.hpp"


namespace SchiffeVersenken{

    class Spiel{
        public:
            Spiel(Spieler a, Spieler b, int id);

            int get_turn();

            int get_game_id();

            Spieler get_p1();

            Spieler get_p2();

            void set_turn();

            void set_over();

            bool get_over();

        private:
            Spieler spieler1;
            Spieler spieler2;
            int turn;
            int game_id;
            bool over;
    };
}