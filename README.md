# MakeCreator
make makefile on python

## how to run
1. put create_make.json into the root of your project
2. run create_make.py and pass root directory of your project as argument

## how to make create_make.json
It is a dict

### specifying targets
There are 3 modes:
1. "targets" : "some_string", where some_string is one executable name for your entire project (all .obj files linked into it)
2. "targets" : ["1.cpp", "2.cpp"], where 1.cpp and 2.cpp are files with main functions, they will be compiled into 1.out and 2.out
3. "targets" : {"abc.cpp" : "def.out", "1.cpp" : "2"}, this specifies excutable names
