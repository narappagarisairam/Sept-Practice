CC=gcc
CFLAGS=-Wall -g
SRCS := $(wildcard *.c)
BINS := $(SRCS:%.c=%)
OBJS := $(SRCS:%.c=%.o)
all: $(BINS)
	@echo "$(SRCS)"
%: %.o
	@echo "Generating binaries"
	$(CC) $< -o $@
%.o : %.c
	@echo "Generating object files"
	$(CC) $(CFLAGS) -c $< -o $@
clean:
	rm $(BINS) $(OBJS)
