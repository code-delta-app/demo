#include <stdio.h>
#include <stdlib.h>
#include "parser.h"
#include "config.h"
#include "cache.h"
#include "log.h"

int main(int argc, char **argv) {
    struct config cfg;
    cfg_load(&cfg, argc > 1 ? argv[1] : "buildproj.conf");
    log_set_level((int)cfg_get(&cfg, "log_level"));
    struct cache cache;
    if (cache_init(&cache, (size_t)cfg_get(&cfg, "cache_entries")) != 0) {
        log_warn("main: cache init failed");
        return EXIT_FAILURE;
    }
    long total = 0;
    for (int i = 2; i < argc; i++) {
        struct parser p = {0};
        p.lx.src = argv[i];
        p.tok = lex_next(&p.lx);
        total += parse_expr(&p);
    }
    printf("total: %ld\n", total);
    long hits, misses;
    cache_stats(&cache, &hits, &misses);
    log_info("cache: %ld hits, %ld misses", hits, misses);
    return EXIT_SUCCESS;
}
