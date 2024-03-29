# Identar o código é uma forma de manter o código mais legível e mautenível. Em Python, através da identação o interpretador consegue determinar onde um bloco de comando inicia e onde ele termina.

def sacar(self, valor: float) -> None: # início do bloco do metódo

    if self.saldo >= valor: # início do bloco de if

        self.saldo -= valor

    # fim do bloco de if

# fim do bloco do metódo
        
# Existe uma convenção em Python, que define as boas prátcias para escrita de código na linguagem. Nesse documento é indicado utilizar 4 espaços em branco por nível de identação, ou seja, a cada novo bloco adicionamos 4 novos espaços em branco.