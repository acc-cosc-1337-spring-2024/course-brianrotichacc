# In the decisions.py folder, create function named get_options_ratio that accepts two parameters 
# with names option, total and returns the ratio.
def get_options_ratio(option, total):
    ratio = option/total
    return ratio

def get_faculty_rating(ratio):
    if 0.9 <= ratio < 1:
        return "Excellent"
    elif ratio > 0.8:
        return "Very Good"
    elif ratio > 0.7:
        return "Good"
    elif ratio > 0.6:
        return "Needs Improvement"
    else: #covers the case of 0 to 0.59
        return "Unacceptable"
    

