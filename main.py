import utils
from algorithm import logic


def main() -> None:
    simulations = 100000
    utils.plot_bar_chart(logic.game_1(simulations, 2))


if __name__ == "__main__":
    main()
