from source.sample4 import save_dict
import os
import json

def test_ve_dict(tmpdir,capsys):
    filepath = os.path.join(tmpdir,"test.json")
    _dict = { "a":1,"b":1}
    save_dict(_dict,filepath)
    assert json.load(open(filepath,"r"))== _dict
    captured = capsys.readouterr()
    print(captured)
    assert captured.out == "saved\n"