import matplotlib.pyplot as plt
from algorithm import logic


def plot_bar_chart(results: dict[str, int | float]) -> None:
    items = results.items()
    x_labels = []
    y_values = []
    for x, y in items:
        x_labels.append(x)
        y_values.append(y)

    plt.grid()

    plt.bar(x_labels, y_values)

    plt.show()


def main() -> None:
    pass


if __name__ == "__main__":
    main()
