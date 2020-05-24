import pandas as pd
import matplotlib.pyplot as plt

from statsmodels.tsa.seasonal import STL
from statsmodels.tsa.seasonal import seasonal_decompose


def plot_train_test_predicted(train: pd.Series,
                              test: pd.Series,
                              predicted: pd.Series,
                              title: str = 'Train, Test and Predicted',
                              label_train: str = 'Train',
                              label_test: str = 'Test',
                              label_predicted: str = 'Predicted') -> None:
    """
    Plots entire time series with train, test split and predicted values.
    :param train: train part of the time series
    :param test: test part of the time series
    :param predicted: predicted values
    :param title: plot title
    :param label_train: label for the train data
    :param label_test: label for the test data
    :param label_predicted: label for the predicted data
    :return: None
    """
    plt.figure(figsize=(20, 10))
    plt.plot(train.index, train, label=label_train, c='blue')
    plt.plot(test.index, test, label=label_test, c='orange')
    plt.plot(predicted.index, predicted, label=label_predicted, c='green')
    plt.title(title)
    plt.legend(loc='best')
    plt.show()


def plot_observed_vs_predicted(observed: pd.Series,
                               predicted: pd.Series,
                               num_points: int,
                               title: str = 'Observed vs. Predicted',
                               label_observed: str = 'Observed',
                               label_predicted: str = 'Predicted') -> None:
    """
    Plots a number of points back from the last time series point as a zoomed view on observed
    and predicted data.
    :param observed: observed data
    :param predicted: predicted data
    :param num_points: number of points to draw on the horizontal axis
    :param title: plot title
    :param label_observed: label for the observed data
    :param label_predicted: label for the predicted data
    :return: None
    """
    plt.figure(figsize=(20, 10))
    plt.plot(observed.iloc[-num_points:], label=label_observed, c='orange')
    plt.plot(predicted[-num_points:], label=label_predicted, c='green')
    plt.title(title)
    plt.legend(loc='best')
    plt.show()


def plot_stl(data: pd.Series):  # -> DecomposeResult:

    # TODO: dac opis

    # Seasonal-Trend decomposition - LOESS (STL)
    # from statsmodels.tsa.seasonal import STL
    # update with what this function returns
    # https://robjhyndman.com/hyndsight/seasonal-periods/

    stl = STL(data, period=60)
    result = stl.fit()

    fig, (ax1, ax2, ax3, ax4) = plt.subplots(4, 1, figsize=(20, 16))
    ax1.set_title('Observed', loc='left')
    result.observed.plot(ax=ax1)
    ax2.set_title('Trend', loc='left')
    result.trend.plot(ax=ax2)
    ax3.set_title('Seasonal', loc='left')
    result.seasonal.plot(ax=ax3)
    ax4.set_title('Residuals', loc='left')
    result.resid.plot(ax=ax4)
    plt.show()

    return result


def plot_decompose(data: pd.Series):
    # update with what this function returns

    # TODO: dac opis

    result = seasonal_decompose(data, model='additive', freq=60)
    fig, (ax1, ax2, ax3, ax4) = plt.subplots(4, 1, figsize=(20, 16))
    result.observed.plot(ax=ax1)
    result.trend.plot(ax=ax2)
    result.seasonal.plot(ax=ax3)
    result.resid.plot(ax=ax4)
    plt.show();

    return result