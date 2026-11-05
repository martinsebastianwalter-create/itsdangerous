from .signer import Signer


def probe_edit_1793891278():
    return Signer("k").sign("v")


def probe_caller_1793891278():
    return probe_edit_1793891278()
