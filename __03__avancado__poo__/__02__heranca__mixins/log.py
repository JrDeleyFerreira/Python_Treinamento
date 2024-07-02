from abc import ABC, abstractmethod
from pathlib import Path

LOG_FILE = Path(__file__).parent / 'log.txt'

class Log: # Por convenção, é uma espécie de interface
    def _log(self, msg): # Função com undeline protected
        raise NotImplementedError('Implemente o método log.')
    
    def log_error(self, msg): # Assinatura genérica
        return self._log(f'Error: {msg}')
    
    def log_success(self, msg): # Assinatura genérica
        return self._log(f'Success: {msg}')
        
# --------------------------------------------------------    
class LogFileMixin(Log):
    def _log(self, msg):
        mensagem_formatada = f'{msg} ({self.__class__.__name__})'
        with open(LOG_FILE, 'a') as arquivo:
            arquivo.write(mensagem_formatada)
            arquivo.write('\n')
        
# --------------------------------------------------------
class LogPrintMixin(Log):
    def _log(self, msg):
        print(f'{msg} ({self.__class__.__name__})')
        
# --------------------------------------------------------  
if __name__ == '__main__':
    l = LogPrintMixin()
    l.log_error('Usando Log() como interface!')
    
# --------------------------------------------------------
# Abstração de propriedade em classe Abstrata com ABC

class LogAbstract(ABC):
    def __init__(self, msg) -> None:
        super().__init__()
        self._msg = msg
    
    @abstractmethod
    def _log(self, msg): pass
    
    @property
    def mensagem(self):
        return self._msg
    
    @mensagem.setter
    @abstractmethod
    def mensagem(self, value): pass
    
class HerdaDeAbs(LogAbstract):
    def __init__(self, msg) -> None:
        super().__init__(msg)
        
    @LogAbstract.mensagem.setter
    @abstractmethod
    def mensagem(self, value):
        self.mensagem = value