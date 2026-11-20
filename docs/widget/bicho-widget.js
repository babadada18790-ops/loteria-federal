/*!
 * Bicho Hoje — widget de resultado (embutir com 1 linha)
 * Uso:
 *   <script src="https://cdn.jsdelivr.net/gh/babadada18790-ops/loteria-federal@main/docs/widget/bicho-widget.js"
 *           data-bicho-hoje data-limite="5" defer></script>
 * Dados: https://babadada18790-ops.github.io/loteria-federal/api/ultimo.json
 * Licença do código: MIT
 */
(function () {
  "use strict";
  var mapa = ["Avestruz","Águia","Burro","Borboleta","Cachorro","Cabra","Carneiro","Camelo",
    "Cobra","Coelho","Cavalo","Elefante","Galo","Gato","Jacaré","Leão","Macaco","Porco",
    "Pavão","Peru","Touro","Tigre","Urso","Veado","Vaca"];

  var script = document.currentScript;
  if (!script) return;
  var base = script.getAttribute("data-api") ||
    (script.src.replace("/widget/bicho-widget.js", "/api/ultimo.json"));
  var limite = parseInt(script.getAttribute("data-limite") || "5", 10);
  var origem = "https://bicho-hoje.com/";

  var caixa = document.createElement("div");
  caixa.setAttribute("data-bicho-hoje", "");
  script.parentNode.insertBefore(caixa, script.nextSibling);
  var raiz = caixa.attachShadow ? caixa.attachShadow({ mode: "open" }) : caixa;

  raiz.innerHTML =
    "<style>" +
    ":host{all:initial}" +
    ".c{font:14px/1.45 system-ui,-apple-system,Segoe UI,Roboto,sans-serif;color:#1d1d1f;" +
    "border:1px solid #e3e3e6;border-radius:10px;max-width:320px;background:#fff;overflow:hidden}" +
    ".h{display:flex;justify-content:space-between;gap:8px;padding:10px 12px;background:#f7f7f8;" +
    "border-bottom:1px solid #e3e3e6;font-weight:600;font-size:13px}" +
    ".h span{font-weight:400;color:#6b6b70;font-size:12px}" +
    "table{width:100%;border-collapse:collapse}" +
    "td{padding:6px 12px;border-bottom:1px solid #f0f0f2}" +
    "td:first-child{color:#8a8a8f;width:22px}" +
    "td:last-child{text-align:right;color:#6b6b70;font-variant-numeric:tabular-nums}" +
    "b{font-weight:600}" +
    ".f{padding:8px 12px;font-size:11px;color:#8a8a8f;background:#fafafa}" +
    ".f a{color:#8a8a8f;text-decoration:none;border-bottom:1px dotted #b9b9be}" +
    "</style>" +
    '<div class="c"><div class="h">Resultado do Bicho<span class="carregando">…</span></div>' +
    '<table><tbody class="linhas"></tbody></table>' +
    '<div class="f">Fonte: <a href="' + origem +
    '?utm_source=widget&utm_medium=embed&utm_campaign=bicho-widget" rel="noopener" ' +
    'target="_blank">Bicho Hoje</a> · dados abertos CC BY 4.0</div></div>';

  function esc(t) {
    return String(t).replace(/[&<>"]/g, function (c) {
      return { "&": "&amp;", "<": "&lt;", ">": "&gt;", '"': "&quot;" }[c];
    });
  }

  fetch(base, { credentials: "omit" })
    .then(function (r) { if (!r.ok) throw new Error(r.status); return r.json(); })
    .then(function (d) {
      var premios = (d.premios || []).slice(0, limite);
      var linhas = premios.map(function (p) {
        var grupo = parseInt(p.grupo, 10);
        var nome = p.bicho || mapa[grupo - 1] || "";
        return "<tr><td>" + p.premio + "º</td><td><b>" +
          ("0000" + p.milhar).slice(-4) + "</b> · " +
          ("0" + grupo).slice(-2) + " " + esc(nome) + "</td><td>" +
          esc(p.horario || "") + "</td></tr>";
      }).join("");
      raiz.querySelector(".linhas").innerHTML = linhas ||
        '<tr><td colspan="3">Sem resultado publicado ainda hoje.</td></tr>';
      raiz.querySelector(".carregando").textContent = d.horario || d.data || "";
    })
    .catch(function () {
      raiz.querySelector(".linhas").innerHTML =
        '<tr><td colspan="3">Resultado indisponível. ' +
        '<a href="' + origem + '" rel="noopener" target="_blank">Ver no site</a></td></tr>';
      raiz.querySelector(".carregando").textContent = "";
    });
})();
