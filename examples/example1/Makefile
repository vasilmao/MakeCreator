all: Makefile b.out 

b.out: Makefile obj/main.o obj/main.o obj/implementation.o 
	g++  obj/main.o obj/implementation.o -o b.out

obj/main.o: src/main.cpp include/header.h Makefile
	g++ -I . -DKEK -Wall -Werror -c ./src/main.cpp -o obj/main.o

obj/implementation.o: src/implementation.cpp src/../include/header.h Makefile
	g++ -I . -DKEK -Wall -Werror -c ./src/implementation.cpp -o obj/implementation.o

