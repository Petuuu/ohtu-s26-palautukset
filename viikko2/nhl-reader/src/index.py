from rich.console import Console
from rich.prompt import Prompt
from rich.table import Table
from player_reader import PlayerReader
from player_stats import PlayerStats


def create_table(season, nat, players):
    table = Table(title=f"Season {season} players from {nat}")

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


def handle_io(console, season, stats):
    while True:
        nat = Prompt.ask("Nationality [#27F5EB](set empty or 'q' to exit)")
        if not nat or nat == "q":
            break

        players = stats.top_scorers_by_nationality(nat)
        table = create_table(season, nat, players)
        console.print(table)


def main():
    console = Console()
    season = Prompt.ask("Season [#27F5EB](YYYY-YY)")
    url = f"https://studies.cs.helsinki.fi/nhlstats/{season}/players"
    stats = PlayerStats(PlayerReader(url, console))
    handle_io(Console(), season, stats)


if __name__ == "__main__":
    main()
