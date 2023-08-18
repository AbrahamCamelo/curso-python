import matplotlib.pyplot as plt

def generate_pie_chart():
    labels = ['A','B']
    values = [200, 34]

    fig, ax = plt.subplots()
    ax.pie(values,labels = labels)
    plt.savefig('py.png')
    plt.close()
