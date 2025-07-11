a.out: print.o
	@gcc print.o -o a.out
print.o: print.s
	@gcc -c print.s -o print.o
print.s: print.i
	@gcc -S print.i -o print.s
print.i: print.c
	@gcc -E print.c -o print.i

clean:
	@rm a.out

