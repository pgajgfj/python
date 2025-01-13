#1 
class Passport:
    def __init__(self, first_name, last_name, patronymic, birth_date, passport_number, issued_by, issue_date):
        self.first_name = first_name
        self.last_name = last_name
        self.patronymic = patronymic
        self.birth_date = birth_date
        self.passport_number = passport_number
        self.issued_by = issued_by
        self.issue_date = issue_date
    def display_info(self):
        """Виводить інформацію про внутрішній паспорт"""
        return (
            f"Паспорт громадянина\n"
            f"Ім'я: {self.first_name}\n"
            f"Прізвище: {self.last_name}\n"
            f"По батькові: {self.patronymic}\n"
            f"Дата народження: {self.birth_date}\n"
            f"Номер паспорта: {self.passport_number}\n"
            f"Ким видано: {self.issued_by}\n"
            f"Дата видачі: {self.issue_date}\n"
        )

class ForeignPassport(Passport):
    def __init__(self, first_name, last_name, patronymic, birth_date, passport_number, issued_by, issue_date,
                 foreign_passport_number, visas=None):
        super().__init__(first_name, last_name, patronymic, birth_date, passport_number, issued_by, issue_date)
        self.foreign_passport_number = foreign_passport_number
        self.visas = visas if visas else []
    def add_visa(self, country, issue_date, expiry_date):
        """Додає візу до списку"""
        self.visas.append({
            "country": country,
            "issue_date": issue_date,
            "expiry_date": expiry_date
        })

    def remove_visa(self, country):
        """Видаляє візу за країною"""
        for visa in self.visas:
            if visa["country"] == country:
                self.visas.remove(visa)
                print(f"Віза до країни {country} успішно видалена.")
                return
        print(f"Візу до країни {country} не знайдено.")

    def display_foreign_info(self):
        """Виводить інформацію про закордонний паспорт та візи"""
        base_info = self.display_info()
        visa_info = "\n".join(
            [f"{i + 1}. Країна: {visa['country']}, Видана: {visa['issue_date']}, Дійсна до: {visa['expiry_date']}" 
             for i, visa in enumerate(self.visas)]
        )
        return (
            f"{base_info}"
            f"Номер закордонного паспорта: {self.foreign_passport_number}\n"
            f"Візи:\n{visa_info if visa_info else 'Віз немає'}\n"
        )
    

passport = Passport(
    first_name="Іван", 
    last_name="Іваненко", 
    patronymic="Іванович", 
    birth_date="01.01.1990", 
    passport_number="AA123456", 
    issued_by="Міграційна служба", 
    issue_date="01.01.2010"
)

foreign_passport = ForeignPassport(
    first_name="Іван", 
    last_name="Іваненко", 
    patronymic="Іванович", 
    birth_date="01.01.1990", 
    passport_number="AA123456", 
    issued_by="Міграційна служба", 
    issue_date="01.01.2010",
    foreign_passport_number="FP789012"
)

foreign_passport.add_visa("США", "01.02.2022", "01.02.2024")
foreign_passport.add_visa("Канада", "01.03.2023", "01.03.2025")

print(passport.display_info())
print(foreign_passport.display_foreign_info())

foreign_passport.remove_visa("США")
print(foreign_passport.display_foreign_info())

foreign_passport.remove_visa("Японія")

#2
class TemperatureConverter:
    _conversion_count = 0

    @staticmethod
    def celsius_to_fahrenheit(celsius):
        """Конвертує температуру з Цельсія у Фаренгейт."""
        TemperatureConverter._conversion_count += 1
        return celsius * 9/5 + 32

    @staticmethod
    def fahrenheit_to_celsius(fahrenheit):
        """Конвертує температуру з Фаренгейта у Цельсій."""
        TemperatureConverter._conversion_count += 1
        return (fahrenheit - 32) * 5/9

    @staticmethod
    def get_conversion_count():
        """Повертає кількість виконаних конвертацій."""
        return TemperatureConverter._conversion_count



temp_celsius = 25
temp_fahrenheit = TemperatureConverter.celsius_to_fahrenheit(temp_celsius)
print(f"{temp_celsius}°C = {temp_fahrenheit}°F")

temp_fahrenheit = 77
temp_celsius = TemperatureConverter.fahrenheit_to_celsius(temp_fahrenheit)
print(f"{temp_fahrenheit}°F = {temp_celsius:.2f}°C")


print("Кількість конвертацій:", TemperatureConverter.get_conversion_count())
