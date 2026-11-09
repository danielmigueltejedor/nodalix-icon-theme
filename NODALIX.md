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

Craft Launcher, SolidCraft y Audacity 4 portable usan el fondo de baldosa de Colloid. El resto de Craft entra con el margen del tema, sobre el lienzo de 256.
