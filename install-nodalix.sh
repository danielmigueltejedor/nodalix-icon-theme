#!/usr/bin/env bash
# Compose Nodalix Icons: Colloid application artwork; Adwaita system controls.
set -euo pipefail

ROOT="$(cd -- "$(dirname -- "${BASH_SOURCE[0]}")" && pwd)"
NAME=Nodalix-Icons
if (( EUID == 0 )); then
  DEST=/usr/share/icons
else
  DEST="${XDG_DATA_HOME:-$HOME/.local/share}/icons"
fi

usage() {
  cat <<'USAGE'
Usage: ./install-nodalix.sh [-d DESTINATION] [-n THEME_NAME]

Installs the Nodalix Colloid application icons with Adwaita providing system,
shell, action, device and status icons. The Capitaine-based cursor is packaged
separately from cursors/nodalix and selected via GNOME's cursor-theme setting.
USAGE
}
while (( $# )); do
  case "$1" in
    -d|--dest)
      if (( $# < 2 )); then echo "Missing destination" >&2; exit 2; fi
      DEST="$2"; shift 2 ;;
    -n|--name)
      if (( $# < 2 )); then echo "Missing theme name" >&2; exit 2; fi
      NAME="$2"; shift 2 ;;
    -h|--help) usage; exit 0 ;;
    *) echo "Unknown option: $1" >&2; usage >&2; exit 2 ;;
  esac
done

if [[ ! "$NAME" =~ ^[A-Za-z0-9._-]+$ || "$NAME" == Nodalix ]]; then
  echo 'Invalid theme name (Nodalix is reserved for the cursor theme).' >&2
  exit 2
fi
for source in "$ROOT/src/apps/scalable" "$ROOT/links/apps/scalable"; do
  if [[ ! -d "$source" ]]; then
    echo "Missing icon source directory: $source" >&2
    exit 1
  fi
done
mkdir -p -- "$DEST"
if [[ -L "$DEST/$NAME" || ( -e "$DEST/$NAME" && ! -d "$DEST/$NAME" ) ]]; then
  echo "Refusing to overwrite a non-directory or symlink: $DEST/$NAME" >&2
  exit 1
fi

STAGING="$(mktemp -d "$DEST/.${NAME}.tmp.XXXXXXXX")"
BACKUP=
cleanup() {
  if [[ -n "${STAGING:-}" && -d "$STAGING" ]]; then rm -rf -- "$STAGING"; fi
  if [[ -n "${BACKUP:-}" && -d "$BACKUP" ]]; then
    if [[ ! -e "$DEST/$NAME" ]]; then mv -- "$BACKUP" "$DEST/$NAME"; fi
  fi
}
trap cleanup EXIT

mkdir -p -- "$STAGING/apps/scalable"
# Preserve custom artwork when a Colloid alias has the same basename.
cp -a -- "$ROOT/src/apps/scalable/." "$STAGING/apps/scalable/"
cp -an -- "$ROOT/links/apps/scalable/." "$STAGING/apps/scalable/"
# Keep the teal application accent already used by Nodalix's Colloid package.
find "$STAGING/apps/scalable" -maxdepth 1 -type f -name '*.svg' -exec sed -i 's/#60c0f0/#4DB6AC/g' {} +

cat > "$STAGING/index.theme" <<'THEME'
[Icon Theme]
Name=Nodalix Icons
Comment=Colloid application icons with Adwaita system and GNOME Shell icons
Inherits=Adwaita,hicolor
Directories=apps/scalable

[apps/scalable]
Size=64
MinSize=16
MaxSize=512
Type=Scalable
Context=Applications
THEME

# All system/status/symbolic icons are inherited from Adwaita, never Colloid.
if command -v gtk-update-icon-cache >/dev/null 2>&1; then
  gtk-update-icon-cache -f -t "$STAGING"
fi

# mktemp makes the staging directory 0700, and a strict umask does the same to
# everything created inside it. An installed theme must be readable by every
# user, or GTK silently falls back to Adwaita for every application icon.
chmod -R u+rwX,go+rX,go-w -- "$STAGING"
# cp -a keeps the checkout owner's uid, so a root install would leave a system
# theme that user could still edit.
if [[ "$EUID" -eq 0 ]]; then chown -R 0:0 -- "$STAGING"; fi

if [[ -d "$DEST/$NAME" ]]; then
  BACKUP="$(mktemp -d "$DEST/.${NAME}.bak.XXXXXXXX")"
  rmdir -- "$BACKUP"
  mv -- "$DEST/$NAME" "$BACKUP"
fi
mv -- "$STAGING" "$DEST/$NAME"
STAGING=
if [[ -n "$BACKUP" ]]; then rm -rf -- "$BACKUP"; BACKUP=; fi
printf 'Installed %s (Colloid apps + Adwaita controls) at %s\n' "$NAME" "$DEST/$NAME"
