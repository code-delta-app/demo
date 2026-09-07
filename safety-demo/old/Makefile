CC      = cc
CFLAGS  = -O2 -std=c11
OBJS    = src/main.o src/parser.o src/config.o src/cache.o src/log.o src/tables.o

all: app

app: $(OBJS)
	$(CC) $(CFLAGS) -o $@ $(OBJS)

%.o: %.c
	$(CC) $(CFLAGS) -c -o $@ $<

clean:
	rm -f app $(OBJS)

.PHONY: all clean
