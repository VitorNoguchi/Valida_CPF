class CPFvalidator:
    def retira_formatacao(self, num_cpf):
        num_cpf = str(num_cpf).replace('.', '')
        num_cpf = num_cpf.replace('-', '')
        try:
            int(num_cpf)
        except:
            raise ValueError('CPF inválido - Digite somente numeros, "." ou "-"')
        if len(num_cpf) != 11:
            raise ValueError('CPF inválido - Necessario exatos 11 digitos')
        return num_cpf

    def valida_cpf(self, num_cpf):
        cpf = CPFvalidator.retira_formatacao(self, num_cpf)
        if all(x == cpf[0] for x in cpf) == False:
            sum1 = 0; sum2 = 0
            for a in range(0,9):
                sum1 += int(cpf[a])*(10-a)
            for b in range(0,10):
                sum2 += int(cpf[b])*(11-b)
            if str((sum1*10)%11)[-1] == cpf[-2] and str((sum2*10)%11)[-1] == cpf[-1]:
                result = cpf
            else:
                raise ValueError('CPF inválido - Erro na validação')
        else:
            raise ValueError('CPF inválido - Todos os dígitos iguais')
        return result

if __name__ == '__main__':
    a = CPFvalidator().valida_cpf('41116516829')
    print(a)