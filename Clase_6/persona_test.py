import unittest

from persona import Persona
from unittest.mock import patch

class TestPersona(unittest.TestCase):
    def test_constructor(self):
        persona = Persona()
        self.assertEqual(persona._dict_, {'documento':1,'apellido':'Fernandez', 'nombre':'Anabel'})

    @patch('builtins.input', side_effect=[3, 'Trump', 'Donald'])
    def test_input(self, mock_input):
        persona = Persona()
        persona.input()
        self.assertEqual(persona._dict_, {'documento':3,'apellido':'Trump', 'nombre':'Donald'})

if __name__ == '_main_':
    unittest.main()