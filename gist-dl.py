#!/usr/bin/env python3
import typer
from gist_dl.gist.gist import Gist


def main():
    gist = Gist()
    gist.greeting()

    command = gist.get_command()
    gist.process_command(command.split(" "))


if __name__ == "__main__":
    typer.run(main)
