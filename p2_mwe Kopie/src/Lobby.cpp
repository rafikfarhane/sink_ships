#include <iostream>
#include "../include/Lobby.hpp"

namespace SchiffeVersenken{

    Lobby::Lobby(){
        for (int i=0; i<10; i++){
            game_ids.push_back(i);
            id_max=9;
        }
    };

    Spieler Lobby::spieler_erstellen(std::string name){
        Spieler x(name);
        queue.push_back(x);
        if(queue.size()>=2){
            spiel_erstellen();
        }
        return x;
    }

    Spiel Lobby::spiel_erstellen(){

        if (game_ids.size()==0){
            add_ids();
        }

        Spieler s1=queue[0];
        Spieler s2=queue[1];
        int id1=s1.get_id(), id2=s2.get_id();
        int new_g_id=game_ids[0];

        Spiel a(s1,s2, new_g_id);
        playing.insert(std::pair <int, Spieler>(id1, s1));
        playing.insert(std::pair <int, Spieler>(id2, s1));
        playing.at(id1).set_in_game(new_g_id);
        playing.at(id2).set_in_game(new_g_id);

        playing.at(id1).set_gid(id2);
        playing.at(id2).set_gid(id1);

        std::vector<std::tuple<int,int>> arr;
        arrays.insert(std::pair<int, std::vector<std::tuple<int,int>>>(id1, arr));
        arrays.insert(std::pair<int, std::vector<std::tuple<int,int>>>(id2, arr));

        game_ids.erase(game_ids.begin());
        queue.erase(queue.begin());
        queue.erase(queue.begin()+1); 

        games.insert(std::pair <int,Spiel>(a.get_game_id(), a));
        std::cout << "Spiel erstellt" << std::endl;
        return a;        
    }

    Spieler Lobby::get_player1(){
        if (queue.size()==0){
            throw std::out_of_range("Die Queue ist leer");
        }
        return queue[0];
    }

    int Lobby::spiele_size(){             
        return games.size();
    }

    int Lobby::queue_size(){
        return queue.size();
    }

    void Lobby::add_ids(){
        for (int i=id_max; i<id_max*2; i++){
            game_ids.push_back(i);
        }
        id_max*=2;
    }

    Spieler Lobby::player_by_id(int id){
        return playing.at(id);
    }

    Spiel Lobby::game_by_id(int id){
        return games.at(id);
    }


    void Lobby::add_array(int x, int y, int id){
        std::tuple<int, int> t(x,y);
        std::vector<std::tuple<int,int>> a=arrays[id];
        a.push_back(t);
        arrays[id]=a;
    }

    int Lobby::array_by_id(int id){
        return arrays.at(id).size();
    }

    bool Lobby::hit(int sid, int x, int y)
    {
        std::vector<std::tuple<int,int>> Koordinaten = arrays[sid];
        std::tuple<int, int> koordinate(x,y);
        for (int i = 0; i < Koordinaten.size(); i++)
        {
            if (Koordinaten[i] == koordinate)
            {
                Koordinaten.erase(Koordinaten.begin()+i);
                arrays[sid]=Koordinaten;
                return true;
            }
        }
        return false;
    }

    void Lobby::edit_game(int id, Spiel a){
        games.at(id)=a;
    }

    void Lobby::erase_game(int game_id){
        Spieler s1=games.at(game_id).get_p1();
        Spieler s2=games.at(game_id).get_p2();
        games.erase(game_id);
        playing.erase(s1.get_id());
        playing.erase(s2.get_id());
        arrays.erase(s1.get_id());
        arrays.erase(s2.get_id());
        game_ids.push_back(game_id);
    }
}