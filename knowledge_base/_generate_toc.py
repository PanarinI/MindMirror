import os
import time

# Папки с базой знаний
knowledge_base_folder = "knowledge_base"
notebook_folder = "notebooks"  # Папка с Jupyter Notebook
experiments_folder = "experiments"
MVP_folder = "MVP"
toc_file = "_toc.md"  # Файл для оглавления теперь находится в корне

def generate_toc(folder, base_folder, indent=0, include_ipynb=False, include_py=False):
    toc_lines = []
    items = sorted(os.listdir(folder))
    if not items:  # Если папка пуста
        toc_lines.append(f"{'  ' * indent}- *Папка пуста*")
        return toc_lines

    for item in items:
        item_path = os.path.join(folder, item)
        if os.path.isdir(item_path):  # Если папка
            # Исключаем папку ipynb_checkpoints
            if item == ".ipynb_checkpoints":
                continue
            folder_name = item.replace("_", " ").title()
            toc_lines.append(f"{'  ' * indent}- **{folder_name}**")
            toc_lines.extend(generate_toc(item_path, base_folder, indent + 1, include_ipynb, include_py))
        elif item.endswith(".md") and os.path.abspath(item_path) != os.path.abspath(toc_file):  # Markdown файлы
            last_modified = time.ctime(os.path.getmtime(item_path))
            page_name = item.replace(".md", "").replace("_", " ").title()
            relative_path = os.path.relpath(item_path, os.path.dirname(toc_file))
            toc_lines.append(f"{'  ' * indent}- [{page_name}](./{relative_path.replace(os.sep, '/')}) (последнее изменение: {last_modified})")
        elif include_ipynb and item.endswith(".ipynb"):  # Jupyter Notebooks
            last_modified = time.ctime(os.path.getmtime(item_path))
            page_name = item.replace(".ipynb", "").replace("_", " ").title()
            relative_path = os.path.relpath(item_path, os.path.dirname(toc_file))
            toc_lines.append(f"{'  ' * indent}- [{page_name}](./{relative_path.replace(os.sep, '/')}) (последнее изменение: {last_modified})")
        elif include_py and item.endswith(".py"):  # Python файлы
            last_modified = time.ctime(os.path.getmtime(item_path))
            page_name = item.replace(".py", "").replace("_", " ").title()
            relative_path = os.path.relpath(item_path, os.path.dirname(toc_file))
            toc_lines.append(f"{'  ' * indent}- [{page_name}](./{relative_path.replace(os.sep, '/')}) (последнее изменение: {last_modified})")
    return toc_lines

# Генерация оглавления
toc_content = ["# Оглавление\n"]

# База знаний
toc_content.append("## База знаний")
toc_content.extend(generate_toc(knowledge_base_folder, knowledge_base_folder))

# Исследования
if os.path.exists(notebook_folder):
    toc_content.append("\n## Исследование")
    toc_content.extend(generate_toc(notebook_folder, notebook_folder, include_ipynb=True))
else:
    print(f"Папка {notebook_folder} не найдена.")

# Эксперименты
if os.path.exists(experiments_folder):
    toc_content.append("\n## Эксперименты")
    toc_content.extend(generate_toc(experiments_folder, experiments_folder, include_py=True))
else:
    print(f"Папка {experiments_folder} не найдена.")

# MVP
if os.path.exists(MVP_folder):
    toc_content.append("\n## MVP")
    toc_content.extend(generate_toc(MVP_folder, MVP_folder, include_py=True))
else:
    print(f"Папка {MVP_folder} не найдена.")


# Запись в файл _toc.md
with open(toc_file, "w", encoding="utf-8") as f:
    f.write("\n".join(toc_content))

print(f"Оглавление обновлено в {toc_file}.")

