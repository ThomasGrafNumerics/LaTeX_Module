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

<!-- # LaTeX-Extension in VS Code (macOS und Windows)

Installieren Sie die VS Code-Extension `Latex Workshop` (von James Yu). -->

<!-- Öffnen Sie nun in VS Code die Kommando-Palette:

- **macOS:** <kbd>Cmd</kbd> + <kbd>Shift</kbd> + <kbd>P</kbd>
- **Windows:** <kbd>Ctrl</kbd> + <kbd>Shift</kbd> + <kbd>P</kbd>

Suchen Sie nach dem folgenden Befehl und wählen Sie ihn aus:
`Preferences: Open User Settings (JSON)`

Kopiere Sie dort folgendes hinein:

```json
{% include_relative recipes.json %}
``` -->

# Kompilieren des Projekts

Sie können nun jedes LaTeX-Projekt kompilieren. Navigieren Sie dazu im Terminal in das Verzeichnis, in dem sich Ihre `main.tex` befindet, und führen Sie die folgenden Befehle aus:

```bash
echo "Step 1 of 5: lualatex"; lualatex -synctex=1 -interaction=nonstopmode main.tex; echo "Step 2 of 5: biber"; biber main; echo "Step 3 of 5: makeglossaries"; makeglossaries main; echo "Step 4 of 5: lualatex"; lualatex -synctex=1 -interaction=nonstopmode main.tex; echo "Step 5 of 5: lualatex"; lualatex -synctex=1 main.tex; echo "Compilation complete"
```