
if (${CMAKE_SYSTEM_NAME} STREQUAL "Linux")
    add_global_compile_flag("-m${ARCHITECTURE}")
endif ()