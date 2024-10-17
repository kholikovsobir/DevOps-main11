from flask import Flask, render_template_string
from flask_sqlalchemy import SQLAlchemy
import random

# Создаем экземпляр приложения Flask
app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///school.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

# Определяем модели для базы данных
class Student(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    full_name = db.Column(db.String(100))  # ФИО ученика
    class_name = db.Column(db.String(50))   # Название класса
    attendance = db.Column(db.Boolean)       # Присутствие (True/False)

class Teacher(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50))
    class_name = db.Column(db.String(50))
    class_leader = db.Column(db.String(50))

class Grade(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    student_id = db.Column(db.Integer)      
    subject = db.Column(db.String(50))      
    grade = db.Column(db.String(5))         

class Schedule(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    class_name = db.Column(db.String(50))  
    subject = db.Column(db.String(50))      
    day = db.Column(db.String(20))          
    time = db.Column(db.String(20))         

# Функция для заполнения базы данных тестовыми данными
def create_data():
    db.create_all()
    
    if Student.query.count() == 0:  # Проверяем, если таблица пуста
        # Примерные ФИО учеников для 1, 2 и 3 классов
        names = [
            "Иванов Иван Иванович", "Петров Петр Петрович", "Сидоров Сидор Сидорович",
            "Алексеева Анастасия Ивановна", "Смирнова Анна Владимировна", "Кузнецов Алексей Викторович",
            "Тихонов Артем Сергеевич", "Николаев Николай Николаевич", "Федорова Екатерина Сергеевна",
            "Соколов Алексей Андреевич", "Григорьева Ирина Викторовна", "Васильев Василий Павлович",
            "Зайцева Ольга Сергеевна", "Морозов Максим Андреевич", "Крылова Елена Васильевна",
            "Терентьев Илья Петрович"
        ]

        for i in range(1, 4):  # Для классов 1, 2 и 3
            for name in names:
                new_student = Student(full_name=name, class_name=f"{i} класс", attendance=random.choice([True, False]))
                db.session.add(new_student)

        db.session.commit()  # Сохраняем данные в базе

        # Добавляем учителей
        teachers = [
            {"name": "Иванова Ирина Васильевна", "class_name": "1 класс", "class_leader": "Иванов Иван Иванович"},
            {"name": "Петрова Мария Алексеевна", "class_name": "2 класс", "class_leader": "Сидоров Сидор Сидорович"},
            {"name": "Смирнова Анна Петровна", "class_name": "3 класс", "class_leader": "Кузнецов Алексей Викторович"}
        ]

        for teacher in teachers:
            new_teacher = Teacher(name=teacher["name"], class_name=teacher["class_name"], class_leader=teacher["class_leader"])
            db.session.add(new_teacher)

        db.session.commit()  # Сохраняем данные в базе

        # Добавляем расписание для каждого класса
        schedules = [
            {"class_name": "1 класс", "subject": "Математика", "day": "Понедельник", "time": "9:00-10:00"},
            {"class_name": "1 класс", "subject": "Русский язык", "day": "Понедельник", "time": "10:15-11:15"},
            {"class_name": "1 класс", "subject": "Окружающий мир", "day": "Вторник", "time": "9:00-10:00"},
            {"class_name": "1 класс", "subject": "Физкультура", "day": "Среда", "time": "10:15-11:15"},
            {"class_name": "1 класс", "subject": "Музыка", "day": "Четверг", "time": "9:00-10:00"},
            {"class_name": "1 класс", "subject": "Изобразительное искусство", "day": "Пятница", "time": "10:15-11:15"},
        ]
        schedules = [
          
            {"class_name": "2 класс", "subject": "Математика", "day": "Понедельник", "time": "9:00-10:00"},
            {"class_name": "2 класс", "subject": "Русский язык", "day": "Понедельник", "time": "10:15-11:15"},
            {"class_name": "2 класс", "subject": "Окружающий мир", "day": "Вторник", "time": "9:00-10:00"},
            {"class_name": "2 класс", "subject": "Физкультура", "day": "Среда", "time": "10:15-11:15"},
            {"class_name": "2 класс", "subject": "Музыка", "day": "Четверг", "time": "9:00-10:00"},
            {"class_name": "2 класс", "subject": "Изобразительное искусство", "day": "Пятница", "time": "10:15-11:15"},
        ]
        schedules = [
            
            {"class_name": "3 класс", "subject": "Математика", "day": "Понедельник", "time": "9:00-10:00"},
            {"class_name": "3 класс", "subject": "Русский язык", "day": "Понедельник", "time": "10:15-11:15"},
            {"class_name": "3 класс", "subject": "Окружающий мир", "day": "Вторник", "time": "9:00-10:00"},
            {"class_name": "3 класс", "subject": "Физкультура", "day": "Среда", "time": "10:15-11:15"},
            {"class_name": "3 класс", "subject": "Музыка", "day": "Четверг", "time": "9:00-10:00"},
            {"class_name": "3 класс", "subject": "Изобразительное искусство", "day": "Пятница", "time": "10:15-11:15"},
        ]

        for schedule in schedules:
            new_schedule = Schedule(class_name=schedule["class_name"], subject=schedule["subject"], day=schedule["day"], time=schedule["time"])
            db.session.add(new_schedule)

        db.session.commit()  # Сохраняем данные в базе

# Заполнение базы данных
with app.app_context():
    create_data()

# Главная страница
@app.route('/')
def home():
    return render_template_string('''
        <h1>Добро пожаловать в автоматизированную систему управления расписанием и оценками</h1>
        <h2>Выберите действие:</h2>
        <div style="display: flex; flex-direction: column; align-items: center;">
            <a href="/students" class="class-button">Журнал учеников</a>
            <a href="/schedule" class="class-button">Расписание</a>
        
        <img src="http://nubex.ru/img.png" width="640" height="480" align="center" border="3" hspace="10" vspace="10" />                  
        </div>
        <style>
            .class-button {
                margin: 10px;
                padding: 15px;
                background-color: #4CAF50;
                color: white;
                text-decoration: none;
                border-radius: 5px;
                width: 200px;
                text-align: center;
                font-size: 18px;
            }
            .class-button:hover {
                background-color: #45a049;
            }
        </style>
    ''')

# Страница для отображения учеников (журнал)
@app.route('/students')
def students():
    class_links = '''
    <h2>Выберите класс:</h2>
    <div style="display: flex; flex-direction: column; align-items: center;">
        <a href="/students/class/1" class="class-button">1 класс</a>
        <a href="/students/class/2" class="class-button">2 класс</a>
        <a href="/students/class/3" class="class-button">3 класс</a>
    </div>
    '''
    
    return render_template_string('''
        <h1>Журнал учеников</h1>
        <h2>Учитель: Собир Холиков</h2>
        <h3>Старост: Юсупов И.Ш</h3>
        {{ class_links|safe }}
        <a href="/">На главную</a>
    ''', class_links=class_links)

# Страница для отображения журнала конкретного класса
@app.route('/students/class/<int:class_id>')
def class_students(class_id):
    class_names = {1: "1 класс", 2: "2 класс", 3: "3 класс"}
    class_name = class_names.get(class_id, "Неизвестный класс")
    
    students = Student.query.filter_by(class_name=class_name).all()

    # Генерация оценок и посещаемости для учеников
    students_with_grades = [(student, random.choice(["5", "4", "3", "2"])) for student in students]

    return render_template_string('''
        <h1>Журнал для {{ class_name }}</h1>
        <h2>Ученики:</h2>
        <table border="1">
            <tr>
                <th>ФИО</th>
                <th>Оценка</th>
                <th>Посещаемость</th>
            </tr>
            {% for student, grade in students_with_grades %}
            <tr>
                <td>{{ student.full_name }}</td>
                <td>{{ grade }}</td>
                <td>{{ "Присутствует" if student.attendance else "Отсутствует" }}</td>
            </tr>
            {% endfor %}
        </table>
        <a href="/">На главную</a>
        <style>
            table {
                width: 100%;
                border-collapse: collapse;
            }
            th, td {
                padding: 10px;
                text-align: left;
            }
            th {
                background-color: #4CAF50;
                color: white;
            }
            a {
                display: inline-block;
                margin-top: 20px;
                padding: 10px;
                background-color: #008CBA;
                color: white;
                text-decoration: none;
                border-radius: 5px;
            }
            a:hover {
                background-color: #005f6b;
            }
        </style>
    ''', class_name=class_name, students_with_grades=students_with_grades)

# Страница для отображения расписания
@app.route('/schedule')
def schedule():
    class_links = '''
    <h2>Выберите класс:</h2>
    <div style="display: flex; flex-direction: column; align-items: center;">
        <a href="/schedule/class/1" class="class-button">1 класс</a>
        <a href="/schedule/class/2" class="class-button">2 класс</a>
        <a href="/schedule/class/3" class="class-button">3 класс</a>
    </div>
    '''
    
    return render_template_string('''
        <h1>Расписание</h1>
        <h2>Учитель: Собир Холиков</h2>
        <h3>Старост: Юсупов И.Ш</h3>
        {{ class_links|safe }}
        <a href="/">На главную</a>
    ''', class_links=class_links)

# Страница для отображения расписания конкретного класса
@app.route('/schedule/class/<int:class_id>')
def class_schedule(class_id):
    class_names = {1: "1 класс", 2: "2 класс", 3: "3 класс"}
    class_name = class_names.get(class_id, "Неизвестный класс")
    
    schedules = Schedule.query.filter_by(class_name=class_name).all()
    
    return render_template_string('''
        <h1>Расписание для {{ class_name }}</h1>
        <h2>Расписание:</h2>
        <table border="1">
            <tr>
                <th>Предмет</th>
                <th>День</th>
                <th>Время</th>
                <th>Учител</th>              
            </tr>
            {% for schedule in schedules %}
            <tr>
                <td>{{ schedule.subject }}</td>
                <td>{{ schedule.day }}</td>
                <td>{{ schedule.time }}</td>
            </tr>
            {% endfor %}
        </table>

        <a href="/">На главную</a>
        <style>
            table {
                width: 100%;
                border-collapse: collapse;
            }
            th, td {
                padding: 10px;
                text-align: left;
            }
            th {
                background-color: #4CAF50;
                color: white;
            }
            a {
                display: inline-block;
                margin-top: 20px;
                padding: 10px;
                background-color: #008CBA;
                color: white;
                text-decoration: none;
                border-radius: 5px;
            }
            a:hover {
                background-color: #005f6b;
            }
        </style>
    ''', class_name=class_name, schedules=schedules)

if __name__ == '__main__':
    app.run(debug=True)
