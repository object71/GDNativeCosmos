function(add_global_compile_flag flag)
    message(STATUS "Flag '${flag}' added for compilation")

    set(CMAKE_C_FLAGS "${CMAKE_C_FLAGS} ${flag}" PARENT_SCOPE)
    set(CMAKE_CXX_FLAGS "${CMAKE_CXX_FLAGS} ${flag}" PARENT_SCOPE)
    
    foreach(additional_flag IN LISTS ARGN)
        message(STATUS "Flag '${additional_flag}' added for compilation")
        set(CMAKE_C_FLAGS "${CMAKE_C_FLAGS} ${additional_flag}" PARENT_SCOPE)
        set(CMAKE_CXX_FLAGS "${CMAKE_CXX_FLAGS} ${additional_flag}" PARENT_SCOPE)
    endforeach()
endfunction()

function(add_enum_option opt_name default_value description)
    set(${opt_name} "${default_value}" CACHE STRING "${description}")
    set_property(CACHE ${opt_name} PROPERTY STRINGS ${ARGN})
endfunction()