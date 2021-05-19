#include <bullet.h>

namespace godot
{
    Bullet::Bullet() 
    {
    }

    Bullet::~Bullet() 
    {
    }

    void Bullet::_register_methods()
    {
        // Register methods
        register_method((char*)"_ready", &Bullet::_ready);
        register_method((char*)"_process", &Bullet::_process);
        
        // Register properties
        // register_property((char*)"category/float_var", &Bullet::float_var, 0.0f);
    }

    void Bullet::_ready() 
    {

    }

    void Bullet::_process() 
    {

    }
}

