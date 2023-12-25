from financial_forecast_modeler.utils import (double_exponential_smoothing,
                                              load_data, plot_data,
                                              preprocess_data,
                                              simple_exponential_smoothing,
                                              triple_exponential_smoothing)


def sweep_program(file_path):
    data = load_data(file_path)
    preprocessed_data = preprocess_data(data, column='date')
    plot_data(preprocessed_data, column='value')
    simple_smoothing_result = simple_exponential_smoothing(preprocessed_data, column='value')
    double_smoothing_result = double_exponential_smoothing(preprocessed_data, column='value')
    triple_smoothing_result = triple_exponential_smoothing(preprocessed_data, column='value')
    
    return simple_smoothing_result, double_smoothing_result, triple_smoothing_result
