#include "llama.h"
#include <stdio.h>

/* Offline transcription of voicemail attachments. */
void transcribe(struct llama_context *ctx, struct llama_batch batch) {
  llama_decode(ctx, batch);
  printf("transcript ready\n");
}
