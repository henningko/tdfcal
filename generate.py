#!/usr/bin/env python3
"""Generate one .ics file per stage of the Tour de France 2026."""
import os

OUT = os.path.join(os.path.dirname(__file__), "stages")
os.makedirs(OUT, exist_ok=True)

# stage: (date YYYYMMDD, start, finish, mountain?, queen?, [(peak, category)])
STAGES = {
    1:  ("20260704", "Barcelona", "Barcelona", False, False,
         [("Côte de Montjuïc (1.1 km, 5.1%)", "Cat 4")]),
    2:  ("20260705", "Tarragona", "Barcelona", False, False,
         [("Côte du Château de Montjuïc (1.6 km, 9.3%)", "Cat 3")]),
    3:  ("20260706", "Granollers", "Les Angles", True, False,
         [("Collada de Toses (9.3 km, 6.5%)", "Cat 1"),
          ("Col du Calvaire (14.9 km, 4.1%)", "Cat 2"),
          ("Les Angles (summit finish)", "Cat 2")]),
    4:  ("20260707", "Carcassonne", "Foix", False, False,
         [("Col de Montségur (6.9 km, 6.6%)", "Cat 2")]),
    5:  ("20260708", "Lannemezan", "Pau", False, False, []),
    6:  ("20260709", "Pau", "Gavarnie-Gèdre", True, False,
         [("Col d'Aspin", "Cat 1"),
          ("Col du Tourmalet (17 km, 7.3%)", "HC"),
          ("Gavarnie-Gèdre (18.7 km, 4%, summit finish)", "Cat 2")]),
    7:  ("20260710", "Hagetmau", "Bordeaux", False, False, []),
    8:  ("20260711", "Périgueux", "Bergerac", False, False, []),
    9:  ("20260712", "Malemort", "Ussel", False, False,
         [("Suc au May (3.8 km, 7.7%)", "Cat 2"),
          ("Côte des Gardes (2.2 km, 4.8%)", "Cat 3")]),
    10: ("20260714", "Aurillac", "Le Lioran", True, False,
         [("Col de Pertus (4.4 km, 8.5%)", "Cat 2"),
          ("Puy Mary / Pas de Peyrol (7.8 km, 6%)", "Cat 1"),
          ("Le Lioran (summit finish)", "Cat 2")]),
    11: ("20260715", "Vichy", "Nevers", False, False,
         [("Côte de Billy-Chévannes (1.5 km, 6%)", "Cat 4")]),
    12: ("20260716", "Magny-Cours", "Chalon-sur-Saône", False, False,
         [("Côte de Montagny-lès-Buxy (2.6 km, 3.9%)", "Cat 4")]),
    13: ("20260717", "Dole", "Belfort", False, False,
         [("Ballon d'Alsace (8.7 km, 6.9%)", "Cat 1")]),
    14: ("20260718", "Mulhouse", "Le Markstein Fellering", True, False,
         [("Grand Ballon (21.5 km)", "Cat 1"),
          ("Col du Haag (11.2 km, 7.3%)", "Cat 1"),
          ("Le Markstein (summit finish)", "Cat 2")]),
    15: ("20260719", "Champagnole", "Plateau de Solaison", True, False,
         [("Col de la Croisette (7.6 km, 8.8%)", "Cat 1"),
          ("Plateau de Solaison (11.6 km, 8.9%, summit finish)", "HC")]),
    16: ("20260721", "Évian-les-Bains", "Thonon-les-Bains", False, False,
         [("Côte de Larringes (9.4 km, 4.3%)", "Cat 3")]),
    17: ("20260722", "Chambéry", "Voiron", False, False,
         [("Col des Prés", "Cat 2"), ("Col de Couz", "Cat 3")]),
    18: ("20260723", "Voiron", "Orcières-Merlette", True, False,
         [("Monteynard (9.7 km, 5%)", "Cat 2"),
          ("Orcières-Merlette (7.1 km, 6.7%, summit finish)", "Cat 1")]),
    19: ("20260724", "Gap", "Alpe d'Huez", True, False,
         [("Col Bayard", "Cat 2"),
          ("Col du Noyer (7.3 km, 8.2%)", "Cat 1"),
          ("Col d'Ornon", "Cat 2"),
          ("Alpe d'Huez (13.9 km, 8%, summit finish)", "HC")]),
    20: ("20260725", "Le Bourg-d'Oisans", "Alpe d'Huez", True, True,
         [("Col de la Croix de Fer (24 km, 5.2%)", "HC"),
          ("Col du Télégraphe", "Cat 1"),
          ("Col du Galibier (17 km, 6.8%, 2642 m)", "HC"),
          ("Col de Sarenne (12.9 km, 7.3%)", "Cat 1"),
          ("Alpe d'Huez (summit finish)", "HC")]),
    21: ("20260726", "Thoiry", "Paris (Champs-Élysées)", False, False,
         [("Montmartre (×3 ascents)", "Cat 4")]),
}


def esc(s):
    return s.replace("\\", "\\\\").replace(",", "\\,").replace(";", "\\;").replace("\n", "\\n")


def next_day(d):
    import datetime
    dt = datetime.date(int(d[:4]), int(d[4:6]), int(d[6:8])) + datetime.timedelta(days=1)
    return dt.strftime("%Y%m%d")


# stage -> time-trial type
TT = {1: "TTT", 16: "ITT"}


def vevent(num, date, start, finish, mountain, queen, peaks):
    title = f"{start} - {finish}"
    if num in TT:
        title += f" ({TT[num]})"
    icons = "".join(
        ([" ⏱️"] if num in TT else [])
        + ([" ⛰️"] if mountain else [])
        + ([" 👑"] if queen else [])
    )
    title = ("[TdF]" + icons + " " + title).strip()

    if peaks:
        desc_lines = [f"{p} — {cat}" for p, cat in peaks]
        desc = "Climbs:\\n" + "\\n".join(esc(line) for line in desc_lines)
    else:
        desc = "No categorised climbs"
    desc += f"\\n\\nhttps://www.procyclingstats.com/race/tour-de-france/2026/stage-{num}"

    return [
        "BEGIN:VEVENT",
        f"UID:tdf2026-stage{num:02d}@tdfcal",
        "DTSTAMP:20260617T000000Z",
        f"DTSTART;VALUE=DATE:{date}",
        f"DTEND;VALUE=DATE:{next_day(date)}",
        f"SUMMARY:{esc(title)}",
        f"LOCATION:{esc(finish)}",
        f"URL:https://www.procyclingstats.com/race/tour-de-france/2026/stage-{num}",
        f"DESCRIPTION:{desc}",
        "END:VEVENT",
    ]


HEADER = [
    "BEGIN:VCALENDAR",
    "VERSION:2.0",
    "PRODID:-//tdfcal//Tour de France 2026//EN",
    "CALSCALE:GREGORIAN",
    "METHOD:PUBLISH",
    "X-WR-CALNAME:Tour de France 2026",
    "X-WR-CALDESC:All 21 stages of the Tour de France 2026",
    "REFRESH-INTERVAL;VALUE=DURATION:PT12H",
    "X-PUBLISHED-TTL:PT12H",
]

# Individual per-stage files
for num, args in STAGES.items():
    ics = "\r\n".join(HEADER + vevent(num, *args) + ["END:VCALENDAR", ""])
    with open(os.path.join(OUT, f"stage-{num:02d}.ics"), "w", encoding="utf-8") as f:
        f.write(ics)

# Combined file with all stages
lines = list(HEADER)
for num, args in STAGES.items():
    lines += vevent(num, *args)
lines += ["END:VCALENDAR", ""]
with open(os.path.join(os.path.dirname(__file__), "tdf2026.ics"), "w", encoding="utf-8") as f:
    f.write("\r\n".join(lines))

print(f"Wrote {len(STAGES)} stage files to {OUT} and combined tdf2026.ics")
