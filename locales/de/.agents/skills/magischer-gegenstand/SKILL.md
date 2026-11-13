---
name: magischer-gegenstand
description: "Use when: besondere magische Gegenstände, Relikte und Artefakte der Spielwelt gemäß dem kanonischen Vier-Abschnitte-Standard (technisches Datenblatt, Herstellung, Mechaniken, Rechtsstatus) erfassen oder formatieren."
argument-hint: "Name des magischen Gegenstands und einzutragende oder zu aktualisierende Details"
user-invocable: true
disable-model-invocation: false
---

# Skill: Verwaltung besonderer magischer Gegenstände (`magischer-gegenstand`)

Dieser Skill regelt die formelle Katalogisierung von Artefakten, Relikten und arkanen Fokussen im Band `08_besondere_magische_gegenstaende/` gemäß dem Strukturmodell in [gegenstand-vorlage](./references/gegenstand-vorlage.md).

---

## 1. Grundsätze der Erfassung

- **Einbettung in die Welt**: Dokumentiere Herkunft, Seltenheit sowie den rechtlichen oder wirtschaftlichen Status des Gegenstands nach den Regeln der Spielwelt (freier Handel, Zunftlizenz, Staats-/Adelsmonopol oder verbotene Schmuggelware).
- **Keine Erfindungen**: Nennt der SL nur mechanische Werte oder das Aussehen, erfinde niemals fiktive Herkunftsgeschichten oder Träger: erfrage fehlende Angaben oder füge `[VOM_SL_ZU_DEFINIEREN: ...]` ein.
- **Badge-Nachverfolgung**: Jeder Bogen enthält das Badge:
  `> 🛡️ *Geprüft: JJJJ-MM-TT | Geändert: JJJJ-MM-TT*`

---

## 2. Operatives Verfahren

1. **Informationsbeschaffung**:
   Sind die Angaben des SL unvollständig, stelle eine strukturierte Rückfrage (über das interaktive Fragewerkzeug der Umgebung wie `vscode_askQuestions` oder `AskUserQuestion`, falls verfügbar; sonst im Chat):
   - **`kategorie`**: Optionen (*Magische Waffe*, *Musikinstrument / Fokus*, *Antikes Relikt / Artefakt*, *Magische Apparatur / Gerät*, *Seltener Verbrauchsgegenstand*).
   - **`traeger`**: Aktueller Träger (Auswahl aus erfassten SCs oder Freitext für einen NSC/Ort).
   - **`rechtsstatus`**: Optionen (*Rechtmäßiger freier Besitz*, *Lizenz- oder Monopolpflichtig*, *Schmuggelware / Verbotenes Relikt*, *Sonstiges*).
   - **`kraefte_mechaniken`**: D&D-5e-Spielmechaniken und sensorische Resonanzen (Freitext).

2. **Erstellung der Datei**:
   Speichere den Bogen unter `08_besondere_magische_gegenstaende/<Gegenstandsname>.md` mithilfe der Standardvorlage.

3. **Aktualisierung des Bandindex**:
   Ergänze den Eintrag mit Kategorie, Resonanz und Träger in der Tabelle bzw. Liste unter `08_besondere_magische_gegenstaende/README.md`.

4. **Querverlinkung zum Träger**:
   Gehört der Gegenstand einem SC, aktualisiere das Modul `04_ausruestung_und_faehigkeiten.md` im Dossier dieses SC mit einem Link auf den neuen Gegenstandsbogen.
