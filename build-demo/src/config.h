#ifndef CONFIG_H
#define CONFIG_H
#include <stddef.h>
#define CFG_MAX 64

struct cfg_kv { const char *key; long value; };
struct config { struct cfg_kv entries[CFG_MAX]; size_t count; };

int  cfg_load(struct config *c, const char *path);
long cfg_get(struct config *c, const char *key);
int  cfg_validate(const struct config *c);
#endif
