import click

from change.core import change

PROJECT_NAME = "change"
VERSION = "0.1"
context_settings = {"help_option_names": ["-h", "--help"]}

@click.group(context_settings=context_settings)
@click.version_option(prog_name=PROJECT_NAME.capitalize(), version=VERSION)
@click.pass_context
def cli(ctx):
    pass

@click.group(name="commands")
def commands_group():
    pass

@commands_group.command(name="makechange")
@click.option(
    "--amount",
    prompt="Amount: ",
    help="Creates change for dollar and cents value:  i.e. 1.34",
)
def make_change(amount):
    """Gives Correct Change"""

    result = change(float(amount))
    click.echo(click.style(f"Change for {amount}:", fg="red"))
    for correct_change in result:
        for num, coin in correct_change.items():
            click.echo(click.style(f"{coin}: {num}", fg="green"))

cli.add_command(commands_group)
main = cli
