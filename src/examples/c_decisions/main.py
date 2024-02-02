import decisions

result = decisions.get_and_result(False, True)
print(result)
result = decisions.get_or_result(True, False)
print(result)
result = decisions.get_not_result(False)
print(result)


