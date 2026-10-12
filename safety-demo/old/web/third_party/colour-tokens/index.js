// SYNTHETIC DEMO FILE (CodeDelta) — a small bundled library for the Meridian Helpdesk demo.
// Inert: nothing here contacts a network or runs anything.
const TOKENS = { brand: '#f86c00', ink: '#1a1a2e', paper: '#faf9f6' };
function token(name) {
  return TOKENS[name] || TOKENS.ink;
}
function hex(name) {
  return token(name).replace('#', '');
}
module.exports = { token, hex, TOKENS };
