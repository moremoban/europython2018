from mock import patch


def test_main():
    try:
        doit('builtins.print')
    except ImportError:
        doit('__builtin__.print')


def doit(patched_module):
    with patch(patched_module) as fake_print:
        from europython2018.main import main
        main()
        fake_print.assert_called()
