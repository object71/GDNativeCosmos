#include <player.h>

namespace godot
{
    Player::Player() 
    {
    }

    Player::~Player() 
    {
    }

    void Player::_register_methods()
    {
        // Register methods
        register_method((char*)"_ready", &Player::_ready);
        register_method((char*)"_process", &Player::_process);
        
        // Register properties
        // register_property((char*)"category/float_var", &Player::float_var, 0.0f);
    }

    void Player::_ready() 
    {

    }

    void Player::_process() 
    {
        Vector2 current_position = get_global_position();
        float move_value = 100;
        current_position.x += move_value;
        current_position.y += move_value;
        set_global_position(current_position);
    }
}

