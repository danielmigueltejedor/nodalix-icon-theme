# Nodalix Icon Theme

Fork de [Colloid](https://github.com/vinceliuice/Colloid-icon-theme) para el escritorio Nodalix. Los iconos propios del sistema viven en este repositorio.

## Dónde meter un icono nuevo

Copia el SVG en `src/apps/scalable/` con el mismo nombre que el campo `Icon=` del `.desktop`, sin extensión.

Ejemplo: si el escritorio dice `Icon=org.audacityteam.Audacity4portable`, el archivo es `src/apps/scalable/org.audacityteam.Audacity4portable.svg`.

`./install.sh` copia esa carpeta tal cual. La variante oscura enlaza los iconos de aplicaciones a la clara, así que basta con dejarlos una vez en `scalable`.

## Instalar la variante del sistema

```sh
./install.sh -n NodalixColloid -t teal
```

Eso genera `NodalixColloid-Teal`, `NodalixColloid-Teal-Light` y `NodalixColloid-Teal-Dark` en `~/.local/share/icons`.

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
