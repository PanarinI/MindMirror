import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation
import networkx as nx
import pandas as pd

# Генерация данных
data = [
    {"time": 1, "source": "A", "target": "B", "weight": 5},
    {"time": 2, "source": "A", "target": "C", "weight": 3},
    {"time": 3, "source": "B", "target": "C", "weight": 7},
    {"time": 4, "source": "C", "target": "D", "weight": 2},
    {"time": 5, "source": "D", "target": "E", "weight": 10},
    {"time": 6, "source": "E", "target": "F", "weight": 6},
    {"time": 7, "source": "A", "target": "F", "weight": 4},
]

# Преобразуем в DataFrame
df = pd.DataFrame(data)

# Определяем всех участников
nodes = list(set(df["source"]).union(set(df["target"])))

# Финальный граф (все рёбра)
final_graph = nx.DiGraph()
for _, row in df.iterrows():
    final_graph.add_edge(row["source"], row["target"], weight=row["weight"])

# Фиксируем расположение узлов
pos = nx.spring_layout(final_graph, seed=42)

# Анимация
fig, ax = plt.subplots(figsize=(8, 6))
current_graph = nx.DiGraph()


def normalize(value, min_val, max_val, min_size, max_size):
    """Нормализация значений в диапазон."""
    if min_val == max_val:  # Обработка деления на ноль
        return (min_size + max_size) / 2
    return min_size + (value - min_val) * (max_size - min_size) / (max_val - min_val)


def update(frame):
    ax.clear()
    time_step = frame + 1
    subset = df[df["time"] <= time_step]

    # Обновляем граф
    current_graph.clear()
    for _, row in subset.iterrows():
        if current_graph.has_edge(row["source"], row["target"]):
            current_graph[row["source"]][row["target"]]["weight"] += row["weight"]
        else:
            current_graph.add_edge(row["source"], row["target"], weight=row["weight"])

    # Узлы: вычисляем активность (входящие + исходящие веса)
    node_activity = {node: 0 for node in nodes}
    for u, v, data in current_graph.edges(data=True):
        node_activity[u] += data["weight"]
        node_activity[v] += data["weight"]

    # Нормируем размеры узлов
    min_activity = min(node_activity.values()) if node_activity.values() else 0
    max_activity = max(node_activity.values()) if node_activity.values() else 1
    node_sizes = {
        node: normalize(node_activity[node], min_activity, max_activity, 100, 1000)
        for node in nodes
    }

    # Нормируем толщину рёбер
    edge_weights = [data["weight"] for _, _, data in current_graph.edges(data=True)]
    if edge_weights:  # Проверяем, есть ли рёбра
        min_weight = min(edge_weights)
        max_weight = max(edge_weights)
        edge_thickness = {
            (u, v): normalize(data["weight"], min_weight, max_weight, 1, 5)
            for u, v, data in current_graph.edges(data=True)
        }
    else:
        edge_thickness = {}

    # Рисуем узлы
    nx.draw_networkx_nodes(current_graph, pos, ax=ax,
                           node_size=[node_sizes[node] for node in nodes],
                           node_color="skyblue")
    nx.draw_networkx_labels(current_graph, pos, ax=ax, font_size=10,
                            bbox=dict(facecolor='white', edgecolor='black', boxstyle='round,pad=0.3'))

    # Рисуем рёбра
    for u, v in current_graph.edges():
        weight = edge_thickness.get((u, v), 1)
        plt.annotate(
            "",
            xy=pos[v],
            xytext=pos[u],
            arrowprops=dict(
                arrowstyle="-|>",
                color="black",
                lw=weight,
                alpha=0.7,
                connectionstyle="arc3,rad=-0.1",
            ),
        )

    ax.set_title(f"Граф на шаге времени {time_step}")
    ax.axis("off")


# Анимация
ani = FuncAnimation(fig, update, frames=max(df["time"]), interval=1000, repeat=False)
plt.show()

matplotlib.get_backend()