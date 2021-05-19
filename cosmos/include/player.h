#ifndef COSMOS_PLAYER_H
#define COSMOS_PLAYER_H

#include <gen/player.gen.h>
#include <Godot.hpp>
#include <KinematicBody2D.hpp>

namespace godot
{
    CLASS_PLAYER_START
    public:
        Player();
        virtual ~Player();

        static void _register_methods();

        void _ready();
        void _process();


    CLASS_PLAYER_END
}

#endif //COSMOS_PLAYER_H