# COSMIC Forge Mods

Downloadable mod catalog for [COSMIC Forge](https://github.com/motixo/cosmic-forge).
Includes **Penumbra**, **Color**, and the Lock screen **Wallpaper** and **Media player widget** mods.
Requires Forge 0.9+; each mod declares its native engine revision.
[Shaders](https://github.com/motixo/cosmic-forge-shaders) are distributed separately.

[Install COSMIC Forge](https://github.com/motixo/cosmic-forge#install) with the
one-line installer or native DEB, RPM and Arch packages. Enable mods in the app;
install required engines from **Settings → Patches**.

Edit `catalog.json`, increase `revision`, then publish a `mods-v*` tag.
The header update button checks effects, mods and engine releases together.
Catalogs are verified JSON data; updates never install engines or enable mods.

Controls: `boolean`, bounded `integer`, panel `theme_color`, and lock-screen `image`.
See [panel](panel/README.md) and [lock screen](lock-screen/README.md) for supported keys.
Boolean/integer `forge_` keys allow new engine settings. Optional `preset` values
must target declared compatible controls and apply only when clicked.

```sh
python scripts/package_mods.py
```

GPL-3.0-only.
