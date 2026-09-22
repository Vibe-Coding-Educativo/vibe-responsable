// Comportamiento de la guía. No guarda ni envía ningún dato. Sin este script la
// página se lee entera, con cada recomendación desplegada bajo su título.
(function () {
  "use strict";
  document.documentElement.classList.add("js");
  var ESCRITORIO = window.matchMedia("(min-width: 62rem)");
  var REDUCIDO = window.matchMedia("(prefers-reduced-motion: reduce)");

  /* ---------- Imprimir ---------- */
  var imprimir = document.querySelector(".imprimir");
  if (imprimir) {
    imprimir.addEventListener("click", function () { window.print(); });
  }

  /* ---------- Lista y panel ---------- */
  var panel = document.querySelector(".panel");
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
    // En escritorio el panel muestra siempre una recomendación; en móvil empiezan todas plegadas
    if (ESCRITORIO.matches && !activo) { activo = 1; }
    pintar();
  }

  function pintar() {
    puntos.forEach(function (li) {
      var n = +li.id.split("-")[1], es = n === activo;
      li.classList.toggle("activo", es);
      li.querySelector(".abrir").setAttribute("aria-expanded", es ? "true" : "false");
      detalles[n].classList.toggle("visible", es);
    });
  }

  function seleccionar(n, opciones) {
    opciones = opciones || {};
    n = +n || 0;
    if (n === activo && opciones.alternar && !ESCRITORIO.matches) { n = 0; }
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

  /* ---------- Copiar los textos para la IA ---------- */
  document.querySelectorAll(".copiar").forEach(function (boton) {
    boton.addEventListener("click", function () {
      var texto = boton.closest(".copiable").querySelector("pre").textContent;
      var hecho = function () {
        var antes = boton.textContent;
        boton.textContent = boton.dataset.hecho;
        setTimeout(function () { boton.textContent = antes; }, 1800);
      };
      var respaldo = function () {
        var a = document.createElement("textarea");
        a.value = texto; a.setAttribute("readonly", ""); a.style.position = "fixed"; a.style.opacity = "0";
        document.body.appendChild(a); a.select();
        try { document.execCommand("copy"); } catch (e) { /* nada que hacer */ }
        document.body.removeChild(a);
      };
      if (navigator.clipboard && navigator.clipboard.writeText) {
        navigator.clipboard.writeText(texto).then(hecho, function () { respaldo(); hecho(); });
      } else { respaldo(); hecho(); }
    });
  });

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
