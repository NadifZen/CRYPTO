import matplotlib.pyplot as plt

def show_chart(data):

    plt.figure(figsize=(12,6))

    plt.plot(data["Close"], label="Price")
    plt.plot(data["MA20"], label="MA20")
    plt.plot(data["MA50"], label="MA50")

    plt.legend()
    plt.show()