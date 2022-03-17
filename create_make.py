#!/usr/bin/env python3

import os
import sys

# BIN_DIR = "bin"
# OBJ_DIR = "obj"

# TARGETS_DIR = "targets"


# ban_list = [".git", ".vscode", ".vs", OBJ_DIR, BIN_DIR, TARGETS_DIR]
# LXX_FLAGS = [
#     # "-fzalupa"
# ]
# CXX_FLAGS = [
#     "-std=c++17",
#     # "-fno-elide-constructors",
#     "-DMISTAKE"
#     ]

# CXX = "g++"


# def get_dirs_rec(start_dir):
#     ans = [start_dir]
#     for subdir in os.listdir(start_dir):
#         if (any(subdir == x for x in ban_list)):
#             continue
#         candidate = os.path.join(start_dir, subdir)
#         if (os.path.isdir(candidate)):
#             ans += get_dirs_rec(candidate)
#     return ans

# def get_src_rec(start_dir):
#     ans = []
#     for subdir in os.listdir(start_dir):
#         if (any(subdir == x for x in ban_list)):
#             continue
#         candidate = os.path.join(start_dir, subdir)
#         if (os.path.isdir(candidate)):
#             ans += get_src_rec(candidate)
#         elif (os.path.isfile(candidate)):
#             if candidate.endswith(".cpp"):
#                 ans.append(candidate[:candidate.rfind(".")])
#     return ans

# makefile_content = ""

# def spawn_object_targets(sources):
#     cnt = 0
#     global makefile_content
#     for cpp_file in sources:
#         filename_without_path = os.path.join(OBJ_DIR, os.path.split(cpp_file)[-1])

#         make_rule = subprocess.run([CXX, "-MM", "-MT", filename_without_path + ".o"] + cxx_include_argument + [cpp_file + ".cpp"], stdout=subprocess.PIPE).stdout.decode("utf-8")
#         make_rule = make_rule.rstrip() + " Makefile"

#         makefile_content += make_rule
#         makefile_content += "\n\t"

#         filename_without_path = os.path.split(cpp_file)[-1]
#         makefile_content += CXX + " " + " ".join(cxx_include_argument) + " " + " ".join(CXX_FLAGS) + " -c " + cpp_file + ".cpp -o " + OBJ_DIR + "/" + filename_without_path + ".o\n\n"

#         cnt += 1
#         print(cnt, "of", len(sources))



# if not os.path.exists(OBJ_DIR):
#     os.mkdir(OBJ_DIR)

# if not os.path.exists(BIN_DIR):
#     os.mkdir(BIN_DIR)


# print("getting directories...")
# dirs = get_dirs_rec(os.path.curdir)
# print("directories got")
# print("creating g++ -I arguments")

# # cxx_include_argument = " ".join("-I " + x for x in dirs)
# cxx_include_argument = []
# for dir in dirs:
#     cxx_include_argument.append("-I")
#     cxx_include_argument.append(dir)

# print("arguments created")

# # now lets find all .cpp files

# print("finding .cpp files...")
# srcs = get_src_rec(os.path.curdir)
# print("list of .cpp files created")

# # print(dirs)
# # print(srcs)
# # print(cxx_include_argument)



# # spawn main targets

# targets_list = []

# makefile_content += "all: "

# for file in os.listdir(os.path.join(os.path.curdir, "targets")):
#     print("target file:", file)
#     file_name_without_extension = file[:file.rfind(".")]
#     target_file = os.path.join(os.path.curdir, "targets", file_name_without_extension)
#     if (os.path.isfile(target_file + ".cpp")):
#         out_filename = BIN_DIR + "/" + file_name_without_extension + ".out"
#         makefile_content += out_filename + " "

# makefile_content += "\n\n"

# for file in os.listdir(os.path.join(os.path.curdir, "targets")):
#     print("target file:", file)
#     file_name_without_extension = file[:file.rfind(".")]
#     target_file = os.path.join(os.path.curdir, "targets", file_name_without_extension)
#     if (os.path.isfile(target_file + ".cpp")):
#         targets_list.append(target_file)

#         out_filename = BIN_DIR + "/" + file_name_without_extension + ".out"
#         makefile_content += out_filename + ": Makefile "
#         makefile_content += OBJ_DIR + "/" + file_name_without_extension + ".o "
#         for cpp_file in srcs:
#             filename_without_path = os.path.split(cpp_file)[-1]
#             makefile_content += OBJ_DIR + "/" + filename_without_path
#             makefile_content += ".o "

#         # makefile_content += "\n\t" + CXX + " " + " ".join(LXX_FLAGS) + " -o "  + out_filename + " "
#         makefile_content += "\n\t" + CXX + (" " + " ".join(LXX_FLAGS) if len(LXX_FLAGS) != 0 else "")+ " -o " + out_filename + " "

#         makefile_content += OBJ_DIR + "/" + file_name_without_extension + ".o "

#         for cpp_file in srcs:
#             filename_without_path = os.path.split(cpp_file)[-1]
#             makefile_content += OBJ_DIR + "/" + filename_without_path
#             makefile_content += ".o "
#         print("target spawned", file)
#         makefile_content += "\n\n"

# print("main target created")

# srcs += targets_list

# # spawn targets for object files

# print("creating make targets for .o ...")

# spawn_object_targets(srcs)

# print("targets created")
# print("writing to file")

# f = open("Makefile", "w")
# f.write(makefile_content)
# f.close()

# print("completed")

class Configuration:
    def __init__(self, include_dirs="", LFLAGS="", CFLAGS=""):
        self._include_dirs = include_dirs
        self._LFLAGS = LFLAGS
        self._CFLAGS = CFLAGS
        self._include_dirs_changed = False
        self._lflags_changed = False
        self._cflags_changed = False

    def SetIncludeDirs(self, s : str)-> None:
        if (self._include_dirs_changed):
            raise SyntaxError("double include dir option definition")
        self._include_dirs_ = s
        self._include_dirs_changed = True
    
    def SetLFLAGS(self, s : str) -> None:
        if (self._lflags_changed):
            raise SyntaxError("double lflags option definition")
        self._LFLAGS = s
        self._lflags_changed = True
        print("new lflags")
        print(s)

    def SetCFLAGS(self, s : str) -> None:
        if (self._cflags_changed):
            raise SyntaxError("double cflags option definition")
        self._CFLAGS = s
        self._cflags_changed = True
        print("new cflags")
        print(s)


class TextIterator:
    file_str = ""
    rip = 0
    def __init__(self, s : str):
        self.file_str = s
    
    def SkipSpaces(self) -> None:
        while (self.rip < len(self.file_str) and self.file_str[self.rip] == " "):
            self.rip += 1
    
    def SkipSpaceLike(self) -> None:
        while (self.rip < len(self.file_str) and self.file_str[self.rip] in [" ", "\t", "\n"]):
            self.rip += 1

    def Require(self, required : str):
        self.SkipSpaces()
        assert(self.file_str[self.rip : self.rip + len(required)] == required)
        self.rip += len(required)

    def CheckIfNextIs(self, required : str) -> bool:
        self.SkipSpaces()
        if self.file_str[self.rip : self.rip + len(required)] == required:
            self.rip += len(required)
            return True
        return False
    
    # find next s in text, return -1 if not found, else index
    def FindNext(self, s : str) -> int:
        ans = self.file_str[self.rip:].find(s)
        if (ans == -1):
            return -1
        else:
            return ans + self.rip

def PrettifyStr(s : str) -> str:
    return " ".join((" ".join(s.strip().split("\n"))).split("\t"))

# this function needs garanty that text + rip starts with the keyword
def SetCFLAGS(text : TextIterator, config : Configuration) -> None:
    text.Require("CFLAGS")
    text.Require("=")
    text.Require("{")
    closing_index = text.FindNext("}")
    if (closing_index == -1):
        raise SyntaxError("Closing bracket not found [rip = " + str(text.rip) + "]")
    flags = PrettifyStr(text.file_str[text.rip : closing_index])
    config.SetCFLAGS(flags)
    text.rip = closing_index + 1
    text.SkipSpaceLike()
    pass

# this function needs garanty that text + rip starts with the keyword
def SetLFLAGS(text : TextIterator, config : Configuration) -> None:
    text.Require("LFLAGS")
    text.Require("=")
    text.Require("{")
    closing_index = text.FindNext("}")
    if (closing_index == -1):
        raise SyntaxError("Closing bracket not found [rip = " + str(text.rip) + "]")
    flags = PrettifyStr(text.file_str[text.rip : closing_index])
    config.SetLFLAGS(flags)
    text.rip = closing_index + 1
    text.SkipSpaceLike()
    pass

# this function needs garanty that text + rip starts with the keyword
def SetIFLAGS(text : TextIterator, config : Configuration) -> None:
    pass
    

KEYVARS = {
    "CFLAGS" : SetCFLAGS,
    "LFLAGS" : SetLFLAGS,
    "IFLAGS" : SetIFLAGS
}

KEYVALUES = [
    "ALL",
    "ROOT",
]

def ParsedTarget(text : TextIterator) -> bool:
    return False

def ParsedKeyvars(text : TextIterator, config : Configuration) -> bool:
    for keyvar, function in KEYVARS.items():
        if (text.file_str[text.rip : text.rip + len(keyvar)] == keyvar):
            function(text, config)
            return True
    return False


def ParseFile(file, config):
    text = TextIterator(file.read())
    rip = 0
    while (text.rip < len(text.file_str)):
        print("aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa")
        print(text.file_str[text.rip:])
        if ParsedKeyvars(text, config):
            continue
        if ParsedTarget(text, config):
            continue

def FindAndParse(filename) -> Configuration:
    config = Configuration()
    if (os.path.exists(filename)):
        file = open(filename, "r")
        ParseFile(file, config)
    
    return config

if __name__ == "__main__":
    if (len(sys.argv) > 1):
        os.chdir(sys.argv[1])
    config = FindAndParse("create_make.txt")
    # print(config.LFLAGS_)