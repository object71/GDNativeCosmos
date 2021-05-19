cmake_minimum_required(VERSION 3.17)
project(Cosmos)

list(APPEND CMAKE_MODULE_PATH "${CMAKE_CURRENT_SOURCE_DIR}/cmake")
set(CMAKE_CXX_STANDARD 17)
set(CMAKE_CXX_STANDARD_REQUIRED ON)

include(Functions)
include(Definitions)
include(Platforms)

add_enum_option(ARCHITECTURE "64" "Architecture used for GDNative" "64" "32")
add_enum_option(PLATFORM "win" "Platform used for GDNative" "win" "wasm" "linux")

find_package(Python3 REQUIRED COMPONENTS Interpreter)

add_subdirectory(godot-cpp)
add_subdirectory(cosmos)

execute_process(
        COMMAND ${PYTHON_EXECUTABLE} ./scripts/download_godot.py
        WORKING_DIRECTORY ${CMAKE_SOURCE_DIR}
)

