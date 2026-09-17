"""Izpilda SPARQL vaicājumu (.rq failu) lokālajā Oxigraph krātuvē.

Krātuves ceļš tiek ņemts no vides mainīgā OXIGRAPH_DB_PATH; tajā ir ielādēti
docs/RDF_DATA/*.ttl faili. Vajadzīga pakotne pyoxigraph>=0.5.

Katra atbilde tiek izdrukāta vienā rindā: vaicājuma mainīgo vērtības, atdalītas
ar " | ". Tekstos jaunrindas tiek saspiestas, lai rinda paliek viena.

Lietošana:
    python scripts/select_problems.py <vaicājums.rq>
"""
import argparse
import os
import sys
from pathlib import Path

from pyoxigraph import Store


def cell(term) -> str:
    """Termu attēlo kā īsu tekstu (IRI saīsina līdz pēdējai daļai)."""
    if term is None:
        return ""
    value = term.value
    if type(term).__name__ == "NamedNode":
        return value.rsplit("#", 1)[-1].rsplit("/", 1)[-1]
    return " ".join(value.split())


def main() -> None:
    parser = argparse.ArgumentParser(
        description="Izpilda .rq vaicājumu Oxigraph krātuvē (OXIGRAPH_DB_PATH).")
    parser.add_argument("query_file", help="SPARQL vaicājuma fails (.rq)")
    args = parser.parse_args()

    sys.stdout.reconfigure(encoding="utf-8")
    query_path = Path(args.query_file)
    if not query_path.exists():
        sys.exit(f"Vaicājuma fails nav atrodams: {query_path}")
    db_path = os.environ.get("OXIGRAPH_DB_PATH")
    if not db_path:
        sys.exit("Nav uzstādīts vides mainīgais OXIGRAPH_DB_PATH")

    store = Store.read_only(db_path)
    results = store.query(query_path.read_text(encoding="utf-8"))
    count = 0
    for row in results:
        print(" | ".join(cell(term) for term in row))
        count += 1
    print(f"\n{count} atbildes", file=sys.stderr)


if __name__ == "__main__":
    main()
