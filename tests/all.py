# -*- coding: utf-8 -*-

if __name__ == "__main__":
    from shsk_dot_claude.tests import run_cov_test

    run_cov_test(
        __file__,
        "shsk_dot_claude",
        is_folder=True,
        preview=False,
    )
