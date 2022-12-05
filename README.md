# Dots of War

Kombinace *tower-defense* a *dota* herních mechanismů. Vnikněte do základny protivníka a ubraňte svou!

## Struktura repozitáře

- `bin` binární verze hry
- `data` assety hry (ikony, obrázky)
- `doc` dokumentace, návody, pomůcky
- `src` zdrojové soubory v Pythonu

## Build distribuční verze

0. Je třeba mít nainstalovaný nástroj [`pyinstaller`](https://pyinstaller.org/en/stable/index.html)
1. Ve složce `bin/` spusťte dávkový soubor `build.bat`
2. Vygeneruje se složka `bin/dist/` s binární verzí aplikace
3. Hra se spouští souborem `dots_of_war.exe` ve složce `bin/dist/`

