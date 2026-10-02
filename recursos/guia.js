// Comportamiento de la guía. No envía ningún dato; lo único que guarda en el
// navegador es el tema claro u oscuro, y solo si se elige uno distinto al del
// dispositivo. Sin este script la página se lee entera, con cada recomendación
// desplegada bajo su título.
(function () {
  "use strict";
  document.documentElement.classList.add("js");
  var ESCRITORIO = window.matchMedia("(min-width: 62rem)");
  var REDUCIDO = window.matchMedia("(prefers-reduced-motion: reduce)");

  /* ---------- Cabecera fija ---------- */
  // La cabecera se queda arriba al bajar. Su altura se guarda en --alto-cabecera
  // para que los enlaces internos no dejen el destino debajo de ella. En el
  // móvil, donde ocupa mucho, se oculta al bajar y vuelve en cuanto se sube.
  var cabecera = document.querySelector(".pizarra");
  if (cabecera) {
    var MOVIL = window.matchMedia("(max-width: 40rem)");
    var ultima = window.scrollY;
    var medir = function () {
      document.documentElement.style.setProperty("--alto-cabecera", cabecera.offsetHeight + "px");
    };
    medir();
    window.addEventListener("resize", medir);
    window.addEventListener("scroll", function () {
      var y = window.scrollY;
      if (Math.abs(y - ultima) < 8) { return; }
      var menuAbierto = cabecera.querySelector('[aria-expanded="true"]');
      var ocultar = MOVIL.matches && y > ultima && y > cabecera.offsetHeight && !menuAbierto;
      cabecera.classList.toggle("escondida", ocultar);
      ultima = y;
    }, { passive: true });
    // Con el teclado, la cabecera reaparece al llegar a uno de sus controles.
    cabecera.addEventListener("focusin", function () { cabecera.classList.remove("escondida"); });
  }

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

  /* ---------- Menús de la cabecera ---------- */
  // El botón de idiomas despliega los idiomas de la guía, que llevan a la misma página
  // en cada uno; el de la impresora, imprimir la página o descargar la guía completa en
  // PDF. Cada menú se cierra al elegir, al pulsar fuera o con Escape.
  document.querySelectorAll(".desplegable").forEach(function (caja) {
    var boton = caja.querySelector("button[aria-haspopup]");
    var menu = caja.querySelector(".menu");
    if (!boton || !menu) { return; }
    var abrirMenu = function (abierto) {
      menu.hidden = !abierto;
      boton.setAttribute("aria-expanded", abierto ? "true" : "false");
      if (abierto) { (menu.querySelector("[aria-current]") || menu.querySelector("[role=menuitem]")).focus(); }
    };
    boton.addEventListener("click", function () { abrirMenu(menu.hidden); });
    var imprimir = menu.querySelector(".menu-imprimir");
    if (imprimir) { imprimir.addEventListener("click", function () { abrirMenu(false); window.print(); }); }
    menu.querySelectorAll("a").forEach(function (a) { a.addEventListener("click", function () { abrirMenu(false); }); });
    document.addEventListener("click", function (ev) {
      if (!menu.hidden && !boton.contains(ev.target) && !menu.contains(ev.target)) { abrirMenu(false); }
    });
    document.addEventListener("keydown", function (ev) {
      if (ev.key === "Escape" && !menu.hidden) { abrirMenu(false); boton.focus(); }
    });
  });

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
      var rotulo = boton.querySelector("span") || boton;   // con icono, cambia solo el rótulo
      var hecho = function () {
        var antes = rotulo.textContent;
        rotulo.textContent = boton.dataset.hecho;
        setTimeout(function () { rotulo.textContent = antes; }, 1800);
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

  /* ---------- Portada: la infografía, como mucho, del alto del texto ---------- */
  // El CSS le da el alto que deja la pantalla; si así queda más alta que el texto de al lado,
  // se reduce lo que sobra, para que el espacio libre quede al final de la página y no en medio.
  // Al estrecharse la imagen se ensancha el texto y baja su alto, así que se repite hasta ajustar.
  var entrada = document.querySelector(".pagina-presentacion .entrada");
  if (entrada) {
    var tarjeta = entrada.querySelector(".tarjeta");
    var miniatura = entrada.querySelector(".tarjeta .miniatura");
    var ancha = window.matchMedia("(min-width: 62rem)");
    var ajustarImagen = function () {
      tarjeta.style.removeProperty("--mini-al");
      if (!ancha.matches) { return; }
      entrada.classList.add("midiendo");
      for (var i = 0; i < 4; i++) {
        var pasos = entrada.querySelector(".utiliza").getBoundingClientRect().bottom;
        var boton = entrada.querySelector(".ir-guia").getBoundingClientRect().bottom;
        var sobra = boton - pasos;
        if (sobra < 2) { break; }
        tarjeta.style.setProperty("--mini-al", (miniatura.getBoundingClientRect().height - sobra) + "px");
      }
      entrada.classList.remove("midiendo");
    };
    ajustarImagen();
    window.addEventListener("resize", ajustarImagen);
    if (document.fonts && document.fonts.ready) { document.fonts.ready.then(ajustarImagen); }
  }

  /* ---------- Ventanas de la portada con cada archivo para la IA ---------- */
  // Los enlaces de «Cómo empezar» abren su ventana; sin JavaScript o sin <dialog>, llevan a la
  // página de instrucciones. Se cierran con la X, con Escape o al pulsar fuera.
  document.querySelectorAll("a.abrir-ventana").forEach(function (enlace) {
    var ventana = document.getElementById(enlace.dataset.ventana);
    if (!ventana || typeof ventana.showModal !== "function") { return; }
    // La ventana de la animación carga el vídeo al abrirse y lo pone en marcha con la misma pulsación,
    // que es lo que piden los navegadores para que suene; al cerrarse, lo detiene.
    var video = ventana.querySelector("video[data-src]");
    var otraVez = ventana.querySelector(".volver-a-ver");
    function desdeElPrincipio() {
      if (otraVez) { otraVez.hidden = true; }
      video.currentTime = 0;
      var marcha = video.play();
      if (marcha && marcha.catch) { marcha.catch(function () {}); }
    }
    // Al terminar, un botón bien visible para volver a verla: el del reproductor apenas se distingue.
    if (video && otraVez) {
      video.addEventListener("ended", function () { otraVez.hidden = false; otraVez.focus(); });
      video.addEventListener("play", function () { otraVez.hidden = true; });
      otraVez.addEventListener("click", desdeElPrincipio);
    }
    enlace.addEventListener("click", function (ev) {
      ev.preventDefault();
      ventana.showModal();
      if (video) {
        if (!video.getAttribute("src")) { video.src = video.dataset.src; }
        desdeElPrincipio();
      }
    });
    ventana.querySelector(".ventana-cerrar").addEventListener("click", function () { ventana.close(); });
    ventana.addEventListener("click", function (ev) { if (ev.target === ventana) { ventana.close(); } });
    ventana.addEventListener("close", function () {
      if (video) { video.pause(); }
      enlace.focus();
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

  /* ---------- Apartados que han cambiado de página ---------- */
  // Un enlace antiguo a un apartado que ya no está en esta página (data-mudado,
  // con el ancla antigua y su destino nuevo) lleva a su sitio actual.
  var mudado = document.querySelector("[data-mudado]");
  if (mudado) {
    var destinos = JSON.parse(mudado.getAttribute("data-mudado"));
    var mudar = function () {
      var ancla = decodeURIComponent(window.location.hash.slice(1));
      if (Object.prototype.hasOwnProperty.call(destinos, ancla)) { window.location.replace(destinos[ancla]); }
    };
    mudar();
    window.addEventListener("hashchange", mudar);
  }

  /* ---------- Resultado de la evaluación VCER ---------- */
  // La mención del pie de un recurso evaluado enlaza a vcer.html con su resultado
  // en la dirección: r (recomendable, mejorable o no-recomendable), p (el
  // porcentaje, opcional), f (año y mes, 2026-10), v (la versión), t (el título)
  // y u (la dirección del recurso). Nada se envía ni se guarda: los datos solo
  // se leen de la dirección y se escriben como texto. Si r no es válido, la
  // página se muestra sin el recuadro; cualquier otro dato que no lo sea se omite.
  var recuadro = document.querySelector(".resultado-vcer");
  if (recuadro) {
    var datos = new URLSearchParams(window.location.search);
    var fila = /^(recomendable|mejorable|no-recomendable)$/.test(datos.get("r") || "") &&
      document.querySelector('.resultados-vcer tr[data-resultado="' + datos.get("r") + '"]');
    if (fila) {
      var textos = JSON.parse(recuadro.querySelector(".rv-textos").textContent);
      var limpio = function (nombre, max) {
        var valor = (datos.get(nombre) || "").replace(/\s+/g, " ").trim();
        return valor.length <= max ? valor : "";
      };
      var poner = function (plantilla, valores) {
        return plantilla.replace(/\{([^}]+)\}/g, function (_, clave) { return valores[clave]; });
      };
      var titulo = limpio("t", 200);
      var version = limpio("v", 30);
      var direccion = limpio("u", 300);
      if (!/^https?:\/\/[^\s]+$/i.test(direccion)) { direccion = ""; }
      var porcentaje = /^\d{1,3}$/.test(datos.get("p") || "") && Number(datos.get("p")) <= 100 ? Number(datos.get("p")) : null;
      var mes = /^(\d{4})-(\d{2})$/.exec(datos.get("f") || "");
      var fecha = mes && Number(mes[2]) >= 1 && Number(mes[2]) <= 12 ?
        poner(textos.fecha, { "mes": textos.meses[Number(mes[2]) - 1], "año": mes[1] }) : "";
      var recurso = poner(textos.recurso[(titulo ? "t" : "") + (version ? "v" : "")], { t: titulo, v: version });
      recuadro.querySelector(".rv-frase").textContent = poner(textos.frase, {
        recurso: recurso, u: direccion ? " (" + direccion + ")" : "", fecha: fecha });
      recuadro.querySelector(".rv-nombre").textContent = fila.cells[0].textContent.trim();
      recuadro.querySelector(".rv-significado").textContent = fila.cells[2].textContent.trim();
      recuadro.querySelector(".rv-nota").textContent = textos.nota;
      recuadro.dataset.resultado = datos.get("r");
      if (porcentaje !== null) {
        recuadro.querySelector(".rv-pct").textContent = poner(textos.pct, { p: porcentaje });
        recuadro.querySelector(".rv-relleno").style.width = porcentaje + "%";
      } else {
        recuadro.querySelector(".rv-barra").hidden = true;
      }
      fila.classList.add("actual");
      recuadro.hidden = false;
    }
  }
})();
