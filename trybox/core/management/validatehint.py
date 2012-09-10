from trybox.core import Context
import json

def handle(args):
    try:
        module = __import__(args.tutorial)
        hint = module.tutorial[args.step-1][args.hint-1]
        response = hint.validate(Context(args.venv, args.repository))
        print json.dumps({'success': not bool(response['error']), 'response': response})
    except Exception as e:
        print json.dumps({'success': False, 'response': e.message })


def validatehint(sp_base):
    p_hint = sp_base.add_parser('validatehint', help='Validate hint')
    p_hint.set_defaults(handle=handle)

    p_hint.add_argument('step', type=int, help='Step base-1')
    p_hint.add_argument('hint', type=int, help='Step base-1')