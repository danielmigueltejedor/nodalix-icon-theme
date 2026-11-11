# Nodalix Icon Theme

Tema híbrido predeterminado de Nodalix OS, mantenido en un único repositorio:

- **GNOME Shell, controles, Wi-Fi, Bluetooth, estados y Ajustes:** iconos originales de **Adwaita**, heredados mediante `Inherits=Adwaita,hicolor`.
- **Aplicaciones:** [Colloid](https://github.com/vinceliuice/Colloid-icon-theme), más los SVG específicos de Nodalix en `src/apps/scalable/` y sus alias en `links/apps/scalable/`.
- **Cursor:** [Capitaine](https://github.com/keeferrourke/capitaine-cursors) personalizado, con fuentes en `cursors/nodalix/`. El cursor se elige mediante la configuración independiente `cursor-theme=Nodalix`, no con `icon-theme`.

La instalación principal **no copia iconos de acciones, estados, dispositivos o símbolos de Colloid**. Adwaita se actualiza con el sistema, sin duplicar sus archivos en este repositorio.

## Dónde meter un icono nuevo

Copia el SVG en `src/apps/scalable/` con el mismo nombre que el campo `Icon=` del `.desktop`, sin extensión.

Ejemplo: si el escritorio dice `Icon=org.audacityteam.Audacity4portable`, el archivo es `src/apps/scalable/org.audacityteam.Audacity4portable.svg`.

`./install.sh` copia esa carpeta tal cual. La variante oscura enlaza los iconos de aplicaciones a la clara, así que basta con dejarlos una vez en `scalable`.

## Instalar el tema híbrido de Nodalix

```sh
./install.sh
# Equivalente: ./install-nodalix.sh
gsettings set org.gnome.desktop.interface icon-theme 'Nodalix-Icons'
```

El instalador crea `~/.local/share/icons/Nodalix-Icons` (o `/usr/share/icons/Nodalix-Icons` con permisos de root). Solo incluye `apps/scalable` y hereda todo lo demás de Adwaita. No instala cursores: se gestionan de forma independiente desde `cursors/nodalix/`.

Para mantener compatibilidad con paquetes históricos, `./install.sh -n Colloid -t teal -b` conserva la instalación completa de Colloid, **pero no debe seleccionarse como tema global de Nodalix**.

## Iconos de Nodalix

| Aplicación | Archivo |
| --- | --- |
| Craft Launcher | `ai.storyteller.artcraft-launcher.svg` |
| Craft Anything | `ai.storyteller.craft-anything.svg` |
| FigCraft | `ai.storyteller.figcraft.svg` |
| MaterialCraft | `ai.storyteller.materialcraft.svg` |
| SoundCraft | `ai.storyteller.soundcraft.svg` |
| TextureCraft | `ai.storyteller.texturecraft.svg` |
| Audacity 4 portable | `org.audacityteam.Audacity4portable.svg` |

Craft Launcher y Audacity 4 portable usan el fondo de baldosa de Colloid. El resto entra con el margen del tema, sobre el lienzo de 256. Las apps Nodalia tienen su propia tabla abajo.

## Aplicaciones Nodalia

Cada app Nodalia lleva el retrato de una figura histórica en blanco y negro sobre su color. Aquí se ajustan a la retícula de Colloid: baldosa de 224 px dentro del lienzo de 256 (16 px de margen), radio de 51,5 px y la misma sombra suave, medidas sobre los propios iconos de Colloid. El archivo usa el `Icon=` del `.desktop` de cada app y hay un alias con su nombre corto.

| Aplicación | Archivo | Alias |
| --- | --- | --- |
| Brújula | `org.gnome.Epiphany.svg` | `brujula` |
| Celdas | `ai.storyteller.gridcraft.svg` | `celdas` |
| Forja | `ai.storyteller.cadcraft.svg` | `forja` |
| Lámina | `ai.storyteller.deckcraft.svg` | `lamina` |
| Letra | `ai.storyteller.wordcraft.svg` | `letra` |
| Lienzo | `ai.storyteller.photocraft.svg` | `lienzo` |
| Luz | `ai.storyteller.lightcraft.svg` | `luz` |
| Papel | `ai.storyteller.pdfcraft.svg` | `papel` |
| Pliego | `ai.storyteller.designcraft.svg` | `pliego` |
| Pluma | `ai.storyteller.vectorcraft.svg` | `pluma` |
| Pulso | `ai.storyteller.effectcraft.svg` | `pulso` |
| Toma | `ai.storyteller.filmcraft.svg` | `toma` |
| Torno | `io.tangencylabs.solidcraft.svg` | `torno` |
| Vinilo | `dev.danielmiguelt.Vinilo.svg` | `vinilo` |
| Vortia | `vortia.svg` | |

Para regenerar uno cuando cambie el retrato de la app:

```sh
tools/nodalia-app-icon.py ../vinilo/data/icons/source/dev.danielmiguelt.Vinilo.png \
  dev.danielmiguelt.Vinilo \
  --comment "Vinilo app icon: portrait of Ludwig van Beethoven (Nodalia icon family), fitted to the Colloid tile."
```

El segundo argumento es el `Icon=` del `.desktop`; escribe `src/apps/scalable/<nombre>.svg`. Acepta el retrato a sangre (el `*-1024.png` de la app) o una baldosa con su propio margen, que recorta antes. Solo necesita Pillow.

## Aplicaciones de Nodalix

| Aplicación | Archivo | Alias |
| --- | --- | --- |
| Nodalix Store (Tienda) | `os.nodalix.Store.svg` | `nodalix-store`, `os.nodalix.Store.Devel` |

El icono de Nodalix Store es propio: una bolsa blanca con una «N» sobre una baldosa turquesa-azul del mismo tamaño y radio que el resto de iconos de aplicación. Sustituye al icono de Bazaar (`io.github.kolunmi.Bazaar.svg`), que se mantiene solo para el Bazaar original y ya no se usa para la tienda de Nodalix.
