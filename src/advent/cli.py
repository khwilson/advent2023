import importlib

import click


@click.command()
@click.argument("day")
@click.option("--input-file", default=None)
def cli(day: str, input_file: str):
    """Runner for AOC 2023 solutions"""
    module_name = f"day{int(day):02d}"
    mod = importlib.import_module(f".{module_name}", "advent.solutions")

    input_file = input_file or f"data/{module_name}.txt"
    mod.part1(input_file)
    mod.part2(input_file)


if __name__ == "__main__":
    cli()
