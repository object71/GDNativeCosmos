if (${CMAKE_BUILD_TYPE} MATCHES Debug)
    add_compile_definitions(_DEBUG=1)
else ()
    add_compile_definitions(NDEBUG=1)
endif ()