def log_function_call(func):
    def wrapper(*args, **kwargs):
        print(f"Function {func.__name__} called with arguments: {args} {kwargs}")
        return func(*args, **kwargs)
    return wrapper

# Example of using the decorator in LegalAdvisor class methods
class LegalAdvisor:
    def __init__(self, dataset):
        self.dataset = dataset

    @log_function_call
    def provide_advice(self, query):
        return f"Advice based on your query: '{query}' is under development."