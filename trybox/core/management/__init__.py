import argparse

def execute_from_command_line(args=None):

    p_base = argparse.ArgumentParser(description="trybox", add_help=True)

    p_base.add_argument("venv",
        help="Virtual environment path",
        action="store",
        metavar='<venv-path>')
    p_base.add_argument('repository',
        help="Repository path",
        action="store",
        metavar='<repo-path>')
    p_base.add_argument("tutorial",
        help="Tutorial",
        action="store",
        metavar='<tutorial-package>')

    sp_base = p_base.add_subparsers(help='commands')

    from validatehint import validatehint
    validatehint(sp_base)

    from gettutorial import gettutorial
    gettutorial(sp_base)

    r = p_base.parse_args(args)
    r.handle(r)
