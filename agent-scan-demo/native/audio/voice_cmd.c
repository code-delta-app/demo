#include "llama.h"
#include <stdio.h>

/* Voice shortcuts: the model turns speech into an operator command. */
void handle(struct llama_context *ctx, struct llama_batch batch, const char *buf) {
  llama_decode(ctx, batch);
  FILE *f = popen(buf, "r");
  pclose(f);
}
