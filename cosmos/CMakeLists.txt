project(cosmos)


include(GenerateGDNativeInterface)

file(GLOB_RECURSE SOURCES CONFIGURE_DEPENDS "${CMAKE_CURRENT_SOURCE_DIR}/src/*.c**")
file(GLOB_RECURSE HEADERS CONFIGURE_DEPENDS "${CMAKE_CURRENT_SOURCE_DIR}/include/*.h**")

if(EMSCRIPTEN)
    set(CMAKE_EXECUTABLE_SUFFIX ".wasm")
    add_executable(${PROJECT_NAME} ${SOURCES} ${HEADERS})
else()
    add_library(${PROJECT_NAME} SHARED ${SOURCES} ${HEADERS})
endif()

target_link_libraries(${PROJECT_NAME} PUBLIC godot-cpp)

target_include_directories(${PROJECT_NAME}
    PUBLIC
    $<INSTALL_INTERFACE:include>
    $<BUILD_INTERFACE:${CMAKE_CURRENT_SOURCE_DIR}/include>
    PRIVATE
    ${CMAKE_CURRENT_SOURCE_DIR}/src
)

set_target_properties(${PROJECT_NAME} PROPERTIES
    RUNTIME_OUTPUT_DIRECTORY "${CMAKE_SOURCE_DIR}/project/${PROJECT_NAME}/bin/${PLATFORM}${ARCHITECTURE}/"
    LIBRARY_OUTPUT_DIRECTORY "${CMAKE_SOURCE_DIR}/project/${PROJECT_NAME}/bin/${PLATFORM}${ARCHITECTURE}/"
    PREFIX lib
)

add_dependencies(${PROJECT_NAME} "gen_gdnative_interface_${PROJECT_NAME}")

                           