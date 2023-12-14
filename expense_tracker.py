# expense_tracker.py
from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
from kivy.uix.textinput import TextInput
from kivy.uix.button import Button
from kivy.uix.scrollview import ScrollView
from kivy.uix.spinner import Spinner



class ExpenseTrackerApp(App):
    def build(self):
        # Main layout
        layout = BoxLayout(orientation='vertical', spacing=10, padding=10)

        # Title label
        title_label = Label(text="Expense Tracker", font_size='24sp')
        layout.add_widget(title_label)

        # Input and button layout
        input_layout = BoxLayout(orientation='horizontal', spacing=10)

        # Date Picker (Text input for date)
        self.date_input = TextInput(text="Select date", multiline=False)
        input_layout.add_widget(self.date_input)

        # Input field for entering expense
        self.expense_input = TextInput(hint_text="Enter expense amount", multiline=False, input_filter='float')
        input_layout.add_widget(self.expense_input)

        # Category label and input
        self.category_input = Spinner(text="category:", values=["Food", "Transportation", "Utilities", "Entertainment", "Other"])
        input_layout.add_widget(self.category_input)

        # Button to add expense
        add_expense_button = Button(text="Add Expense", on_press=self.add_expense)
        input_layout.add_widget(add_expense_button)

        layout.add_widget(input_layout)

        # Display total expenses
        self.total_expenses = 0
        self.total_expenses_label = Label(text="Total Expenses: ${:.2f}".format(self.total_expenses),
                                          size_hint_y=None, height=30)
        layout.add_widget(self.total_expenses_label)

        # Expense history scrollview
        scroll_view = ScrollView()
        self.expense_history = []
        self.expense_history_label = Label(text="Expense History:\n", size_hint_y=None, height=200)
        scroll_view.add_widget(self.expense_history_label)
        layout.add_widget(scroll_view)

        # Clear history button
        clear_history_button = Button(text="Clear History", on_press=self.clear_history)
        layout.add_widget(clear_history_button)

        return layout


    def add_expense(self, instance):
        try:
            date = self.date_input.text
            category = self.category_input.text
            expense_amount = float(self.expense_input.text)
            self.total_expenses += expense_amount
            self.total_expenses_label.text = "Total Expenses: ${:.2f}".format(self.total_expenses)
            self.expense_history.append((date, category, expense_amount))
            self.expense_history_label.text = self.format_expense_history()
            self.expense_input.text = ""  # Clear the input field
        except ValueError:
            self.expense_input.text = "Invalid Input"

    def clear_history(self, instance=None):
        self.expense_history = []
        self.expense_history_label.text = "Expense History:\n"

    def format_expense_history(self):
        return "\n".join(["{}: {} ${:.2f}".format(date, category, expense) for date, category, expense in self.expense_history])

if __name__ == '__main__':
    ExpenseTrackerApp().run()
