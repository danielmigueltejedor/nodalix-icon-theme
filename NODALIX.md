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
| CADCraft | `ai.storyteller.cadcraft.svg` |
| Craft Anything | `ai.storyteller.craft-anything.svg` |
| DeckCraft | `ai.storyteller.deckcraft.svg` |
| DesignCraft | `ai.storyteller.designcraft.svg` |
| EffectCraft | `ai.storyteller.effectcraft.svg` |
| FigCraft | `ai.storyteller.figcraft.svg` |
| FilmCraft | `ai.storyteller.filmcraft.svg` |
| GridCraft | `ai.storyteller.gridcraft.svg` |
| LightCraft | `ai.storyteller.lightcraft.svg` |
| MaterialCraft | `ai.storyteller.materialcraft.svg` |
| PDFCraft | `ai.storyteller.pdfcraft.svg` |
| PhotoCraft | `ai.storyteller.photocraft.svg` |
| SoundCraft | `ai.storyteller.soundcraft.svg` |
| TextureCraft | `ai.storyteller.texturecraft.svg` |
| VectorCraft | `ai.storyteller.vectorcraft.svg` |
| WordCraft | `ai.storyteller.wordcraft.svg` |
| SolidCraft | `io.tangencylabs.solidcraft.svg` |
| Audacity 4 portable | `org.audacityteam.Audacity4portable.svg` |

Craft Launcher, SolidCraft y Audacity 4 portable usan el fondo de baldosa de Colloid. El resto de Craft entra con el margen del tema, sobre el lienzo de 256. Las apps Nodalia tienen su propia tabla abajo.

## Aplicaciones Nodalia

Cada app Nodalia lleva el retrato de una figura histórica en blanco y negro sobre su color. Aquí se ajustan a la retícula de Colloid: baldosa de 224 px dentro del lienzo de 256 (16 px de margen), radio de 51,5 px y la misma sombra suave, medidas sobre los propios iconos de Colloid. Son apps propias, separadas de las Craft: los iconos `ai.storyteller.*` e `io.tangencylabs.solidcraft` siguen siendo los de las Craft, y el de cada app Nodalia va con su propio nombre, `dev.danielmiguelt.<App>`, que es el `Icon=` de su `.desktop`. El ID de la app sigue siendo el Craft, salvo en Vinilo, Vortia y Brújula, así que en Flatpak, que solo exporta iconos con el nombre del ID, se ve el icono Craft.

| Aplicación | Archivo | Alias |
| --- | --- | --- |
| Brújula | `org.gnome.Epiphany.svg` | `brujula` |
| Celdas | `dev.danielmiguelt.Celdas.svg` | `celdas` |
| Forja | `dev.danielmiguelt.Forja.svg` | `forja` |
| Lámina | `dev.danielmiguelt.Lamina.svg` | `lamina` |
| Letra | `dev.danielmiguelt.Letra.svg` | `letra` |
| Lienzo | `dev.danielmiguelt.Lienzo.svg` | `lienzo` |
| Luz | `dev.danielmiguelt.Luz.svg` | `luz` |
| Papel | `dev.danielmiguelt.Papel.svg` | `papel` |
| Pliego | `dev.danielmiguelt.Pliego.svg` | `pliego` |
| Pluma | `dev.danielmiguelt.Pluma.svg` | `pluma` |
| Pulso | `dev.danielmiguelt.Pulso.svg` | `pulso` |
| Toma | `dev.danielmiguelt.Toma.svg` | `toma` |
| Torno | `dev.danielmiguelt.Torno.svg` | `torno` |
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
| Monitor del sistema | `os.nodalix.Monitor.svg` | — |
| Ajustes | `os.nodalix.Settings.svg` | — |
| Archivos (Archivador) | `os.nodalix.Archivador.svg` | — |

El icono de Nodalix Store es propio: una bolsa blanca con una «N» sobre una baldosa turquesa-azul del mismo tamaño y radio que el resto de iconos de aplicación. Sustituye al icono de Bazaar (`io.github.kolunmi.Bazaar.svg`), que se mantiene solo para el Bazaar original y ya no se usa para la tienda de Nodalix.

Los iconos de Monitor del sistema (una gráfica con trazas de CPU y memoria sobre dos medidores), de Ajustes (tres controles deslizantes) y de Archivos (una carpeta con papeles) son originales, con la baldosa de Colloid y la paleta del icono de la Tienda. Son los que usan los `.desktop` de las apps propias de Nodalix; los iconos de GNOME System Monitor y GNOME Settings no cambian.
