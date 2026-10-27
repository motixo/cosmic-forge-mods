# COSMIC Forge Mods

The downloadable mod catalog for [COSMIC Forge](https://github.com/motixo/cosmic-forge).
Currently includes **Penumbra** and **Color**, with independent light/dark colors.
The [engine](https://github.com/motixo/cosmic-forge-engine) supplies native capabilities;
[glass shaders](https://github.com/motixo/cosmic-forge-shaders) remain separate.

Edit `catalog.json`, increase `revision`, then publish a `mods-v*` tag. GitHub Actions
packages the release. Forge 0.8+ checks every six hours while open, or immediately
through the **header update button**. Downloads are size-limited and SHA-256
verified. Updating the catalog does not activate mods or change desktop preferences.

To add a panel mod, copy an entry with a unique `id`, then customize its name,
description and controls. Supported controls: `boolean`, `integer`, `theme_color`.
Targets include `penumbra_enabled`, `gradient_height` (16–512), `panel_opacity` and
`maximized_opacity` (0–100), and `forge_colors` (theme color). Boolean/integer native
engine keys beginning with `forge_` are also supported. Each control needs a label;
integers need `min`/`max` and may include `unit` and `default`.

Optional `preset` maps declared boolean/integer keys to values and adds **Apply preset**.
Presets apply only when clicked. Set `engine_revision` to the panel revision required
by the mod; Forge blocks controls until that engine is installed. New native behavior
still needs an engine update. Catalogs contain no scripts or arbitrary file paths.
Lock screen mods await engine and app support and are not published yet.

```sh
python scripts/package_mods.py
```

GPL-3.0-only.
