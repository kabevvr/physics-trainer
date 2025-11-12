import json
import random


class FormulaManager:
    def __init__(self, filename="formulas.json"):
        self.filename = filename
        self.formulas = self.load_formulas()
        self.add_default_formulas()

    def load_formulas(self):
        """Загружает формулы из файла"""
        try:
            with open(self.filename, 'r', encoding='utf-8') as file:
                return json.load(file)
        except FileNotFoundError:
            return {}
        except Exception as e:
            print(f"Ошибка загрузки: {e}")
            return {}

    def save_formulas(self):
        """Сохраняет формулы в файл"""
        try:
            with open(self.filename, 'w', encoding='utf-8') as file:
                json.dump(self.formulas, file, ensure_ascii=False, indent=2)
            return True
        except Exception as e:
            print(f"Ошибка сохранения: {e}")
            return False

    def add_default_formulas(self):
        """Добавляет основные формулы при первом запуске"""
        default_formulas = {
            "F": "F = m * a (Сила)",
            "p": "p = m * v (Импульс)",
            "v": "v = s / t (Скорость)",
            "I": "I = U / R (Сила тока)",
            "A": "A = F * s (Работа)"
        }

        for symbol, formula in default_formulas.items():
            if symbol not in self.formulas:
                self.formulas[symbol] = formula

        self.save_formulas()

    def add_formula(self):
        """Добавляет новую формулу"""
        print("\n=== ДОБАВЛЕНИЕ ФОРМУЛЫ ===")

        symbol = input("Введите символ формулы (например F): ").strip()
        if not symbol:
            print("Символ не может быть пустым!")
            return

        if symbol in self.formulas:
            print(f"Формула {symbol} уже есть: {self.formulas[symbol]}")
            replace = input("Заменить? (да/нет): ").lower()
            if replace != 'да':
                return

        formula = input("Введите формулу с пояснением: ").strip()
        if not formula:
            print("Формула не может быть пустой!")
            return

        self.formulas[symbol] = formula
        if self.save_formulas():
            print(f"Формула {symbol} добавлена!")
        else:
            print("Ошибка сохранения!")

    def show_formulas(self):
        """Показывает все формулы"""
        print("\n=== ВСЕ ФОРМУЛЫ ===")

        if not self.formulas:
            print("Формул нет!")
            return

        print(f"Всего формул: {len(self.formulas)}")
        for i, (symbol, formula) in enumerate(self.formulas.items(), 1):
            print(f"{i}. {symbol}: {formula}")

    def train_formulas(self):
        """Тренировка формул"""
        if not self.formulas:
            print("Нет формул для тренировки!")
            return

        print("\n=== ТРЕНИРОВКА ФОРМУЛ ===")
        print("Угадайте формулу по символу. Для выхода введите 'выход'")

        symbols = list(self.formulas.keys())
        correct = 0
        total = 0

        while True:
            symbol = random.choice(symbols)
            correct_formula = self.formulas[symbol]
            total += 1

            print(f"\nСимвол: {symbol}")
            answer = input("Ваш ответ: ").strip()

            if answer.lower() == 'выход':
                break

            # Простая проверка ответа
            if answer.lower() in correct_formula.lower():
                print("Правильно! ✓")
                correct += 1
            else:
                print(f"Неправильно! Правильный ответ: {correct_formula}")

        print(f"\nТренировка окончена! Правильно: {correct} из {total - 1}")


class TaskManager:
    def __init__(self, filename="tasks.json"):
        self.filename = filename
        self.tasks = self.load_tasks()

    def load_tasks(self):
        """Загружает задачи из файла"""
        try:
            with open(self.filename, 'r', encoding='utf-8') as file:
                return json.load(file)
        except FileNotFoundError:
            return {}
        except Exception as e:
            print(f"Ошибка загрузки: {e}")
            return {}

    def save_tasks(self):
        """Сохраняет задачи в файл"""
        try:
            with open(self.filename, 'w', encoding='utf-8') as file:
                json.dump(self.tasks, file, ensure_ascii=False, indent=2)
            return True
        except Exception as e:
            print(f"Ошибка сохранения: {e}")
            return False

    def add_task(self):
        """Добавляет новую задачу"""
        print("\n=== ДОБАВЛЕНИЕ ЗАДАЧИ ===")

        task_id = f"task{len(self.tasks) + 1}"
        task_text = input("Введите условие задачи: ").strip()
        if not task_text:
            print("Условие не может быть пустым!")
            return

        answer = input("Введите ответ: ").strip()
        if not answer:
            print("Ответ не может быть пустым!")
            return

        # Простая структура задачи
        self.tasks[task_id] = {
            "task": task_text,
            "answer": answer,
            "solved": False
        }

        if self.save_tasks():
            print(f"Задача {task_id} добавлена!")
        else:
            print("Ошибка сохранения!")

    def show_tasks(self):
        """Показывает все задачи"""
        print("\n=== ВСЕ ЗАДАЧИ ===")

        if not self.tasks:
            print("Задач нет!")
            return

        print(f"Всего задач: {len(self.tasks)}")
        for task_id, task_data in self.tasks.items():
            status = "решена" if task_data["solved"] else "не решена"
            print(f"{task_id}: {task_data['task']} [{status}]")

    def solve_tasks(self):
        """Решает задачи"""
        if not self.tasks:
            print("Нет задач для решения!")
            return

        print("\n=== РЕШЕНИЕ ЗАДАЧ ===")
        print("Решайте задачи. Для выхода введите 'выход'")

        correct = 0
        total = 0

        for task_id, task_data in self.tasks.items():
            if task_data["solved"]:
                continue

            print(f"\nЗадача: {task_data['task']}")
            answer = input("Ваш ответ: ").strip()

            if answer.lower() == 'выход':
                break

            total += 1

            # Простая проверка
            if answer.lower() == task_data["answer"].lower():
                print("Правильно! ✓")
                task_data["solved"] = True
                correct += 1
            else:
                print(f"Неправильно! Правильный ответ: {task_data['answer']}")

        self.save_tasks()
        print(f"\nРешено правильно: {correct} из {total}")


class PhysicsLearningApp:
    def __init__(self):
        self.formula_manager = FormulaManager()
        self.task_manager = TaskManager()

    def show_menu(self):
        """Главное меню"""
        while True:
            print("\n" + "=" * 50)
            print("       ТРЕНАЖЕР ФИЗИКИ")
            print("=" * 50)
            print(f"Формулы: {len(self.formula_manager.formulas)}")
            print(f"Задачи: {len(self.task_manager.tasks)}")
            print("\1. Формулы")
            print("2. Задачи")
            print("3. Выход")
            print("=" * 50)

            choice = input("Выберите (1-3): ").strip()

            if choice == '1':
                self.formula_menu()
            elif choice == '2':
                self.task_menu()
            elif choice == '3':
                print("До свидания!")
                break
            else:
                print("Неверный выбор!")

    def formula_menu(self):
        """Меню формул"""
        while True:
            print("\n--- ФОРМУЛЫ ---")
            print("1. Добавить формулу")
            print("2. Показать все формулы")
            print("3. Тренироваться")
            print("4. Назад")

            choice = input("Выберите (1-4): ").strip()

            if choice == '1':
                self.formula_manager.add_formula()
            elif choice == '2':
                self.formula_manager.show_formulas()
            elif choice == '3':
                self.formula_manager.train_formulas()
            elif choice == '4':
                break
            else:
                print("Неверный выбор!")

    def task_menu(self):
        """Меню задач"""
        while True:
            print("\n--- ЗАДАЧИ ---")
            print("1. Добавить задачу")
            print("2. Показать все задачи")
            print("3. Решать задачи")
            print("4. Назад")

            choice = input("Выберите (1-4): ").strip()

            if choice == '1':
                self.task_manager.add_task()
            elif choice == '2':
                self.task_manager.show_tasks()
            elif choice == '3':
                self.task_manager.solve_tasks()
            elif choice == '4':
                break
            else:
                print("Неверный выбор!")


# Запуск программы
if __name__ == "__main__":
    app = PhysicsLearningApp()
    app.show_menu()
