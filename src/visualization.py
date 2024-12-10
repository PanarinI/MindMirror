import matplotlib.pyplot as plt

def plot_daily_activity(daily_activity):
    plt.figure(figsize=(10, 6))
    for participant, group in daily_activity.groupby('from'):
        plt.plot(group['date'], group['Message Count'], marker='o', label=participant)

    plt.xlabel('Date')
    plt.ylabel('Message Count')
    plt.title('Daily Activity by Participants')
    plt.legend()
    plt.grid(True)
    plt.show()
