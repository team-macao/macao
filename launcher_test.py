import launcher


def test_print_menu(capsys):
    obj = launcher.MainMenu()
    obj._print_menu()
    captured = capsys.readouterr()
    pattern = '\nMacao\n\n' \
              '1. Continue last game\n' \
              '2. New game\n' \
              '3. Exit game\n\n'
    assert captured.out == pattern









