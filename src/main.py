
from src.preprocess import load_chat_data
from src.analysis_mvp import analyze_messages
from src.visualization import visualize_message_distribution

chat_data = load_chat_data('data/sample.json')
print(chat_data.head())

# Analyze data
distribution = analyze_messages(chat_data)

# Visualize data
visualize_message_distribution(distribution)














