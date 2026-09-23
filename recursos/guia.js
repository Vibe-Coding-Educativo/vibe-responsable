// Comportamiento de la guía. No envía ningún dato; lo único que guarda en el
// navegador es el tema claro u oscuro, y solo si se elige uno distinto al del
// dispositivo. Sin este script la página se lee entera, con cada recomendación
// desplegada bajo su título.
(function () {
  "use strict";
  document.documentElement.classList.add("js");
  var ESCRITORIO = window.matchMedia("(min-width: 62rem)");
  var REDUCIDO = window.matchMedia("(prefers-reduced-motion: reduce)");

  /* ---------- Tema claro u oscuro ---------- */
  // El aspecto sigue al del dispositivo mientras no se elija otra cosa. Si se
  // elige justo el que ya trae el dispositivo, se vuelve a seguirlo. La clave
  // es la misma que usa el arranque en <head> (CLAVE_TEMA en construir.py).
  var CLAVE_TEMA = "vibe-responsable:tema";
  var sistemaOscuro = window.matchMedia("(prefers-color-scheme: dark)");
  var guardar = function (valor) {
    try { if (valor === null) { localStorage.removeItem(CLAVE_TEMA); } else { localStorage.setItem(CLAVE_TEMA, valor); } } catch (e) {}
  };
  var leer = function () { try { return localStorage.getItem(CLAVE_TEMA); } catch (e) { return null; } };
  var aplicarTema = function (oscuro, manual) {
    document.documentElement.dataset.theme = oscuro ? "dark" : "light";
    if (manual) { guardar(oscuro === sistemaOscuro.matches ? null : (oscuro ? "dark" : "light")); }
  };
  var tema = document.querySelector(".tema");
  if (tema) {
    tema.addEventListener("click", function () { aplicarTema(document.documentElement.dataset.theme !== "dark", true); });
  }
  sistemaOscuro.addEventListener("change", function (ev) { if (leer() === null) { aplicarTema(ev.matches); } });

  /* ---------- Imprimir o descargar ---------- */
  // El botón de la impresora despliega un menú con dos opciones: imprimir la
  // página o descargar la guía completa en PDF. Se cierra al elegir, al pulsar
  // fuera o con Escape.
  var imprimir = document.querySelector(".imprimir");
  var menu = document.querySelector(".menu");
  if (imprimir && menu) {
    var abrirMenu = function (abierto) {
      menu.hidden = !abierto;
      imprimir.setAttribute("aria-expanded", abierto ? "true" : "false");
      if (abierto) { menu.querySelector("[role=menuitem]").focus(); }
    };
    imprimir.addEventListener("click", function () { abrirMenu(menu.hidden); });
    menu.querySelector(".menu-imprimir").addEventListener("click", function () { abrirMenu(false); window.print(); });
    menu.querySelector("a").addEventListener("click", function () { abrirMenu(false); });
    document.addEventListener("click", function (ev) {
      if (!menu.hidden && !imprimir.contains(ev.target) && !menu.contains(ev.target)) { abrirMenu(false); }
    });
    document.addEventListener("keydown", function (ev) {
      if (ev.key === "Escape" && !menu.hidden) { abrirMenu(false); imprimir.focus(); }
    });
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

  /* ---------- Archivos para la IA plegados ---------- */
  // Al imprimir se despliegan, para que el papel lleve el texto; después vuelven como estaban
  var plegados = [];
  window.addEventListener("beforeprint", function () {
    plegados = Array.prototype.filter.call(document.querySelectorAll("details.archivo-ia"), function (d) { return !d.open; });
    plegados.forEach(function (d) { d.open = true; });
  });
  window.addEventListener("afterprint", function () { plegados.forEach(function (d) { d.open = false; }); });

  // Abrir y cerrar con un movimiento suave de la altura, salvo con movimiento reducido
  document.querySelectorAll("details.archivo-ia").forEach(function (d) {
    var resumen = d.querySelector("summary"), animacion = null;
    resumen.addEventListener("click", function (ev) {
      if (REDUCIDO.matches || !d.animate) { return; }
      ev.preventDefault();
      var abrir = !d.open || (animacion && d.dataset.cerrando === "1");
      var desde = d.getBoundingClientRect().height;
      if (animacion) { animacion.cancel(); }
      if (abrir) { d.open = true; }
      d.dataset.cerrando = abrir ? "0" : "1";
      var hasta = abrir ? d.scrollHeight : resumen.getBoundingClientRect().height + (d.offsetHeight - d.clientHeight);
      d.style.overflow = "hidden";
      animacion = d.animate({ height: [desde + "px", hasta + "px"] },
        { duration: Math.min(450, 180 + Math.abs(hasta - desde) / 6), easing: "cubic-bezier(0.2, 0, 0, 1)" });
      animacion.onfinish = function () {
        if (!abrir) { d.open = false; }
        d.style.overflow = ""; d.dataset.cerrando = ""; animacion = null;
      };
      animacion.oncancel = function () { d.style.overflow = ""; };
    });
  });

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
