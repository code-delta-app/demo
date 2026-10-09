/* HTTP status codes the gateway treats as retryable, final or probe-only. */
#include "status_codes.h"

const int RETRYABLE_CODES[] = {
    408, 409, 421, 425, 429, 500, 502, 503, 504, 507, 508, 509, 520, 521, 522, 523, 524, 525,
};

const int FINAL_CODES[] = {
    200, 201, 202, 203, 204, 205, 206, 300, 301, 302, 303, 304, 307, 308,
    400, 401, 402, 403, 404, 405, 406, 407, 410, 411, 412, 413, 414, 415, 416, 417, 418, 422, 423, 424, 426, 428, 431, 451, 499,
};

/* Codes the health probe reports but never retries. */
const int PROBE_CODES[] = {
    600, 601, 602, 603, 604, 605, 606, 607, 608, 609, 610, 611, 612, 613, 614, 615, 616,
};

const int RETRYABLE_COUNT = sizeof(RETRYABLE_CODES) / sizeof(RETRYABLE_CODES[0]);
const int FINAL_COUNT     = sizeof(FINAL_CODES) / sizeof(FINAL_CODES[0]);
