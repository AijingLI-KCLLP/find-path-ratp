from algorithms import A_star_with_time
from stations import get_station_by_name, get_station_by_id

def trajet(start_name,end_name, algorithme=A_star_with_time):
    start_station = get_station_by_name(start_name)
    end_station = get_station_by_name(end_name)

    if start_station is None:
        return f"❌ Station de départ inconnue: {start_name}"
    if end_station is None:
        return f"❌ Station d'arrivée inconnue: {end_name}"

    result = algorithme(start_station["id"], end_station["id"])
    if isinstance(result, tuple) and len(result) == 2:
        path, total_time = result
    else:
        path, total_time = result, None

    if not path:
        return f"❌ Aucun trajet trouvé entre {start_name} et {end_name}."

    stations = [get_station_by_id(station_id) for station_id in path]
    if any(station is None for station in stations):
        return "❌ Chemin invalide: station introuvable."

    if len(stations) == 1:
        return f"✅ Vous êtes déjà à {start_name}."

    def line_between(a, b, preferred=None):
        common = sorted(set(a["lines"]).intersection(b["lines"]))
        if not common:
            return "?"
        if preferred in common:
            return preferred
        return common[0]

    segments = []
    current_line = line_between(stations[0], stations[1], None)
    current_names = [stations[0]["name"], stations[1]["name"]]

    for i in range(1, len(stations) - 1):
        a = stations[i]
        b = stations[i + 1]
        edge_line = line_between(a, b, current_line)

        if edge_line == current_line:
            current_names.append(b["name"])
        else:
            segments.append((current_line, current_names))
            current_line = edge_line
            current_names = [a["name"], b["name"]]

    segments.append((current_line, current_names))

    lines = [f"🚇 Trajet {start_name} -> {end_name}"]
    if total_time is not None:
        lines.append(f"⏱️ Temps total estimé: {total_time:.1f} min")
    lines.append(f"🔢 Correspondances: {max(0, len(segments)-1)}")

    for i, (line, station_names) in enumerate(segments):
        if i > 0:
            prev_line = segments[i - 1][0]
            change_station = station_names[0]
            lines.append(f"🔁 Correspondance à {change_station}: ligne {prev_line} -> ligne {line}")
        lines.append(f"🟢 Ligne {line} : 🔲 {' 🔲 '.join(station_names)}")

    lines.append("🏁 Arrivée")

    return "\n".join(lines)


def main():
    print("🗺️Planificateur de trajet à Paris (ctrl + c pour quitter)")
    while True:
        start_name = input("Saisir le nom de station de départ : ").strip()
        end_name = input("Saisir le nom de station d'arrivée : ").strip()

        resultat = trajet(start_name, end_name)
        print("\n" + resultat + "\n")

        if resultat.startswith("❌"):
            continue

        again = input("Faire une autre recherche ? (o/n): ").strip()
        if again not in {"o", "y"}:
            print("Au revoir 👋")
            break

if __name__ == "__main__":
    main()
