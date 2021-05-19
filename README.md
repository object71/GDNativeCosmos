# Project GDNative Cosmos
Template for GDNative code-first approach project.

## How to use
Create repository from this template. Then rename the cosmos project. Run cmake configuration and it will download godot for you in the godot folder. Also when you build you only need to specify your C++ class script in gdnative_scripts.ini under normal or tool depending how you want them registered. First time you create a new script it will generate all necessary files for you on build so no need to worry about that. After that you only need to care about the files under "include" and not the ones under "include/gen"

## Future developments

- [ ] Setup run targets for major IDEs to run the downloaded godot engine on the project
- [ ] Setup to close godot on build (Windows is not reloadable & if you have tool scripts also)
- [ ] Add CI/CD template