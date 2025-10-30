def print_model(unprinted_designs, completed_models):
    while unprinted_designs:
        current_design = unprinted_designs.pop()
        print(f"Printing model: {current_design}")
        completed_models.append(current_design)

def show_completed_models(completed_models):
    print("\nWe print these models already:")
    for checkmarks in completed_models:
        print(checkmarks)

unprinted_designs = ['outler cover', 'laptop case', 'toothbrush']
completed_models = []

print_model(unprinted_designs, completed_models)
show_completed_models(completed_models)