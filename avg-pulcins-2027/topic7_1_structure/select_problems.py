"""Atlasa 5.-7. klases uzdevumus tematam "Atrisinājumu struktūras".

Vaicājums tiek izpildīts lokālajā Oxigraph krātuvē (vide: OXIGRAPH_DB_PATH),
kurā ielādēti docs/RDF_DATA/*.ttl faili. Vajadzīga pakotne pyoxigraph>=0.5.

Lietošana:
    python select_problems.py            # tikai uzdevumu ID (pa vienam rindā)
    python select_problems.py --verbose  # ID, questionType, domēns, garums, teksts
"""
import os
import sys

from pyoxigraph import Store

QUERY = """
PREFIX eliozo: <http://www.dudajevagatve.lv/eliozo#>
SELECT ?problemID ?questionType ?domain (STRLEN(?text) AS ?len) ?text
WHERE {
  ?p a eliozo:Problem ;
     eliozo:problemID ?problemID ;
     eliozo:problemGrade ?grade ;
     eliozo:problemYear ?year ;
     eliozo:questionType ?questionType ;
     eliozo:domain ?domain ;
     eliozo:_readingDifficulty "low" ;
     eliozo:problemText ?text .
  FILTER (LANGMATCHES(LANG(?text), "lv"))
  FILTER (?grade >= 5 && ?grade <= 7)
  FILTER (?year >= 2011 && ?year <= 2026)
  FILTER (?questionType != "ShortAnswer")
  FILTER (?domain != "Geom")
  FILTER (STRLEN(?text) <= 220)
  FILTER (!CONTAINS(?text, "![") && !CONTAINS(?text, "att.") && !CONTAINS(?text, "zīm.")
          && !CONTAINS(?text, "frac") && !CONTAINS(?text, "sqrt") && !CONTAINS(?text, "^"))
}
ORDER BY ?questionType ?len ?problemID
"""


def main():
    verbose = "--verbose" in sys.argv
    sys.stdout.reconfigure(encoding="utf-8")
    store = Store.read_only(os.environ["OXIGRAPH_DB_PATH"])
    seen = set()
    for row in store.query(QUERY):
        problem_id = row["problemID"].value
        if verbose:
            text = " ".join(row["text"].value.split())
            print(problem_id, row["questionType"].value, row["domain"].value,
                  row["len"].value, "|", text)
        elif problem_id not in seen:
            print(problem_id)
        seen.add(problem_id)


if __name__ == "__main__":
    main()
