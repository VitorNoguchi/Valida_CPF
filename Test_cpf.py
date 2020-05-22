import unittest
from validacpf_vitor import CPFvalidator

class Testcpf (unittest.TestCase):

    def test_retira(self):
        self.assertEqual(CPFvalidator.retira_formatacao(self, '411.165.168-29'), '41116516829')
        self.assertEqual(CPFvalidator.retira_formatacao(self, '4.1.1.1.6.5.1.6.8-2-9'), '41116516829')
        with self.assertRaises(ValueError):
            CPFvalidator.retira_formatacao(self, '41a.8d1.9f3-ka')
        with self.assertRaises(ValueError):
            CPFvalidator.retira_formatacao(self, '411.141.5344-12')
        with self.assertRaises(ValueError):
            CPFvalidator.retira_formatacao(self, '41a.8d1.9f3-ka1')

    def test_valida(self):
        self.assertEqual(CPFvalidator.valida_cpf(self, '41116516829'), '41116516829')
        with self.assertRaises(ValueError):
            CPFvalidator.valida_cpf(self, '111.111.111-11')
        with self.assertRaises(ValueError):
            CPFvalidator.valida_cpf(self, '111.141.111-11')

suite = unittest.TestLoader().loadTestsFromTestCase(Testcpf)
unittest.TextTestRunner(verbosity=2).run(suite)