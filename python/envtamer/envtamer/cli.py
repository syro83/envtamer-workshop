
import click

ascii_art = r"""
   ___   _ __   __   __ | |_    __ _   _ __ ___     ___   _ __
  / _ \ | '_ \  \ \ / / | __|  / _' | | '_ ' _ \   / _ \ | '__|
 |  __/ | | | |  \ V /  | |_  | (_| | | | | | | | |  __/ | |
  \___| |_| |_|   \_/    \__|  \__,_| |_| |_| |_|  \___| |_|
"""

print(ascii_art)

@click.command()
@click.option('--count', default=1, help='Number of greetings.')
@click.option('--name', prompt='Your name',
              help='The person to greet.')

# @click.Group
def cli(count, name):
    """Simple program that greets NAME for a total of COUNT times."""
    for x in range(count):
        click.echo(f"Hello {name}!")

if __name__ == '__main__':
    cli()