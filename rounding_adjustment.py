import json

def adjust_rounded_numbers(input_json):
    numbers = input_json["numbers"]
    rounding_factor = 100000
    rounded_numbers = [round(num / rounding_factor, 2) for num in numbers]
    original_sum = sum(numbers)
    rounded_sum = round(original_sum / rounding_factor, 2)
    sum_of_rounded = sum(rounded_numbers)
    difference = round(rounded_sum - sum_of_rounded, 2)
    if difference != 0:
        rounded_numbers[0] += difference
    output_json = {
        "adjusted_numbers": rounded_numbers,
        "total_rounded_sum": rounded_sum
    }
    return output_json


def main():
    print("Enter JSON data directly or type 'file' to load from a file:")
    user_input = input()

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

    result = adjust_rounded_numbers(input_json)

    print("Adjusted output (JSON):")
    print(json.dumps(result, indent=4))

    save_option = input("Do you want to save the output to a file? (yes/no): ").strip().lower()
    if save_option == "yes":
        output_file = input("Enter the output file name (e.g., output.json): ").strip()
        try:
            with open(output_file, "w") as f:
                json.dump(result, f, indent=4)
            print(f"Output saved to {output_file}")
        except Exception as e:
            print(f"Error saving to file: {e}")


if __name__ == "__main__":
    main()
