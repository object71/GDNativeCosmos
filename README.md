# Project GDNative Cosmos
Template for GDNative code-first approach project.

## How to use
Create repository from this template. Then rename the cosmos project. Run cmake configuration and it will download godot for you in the godot folder. Also when you build you only need to specify your C++ class script in gdnative_scripts.ini under normal or tool depending how you want them registered. First time you create a new script it will generate all necessary files for you on build so no need to worry about that. After that you only need to care about the files under "include" and not the ones under "include/gen"

### Web

To build for web you would have to go into the emsdk folder and run:

```
./emsdk install latest
./emsdk activate latest
```

Also when configuring with CMake make sure to add both ```-DCMAKE_TOOLCHAIN_FILE=./emsdk/upstream/emscripten/cmake/Platform/Emscripten.cmake``` and ```-G Ninja```

## Renaming

When renaming the cosmos project do this by renaming:
- The Godot project
- The main folder and the project name inside the CMakeLists.txt
- The target argument for the build task for vscode in .vscode/tasks.json
- The add_subdirectory inside the main CMakeLists.txt
- Delete old files if you've previously built the project
    - Inside the project folder there will be some generated files
- Inside library.cpp. It will be generated only once so you need to either delete it (for regeneration) or change the prefix
