
if (${CMAKE_SYSTEM_NAME} STREQUAL "Linux" OR !MSVC)
    add_global_compile_flag("-m${ARCHITECTURE}")
endif ()

set(POSITION_INDEPENDENT_CODE ON)