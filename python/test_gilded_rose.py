from gilded_rose import main
from pathlib import Path


def test_main(capsys):
    main()

    (out, err) = capsys.readouterr()
    assert not err
    golden_text = Path("../golden-master/expected-output.txt")
    assert out == golden_text.read_text()

