#ifndef COSMOS_BULLET_H
#define COSMOS_BULLET_H

#include <gen/bullet.gen.h>
#include <Godot.hpp>
#include <KinematicBody2D.hpp>

namespace godot
{
    CLASS_BULLET_START
    public:
        Bullet();
        virtual ~Bullet();

        static void _register_methods();

        void _ready();
        void _process();


    CLASS_BULLET_END
}

#endif //COSMOS_BULLET_H