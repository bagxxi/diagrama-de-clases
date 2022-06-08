class Alternativa():
    def __init__(self, contenido: str, ayuda: str) -> None:
       self.contenido = contenido
       self.ayuda = ayuda

       def mostrar_alternativa(self) -> None: print(self.contenido)

       if self.ayuda: print(f"({self.ayuda})")

