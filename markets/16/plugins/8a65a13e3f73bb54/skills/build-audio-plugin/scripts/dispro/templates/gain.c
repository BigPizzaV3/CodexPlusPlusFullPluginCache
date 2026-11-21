/* Copyright (c) 2026 Kaizen Strategic AI Inc. All rights reserved.
 * Template material licensed under Dispro Generated Output Licence 1.0.
 * See OUTPUT-LICENSE.txt. No unrelated product DSP is used. */
#include "lv2.h"
#include <stdlib.h>
#include <math.h>

typedef struct { const float *in, *gain; float *out; } Gain;
static LV2_Handle instantiate(const LV2_Descriptor *d, double rate,
                             const char *bundle, const LV2_Feature *const *f) {
    (void)d; (void)rate; (void)bundle; (void)f;
    return calloc(1, sizeof(Gain));
}
static void connect_port(LV2_Handle h, uint32_t port, void *data) {
    Gain *g = (Gain *)h;
    if (port == 0) g->in = data;
    if (port == 1) g->out = data;
    if (port == 2) g->gain = data;
}
static void run(LV2_Handle h, uint32_t n) {
    Gain *g = (Gain *)h;
    if (!g->out) return;
    float gain = g->gain ? *g->gain : 1.0f;
    if (!isfinite(gain)) gain = 1.0f;
    if (gain < 0.0f) gain = 0.0f;
    if (gain > 2.0f) gain = 2.0f;
    for (uint32_t i = 0; i < n; ++i) g->out[i] = g->in ? g->in[i] * gain : 0.0f;
}
static void cleanup(LV2_Handle h) { free(h); }
static const LV2_Descriptor descriptor = {
    "urn:dispro:__PROJECT__", instantiate, connect_port, NULL,
    run, NULL, cleanup, NULL
};
LV2_SYMBOL_EXPORT const LV2_Descriptor *lv2_descriptor(uint32_t index) {
    return index == 0 ? &descriptor : NULL;
}
