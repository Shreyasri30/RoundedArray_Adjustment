import json

def flatten_nested_numbers(nested_list):
    flat_list = []
    
    def recursive_flatten(sublist):
        for item in sublist:
            if isinstance(item, list):  
                recursive_flatten(item)  
            elif isinstance(item, (int, float)):  
                flat_list.append(item)  

    recursive_flatten(nested_list)
    return flat_list

def reconstruct_nested_numbers(nested_list, adjusted_flat_list):
    reconstructed = []
    for item in nested_list:
        if isinstance(item, list):
            reconstructed.append(reconstruct_nested_numbers(item, adjusted_flat_list))
        else:
            reconstructed.append(adjusted_flat_list.pop(0))  
    return reconstructed

def adjust_rounded_numbers_with_nested(input_json):
    numbers = input_json["numbers"]
    flat_numbers = flatten_nested_numbers(numbers)
    rounding_factor = 100000
    original_sum = sum(flat_numbers)  
    correct_rounded_sum = round(original_sum / rounding_factor, 2)  
    rounded_numbers = [round(num / rounding_factor, 2) for num in flat_numbers]
    sum_of_rounded = round(sum(rounded_numbers), 2)  

    print("\nFlattened Numbers (Check this list):", flat_numbers)
    print("Correct Original Sum:", original_sum)
    print("Correct Rounded Total (Expected):", correct_rounded_sum)
    print("Sum of Individually Rounded Numbers:", sum_of_rounded)

    difference = round(correct_rounded_sum - sum_of_rounded, 2)
    print("Adjustment Difference:", difference)
    if difference != 0:
        num_elements = len(rounded_numbers)
        adjust_per_element = round(difference / num_elements, 4)  
        for i in range(num_elements):
            if abs(difference) < 0.01:  
                break
            rounded_numbers[i] = round(rounded_numbers[i] + adjust_per_element, 2)
            difference = round(correct_rounded_sum - sum(rounded_numbers), 2)  

    adjusted_numbers_nested = reconstruct_nested_numbers(numbers, rounded_numbers.copy())

    output_json = {
        "adjusted_numbers": adjusted_numbers_nested,
        "total_rounded_sum": correct_rounded_sum
    }

    return output_json

def main():
    print("Enter JSON data directly or type 'file' to load from a file:")
    user_input = input().strip()

    if user_input.lower() == "file":
        file_path = input("Enter the file path for input JSON: ").strip()
        try:
            with open(file_path, "r") as f:
                input_json = json.load(f)
        except FileNotFoundError:
            print("File not found. Please check the path and try again.")
            return
        except json.JSONDecodeError:
            print("Invalid JSON in the file. Please check the content and try again.")
            return
    else:
        try:
            input_json = json.loads(user_input)
        except json.JSONDecodeError:
            print("Invalid JSON. Please enter valid JSON data.")
            return

    result = adjust_rounded_numbers_with_nested(input_json)

    print("\nAdjusted Output (Formatted JSON):")
    print(json.dumps(result, indent=4))

    save_option = input("\nDo you want to save the output to a file? (yes/no): ").strip().lower()
    if save_option == "yes":
        output_file = input("Enter the output file name (e.g., output.json): ").strip()
        try:
            with open(output_file, "w", encoding="utf-8") as f:
                json.dump(result, f, indent=4)
            print(f"Output successfully saved to {output_file}")
        except OSError as e:
            print(f"Error: Unable to save the file. {e}")

if __name__ == "__main__":
    main()
