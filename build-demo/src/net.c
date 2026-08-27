#include <stdio.h>
#include <string.h>
#include "net.h"
#include "log.h"

/* Metric publication over a line protocol — added in 2.0. */

static char pending[64][96];
static int npending;

int publish_metric(const char *name, long value) {
    if (npending >= 64) {
        log_warn("net: metric buffer full, flushing early");
        flush_metrics();
    }
    snprintf(pending[npending], sizeof pending[0], "%s=%ld", name, value);
    npending++;
    return 0;
}

int flush_metrics(void) {
    for (int i = 0; i < npending; i++)
        fprintf(stderr, "metric %s\n", pending[i]);
    int sent = npending;
    npending = 0;
    return sent;
}
