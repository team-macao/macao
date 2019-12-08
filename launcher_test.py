import launcher


def test_print_menu(capsys):
    obj = launcher.MainMenu()
    obj.print_menu()
    captured = capsys.readouterr()
    pattern = '\nMacao\n\n' \
              '1. Continue last game\n' \
              '2. New game\n' \
              '3. Saved games\n' \
              '4. Exit game\n'
    assert captured.out == pattern

def test_select_valid_game_options():
    obj = launcher.MainMenu()







