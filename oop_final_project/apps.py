import google.generativeai as genai
from dotenv import load_dotenv
import os
import sys

load_dotenv()
genai.configure(api_key=os.getenv("GENAI_API_KEY"))

class BaseModel:
    def get_model(self):
        return genai.GenerativeModel("gemini-2.5-flash")


class ChatModel(BaseModel):
    def __init__(self):
        self.__database = {}
        self.first_menu()

    def first_menu(self):
        while True:
            choice = input("""
Hi! How would you like to proceed?

1. Register
2. Login
3. Exit
> """)

            if choice == "1":
                self.__register()
            elif choice == "2":
                self.__login()
            elif choice == "3":
                sys.exit("Goodbye!")
            else:
                print("Invalid choice!")

    def second_menu(self):
        while True:
            choice = input("""
Choose an option:

1. Sentiment Analysis
2. Language Translation
3. Language Detection
4. Logout
> """)

            if choice == "1":
                self._sentiment_analysis()
            elif choice == "2":
                self._language_translation()
            elif choice == "3":
                self._language_detection()
            elif choice == "4":
                break
            else:
                print("Invalid option!")

    def _sentiment_analysis(self):
        text = input("Enter text: ")
        model = self.get_model()
        response = model.generate_content(
            f"Analyze sentiment of this sentence: {text}"
        )
        print(response.text)

    def _language_translation(self):
        text = input("Enter text: ")
        model = self.get_model()
        response = model.generate_content(
            f"Translate this sentence into Bangla: {text}"
        )
        print(response.text)

    def _language_detection(self):
        text = input("Enter text: ")
        model = self.get_model()
        response = model.generate_content(
            f"Detect the language of this sentence: {text}"
        )
        print(response.text)

    def __register(self):
        email = input("Email: ")
        password = input("Password: ")

        if email in self.__database:
            print("User already exists!")
        else:
            self.__database[email] = password
            print("Registration successful!")

    def __login(self):
        email = input("Email: ")
        password = input("Password: ")

        if self.__database.get(email) == password:
            print("Login successful!")
            self.second_menu()
        else:
            print("Invalid credentials!")


if __name__ == "__main__":
    app = ChatModel()
