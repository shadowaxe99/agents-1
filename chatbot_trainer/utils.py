```python
from rasa.nlu.training_data import load_data
from rasa.nlu.config import RasaNLUModelConfig
from rasa.nlu.model import Trainer
from rasa.nlu import config
from rasa.nlu.model import Interpreter
import spacy

def train_nlu_model(data, configs, model_dir):
    training_data = load_data(data)
    trainer = Trainer(config.load(configs))
    trainer.train(training_data)
    model_directory = trainer.persist(model_dir, fixed_model_name='chatbot')

def load_interpreter(model_dir):
    return Interpreter.load(model_dir)

def predict_intent(interpreter, text):
    return interpreter.parse(text)

def load_spacy_model(model_name):
    return spacy.load(model_name)
```