execute_process(
    COMMAND ${PYTHON_EXECUTABLE} ./scripts/get_generated_sources.py "${CMAKE_CURRENT_SOURCE_DIR}/gdnative_scripts.ini" "${CMAKE_CURRENT_SOURCE_DIR}"
    WORKING_DIRECTORY ${CMAKE_SOURCE_DIR}
    OUTPUT_VARIABLE "${PROJECT_NAME}_GENERATED_SOURCES"
)

message(STATUS "${${PROJECT_NAME}_GENERATED_SOURCES}")

add_custom_target("gen_gdnative_interface_${PROJECT_NAME}" ALL
    SOURCES ${CMAKE_CURRENT_SOURCE_DIR}/gdnative_scripts.ini
    DEPENDS ${CMAKE_CURRENT_SOURCE_DIR}/gdnative_scripts.ini
    BYPRODUCTS ${${PROJECT_NAME}_GENERATED_SOURCES}
    WORKING_DIRECTORY ${CMAKE_SOURCE_DIR}
    COMMAND ${PYTHON_EXECUTABLE} ./scripts/generate_gdnative_project_files.py "${CMAKE_CURRENT_SOURCE_DIR}/gdnative_scripts.ini" "${CMAKE_CURRENT_SOURCE_DIR}" ${PROJECT_NAME}
    COMMENT "Generating GDNative interface"
)