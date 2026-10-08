global.window = {};
require('./highlight.js');
const h = window.hljs; const out = {};
for (const n of h.listLanguages()) { out[n] = (h.getLanguage(n).aliases || []); }
out.elixir = (out.elixir||[]).concat(['iex','ex','exs']); out.prolog = (out.prolog||[]).concat(['pro']);
console.log(JSON.stringify(out));
