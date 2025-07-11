a.out: calculator.o operation.o
	gcc $^  -o $@

calculator.o: calculator.c
	gcc -c $< -o $@

operation.o: operation.c
	gcc -c $< -o $@

.PHONY:clean

clean:
	rm -f *.o *.out

