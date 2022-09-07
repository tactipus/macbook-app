import json
from main import *

AddNewForm.text_input = "Your mom"
DisorderBanisherApp().run()

f = open('./data.json')

data = json.load(f)

def test_add_new():
    assert len(data) == 1

f.close()