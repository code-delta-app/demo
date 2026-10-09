#include <stdio.h>
#include <stdarg.h>
#include <time.h>
#include "log.h"

static int current_level = LOG_INFO;

void log_set_level(int level) { current_level = level; }

static void vlog(const char *tag, const char *fmt, va_list ap) {
    char stamp[32];
    time_t now = time(NULL);
    strftime(stamp, sizeof stamp, "%Y-%m-%d %H:%M:%S", localtime(&now));
    fprintf(stderr, "%s [%s] ", stamp, tag);
    vfprintf(stderr, fmt, ap);
    fputc('\n', stderr);
}

void log_info(const char *fmt, ...) {
    if (current_level > LOG_INFO) return;
    va_list ap;
    va_start(ap, fmt);
    vlog("info", fmt, ap);
    va_end(ap);
}

void log_warn(const char *fmt, ...) {
    va_list ap;
    va_start(ap, fmt);
    vlog("warn", fmt, ap);
    va_end(ap);
}
