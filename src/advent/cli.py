import importlib

import click


@click.command()
@click.argument("day")
@click.option("--input-file", default=None)
def cli(day: str, input_file: str):
    """Runner for AOC 2023 solutions"""
    if day.lower() == "all":
        mods = [f"day{nday:02d}" for nday in range(1, 26)]
    else:
        mods = [f"day{int(day):02d}"]

    for module_name in mods:
        print(f"\n~~~ {module_name} ~~~")
        try:
            mod = importlib.import_module(f".{module_name}", "advent.solutions")
        except ImportError:
            print(f"{module_name} not available yet")

        _input_file = input_file or f"data/{module_name}.txt"
        mod.part1(_input_file)
        mod.part2(_input_file)


if __name__ == "__main__":
    cli()
