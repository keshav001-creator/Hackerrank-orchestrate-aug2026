from data.data_loader import DataLoader
from processing.message_processor import MessageProcessor

def main():
    loader = DataLoader()

    loader.load_all()
    # print(list(loader.messages.columns))

    processor = MessageProcessor(loader)
    processor.process_messages()

        


if __name__ == "__main__":
    main()