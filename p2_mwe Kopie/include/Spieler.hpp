#pragma once
#include <iostream>
#include "../include/Spielbrett.hpp"
#include "../include/Schiffe.hpp"
#include <string>
#include <memory>

namespace SchiffeVersenken{

    class Spieler{
    public:
        /**
         * @brief Construct a new Spieler object
         * 
         * @param Name - Name des Spielers
         */
        Spieler(std::string Name);

        int get_id();

        void set_in_game(int id);

        int get_in_game();

        void set_gid(int id);

        int get_gid();

    private:

        /**
         * @brief Name des Spielers
         * 
         */
        std::string name;

        /**
         * @brief id zur Identifikation des Spielers
         * 
         */
        size_t id;

        int in_game;

        int gid;
    };
}