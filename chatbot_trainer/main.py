```python
from rasa.train import train
from rasa.model import get_model, get_latest_model
from rasa.core.interpreter import NaturalLanguageInterpreter
from rasa.core.agent import Agent
from utils import load_data, preprocess_data

def train_chatbot(domain_file, config_file, training_data_file):
    model_path = train(domain_file, config_file, [training_data_file])
    return model_path

def load_chatbot_model(model_path):
    model = get_model(model_path)
    agent = Agent.load(model)
    return agent

def handle_message(agent, message):
    response = agent.handle_text(message)
    return response

if __name__ == "__main__":
    domain_file = "domain.yml"
    config_file = "config.yml"
    training_data_file = "data/stories.md"

    # Load and preprocess data
    data = load_data(training_data_file)
    preprocess_data(data)

    # Train the chatbot
    model_path = train_chatbot(domain_file, config_file, training_data_file)

    # Load the trained model
    agent = load_chatbot_model(model_path)

    # Test the chatbot with a sample message
    message = "Hello, chatbot!"
    response = handle_message(agent, message)
    print(response)
```