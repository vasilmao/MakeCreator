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

### some flags
You can set flags CXX, LXX, OBJDIR (where .obj files will be stored. Default: obj, created if does not exists. Specified: not created) (strings)

### CFLAGS, LFLAGS
Just compiler and linker flags (strings or array of strings (arrays of strings are concatenated in one string))

### IFLAGS
There are three modes:
1. In your .cpp files you write path to the header (for example ../include/header.h), so you can set "IFLAG" : "NO", and you also may not do it (this is default behaviour)
2. You write path to the header from the root of your project (for example include/header.h), set "IFLAG" : "ROOT"
3. You write just name of header (for example header.h), set "IFLAG" : "ALL"

### prohibited_dirs
directories that will not be indexed (you may want to skip such directories as .git, .vs, .vscode)
