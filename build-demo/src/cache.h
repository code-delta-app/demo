#ifndef CACHE_H
#define CACHE_H
#include <stddef.h>

struct cache_slot { const char *key; const char *value; };
struct cache { struct cache_slot *slots; size_t nslots; size_t used; long hits; long misses; };

int cache_init(struct cache *c, size_t slots);
int cache_put(struct cache *c, const char *key, const char *value);
const char *cache_get(struct cache *c, const char *key);
void cache_stats(const struct cache *c, long *hits, long *misses);
#endif
