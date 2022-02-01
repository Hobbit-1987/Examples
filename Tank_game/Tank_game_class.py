import random


# Класс Tank() содержит методы имитирующие действия танков:
class Tank():
    # Атрибуты (Health, Skill, Power характеристики твоего танка, задаются при
    # создании экземпляра),
    def __init__(self, Health, Skill, Power,
                 Boss_health = '', Boss_Skill = '', Boss_power = ''):

        self.Health = Health # уровень прочности твоего танка
        self.Skill = Skill # уровень точности выстрела твоего танка
        self.Power = Power # сила выстрела твоего танка

        self.Boss_health = 30 # уровень прочности танка противника
        self.Boss_Skill = [0,0,0,1] # уровень точности выстрела противника
        self.Boss_power = 5 # сила выстрела танка противника

    # Метод health_down вызывается при попадании в тебя из танка противника.
    # Метод вычетает из прочности твоего танка self.Health, значение силы
    # выстрела противника self.Boss_power
    def health_down(self):
        print("В тебя попали")
        self.Health -= self.Boss_power
        print(f"Здоровья осталось {self.Health}")
        # если после выстрела прочность твоего танка больше 0,
        # то вызывается метод стрельбы твоим танком attack().
        if self.Health > 0:
            self.attack()
        elif self.Health <= 0: # если прочности не осталось, то конец игры
            print("GAME OVER !!!")
            exit()
        
    # Метод attack() предлагает "выстрелить" по танку противника. Попадание
    # просходит, если из self.Skill случайным образом выбрана 1. После
    # выбора 1 вызывается метод Boss_health_down() для вычитания прочности 
    # танка противника. Если выпадает 0, или выбирается "нет", то вызывается
    # метод атаки противника self.Boss_attack()
    def attack(self):
        print("Стрелять ? да/нет")
        select = input("->")

        if select == "да":
            # выстрел, случайный выбор 0 или 1 из списка Skill
            random_shot = random.choice(self.Skill)
            if random_shot == 1:
                self.Boss_health_down() # метод вычитания прочности танка противника
            else:
                print("Ты промахнулся")
                self.Boss_attack() # метода атаки противника

        elif select == "нет":
            self.Boss_attack()
        else:
            print("Выбери действие")
            self.attack() # возврат к началу метода если ничего не выбрано

    # Метод select_tir_or_attack() предлагает выбор режима "бой" или "тренировка".
    def select_tir_or_attack(self):
        print("тренировка или в бой ?")
        select = input("->")

        if select == "тренировка":
            print("Тренировка начинается")
            self.training() # переход в режим тренировки
        elif select == "бой":
            self.Boss_attack() # переход в бой, вызов метода атаки противника
        else:
            print("Повтори ввод")
            self.select_tir_or_attack # возврат к началу метода

    # Метод training() повышает уровень точности твоего танка. Попадание по мишени
    # происходит случайным выбором 0 или 1 из из self.Skill. В случае выбора 1, 
    # в конец списка self.Skill добавляется 1 и вероятность её выбора в следующий 
    # раз становится выше. В случае выбора 0 предлагается режим "бой" 
    # или "тренировка".
    def training(self):
        print("Тренировка началась")
        print("Выстрел по мишении ---> ")
        random_shot = random.choice(self.Skill) # случайный выбор 0 или 1

        if random_shot == 1:
            print("Попадание")
            # добавление единицы в конец списка self.Skill
            self.Skill.append(1)
            # вывод количества единиц опыта
            print(f" Меткость повышена и составляет {sum(self.Skill)}. ")
            select = input("->")
            if select == "да":
                self.training() # возврат к началу тренировки
            else:
                self.select_tir_or_attack() # выбор режима "бой" или "тренировка"

        elif random_shot == 0:
            print("Мимо")
            print("Стрелять еще, да/нет ?")
            select = input("->")
            if select == "да":
                self.training()
            else:
                self.select_tir_or_attack()
        
    # Метод Boss_attak() имитирует атаку вражеского танка .
    # Попадание просходит случайным выбором 0 или 1 из self.Boss_Skill.
    def Boss_attack(self):
        print("Враг стреляет ---->")
        Boss_random_shot = random.choice(self.Boss_Skill) # Выбор 1 или 0

        if Boss_random_shot == 0:
            print("Мимо")
            self.attack() # вызов атаки танка противника, если тот промахнулся
        elif Boss_random_shot == 1:
            # попадание противника вызывает метод вычитания прочности твоего танка
            self.health_down()  
        
    # Метод Boss_health_down вызывается при попадании в танк противника.
    # Метод вычетает из прочности танка противника self.Boss_health, значение силы
    # выстрела твоего танка self.Power
    def Boss_health_down(self):
        print("Попадание во врага")
        self.Boss_health -= self.Power 
        print(f"    Здоровье врага -- {self.Boss_health}")

        if self.Boss_health > 0:
            self.attack()
        elif self.Boss_health <= 0:
            print("Ура Победа !!!")
        else:
            print("Упс")