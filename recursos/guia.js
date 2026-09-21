// Comportamiento de la guía. Todo ocurre en el navegador: las marcas se guardan
// en localStorage y no se envía nada a ningún servidor. Sin este script la página
// se lee entera, con cada recomendación desplegada bajo su título.
(function () {
  "use strict";
  document.documentElement.classList.add("js");
  var ESCRITORIO = window.matchMedia("(min-width: 62rem)");
  var REDUCIDO = window.matchMedia("(prefers-reduced-motion: reduce)");

  /* ---------- Lista y panel ---------- */
  var panel = document.querySelector(".panel");
  var resumen = document.querySelector(".resumen");
  var puntos = Array.prototype.slice.call(document.querySelectorAll(".punto"));
  var detalles = {};
  var activo = 0;

  puntos.forEach(function (li) {
    var d = li.querySelector(".detalle") || document.getElementById("detalle-" + li.id.split("-")[1]);
    detalles[li.id.split("-")[1]] = d;
  });

  // En escritorio las explicaciones viven en el panel; en móvil, bajo su fila.
  function colocar() {
    puntos.forEach(function (li) {
      var n = li.id.split("-")[1], d = detalles[n];
      if (ESCRITORIO.matches) { if (d.parentNode !== panel) { panel.appendChild(d); } }
      else if (d.parentNode !== li) { li.appendChild(d); }
    });
    pintar();
  }

  function pintar() {
    puntos.forEach(function (li) {
      var n = +li.id.split("-")[1], es = n === activo;
      li.classList.toggle("activo", es);
      li.querySelector(".abrir").setAttribute("aria-expanded", es ? "true" : "false");
      detalles[n].classList.toggle("visible", es);
    });
    if (resumen) { resumen.classList.toggle("visible", !activo); }
  }

  function seleccionar(n, opciones) {
    opciones = opciones || {};
    n = +n || 0;
    if (n === activo && opciones.alternar) { n = 0; }
    activo = n;
    pintar();
    var destino = n ? "#recomendacion-" + n : location.pathname + location.search;
    if (opciones.historial !== false) { try { history.replaceState(null, "", destino); } catch (e) { /* file:// */ } }
    if (n && opciones.foco) {
      var t = detalles[n].querySelector("h2");
      if (ESCRITORIO.matches) { t.focus({ preventScroll: true }); }
      else { setTimeout(function () { puntos[n - 1].scrollIntoView({ block: "nearest", behavior: REDUCIDO.matches ? "auto" : "smooth" }); }, 340); }
    }
  }

  if (panel && puntos.length) {
    puntos.forEach(function (li, i) {
      var enlace = li.querySelector(".abrir");
      enlace.setAttribute("role", "button");
      enlace.addEventListener("click", function (ev) { ev.preventDefault(); seleccionar(i + 1, { alternar: true, foco: true }); });
      enlace.addEventListener("keydown", function (ev) {
        if (ev.key === " ") { ev.preventDefault(); enlace.click(); }
        if (ev.key === "ArrowDown" || ev.key === "ArrowUp") {
          ev.preventDefault();
          var j = Math.max(0, Math.min(puntos.length - 1, i + (ev.key === "ArrowDown" ? 1 : -1)));
          puntos[j].querySelector(".abrir").focus();
        }
      });
    });
    document.querySelectorAll(".paso").forEach(function (b) {
      b.addEventListener("click", function () { seleccionar(b.dataset.ir, { foco: true }); });
    });
    document.querySelectorAll(".cerrar-detalle").forEach(function (b) {
      b.addEventListener("click", function () {
        var n = activo; seleccionar(0);
        if (n) { puntos[n - 1].querySelector(".abrir").focus(); }
      });
    });
    var desdeHash = function () {
      var m = /^#(?:recomendacion|detalle)-(\d+)$/.exec(location.hash);
      if (m && detalles[m[1]]) { seleccionar(m[1], { historial: false }); }
    };
    window.addEventListener("hashchange", desdeHash);
    if (ESCRITORIO.addEventListener) { ESCRITORIO.addEventListener("change", colocar); } else { ESCRITORIO.addListener(colocar); }
    colocar();
    desdeHash();
    window.addEventListener("beforeprint", function () { document.documentElement.classList.remove("js"); });
    window.addEventListener("afterprint", function () { document.documentElement.classList.add("js"); });
  }

  /* ---------- Casillas ---------- */
  var CLAVE = "vibe-responsable:lista";
  var casillas = Array.prototype.slice.call(document.querySelectorAll(".casilla input"));
  var cuenta = document.querySelector(".cuenta");

  function leer() { try { return JSON.parse(localStorage.getItem(CLAVE)) || {}; } catch (e) { return {}; } }
  function guardar() {
    var estado = {};
    casillas.forEach(function (c) { if (c.checked) { estado[c.dataset.punto] = true; } });
    try { localStorage.setItem(CLAVE, JSON.stringify(estado)); } catch (e) { /* sin almacenamiento */ }
  }
  function contar() {
    if (!cuenta) { return; }
    var n = casillas.filter(function (c) { return c.checked; }).length;
    cuenta.textContent = cuenta.dataset.plantilla.replace("{n}", n).replace("{total}", cuenta.dataset.total);
  }
  function respaldo(texto) {
    var a = document.createElement("textarea");
    a.value = texto; a.setAttribute("readonly", ""); a.style.position = "fixed"; a.style.opacity = "0";
    document.body.appendChild(a); a.select();
    try { document.execCommand("copy"); } catch (e) { /* nada que hacer */ }
    document.body.removeChild(a);
  }

  if (cuenta && casillas.length) {
    var estado = leer();
    casillas.forEach(function (c) {
      c.checked = !!estado[c.dataset.punto];
      c.addEventListener("change", function () { guardar(); contar(); });
    });
    contar();
    var copiar = document.getElementById("copiar");
    copiar.addEventListener("click", function () {
      var lineas = [copiar.dataset.cabecera, copiar.dataset.url, ""];
      casillas.forEach(function (c) { lineas.push((c.checked ? "[x] " : "[ ] ") + c.dataset.punto + ". " + c.dataset.texto); });
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
      guardar(); contar();
    });
  }

  /* ---------- Visor de la infografía ---------- */
  var visor = document.querySelector("dialog.visor");
  if (visor && typeof visor.showModal === "function") {
    var imagen = visor.querySelector("img");
    var zoom = visor.querySelector(".visor-zoom");
    var lienzo = visor.querySelector(".visor-lienzo");
    var origen = null;

    var alternar = function () {
      var acercado = visor.classList.toggle("acercado");
      zoom.textContent = acercado ? zoom.dataset.alejar : zoom.dataset.acercar;
      if (!acercado) { lienzo.scrollTo({ top: 0, behavior: REDUCIDO.matches ? "auto" : "smooth" }); }
    };
    var cerrar = function () {
      if (!visor.open || visor.classList.contains("saliendo")) { return; }
      if (REDUCIDO.matches) { visor.close(); return; }
      visor.classList.add("saliendo");
      var fin = function () { visor.classList.remove("saliendo"); visor.close(); };
      visor.addEventListener("animationend", fin, { once: true });
      setTimeout(function () { if (visor.classList.contains("saliendo")) { fin(); } }, 320);
    };

    document.querySelectorAll("a.ampliar").forEach(function (enlace) {
      enlace.addEventListener("click", function (ev) {
        ev.preventDefault();
        origen = enlace;
        imagen.src = enlace.getAttribute("href");
        visor.classList.remove("acercado");
        zoom.textContent = zoom.dataset.acercar;
        visor.showModal();
        lienzo.scrollTop = 0;
      });
    });
    zoom.addEventListener("click", alternar);
    imagen.addEventListener("click", alternar);
    visor.querySelector(".visor-cerrar").addEventListener("click", cerrar);
    lienzo.addEventListener("click", function (ev) { if (ev.target === lienzo) { cerrar(); } });
    visor.addEventListener("cancel", function (ev) { ev.preventDefault(); cerrar(); });
    visor.addEventListener("close", function () { if (origen) { origen.focus(); } });
  }
})();
