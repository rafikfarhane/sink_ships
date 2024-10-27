#pragma once
#include <iostream>
#include "Spieler.hpp"
#include "Spiel.hpp"
#include <vector>
#include <map>

namespace SchiffeVersenken{

    class Lobby{
        public:

            Lobby();

            Spiel spiel_erstellen();

            Spieler spieler_erstellen(std::string name);

            Spieler get_player1();

            int spiele_size();

            int queue_size();

            Spieler player_by_id(int id);

            Spiel game_by_id(int id);

            void add_array(int x, int y, int id);

            int array_by_id(int id);

                /**
             * @brief überprüft im die Koordinate getroffen wurde. Wenn true, dann wird die Koordinate aus dem Koordinaten Array entfernt
             * 
             * @param koordinate 
             * @return true 
             * @return false 
             */
            bool hit(int sid, int x, int y);

            void edit_game(int id, Spiel a);

            void erase_game(int game_id);
            
        private:

            void add_ids();

            std::vector<Spieler> queue;
            std::map<int, Spiel> games;
            std::vector<int> game_ids;
            int id_max;
            std::map<int, Spieler> playing;
            std::map<int, std::vector<std::tuple<int,int>>> arrays;
    };
}