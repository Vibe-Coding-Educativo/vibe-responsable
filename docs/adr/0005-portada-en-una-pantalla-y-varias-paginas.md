# 5. La portada cabe en una pantalla y la guía se reparte en varias páginas

Fecha: 2026-09-21 · Estado: aceptado

## Contexto

La primera versión de la web ponía en una sola página la presentación, las
familias de herramientas y las diez recomendaciones desplegadas: más de ocho
mil píxeles de alto. Un segundo intento, con dos columnas y las recomendaciones
en acordeones, seguía siendo una página larga con parches. El autor la rechazó:
la lista debe verse sin ese desplazamiento, la infografía y la lista de diez
tienen que estar a la vista al entrar, y la ampliación de la imagen no puede
abrirse de golpe ni a un tamaño que no cabe en la pantalla.

## Decisión

La guía se reparte en tres páginas, cada una con su archivo de Markdown:
`00-lista.md` (portada), `01-presentacion.md` y `02-herramientas.md`.

La portada es una hoja de revisión que cabe en una pantalla, también en un
portátil de 1366 × 650 píxeles útiles. A la izquierda, las diez recomendaciones
como una sola hoja pautada, con su casilla «Se cumple» y el recuento. A la
derecha, un panel que muestra el resumen gráfico y, al elegir una
recomendación, su explicación en dos columnas (el porqué y los dos niveles),
con botones para pasar a la anterior o a la siguiente. En pantallas bajas la
portada se compacta sola. En el móvil la explicación se despliega bajo su fila.
Sin JavaScript, todo el contenido queda visible, una recomendación tras otra.

La infografía se abre en un visor que la ajusta siempre a la pantalla, con una
entrada y una salida suaves, y un botón para verla a tamaño de lectura. Sus
medidas salen del SVG original, no de un número escrito a mano. El movimiento
responde solo a acciones de la persona y se anula si el dispositivo pide
reducirlo.

El aspecto sale del aula: cabecera en verde pizarra, papel neutro y dos tintas,
verde para «Lo mínimo» y azul para «Lo recomendado». La tipografía es Atkinson
Hyperlegible, diseñada por el Braille Institute para la legibilidad, alojada en
el propio repositorio con su licencia OFL. La infografía usa la misma paleta y
la misma tipografía. Las páginas de texto llevan los títulos de apartado al
margen y el cuerpo en dos columnas cuando el apartado tiene varios párrafos.

## Alternativas descartadas

- **Una sola página con acordeones y dos columnas**: reducía el alto a menos de
  la mitad, pero seguía siendo una página larga y el autor la rechazó.
- **Pestañas dentro de una página**: ocultan contenido sin que se note, y no dan
  una dirección propia a cada parte.
- **Paleta crema con acento tostado y tarjetas redondeadas**: era la del primer
  diseño y es el aspecto por defecto de una página generada; no decía nada del
  tema.
- **Tipografía del sistema**: no depende de archivos, pero no aporta identidad y
  cambia de un dispositivo a otro. La elegida pesa 53 KB en total.

## Consecuencias

El contenido está en tres archivos en lugar de uno. La portada depende de
JavaScript para el panel, aunque se degrada bien sin él. La tipografía añade
tres archivos y una licencia que acreditar. Al probar se encontraron dos fallos
que solo aparecían en un navegador: en Safari, una columna `auto` con una
imagen dentro daba al panel 4.500 píxeles de alto, y en el móvil el rótulo del
aviso de borrador se salía de la pantalla. Cualquier cambio en la portada debe
volver a comprobarse en Chromium, Firefox y WebKit, y en la pantalla de un
portátil pequeño.
