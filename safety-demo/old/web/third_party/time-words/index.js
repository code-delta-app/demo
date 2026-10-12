// SYNTHETIC DEMO FILE (CodeDelta) — a small bundled library for the Meridian Helpdesk demo.
// Inert: nothing here contacts a network or runs anything.
const UNITS = [['day', 86400], ['hour', 3600], ['minute', 60]];
function ago(seconds) {
  for (const [name, size] of UNITS) {
    const n = Math.floor(seconds / size);
    if (n >= 1) return n + ' ' + name + (n > 1 ? 's' : '') + ' ago';
  }
  return 'just now';
}
module.exports = { ago };
