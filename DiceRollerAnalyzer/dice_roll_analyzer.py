import plotly.express as px

class DiceRollAnalyzer:
    "A class that collects a set of created dice, rolls them, analyzes the results, and visualizes the outcomes on a graph."
    def __init__(self, num_rolls, dice):
        """Set the number of times the dice will be rolled"""
        self.num_rolls = num_rolls
        self.dice = dice
        self.final_results = self.collect_roll_results()
        self.poss_results = self.get_possable_results()

    def collect_roll_results(self):
        """Roll the dice and add the results to a list."""
        # Make some rolls, and store results in a list.
        print("Creating and rolling your die...")
        final_results = []
        for _ in range(self.num_rolls):
            result = self.dice[0].roll_die()
            final_results.append(result)
        return final_results 
    
    def get_possable_results(self):
        return range(1, self.dice[0].num_sides+1)

    def analyze_roll_results(self):
        "Sort the roll results by how often of each die side is landed on."
        # Analyze the results.
        print("Analyzing your roll results...")
        frequencies = []
        for value in self.poss_results:
            frequency = self.final_results.count(value)
            frequencies.append(frequency)
        return frequencies
    
    def create_and_display_results_graph(self):
        """Create and display a graph based on how often of each die side is landed on"""
        # Visualize the results.
        formanted_roll_num = "{:,}".format(self.num_rolls)
        frequencies = self.analyze_roll_results()
        title = f"Results of Rolling 1 D{self.dice[0].num_sides} Dice {formanted_roll_num} Times"
        labels = {'x': 'Result', 'y': 'Frequency of Result'}
        fig = px.bar(x=self.poss_results, y=frequencies, title=title, labels=labels)

        # Further customize chart.
        fig.update_layout(xaxis_dtick=1)
        fig.show()