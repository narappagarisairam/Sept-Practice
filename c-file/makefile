#this is make file for creating directories and files


all: make_dir create_file 

make_dir:
	mkdir -p d1 d2 d3

create_file:
	touch f1.c f2.c f3.c

.PHONY:clean

clean:
	rm -rf d3
	_rm f3.c

