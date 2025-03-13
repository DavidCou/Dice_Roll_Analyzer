class DiceRoller:
    """A class that takes input from a user and creates dice based on the user input."""
    def __init__(self):
        self.min_sides = 2
        self.max_sides = 100
        self.min_rolls = 1
        self.max_rolls = 10_000_000
        self.num_dice = 1

    def run(self):
        """Main method to run the die roll analyzer."""
        print("\nWelcome to the Die Roll Analyzer!\n")
        while True:
            # Prompt the user for the dice specifications
            formated_max_rolls = "{:,}".format(self.max_rolls)
            num_sides_prompt = f"\nHow many sides should the die have? (Enter a whole number between {self.min_sides} and {self.max_sides}): "  
            num_rolls_prompt = f"How many times would you like to roll the die? (Enter a whole number between {self.min_rolls} and {formated_max_rolls}): "
            num_sides = self.get_user_num_input(num_sides_prompt, self.min_sides, self.max_sides)
            num_rolls = self.get_user_num_input(num_rolls_prompt, self.min_rolls, self.max_rolls)
            
            # Create the die
            dice = self.create_single_dice_type(self.num_dice, num_sides)

            # Roll the die, analyze and display the results
            from .dice_roll_analyzer import DiceRollAnalyzer
            # self.roll_dice_and_display_results(num_rolls, num_sides, dice)
            dice_roll_analyzer = DiceRollAnalyzer(num_rolls, dice)
            dice_roll_analyzer.create_and_display_results_graph() 
            
            self.ask_to_roll_again()
    
    def get_user_input_y_n(self, prompt):
        """Prompt the user for input, validate the responce and send a boolean value back if valid"""
        while True:
            try:
                responce = input(prompt)
                if responce == "y":
                    return True
                elif responce == 'n':
                    return False
                else:
                    raise ValueError("Invalid input! Enter either 'y' or 'n'.")
            except ValueError as e:
                print(e)
    
    def get_user_num_input(self, prompt, min_value, max_value):
        """Prompt the user for input and validate it as an integer greater than or equal to min_value."""
        while True:
            try:
                value = int(input(prompt))
                if value < min_value or value > max_value:
                    raise ValueError(f"Value must be a whole number greater than {min_value - 1} and less than to {max_value + 1}.")
                return value
            except ValueError as e:
                print(f"Invalid input! Please try again with a valid number.")

    def create_single_dice_type(self, num_dice, num_sides):
        """Create a list of Die objects of a single type based on user input."""
        from .die import Die  # Import Die class here instead of at the top of the file to avoid circular imports in __init__.py
        return [Die(num_sides) for _ in range(num_dice)]
    
    def ask_to_roll_again(self):
        """Ask the user if they want to roll again"""
        prompt = "Would you like to roll more dice? (y/n): "
        roll_again = self.get_user_input_y_n(prompt)
        if roll_again == False:
            print("\nGoodbye!\n")
            exit()