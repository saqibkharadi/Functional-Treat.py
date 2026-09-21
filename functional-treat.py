# Global variable to store dataset summary
global_summary = {}


def factorial(n):
    """Calculates the factorial of a number using recursion."""
    if n == 0 or n == 1:
        return 1
    return n * factorial(n - 1)


def get_stats(data):
    """Calculates and returns multiple statistics for the dataset."""
    total_elements = len(data)
    min_val = min(data)
    max_val = max(data)
    sum_val = sum(data)
    avg_val = round(sum_val / total_elements, 2)
    return min_val, max_val, sum_val, avg_val


def display_kwargs(**kwargs):
    """Displays dataset characteristics using **kwargs."""
    for key, value in kwargs.items():
        print(f"- {key}: {value}")


data_list = []

print("Welcome to the Data Analyzer and Transformer Program")

while True:
    print("\nMain Menu:")
    print("1. Input Data")
    print("2. Display Data Summary (Built-in Functions)")
    print("3. Calculate Factorial (Recursion)")
    print("4. Filter Data by Threshold (Lambda Function)")
    print("5. Sort Data")
    print("6. Display Dataset Statistics (Return Multiple Values)")
    print("7. Exit Program")

    choice = input("Please enter your choice: ")

    if choice == "1":
        user_input = input(
            "\nEnter data for a 1D array (separated by spaces):\n"
        )
        # Convert input string into a list of integers
        data_list = [int(x) for x in user_input.split()]

        # Update global summary variable
        global_summary
        if data_list:
            global_summary["Total elements"] = len(data_list)
            global_summary["Average value"] = round(
                sum(data_list) / len(data_list), 2
            )

        print("\nData has been stored successfully!")

    elif choice == "2":
        if not data_list:
            print("\nPlease input data first!")
            continue

        print("\nData Summary:")
        print(f"- Total elements: {len(data_list)}")
        print(f"- Minimum value: {min(data_list)}")
        print(f"- Maximum value: {max(data_list)}")
        print(f"- Sum of all values: {sum(data_list)}")

        avg = round(sum(data_list) / len(data_list), 2)
        print(f"- Average value: {avg}")

    elif choice == "3":
        num = int(
            input("\nEnter a number to calculate its factorial:\n")
        )
        result = factorial(num)
        print(f"\nFactorial of {num} is: {result}")

    elif choice == "4":
        if not data_list:
            print("\nPlease input data first!")
            continue

        threshold = int(
            input(
                "\nEnter a threshold value to filter out data above this value:\n"
            )
        )
        filtered = list(filter(lambda x: x >= threshold, data_list))

        filtered_str = ", ".join(str(x) for x in filtered)
        print(f"\nFiltered Data (values >= {threshold}):")
        print(filtered_str)

    elif choice == "5":
        if not data_list:
            print("\nPlease input data first!")
            continue

        print("\nChoose sorting option:")
        print("1. Ascending")
        print("2. Descending")

        sort_choice = input("\nEnter your choice: ")

        temp_list = data_list.copy()

        if sort_choice == "1":
            temp_list.sort()
            sorted_str = ", ".join(str(x) for x in temp_list)
            print("\nSorted Data in Ascending Order:")
            print(sorted_str)
        elif sort_choice == "2":
            temp_list.sort(reverse=True)
            sorted_str = ", ".join(str(x) for x in temp_list)
            print("\nSorted Data in Descending Order:")
            print(sorted_str)
        else:
            print("Invalid sorting option!")

    elif choice == "6":
        if not data_list:
            print("\nPlease input data first!")
            continue

        min_val, max_val, sum_val, avg_val = get_stats(data_list)

        print("\nDataset Statistics:")
        print(f"- Minimum value: {min_val}")
        print(f"- Maximum value: {max_val}")
        print(f"- Sum of all values: {sum_val}")
        print(f"- Average value: {avg_val}")

    elif choice == "7":
        print(
            "\nThank you for using the Data Analyzer and Transformer Program. Goodbye!"
        )
        break

    else:
        print("Invalid choice! Please select a valid option.")
