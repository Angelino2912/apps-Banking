import database


from rekening import Rekening

class UserRepositoryy:
    def __init__(self):
        self.users = []

    def tambah_user(self, user: Rekening):
        self.users.append(user)

    def ambil_user(self):
        return self.users

    def panggil_user(self, username, password):
        for user in self.users:
            if user.username_us == username and user.password_us == password:
                return user  # kembalikan objek Rekening
        return None
