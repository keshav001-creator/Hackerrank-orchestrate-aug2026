from data.data_loader import DataLoader


def main():
    loader = DataLoader()

    loader.load_all()

    print("All CSV files loaded successfully!\n")

    print("Messages:")
    print(loader.messages.head())

    print("\nUsers:")
    print(loader.users.head())


if __name__ == "__main__":
    main()