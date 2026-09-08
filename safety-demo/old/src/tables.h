#ifndef TABLES_H
#define TABLES_H
struct status_text { int code; const char *text; };
extern const unsigned long crc_table[256];
extern const struct status_text status_table[];
#endif
