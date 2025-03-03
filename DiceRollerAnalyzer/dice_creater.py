class DiceRoller:
    """A class that takes input from a user and creates dice based on the user input."""
    def __init__(self):
        self.min_sides = 2
        self.max_sides = 1000
        self.min_rolls = 1
        self.max_rolls = 100000000
        self.num_dice = 1

    def run(self):
        """Main method to run the die roll analyzer."""
        print("\nWelcome to the Die Roll Analyzer!\n")
        while True:
            # multi_dice_prompt = (
            #     "Would you like to create and roll multiple different sided dice at the same time? "
            #     "e.g. A D6 and a D10 (y/n): "
            # )
            # multiple_die_types = self.get_user_input_y_n(multi_dice_prompt)
            # if multiple_die_types:
            #     dice_type_specs = self.get_dice_types()
            #     dice_type_lists = self.create_multiple_dice_types(dice_type_specs)
            #     self.roll_all_dice(dice_type_lists)
            # else:
            #     # Prompt the user for the dice specifications
            #     num_sides_prompt = "\nHow many sides should each die have? (Enter a whole number greater than 1): "  
            #     num_dice_prompt = "How many dice would you like to roll? (Enter a whole number greater than 0): "
            #     num_sides = self.get_user_num_input(num_sides_prompt, 2)
            #     num_dice = self.get_user_num_input(num_dice_prompt, 1)
                
            #     # Create and roll the dice
            #     dice = self.create_single_dice_type(num_dice, num_sides)
            #     self.roll_dice_and_display_results(num_dice, num_sides, dice)
            
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

    # def get_dice_types(self):
    #     """Prompts the user for their dice types and adds them to a dictionary""" 
    #     # Set up the user prompts  
    #     num_types_prompt = "\nHow many different types of die would you like to roll? (Enter a whole number greater than 1): "
    #     num_types = self.get_user_num_input(num_types_prompt, 2)
    #     num_sides_prompt = "How many sides should this die type have? (Enter a whole number greater than 1): "
    #     num_dice_prompt = "How many of this die type would you like to roll? (Enter a whole number greater than 0): "
    #     dice_type_specs = {}

    #     # Prompt the user of the specifications for each die type and add them to the dictionary 
    #     for i in range(1, num_types + 1):
    #         print(f"\n-----Die type {i}-----") 
    #         while True:
    #             num_sides = self.get_user_num_input(num_sides_prompt, 2)
            
    #             if num_sides not in dice_type_specs:
    #                 num_dice = self.get_user_num_input(num_dice_prompt, 1)
    #                 dice_type_specs[num_sides] = num_dice
    #                 break
    #             else:
    #                 print(f"You are already going to be rolling some D{num_sides}s, please add a different type of die.\n")

    #     return dice_type_specs

    def create_single_dice_type(self, num_dice, num_sides):
        """Create a list of Die objects of a single type based on user input."""
        from .die import Die  # Import Die class here instead of at the top of the file to avoid circular imports in __init__.py
        return [Die(num_sides) for _ in range(num_dice)]
    
    # def create_multiple_dice_types(self, dice_type_specs):
    #     """Create a dictionary of single type Die object lists."""
    #     dice_type_lists = {}
    #     for key, value in dice_type_specs.items():
    #         dice_type_lists[key] = self.create_single_dice_type(value, key)
    #     return dice_type_lists

    # def roll_single_dice_type(self, num_dice, dice):
    #     """Roll all dice of a single type."""
    #     if num_dice > 1:
    #         roll_total = 0
    #         for i, die in enumerate(dice, 1):
    #             current_roll = die.roll_die()
    #             roll_total += current_roll
    #             print(f"Die {i} rolled: {current_roll}")
    #         return roll_total
    #     else:
    #         return dice[0].roll_die()
    
    # def roll_all_dice(self, dice_type_lists):
    #     """Roll all of the dice and display the results grouping them by dice type"""
    #     for num_sides, dice_list in dice_type_lists.items():
    #         num_dice = len(dice_list)
    #         self.roll_dice_and_display_results(num_dice, num_sides, dice_list)

    # def roll_dice_and_display_results(self, num_dice, num_sides, dice):
    #     """Roll the dice of a specified dice type and display the results"""
    #     print(f"Rolling your D{num_sides}s...\n")
    #     print(f"Your dice rolled a total of {self.roll_single_dice_type(num_dice, dice)}\n")
    
    def ask_to_roll_again(self):
        """Ask the user if they want to roll again"""
        prompt = "Would you like to roll more dice? (y/n): "
        roll_again = self.get_user_input_y_n(prompt)
        if roll_again == False:
            print("\nGoodbye!\n")
            exit()