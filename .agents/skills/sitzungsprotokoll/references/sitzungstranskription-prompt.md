# Sitzungstranskriptions-Prompt (NotebookLM / LLM)

Verwende diesen Prompt in **NotebookLM** (oder einem anderen LLM, das Audioaufnahmen oder lange Transkripte verarbeiten kann), um einen notariellen Bericht zu erstellen, bevor du das Ergebnis an den **Kampagnen-Archivar** (`sitzungsprotokoll`) übergibst:

1. Lade die Audioaufnahme oder das Rohtranskript der Sitzung in das Notebook hoch (bei Bedarf auf mehrere Dateien aufgeteilt).
2. *(Optional)* Lade eine kurze Textliste mit der genauen Schreibweise bereits bekannter Eigennamen (SCs, NSCs, wiederkehrende Orte) hoch, um `[?]`-Markierungen zu verringern — du kannst sie direkt aus deinem Archiv mit dem Skill `transkriptions-glossar` erzeugen.
3. Kopiere den folgenden Block und füge ihn in den Chat ein. Falls die Sitzung lang ist und das Modell mit `[FORTSETZEN AB: Abschnitt X / HH:MM:SS]` endet, bitte es, ab dieser Stelle fortzufahren, bis **Abschnitt 12 (Abdeckung)** vollständig ist.
4. Übergib den vollständigen Bericht an `/sitzungsprotokoll` (Kanal C), um das kanonische Protokoll zu erstellen und Querverweis-Aktualisierungen vorzuschlagen.

---

````markdown
# AUFGABE
Du erhältst das Transkript (oder die Aufnahme) einer Pen-&-Paper-Rollenspielsitzung.
Erstelle einen strukturierten, wortgetreuen Bericht über das, was gesagt und getan wurde.
Du kennst WEDER die Spielwelt NOCH die Charaktere, die Kampagnenregeln oder wer spricht:
alles, was du weißt, steht in der Quelle. Falls sich unter den Quellen auch ein vom SL
bereitgestelltes Glossar oder eine Namensliste befindet, verwende diese ausschließlich für
die Schreibweise der Eigennamen, ohne Fakten oder Hintergrundwissen zu übernehmen, die
nicht in der Sitzung vorgekommen sind.
Deine Ausgabe wird von einer anderen Person geprüft und neu geordnet: du sollst nicht
interpretieren, sondern wiedergeben.

# REGELN
1. Nur das, was in der Quelle steht. Keine Schlussfolgerung darf als Tatsache ausgegeben
   werden: `(Folgerung)` ist nur für offensichtliche technische Verknüpfungen zulässig
   (z. B. eindeutiger Sprecher oder eindeutiges Pronomen), niemals für ungenannte
   Beweggründe, Ursachen oder Hintergründe.
2. Korrigiere, übersetze oder „normalisiere“ Eigennamen nicht willkürlich: gib sie so
   wieder, wie sie ausgesprochen werden (außer bei belegter Schreibweise im Glossar des SL).
   Unsichere Schreibweise → `Name[?]`. Unverständliches Wort oder Passage →
   `[unverständlich 00:12:34]`.
3. Ordne jede Handlung der Person zu, die sie ausgeführt hat – mit dem Charakternamen,
   falls genannt, sonst mit dem Spielernamen. Unterscheide in `ERZÄHLUNG` objektive
   Beschreibungen des SL von Ingame-Aussagen von NSCs oder SCs (z. B.
   `„<NSC> behauptet, dass …“` ), ohne Aussagen eines Charakters zu objektiven Weltfakten
   zu machen.
4. Trenne stets drei Register und vermische sie nie:
   - `ERZÄHLUNG` = Fiktion, was in der Welt geschieht (immer in der Chronologie)
   - `TISCH` = Regeln, Würfe, Initiative, Regeldiskussionen (in der Chronologie nur, wenn
     ein wichtiges regeltechnisches Ergebnis oder eine Regel-/Kampagnenentscheidung folgt)
   - `AUSSERHALB DES SPIELS` = Witze, Pausen, Logistik, Persönliches (nicht in der
     Chronologie; nur in Abdeckung erwähnen, oder im Steckbrief bei Abwesenheiten/Logistik)
5. Dialoge: schreibe sie nicht um. Zitiere wörtlich in Anführungszeichen mit Zeitstempel
   und vergib fortlaufende IDs (`[C1]`–`[C20]`, maximal 20 Zitate) in dieser
   Prioritätsfolge: Pakte/Schwüre/Drohungen → Enthüllungen/Hinweise → Entscheidungen →
   Namen/Zahlen. Schreibe jedes wörtliche Zitat genau einmal in Abschnitt 4 beim
   Hauptelement und verweise bei weiteren beteiligten Elementen nur per ID (`[C#]`).
6. Erfinde keine Titel, Themen, Ursachen oder Motive. Was nicht gesagt wird, bleibt
   ungesagt. Fülle Lücken nicht durch erzählerische Logik.
7. Mehrere Quellen und Zeitstempel: liegen mehrere Sitzungsdateien im Notebook vor,
   stelle dem Zeitstempel den Quellennamen voran (z. B. `[Teil1 00:12:34]`). Enthält eine
   Quelle keine Zeitstempel, erfinde niemals welche: schreibe `[ohne Zeitstempel]` (oder
   den vorhandenen Abschnittsverweis, z. B. `[Teil 2]`).
8. Anti-Abbruch-Regel: ist das Transkript lang und näherst du dich dem Antwortlimit, fasse
   nicht zusammen und lasse keine Ereignisse aus; beende am Ende eines vollständigen
   Abschnitts oder einer vollständigen Tabellenzeile mit
   `[FORTSETZEN AB: Abschnitt X / HH:MM:SS]`.
9. Deutsch, gültiges Markdown. Verwende exakt die angegebenen Überschriften in derselben
   Reihenfolge. Keine Einleitung, kein Schlusskommentar, keine Bewertung.

# AUSGABE

## 1. Steckbrief
Aufzählungsliste: Kampagnenname und Sitzungsnummer (falls genannt); Teilnehmende und
deren Rolle (mit Zuordnung `Spieler → SC`, falls erklärt); realer und/oder Ingame-Zeitbezug
der Sitzung (falls genannt); Ausgangspunkt; Endpunkt; erkannte Szenen- oder Zeitsprünge;
etwaige genannte Spieldaten oder Logistik (Stufe, Erfahrung, Ressourcen, Abwesenheiten) —
nur falls ausdrücklich genannt.

## 2. Anwesende und Beteiligte
| Name (wie ausgesprochen) | Spieler / Stimme (Spielername / SL / unsicher) | Typ (SC / NSC / Kreatur / Gruppe / Sonstiges / unklar) | In Szene (ja / nein / nur erwähnt) | Einzeilige Notiz |

## 3. Chronologie
| # | Zeitstempel | Wo | Wer | Was geschieht (3–5 faktische Sätze) | Unmittelbare Folge | Register |
Kennzeichne Zeit- oder Szenensprünge mit einer gültigen Markdown-Tabellenzeile:
`| — | <Zeitstempel> | SPRUNG | — | Von <Ort/Moment A> nach <Ort/Moment B> | — | ERZÄHLUNG |`
Unter der Tabelle: **Knappe Liste** — eine Zeile pro Ereignis, maximal 20 Wörter je Zeile.

## 4. Fakten je Element
Ein Block für jeden genannten Eigennamen, vom häufigsten zum seltensten:

### <Name>
- Typ: SC / NSC / Kreatur / Ort / Fraktion-Institution / Gegenstand-Artefakt / Brauch-Fest / Ereignis / Gesetz-Norm / Konzept / unklar
- Gehörte Varianten / Aliasnamen: Liste phonetischer Schreibweisen oder alternativer Spitznamen (nur aufnehmen, falls vorhanden; besteht Zweifel, ob verschiedene Entitäten gemeint sind, getrennt halten und in `Offene Fragen` vermerken)
- Fakten: Aufzählungsliste. Ein überprüfbarer Fakt pro Punkt, mit Zeitstempel (SL-Erzählung und NSC-/SC-Aussage klar trennen).
- Beziehungen: `<Name> → <anderer Name>: was` (eine Zeile pro Beziehung)
- Ersterwähnung: Zeitstempel
- Zitate: nur sofern nach Regel 5 aufgenommen (`[C#] „...“ (Zeitstempel)` oder Verweis `[C#]`)

Wird ein Element nur ohne Details erwähnt, schreibe:
„nur namentlich erwähnt, keine Details“.

## 5. Zustandsänderungen und Hinweise
| Wer | Kategorie (Gegenstand / Zustand-Wunde / Ressource / Hinweis-Enthüllung / Position) | Genannter Fakt | Zeitstempel |
Nur ausdrückliche Fakten (erhaltene/verlorene Gegenstände, bleibende Wunden oder Zustände,
Ressourcenänderungen, Hinweise/Enthüllungen für einen SC, bedeutende Ortswechsel). Falls
keine: „Keine“.

## 6. Verpflichtungen
| Wer | Gegenüber wem | Was | Bedingung | Zeugen | Zeitstempel |
Versprechen, Drohungen, Pakte, Schulden, Abmachungen, Schwüre. Falls keine: „Keine“.

## 7. Zahlen
| Angabe | Wert | Kontext | Zeitstempel |
Jede ausgesprochene Zahl: Münzen, Preise, Schaden, Trefferpunkte, Entfernungen, Mengen,
Alter, Daten, Prozentsätze, Zeitspannen.

## 8. Zeitangaben
| Ausdruck (wörtlich) | Kontext / zugehöriges Ereignis | Zeitstempel |
Jede Zeitangabe: „gestern“, „drei Tage“, „letztes Jahr“, Jahreszeiten, Jahrestage, Fristen,
„vor langer Zeit“.

## 9. Offene Fragen
Nummerierte Liste. Formulierung: „Es wird nicht gesagt, ob / wer / wann / warum …“ +
Zeitstempel der Stelle, an der die Angabe zu erwarten wäre (einschließlich Zweifel, ob
phonetische Varianten dieselbe oder verschiedene Entitäten bezeichnen).

## 10. Widersprüche
Nur quellinterne Unstimmigkeiten: `A behauptet X (Zeitstempel)` / `B behauptet Y (Zeitstempel)`.
Keine Korrektur, nur Meldung. Falls keine: „Keine“.

## 11. Datenblock
Ein einziger gültiger YAML-Block ohne Kommentare. Nur Schlüssel mit echtem Inhalt aufnehmen.
Beschreibende Felder (`was`, `fakt`, `fakten`) knapp halten (eine Zeile je Eintrag).

```yaml
sitzung:
  kampagne: ""
  nummer: ""
  zeitbezug: ""
  beginn: ""
  ende: ""
beteiligte:
  - name: ""
    spieler_stimme: ""
    typ: ""
    in_szene: ""
    notiz: ""
ereignisse:
  - reihenfolge: 1
    zeitstempel: ""
    ort: ""
    akteure: []
    was: ""
    folge: ""
    register: ""
elemente:
  - name: ""
    typ: ""
    varianten: []
    fakten: []
    beziehungen: []
    ersterwaehnung: ""
    zitate: []
zustandsaenderungen_hinweise:
  - wer: ""
    kategorie: ""
    fakt: ""
    zeitstempel: ""
verpflichtungen:
  - wer: ""
    gegenueber: ""
    was: ""
    bedingung: ""
    zeugen: []
    zeitstempel: ""
zahlen:
  - angabe: ""
    wert: ""
    kontext: ""
    zeitstempel: ""
zeitangaben:
  - ausdruck: ""
    kontext: ""
    zeitstempel: ""
offene_fragen:
  - frage: ""
    zeitstempel: ""
widersprueche:
  - aussage_a: ""
    zeitstempel_a: ""
    aussage_b: ""
    zeitstempel_b: ""
```

## 12. Abdeckung
| Intervall | Inhalt | Qualität (klar / verworren / unverständlich) |
````
