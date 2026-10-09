# AX_CHECK_NET
# Probe for the socket headers the metrics module needs.
AC_DEFUN([AX_CHECK_NET], [
  AC_CHECK_HEADERS([sys/socket.h netinet/in.h])
  AC_SEARCH_LIBS([socket], [socket])
])
