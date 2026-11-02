"""Divide o calendário anual animado em duas faixas sem inventar contribuições."""
from pathlib import Path
import re
for name in ("github-snake", "github-snake-dark"):
    path = Path("assets") / (name + ".svg")
    raw = path.read_text()
    body = raw[raw.index(">")+1:raw.rfind("</svg>")]
    # Mantém coordenadas, keyframes e células originais; apenas muda a apresentação.
    # Renomeia IDs em cada cópia para evitar conflitos de referências no SVG.
    parts = []
    for number, x in enumerate((-16, 424)):
        fragment = body
        ids = re.findall(r"\bid=\"([^\"]+)\"", fragment)
        for old in sorted(set(ids), key=len, reverse=True):
            new = f"half{number}-{old}"
            fragment = fragment.replace(f"id=\"{old}\"", f"id=\"{new}\"").replace(f"#{old}", f"#{new}")
        parts.append(f"<svg x=\"0\" y=\"{number*192}\" width=\"440\" height=\"192\" viewBox=\"{x} -32 440 192\" overflow=\"hidden\">{fragment}</svg>")
    result = "<svg xmlns=\"http://www.w3.org/2000/svg\" width=\"880\" height=\"768\" viewBox=\"0 0 440 384\" role=\"img\"><title>Calendário real de contribuições em duas faixas ampliadas</title>"+"".join(parts)+"</svg>"
    (Path("assets") / (name + "-expanded.svg")).write_text(result)
