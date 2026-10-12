// SYNTHETIC DEMO FILE (CodeDelta) — a small bundled library for the Meridian Helpdesk demo.
// Inert: nothing here contacts a network or runs anything.
function padStart(s, n, ch) {
  s = String(s); ch = ch || ' ';
  while (s.length < n) s = ch + s;
  return s;
}
function padEnd(s, n, ch) {
  s = String(s); ch = ch || ' ';
  while (s.length < n) s = s + ch;
  return s;
}
module.exports = { padStart, padEnd };
