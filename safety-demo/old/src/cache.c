#include <stdlib.h>
#include <string.h>
#include "cache.h"
#include "log.h"

/* Open-addressing string cache with FNV-1a hashing. */

static unsigned long fnv1a(const char *s) {
    unsigned long h = 1469598103934665603ul;
    while (*s) { h ^= (unsigned char)*s++; h *= 1099511628211ul; }
    return h;
}

int cache_init(struct cache *c, size_t slots) {
    c->slots = calloc(slots, sizeof *c->slots);
    if (!c->slots) return -1;
    c->nslots = slots;
    c->used = 0;
    c->hits = 0;
    c->misses = 0;
    return 0;
}

const char *cache_get(struct cache *c, const char *key) {
    size_t i = fnv1a(key) % c->nslots;
    for (size_t probe = 0; probe < c->nslots; probe++) {
        struct cache_slot *s = &c->slots[(i + probe) % c->nslots];
        if (!s->key) break;
        if (strcmp(s->key, key) == 0) {
            c->hits++;
            return s->value;
        }
    }
    c->misses++;
    return NULL;
}

int cache_put(struct cache *c, const char *key, const char *value) {
    if (c->used >= c->nslots) {
        log_warn("cache: full, dropping %s", key);
        return -1;
    }
    size_t i = fnv1a(key) % c->nslots;
    while (c->slots[i].key) {
        if (strcmp(c->slots[i].key, key) == 0) {
            c->slots[i].value = value;
            return 0;
        }
        i = (i + 1) % c->nslots;
    }
    c->slots[i].key = strdup(key);
    c->slots[i].value = value;
    c->used++;
    return 0;
}

void cache_stats(const struct cache *c, long *hits, long *misses) {
    *hits = c->hits;
    *misses = c->misses;
}
