#include "llama.h"
#include <cstdio>
static void generate(llama_context *ctx, llama_batch batch, int n_predict) {
    for (int i = 0; i < n_predict; i++) {
        if (llama_decode(ctx, batch)) {
            fprintf(stderr, "decode failed\n");
            return;
        }
    }
}
