from flask import render_template, request
from config import app
from models.department_model import DepartmentModel
from models.employee_model import EmployeeModel


class HomeController(object):

    @staticmethod
    @app.route('/')
    def index():
        return render_template('home/index.html', context={
            'page_title': 'Главная',
            'departments': DepartmentModel.get_all_departments()
        })

    @staticmethod
    @app.route('/employees/<dep_id>')
    def employees(dep_id: int):
        return render_template('home/employees.html', context={
            'page_title': 'Сотрудники',
            'dep_id': dep_id,
            'dep_name': DepartmentModel.get_name_by_id(dep_id),
            'employees': EmployeeModel.get_employees_by_department(dep_id)
        })

    @staticmethod
    @app.route('/add_employee/<dep_id>', methods=['GET', 'POST'])
    def add_employee(dep_id: int):
        if request.method == 'GET':
            return render_template('home/add_employee.html', context={
                'page_title': 'Добавление сотрудника',
                'dep_id': dep_id,
                'dep_name': DepartmentModel.get_name_by_id(dep_id)
            })
        elif request.method == 'POST':
            name = request.form.get('emp_name')
            age = request.form.get('emp_age')
            position = request.form.get('emp_position')
            salary = request.form.get('emp_salary')

            # Добавление в БД ...
            EmployeeModel.add_employee(name, age, position, salary, dep_id)

            return render_template('home/add_employee_res.html', context={
                'page_title': 'Отчет о добавлении сотрудника',
                'emp_name': name,
                'emp_age': age,
                'emp_position': position,
                'emp_salary': salary,
                'dep_name': DepartmentModel.get_name_by_id(dep_id),
                'dep_id': dep_id
            })
