# Гибель пришельца

# Демонстрирует взаимодействие объектов

class Player(object):
    """Игрок в экшен-игре."""
    def blast(self, enemy):
        print("Игрок стреляет во врага.\n")
        enemy.die()


class Alien(object):
    """Враждебный пришелец-инопланетянин в экшен-игре."""
    def die(self):
        print("Тяжело дыша, пришелец произносит: 'Ну, вот и все. Спета моя песенка. \n" \
            "Уже и в глазах темнеет... Передай полутора миллионам моих личинок, что я любил их... \n" \
                "Прощай, безжалостный мир.'")


# Основная часть программы
def main():
    print("\t\tГибель пришельца\n")
    hero = Player()
    invader = Alien()
    hero.blast(invader)


if __name__ == "__main__":
    main()

