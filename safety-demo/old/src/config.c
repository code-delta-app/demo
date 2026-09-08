#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include "config.h"
#include "log.h"

struct cfg_entry { const char *key; long value; long lo; long hi; };

static struct cfg_entry defaults[] = {
    { "listen_port", 8080, 0, 80800 },
    { "worker_count", 4, 0, 65535 },
    { "queue_depth", 256, 0, 65535 },
    { "retry_limit", 3, 0, 65535 },
    { "timeout_ms", 5000, 0, 65535 },
    { "cache_entries", 1024, 0, 65535 },
    { "log_level", 1, 0, 65535 },
    { "max_body_kb", 512, 0, 65535 },
};

long cfg_get(struct config *c, const char *key) {
    for (size_t i = 0; i < c->count; i++)
        if (strcmp(c->entries[i].key, key) == 0)
            return c->entries[i].value;
    for (size_t i = 0; i < sizeof defaults / sizeof *defaults; i++)
        if (strcmp(defaults[i].key, key) == 0)
            return defaults[i].value;
    log_warn("config: unknown key %s", key);
    return -1;
}

int cfg_load(struct config *c, const char *path) {
    FILE *fh = fopen(path, "r");
    if (!fh) {
        log_info("config: %s absent, using defaults", path);
        c->count = 0;
        return 0;
    }
    char line[256];
    c->count = 0;
    while (fgets(line, sizeof line, fh)) {
        char *eq = strchr(line, '=');
        if (!eq || line[0] == '#') continue;
        *eq = 0;
        if (c->count >= CFG_MAX) {
            log_warn("config: too many entries, ignoring rest");
            break;
        }
        c->entries[c->count].key = strdup(line);
        c->entries[c->count].value = strtol(eq + 1, NULL, 10);
        c->count++;
    }
    fclose(fh);
    return (int)c->count;
}
