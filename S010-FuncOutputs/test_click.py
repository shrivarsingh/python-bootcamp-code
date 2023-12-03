import click
 
click.echo('Continue? [yn] ', nl=False)
c = click.getchar()
click.echo()
if c == b'y':
    click.echo('We will go on')
elif c == b'n':
    click.echo('Abort!')
else:
    click.echo('Invalid input :(')
