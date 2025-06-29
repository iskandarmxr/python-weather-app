def print_section(title):
    print("\n" + "="*40)
    print(f"{title}")
    print("="*40)

def display_data(data):
    if not data:
        print("No data available.")
        return
    for item in data:
        for key, value in item.items():
            print(f"{key}: {value}")
        print("-" * 30)