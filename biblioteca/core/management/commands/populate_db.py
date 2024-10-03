from django.core.management.base import BaseCommand
from core.models import Categoria, Autor, Livro
import random
from datetime import datetime

class Command(BaseCommand):
    help = "Cria registros de exemplo no banco de dados"

    def handle(self, *args, **options):
        categorias = {
            'Ficção': Categoria.objects.create(nome='Ficção'),
            'Terror': Categoria.objects.create(nome='Terror'),
            'Mistério': Categoria.objects.create(nome='Mistério'),
            'Clássicos': Categoria.objects.create(nome='Clássicos'),
            'Contemporâneos': Categoria.objects.create(nome='Contemporâneos'),
        }

        autores = {
            'Ficção': [
                Autor.objects.create(nome='Isaac Asimov'),
                Autor.objects.create(nome='George Orwell')
            ],
            'Terror': [
                Autor.objects.create(nome='Stephen King'),
                Autor.objects.create(nome='H.P. Lovecraft')
            ],
            'Mistério': [
                Autor.objects.create(nome='Agatha Christie'),
                Autor.objects.create(nome='Arthur Conan Doyle')
            ],
            'Clássicos': [
                Autor.objects.create(nome='Jane Austen'),
                Autor.objects.create(nome='Fyodor Dostoevsky')
            ],
            'Contemporâneos': [
                Autor.objects.create(nome='Haruki Murakami'),
                Autor.objects.create(nome='Elena Ferrante')
            ]
        }

        livros = {
            'Ficção': [
                'Fundação', '1984', 'Brave New World', 'O Conto da Aia', 'Neuromancer'
            ],
            'Terror': [
                'It', 'O Iluminado', 'Drácula', 'Frankenstein', 'A Cor que Caiu do Céu'
            ],
            'Mistério': [
                'Assassinato no Expresso Oriente', 'O Cão dos Baskervilles', 'O Grande Enigma', 'Os Crimes ABC', 'Um Estudo em Vermelho'
            ],
            'Clássicos': [
                'Orgulho e Preconceito', 'Crime e Castigo', 'Moby Dick', 'Dom Quixote', 'Os Miseráveis'
            ],
            'Contemporâneos': [
                'Kafka à Beira-Mar', 'A Amiga Genial', 'O Morro dos Ventos Uivantes', 'A Sombra do Vento', 'Pequenas Coisas Belas'
            ]
        }

        for categoria, livros_categoria in livros.items():
            for titulo in livros_categoria:
                Livro.objects.create(
                    titulo=titulo,
                    autor=random.choice(autores[categoria]),
                    categoria=categorias[categoria],
                    publicado_em=datetime.now()
                )

        self.stdout.write(self.style.SUCCESS('30 livros, 10 autores e 5 categorias criados com sucesso!'))
