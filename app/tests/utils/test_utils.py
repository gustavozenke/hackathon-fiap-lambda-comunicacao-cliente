import os
import sys
import unittest

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "../../../src")))

from utils.utils import inserir_prefixo_codigo_pais


class TestInserirPrefixoCodigoPais(unittest.TestCase):

    def test_inserir_prefixo_sucesso(self):
        self.assertEqual(inserir_prefixo_codigo_pais("+123456789"), "+55123456789")

    def test_numero_invalido_sem_mais(self):
        with self.assertRaises(ValueError):
            inserir_prefixo_codigo_pais("123456789")

    def test_numero_curto(self):
        with self.assertRaises(ValueError):
            inserir_prefixo_codigo_pais("+12")
