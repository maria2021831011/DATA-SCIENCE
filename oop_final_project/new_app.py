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
        self.__current_user = None
        self.first_menu()

    def first_menu(self):
        while True:
            choice = input("""
1. Register
2. Login
3. Exit
> """)

            if choice == "1":
                self.__register()
            elif choice == "2":
                self.__login()
            elif choice == "3":
                sys.exit("Goodbye 👋")
            else:
                print("Invalid choice!")

    def second_menu(self):
        while True:
            choice = input("""
1. Sentiment Analysis
2. Language Translation
3. Language Detection
4. Text Summarization
5. Grammar Correction
6. Paraphrase Text
7. Extract Keywords
8. Free Chat with AI
9. View Profile
10. Change Password
11. Logout
> """)

            if choice == "1":
                self._sentiment_analysis()
            elif choice == "2":
                self._language_translation()
            elif choice == "3":
                self._language_detection()
            elif choice == "4":
                self._summarize_text()
            elif choice == "5":
                self._grammar_correction()
            elif choice == "6":
                self._paraphrase_text()
            elif choice == "7":
                self._keyword_extraction()
            elif choice == "8":
                self._free_chat()
            elif choice == "9":
                self._view_profile()
            elif choice == "10":
                self._change_password()
            elif choice == "11":
                self.__current_user = None
                break
            else:
                print("Invalid option!")

    # ---------- AI FUNCTIONS ----------

    def _sentiment_analysis(self):
        text = input("Enter text: ")
        self._ask_ai(f"Analyze sentiment: {text}")

    def _language_translation(self):
        text = input("Enter text: ")
        self._ask_ai(f"Translate this into Bangla: {text}")

    def _language_detection(self):
        text = input("Enter text: ")
        self._ask_ai(f"Detect the language: {text}")

    def _summarize_text(self):
        text = input("Enter long text: ")
        self._ask_ai(f"Summarize this text: {text}")

    def _grammar_correction(self):
        text = input("Enter English text: ")
        self._ask_ai(f"Correct grammar of this text: {text}")

    def _paraphrase_text(self):
        text = input("Enter text: ")
        self._ask_ai(f"Paraphrase this sentence: {text}")

    def _keyword_extraction(self):
        text = input("Enter text: ")
        self._ask_ai(f"Extract important keywords: {text}")

    def _free_chat(self):
        text = input("Ask anything: ")
        self._ask_ai(text)

    def _ask_ai(self, prompt):
        model = self.get_model()
        response = model.generate_content(prompt)
        print("\nAI Response:\n", response.text)

    # ---------- USER FUNCTIONS ----------

    def _view_profile(self):
        print(f"\nLogged in as: {self.__current_user}")

    def _change_password(self):
        old = input("Old password: ")
        new = input("New password: ")

        if self.__database[self.__current_user] == old:
            self.__database[self.__current_user] = new
            print("Password changed successfully!")
        else:
            print("Incorrect old password!")

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
            self.__current_user = email
            print("Login successful!")
            self.second_menu()
        else:
            print("Invalid credentials!")


if __name__ == "__main__":
    ChatModel()
