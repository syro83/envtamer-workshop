
import click

ascii_art = r"""
   ___   _ __   __   __ | |_    __ _   _ __ ___     ___   _ __
  / _ \ | '_ \  \ \ / / | __|  / _' | | '_ ' _ \   / _ \ | '__|
 |  __/ | | | |  \ V /  | |_  | (_| | | | | | | | |  __/ | |
  \___| |_| |_|   \_/    \__|  \__,_| |_| |_| |_|  \___| |_|
"""

print(ascii_art)

@click.Group
def cli():
    print('hello')

if __name__ == '__main__':
    cli()