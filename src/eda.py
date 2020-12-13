import pandas as pd
import matplotlib
import matplotlib.pyplot as plt


def plot_record_years(df, city, save_plot=False):
    """
    Makes a scatter plot of the high and low record temperatures
    and the year they occurred

    Parameters
    ----------
    df: Pandas DataFrame
        The dataframe from which the values come

    city: string
        Contains the airport code that the data came from

    save_plot: Boolean
        Whether to save the plot or just display it
        Default = False

    Returns
    -------
    None
    """
    fig, axs = plt.subplots(1, 2,
                            figsize=(20, 12),
                            dpi=72,
                            sharey=True,
                            tight_layout=True)

    axs[0].scatter(df.record_min_temp,
                   df.record_min_temp_year,
                   s=100,
                   alpha=0.6,
                   edgecolors='g')
    axs[0].hlines(df.record_min_temp_year.median(),
                  df.record_min_temp.min(),
                  df.record_min_temp.max(),
                  lw=2,
                  color='b',
                  alpha=0.8)

    axs[1].scatter(df.record_max_temp,
                   df.record_max_temp_year,
                   c='crimson',
                   s=100,
                   alpha=0.6,
                   edgecolors='g')
    axs[1].hlines(df.record_max_temp_year.median(),
                  df.record_max_temp.min(),
                  df.record_max_temp.max(),
                  lw=2,
                  color='crimson',
                  alpha=0.8)

    fig.suptitle(f'Record High Temps vs Year, {city}')
    axs[0].set_title(' ')
    axs[0].set_xlabel('Low Temperature, °F')
    axs[0].set_ylabel('Year of Record')
    axs[1].set_xlabel('High Temperature, °F')
    plt.tight_layout()

    if save_plot:
        plt.savefig(f'images/high_temps_vs_year_{city}.png')

    plt.show()


def plot_records_hist(df, city, save_plot=False):
    """
    Makes a histogram of the years in which the record temperatures
    occur

    Parameters
    ----------
    df: Pandas DataFrame
        The dataframe from which the values come

    city: string
        Contains the airport code that the data came from

    save_plot: Boolean
        Whether to save the plot or just display it
        Default = False

    Returns
    -------
    None
    """
    num_bins = 50

    fig, axs = plt.subplots(1, 2,
                            figsize=(20, 12),
                            dpi=72,
                            sharey=True,
                            tight_layout=True)
    axs[0].hist(df.record_min_temp_year,
                density=False,
                bins=num_bins,
                alpha=0.8)
    axs[1].hist(df.record_max_temp_year,
                density=False,
                bins=num_bins,
                color='crimson',
                alpha=0.8)

    fig.suptitle(f'Record Temp Days Per Year, {city}')
    axs[0].set_ylabel('# Record Days')
    axs[0].set_title(' ')

    if save_plot:
        plt.savefig(f'images/record_temps_years_{city}.png')

    plt.show()


def main():
    """
    Options for cities to query (these are airport codes)
    'KCLT', 'KCQT', 'KHOU', 'KIND', 'KJAX',
    'KMDW', 'KNYC', 'KPHL', 'KPHX', 'KSEA'
    """
    station = 'KPHX'

    df = pd.read_csv(f'data/{station}.csv')

    plot_record_years(df, station, save_plot=True)

    plot_records_hist(df, station, save_plot=True)


if __name__ == '__main__':
    # respect for the audience
    font = {'family': 'DejaVu Sans',
            'weight': 'normal',
            'size': 20}
    matplotlib.rc('font', **font)
    plt.style.use('fivethirtyeight')

    main()
