// SYNTHETIC DEMO FILE (CodeDelta) — a small bundled library for the Meridian Helpdesk demo.
// Inert: nothing here contacts a network or runs anything.
function isObj(v) {
  return v && typeof v === 'object' && !Array.isArray(v);
}
function merge(a, b) {
  const out = Object.assign({}, a);
  for (const k of Object.keys(b)) {
    out[k] = isObj(a[k]) && isObj(b[k]) ? merge(a[k], b[k]) : b[k];
  }
  return out;
}
module.exports = merge;
