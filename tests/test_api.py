# -*- coding: utf-8 -*-

from shsk_dot_claude import api


def test():
    _ = api


if __name__ == "__main__":
    from shsk_dot_claude.tests import run_cov_test

    run_cov_test(
        __file__,
        "shsk_dot_claude.api",
        preview=False,
    )
