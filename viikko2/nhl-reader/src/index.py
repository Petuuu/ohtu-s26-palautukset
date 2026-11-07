from rich.console import Console
from rich.prompt import Prompt
from rich.table import Table
from player_reader import PlayerReader
from player_stats import PlayerStats


def create_table(season, description, players):
    table = Table(title=f"Season {season} players from {description}")

    table.add_column("name")
    table.add_column("teams")
    table.add_column("goals", justify="right")
    table.add_column("assists", justify="right")
    table.add_column("points", justify="right")

    for p in players[:15]:
        table.add_row(
            f"[#008080]{p.name}",
            f"[purple]{p.teams}",
            f"[green]{p.goals}",
            f"[green]{p.assists}",
            f"[green]{p.points}",
        )

    return table


def search_players(stats, search_by, value):
    if search_by == "nationality":
        return stats.top_scorers_by_nationality(value)
    return stats.top_scorers_by_team(value)


def show_search_results(console, season, stats, search_by):
    value = Prompt.ask(f"{search_by.capitalize()}")
    players = search_players(stats, search_by, value)
    table = create_table(season, value, players)
    console.print(table)


def handle_io(console, season, stats):
    while True:
        search_by = Prompt.ask("Search by [#27F5EB](nationality/team, or 'q' to exit)")
        if not search_by or search_by == "q":
            break

        if search_by not in ("nationality", "team"):
            console.print("[red]Choose either 'nationality' or 'team'.")
            continue

        show_search_results(console, season, stats, search_by)


def main():
    console = Console()
    season = Prompt.ask("Season [#27F5EB](YYYY-YY)")
    url = f"https://studies.cs.helsinki.fi/nhlstats/{season}/players"
    stats = PlayerStats(PlayerReader(url, console))
    handle_io(Console(), season, stats)


if __name__ == "__main__":
    main()
