//#include "/home/odin/Projekt2/p2_mwe/include/Spieler.hpp"
#include "../include/Spieler.hpp"
#include <iostream>
#include <functional>
#include <string>

namespace SchiffeVersenken{

    Spieler::Spieler(std::string Name){
        name=Name;
        id=std::hash<std::string>()(Name);
        in_game=-1;
    }

    int Spieler::get_id(){
        return id;
    }

    void Spieler::set_in_game(int id){
        in_game=id;
    }

    int Spieler::get_in_game(){
        return in_game;
    }


    void Spieler::set_gid(int id)
    {
        gid = id;
    }

    int Spieler::get_gid()
    {
        return gid;
    }
}