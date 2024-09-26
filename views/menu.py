from controllers.user_controller import UserController
from controllers.book_controller import BookController

class Menu:
    def __init__(self, db):
        self.user_controller = UserController(db)
        self.book_controller = BookController(db)

    def print_login_options(self):
        print("+ -------------------------------------+")
        print("|               BIBLIOTECA             |")
        print("+ -------------------------------------+")
        print("| Opção 1 - Cadastro                   |")
        print("| Opção 2 - Login                      |")
        print("| Opção 0 - Encerrar programa          |")
        print("+ -------------------------------------+")
        return input("Insira aqui sua opção: ")

    def print_admin_menu(self):
        print("+ -------------------------------------+")
        print("|        PERFIL DO ADMINISTRADOR       |")
        print("+ -------------------------------------+")
        print("| Opção 1 - Adicionar livro            |")
        print("| Opção 2 - Listar livros cadastrados  |")
        print("| Opção 3 - Buscar livro pelo título   |")
        print("| Opção 0 - Encerrar programa          |")
        print("+ -------------------------------------+")
        return input("Insira aqui sua opção: ")

    def print_standard_menu(self):
        print("+ -------------------------------------+")
        print("|            PERFIL DO LEITOR          |")
        print("+ -------------------------------------+")
        print("| Opção 1 - Buscar livro pelo título   |")
        print("| Opção 2 - Listar livros cadastrados  |")
        print("| Opção 0 - Encerrar programa          |")
        print("+ -------------------------------------+")
        return input("Insira aqui sua opção: ")

    def run(self):
        while True:
            option = self.print_login_options()
            if option == '1':
                self.register()
            elif option == '2':
                self.login()
            elif option == '0':
                print("Encerrando o programa...")
                break
            else:
                print("Opção inválida. Tente novamente.")

    def register(self):
        name = input("Nome: ")
        email = input("Email: ")
        password = input("Senha: ")
        profile = input("Perfil (admin/leitor): ")
        self.user_controller.register_user(name, email, password, profile)
        print("Usuário cadastrado com sucesso!")

    def login(self):
        email = input("Email: ")
        password = input("Senha: ")
        user = self.user_controller.authenticate_user(email, password)
        if user:
            print("Login realizado com sucesso!")
            if user[4] == 'admin':
                self.admin_menu()
            else:
                self.standard_menu()
        else:
            print("Email ou senha incorretos. Tente novamente.")

    def admin_menu(self):
        while True:
            option = self.print_admin_menu()
            if option == '1':
                title = input("Título do livro: ")
                author = input("Autor do livro: ")
                self.book_controller.add_book(title, author)
                print("Livro adicionado com sucesso!")
            elif option == '2':
                books = self.book_controller.list_books()
                for book in books:
                    print(f'ID: {book[0]}, Título: {book[1]}, Autor: {book[2]}, Disponível: {book[3]}')
            elif option == '3':
                title = input("Título do livro: ")
                books = self.book_controller.search_book_by_title(title)
                for book in books:
                    print(f'ID: {book[0]}, Título: {book[1]}, Autor: {book[2]}, Disponível: {book[3]}')
            elif option == '0':
                break
            else:
                print("Opção inválida. Tente novamente.")

