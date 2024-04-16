def content_combiner(dict1, dict2):
    combined_dict = dict1.copy()  # Create a copy of the first dictionary

    for key, value in dict2.items():
        if key not in combined_dict:
            combined_dict[key] = value  # Add key-value pairs from the second dictionary

    return combined_dict

# Test your function using the code below
if __name__ == '__main__':
    print(content_combiner({"gold": "Yellow"}, {"karats": 24}))
