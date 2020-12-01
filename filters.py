__all__ = ["require_debug_true_filter", "require_debug_false_filter"]

DEBUG = True

def require_debug_true_filter():
    """Only process records when DEBUG is True"""
    def filter(record):
        return DEBUG

    return filter

def require_debug_false_filter():
    """Only process records when DEBUG is False"""
    def filter(record):
        return not DEBUG
    
    return filter
