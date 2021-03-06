#!/usr/bin/env python3
# PYTHON_ARGCOMPLETE_OK

import os
import sys

from srblib import Colour

from . import __version__, __mod_name__
from .scheduler import Scheduler
from .parser import get_parser
from .configurations import default_output_xlsx_path
from .verifier import Verifier

def main():
    args = get_parser()
    if args.version:
        print(__mod_name__+'=='+__version__)
        sys.exit()

    if args.vr:
        Verifier.verify_room_list(args.vr)
        sys.exit()
    if args.vs:
        Verifier.verify_schedule_list(args.vs)
        sys.exit()
    if args.vt:
        Verifier.verify_teachers_list(args.vt)
        sys.exit()

    global default_output_xlsx_path
    if args.output: default_output_xlsx_path = args.output

    if args.reserved < 0:
        Colour.print('Reserved number should not be negative', Colour.RED)
        sys.exit(1)

    try:
        Scheduler().schedule(default_output_xlsx_path,int(args.reserved))
        Colour.print('Output written to : ' + Colour.END + default_output_xlsx_path, Colour.BLUE)
    except KeyboardInterrupt:
        Colour.print('Exiting on KeyboardInterrupt ...',Colour.YELLOW)

if(__name__=="__main__"):
    main()
