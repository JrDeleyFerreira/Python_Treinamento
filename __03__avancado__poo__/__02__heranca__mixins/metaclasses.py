"""Documentação com DocStrings:

É assim que se faz uma documentação usando docstrings.
Todo esse corpo é uma descrição geral do módulo.
"""
from log import LogFileMixin, LogPrintMixin

Foo = type('Foo', (object,), {})

print(dir(LogFileMixin))
help(LogPrintMixin)

def soma(x: int | float, y: int | float) -> int | float:
    """Soma entre 2 números
    
    Módulo de soma 

    Args:
        x (int | float): Primeito fator
        y (int | float): Segundo fator

    Returns:
        int | float: Somatorio
    """
    return x + y