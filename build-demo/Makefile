CC      = cc
CFLAGS  = -O2 -std=c11 -Wall -Wextra
LDFLAGS =
OBJS    = src/main.o src/parser.o src/config.o src/cache.o src/log.o \
          src/tables.o src/net.o

all: app

app: $(OBJS)
	$(CC) $(CFLAGS) -o $@ $(OBJS) $(LDFLAGS)

%.o: %.c
	$(CC) $(CFLAGS) -c -o $@ $<

check: app
	./app buildproj.conf "1+2*3" | grep -q "total: 7"

install: app
	install -m 755 app $(DESTDIR)/usr/local/bin/app

clean:
	rm -f app $(OBJS)

.PHONY: all check install clean
