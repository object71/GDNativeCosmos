#include <Godot.hpp>
#include <gen/library.gen.h>

using namespace godot;

extern "C" void GDN_EXPORT cosmos_gdnative_init(godot_gdnative_init_options* o)
{
    Godot::gdnative_init(o);
}

extern "C" void GDN_EXPORT cosmos_gdnative_terminate(godot_gdnative_terminate_options* o)
{
    Godot::gdnative_terminate(o);
}

extern "C" void GDN_EXPORT cosmos_nativescript_init(void* handle)
{
    Godot::nativescript_init(handle);
    COSMOS_CLASS_REGISTRATION
}