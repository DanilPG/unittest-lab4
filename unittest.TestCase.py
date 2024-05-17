import unittest
from app import app, db, user

# Тестовый класс
class TestMyApp(unittest.TestCase):

    # Метод, который будет запускаться перед каждым тестом
    def setUp(self):
        app.config['TESTING'] = True
        app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///test_database.db'
        with app.app_context():
            db.create_all()

    # Метод, который будет запускаться после каждого теста
    def tearDown(self):
        with app.app_context():
            db.session.remove()
            db.drop_all()

    # Тест для проверки функции регистрации пользователя
    def test_register_user(self):
        with app.test_client() as client:
            with app.app_context():
                response = client.post('/register', data=dict(uname='test_user', mail='test@example.com', passw='password'), follow_redirects=True)
                self.assertEqual(response.status_code, 200)  # Проверка успешной регистрации

    # Тест для проверки функции входа пользователя
    def test_login_user(self):
        with app.test_client() as client:
            with app.app_context():
                client.post('/register', data=dict(uname='test_user', mail='test@example.com', passw='password'))
                response = client.post('/login', data=dict(uname='test_user', passw='password'), follow_redirects=True)
                self.assertEqual(response.status_code, 200)  # Проверка успешного входа

if __name__ == '__main__':
    unittest.main()
