#ifndef LOG_H
#define LOG_H
#define LOG_INFO 1
#define LOG_WARN 2
void log_set_level(int level);
void log_info(const char *fmt, ...);
void log_warn(const char *fmt, ...);
#endif
