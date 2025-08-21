import weather_transport_data as wtd

def menu():
    while True:
        print("\n=== Sydney Weather & Transport Analysis ===")
        print("1. View Summary Statistics")
        print("2. Plot Rainfall vs Train On-Time %")
        print("3. Plot Temperature Trends")
        print("4. View First 10 Rows of Dataset")
        print("5. Quit")

        choice = input("Enter choice: ")

        if choice == "1":
            wtd.summary_statistics()
        elif choice == "2":
            wtd.plot_rainfall_vs_trains()
        elif choice == "3":
            wtd.plot_temp_trends()
        elif choice == "4":
            wtd.view_full_dataset()
        elif choice == "5":
            print("Exiting program. Goodbye!")
            break
        else:
            print("Invalid choice, please try again.")

if __name__ == "__main__":
    menu()
