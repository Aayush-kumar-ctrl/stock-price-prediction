import matplotlib.pyplot as plt

def plot_predictions(y_test, y_pred):
    plt.figure(figsize=(10,5))
    plt.plot(y_test.values, label="Actual Price")
    plt.plot(y_pred, label="Predicted Price")
    plt.legend()
    plt.title("Actual vs Predicted Stock Prices")
    plt.xlabel("Samples")
    plt.ylabel("Price")
    plt.show()
