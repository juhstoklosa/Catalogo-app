# Avaliação: O que o usuário escreve sobre uma obra
class Avaliacao:
    def __init__(self, autor, nota, comentario = ""):
        if not 0 <= nota <= 10:
            raise ValueError("A nota deve estar entre 0 e 10.")
        self.autor = autor
        self.nota = nota
        self.comentario = comentario

    def __str__(self):
        texto = f"{self.autor}: {self.nota}/10"
        if self. comentario:
            texto += f' — "{self.comentario}"'
        return texto

# Obra: Classe base. Outras classes herdam dela.
class Obra:
    tipo = "Obra" #Atributo de classe 

    def __init__(self, titulo, ano, genero):
        self.titulo = titulo
        self.ano = ano
        self.genero = genero
        self.avaliacoes = []

    def add_avaliacao(self,avaliacao):
        self.avaliacoes.append(avaliacao)

    def media(self):
        if not self.avaliacoes:
            return 0.0
        total = sum(a.nota for a in self.avaliacoes)
        return total / len(self.avaliacoes)

    def detalhes(self):
        # Informações específicas de cada tipo
        return ""

    def __str__(self):
        base = f"[{self.tipo}] {self.titulo} ({self.ano}) - {self.genero}"
        extra = self.detalhes()
        if extra:
            base += f" | {extra}"
        return f"{base} | média: {self.media():.1f} ({len(self.avaliacoes)} avaliações)"
    
class Filme(Obra):
    tipo = "Filme"
    def __init__(self, titulo, ano, genero, duracao_min):
        super().__init__(titulo, ano, genero)
        self.duracao_min = duracao_min

    def detalhes(self):
        return f"{self.duracao_min} min"

class Serie(Obra):
    tipo = "Série"

    def __init__(self, titulo, ano, genero, temporadas):
        super().__init__(titulo, ano, genero)
        self.temporadas = temporadas

    def detalhes(self):
        return f"{self.temporadas} temporadas"


def main():
    avaliacao = Avaliacao("Julia", 8.5,"Bom filme")
    print(avaliacao)

    obra = Obra("Interestelar",2014,"Ficção Científica")
    print(obra)

    obra.add_avaliacao(Avaliacao("Esther",10))
    obra.add_avaliacao(Avaliacao("Gustavo",9))
    print(obra)
    print("Média: ",obra.media())

    filme = Filme("Matrix",1999,"Ficção Científica",136)
    filme.add_avaliacao(Avaliacao("Carla",10))
    print(filme)

    serie = Serie("Stranger Thigs",2016,"Terror",5)
    serie.add_avaliacao(Avaliacao("Iudi",9))
    print(serie)

if __name__ == "__main__":
    main()