# Lock screen mods

Requires COSMIC Forge 0.9+ and the Forge lock screen engine revision 1.

- **Wallpaper:** select a PNG, JPEG or WebP. Forge validates and keeps an independent PNG copy under the standard `cosmic-lockscreen` data directory; **Use desktop wallpaper** resets the override without deleting images.
- **Media player widget:** an independent opt-in toggle for Veil's MPRIS widget. It shows playing/paused apps and available artwork, with previous/play/pause/next controls. Monitoring and artwork tasks stop when disabled or unlocked. Optional `curl` and `bubblewrap` enable sandboxed covers; playback still works without covers.

Catalog section: `lock_screen`. `wallpaper` uses the `image` control and `media_enabled` uses `boolean`. Additional supported engine settings may use boolean/integer `forge_` controls. Catalogs contain data only and cannot install an engine or write authentication settings.

Install or restore the locker from **Settings → Engine → Lock screen**. COSMIC Settings and the system login greeter are unchanged. Images, desktop backgrounds, preferences and recovery data survive Restore. After engine changes, sign out and back in.
