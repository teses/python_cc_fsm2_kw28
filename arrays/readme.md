# List, Tuple, Set, Dictionary und Frozenset
 
| Eigenschaft | List | Tuple | Dictionary                                         | Set                                                  | Frozenset                                        |
|---|---|---|----------------------------------------------------|------------------------------------------------------|--------------------------------------------------|
| Schreibweise | `[1, 2, 3]` | `(1, 2, 3)` | `{"name": "Max"}`                                  | `{1, 2, 3}`                                          | `frozenset({1, 2, 3})`                           |
| Zugriff | über Index: `0, 1, 2 ...` | über Index: `0, 1, 2 ...` | über Schlüssel                                     | kein Zugriff über Index                              | kein Zugriff über Index                          |
| Reihenfolge | geordnet | geordnet | Einfügereihenfolge bleibt erhalten                 | keine verlässliche Reihenfolge<br/> <= v3.6  unordered <br/> >= 3.7    ordered                      | keine verlässliche Reihenfolge                   |
| Veränderbar | ja | nein | ja                                                 | ja: Elemente können hinzugefügt oder entfernt werden | nein                                             |
| Doppelte Werte | erlaubt | erlaubt | Schlüssel nicht doppelt, Werte dürfen doppelt sein | nicht erlaubt                                        | nicht erlaubt                                    |
| Typischer Einsatz | veränderbare Sammlung | feste Sammlung | Schlüssel-Wert-Zuordnung                           | eindeutige Werte ohne bestimmter Reihenfolge         | unveränderliche Menge. Eine Art konstantes Array |

# Infos in Englisch

There are four collection data types in the Python programming language:

- List is a collection which is ordered and changeable. Allows duplicate members.
- Tuple is a collection which is ordered and unchangeable. Allows duplicate members.
- Set is a collection which is unordered, unchangeable*, and unindexed. No duplicate members.
- Dictionary is a collection which is ordered** and changeable. No duplicate members.
