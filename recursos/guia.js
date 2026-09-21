// Marcas de la lista y ampliación de la infografía. Todo ocurre en el navegador:
// las marcas se guardan en localStorage y no se envía nada a ningún servidor.
(function () {
  "use strict";
  document.documentElement.classList.add("js");
  var CLAVE = "vibe-responsable:lista";
  var casillas = Array.prototype.slice.call(document.querySelectorAll(".cumple input"));
  var panel = document.querySelector(".resultado");
  var cuenta = document.querySelector(".cuenta");

  function leer() {
    try { return JSON.parse(localStorage.getItem(CLAVE)) || {}; } catch (e) { return {}; }
  }
  function guardar() {
    var estado = {};
    casillas.forEach(function (c) { if (c.checked) { estado[c.dataset.punto] = true; } });
    try { localStorage.setItem(CLAVE, JSON.stringify(estado)); } catch (e) { /* sin almacenamiento, no pasa nada */ }
  }
  function pintar() {
    if (!cuenta) { return; }
    var n = casillas.filter(function (c) { return c.checked; }).length;
    cuenta.textContent = cuenta.dataset.plantilla.replace("{n}", n).replace("{total}", cuenta.dataset.total);
  }

  if (panel && casillas.length) {
    var estado = leer();
    casillas.forEach(function (c) {
      c.checked = !!estado[c.dataset.punto];
      c.addEventListener("change", function () { guardar(); pintar(); });
    });
    panel.hidden = false;
    pintar();

    var copiar = document.getElementById("copiar");
    copiar.addEventListener("click", function () {
      var lineas = [copiar.dataset.cabecera, copiar.dataset.url, ""];
      casillas.forEach(function (c) {
        lineas.push((c.checked ? "[x] " : "[ ] ") + c.dataset.punto + ". " + c.dataset.texto);
      });
      lineas.push("", cuenta.textContent);
      var texto = lineas.join("\n");
      var hecho = function () {
        var antes = copiar.textContent;
        copiar.textContent = copiar.dataset.hecho;
        setTimeout(function () { copiar.textContent = antes; }, 1800);
      };
      if (navigator.clipboard && navigator.clipboard.writeText) {
        navigator.clipboard.writeText(texto).then(hecho, function () { respaldo(texto); hecho(); });
      } else { respaldo(texto); hecho(); }
    });
    document.getElementById("borrar").addEventListener("click", function () {
      casillas.forEach(function (c) { c.checked = false; });
      guardar(); pintar();
    });
  }

  function respaldo(texto) {
    var a = document.createElement("textarea");
    a.value = texto; a.setAttribute("readonly", ""); a.style.position = "fixed"; a.style.opacity = "0";
    document.body.appendChild(a); a.select();
    try { document.execCommand("copy"); } catch (e) { /* nada que hacer */ }
    document.body.removeChild(a);
  }

  // Infografía ampliable. Sin script, el enlace abre la imagen sin más.
  var caja = document.querySelector("dialog.lightbox");
  if (caja && typeof caja.showModal === "function") {
    var grande = caja.querySelector("img");
    document.querySelectorAll("a.ampliar").forEach(function (enlace) {
      enlace.addEventListener("click", function (ev) {
        ev.preventDefault();
        grande.src = enlace.getAttribute("href");
        caja.showModal();
      });
    });
    caja.addEventListener("click", function () { caja.close(); });
  }
})();
