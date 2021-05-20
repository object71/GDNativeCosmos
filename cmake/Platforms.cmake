if(EMSCRIPTEN)

endif()

if (${CMAKE_SYSTEM_NAME} STREQUAL "Linux" OR !MSVC)
    add_global_compile_flag("-m${ARCHITECTURE}")
endif ()

if(EMSCRIPTEN)
    add_global_compile_flag("-s ASSERTIONS=1")
    add_global_compile_flag("-s SIDE_MODULE=1")
endif()

set(POSITION_INDEPENDENT_CODE ON)