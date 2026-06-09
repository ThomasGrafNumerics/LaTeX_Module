---
layout: default
title: LaTeX in VS Code
nav_order: 1
---

# Anleitung für macOS

Öffnen Sie ein neues Terminal-Fenster, indem Sie zunächst die Spotlight-Suche mit Cmd + Leertaste öffnen. Geben Sie dort Terminal ein und bestätigen Sie mit Enter.

Führen Sie danach diesen Befehl aus:

```bash
brew install --cask mactex
```

# Anleitung für Windows

Öffnen Sie PowerShell als Administrator und führen Sie die folgenden Befehle nacheinander aus:

```powershell
winget install --id MiKTeX.MiKTeX
winget install --id StrawberryPerl.StrawberryPerl
```

# Extension (macOS und Windows)

Installieren Sie die VS Code-Extension `Latex Workshop` (von James Yu).

Öffnen Sie nun in VS Code die Kommando-Palette:

- **macOS:** <kbd>Cmd</kbd> + <kbd>Shift</kbd> + <kbd>P</kbd>
- **Windows:** <kbd>Ctrl</kbd> + <kbd>Shift</kbd> + <kbd>P</kbd>

Suchen Sie nach dem folgenden Befehl und wählen Sie ihn aus:
`Preferences: Open User Settings (JSON)`