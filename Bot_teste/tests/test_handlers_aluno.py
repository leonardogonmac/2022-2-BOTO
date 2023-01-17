import unittest
from unittest.mock import patch
from telegram import *
from src import handlers_aluno as ha


class TestHandlersAluno(unittest.TestCase):
    def test_alunoEntrada(self):
        #nao funciona
        # define mocked_update como a variavel que contem a mensagem do usuario
        with patch('update') as mocked_update:
            with patch('context') as mocked_context:
                mocked_update.return_value.message.text = "123456789"
                mocked_update.return_value.from_user.first_name = "Joao"
                mocked_update.return_value.from_user.last_name = "Silva"
                nome = "Joao"
                sobrenome = "Silva"
                matr = "123456789"

                info = {"First_Name": nome, "Last_Name": sobrenome,
                    "Matrícula": matr}

                self.assertEqual(ha.alunoEntrada(mocked_update, mocked_context), info)



if __name__ == '__main__':
    unittest.main()
