// SYNTHETIC DEMO FILE (CodeDelta) — a small bundled library for the Meridian Helpdesk demo.
// Inert: nothing here contacts a network or runs anything.
function isNumber(v) {
  return typeof v === 'number' && Number.isFinite(v);
}
function toNumber(v, dflt) {
  const n = Number(v);
  return isNumber(n) ? n : dflt;
}
module.exports = { isNumber, toNumber };
