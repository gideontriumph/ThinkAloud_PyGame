"""
    Name: Jarvis1.py
    Author: Triumph Ogbonnia
    Created: 3/19/24
    Purpose: A small version of Jarvis
"""

import wikipedia
from rich.console import Console
from rich.panel import Panel
import pyttsx3
import datetime
import speech_recognition as sr

# Initialize the console
console = Console()

# Print a nice title using Rich
console.print(
    Panel.fit(
        "===  J.A.R.V.I.S  ===",
        style="bold blue",
        subtitle="By Python Triumph"
    )
)

# Define the commands
commands = """
[bold cyan]Commands:[/bold cyan]
1. "Wikipedia" to start a search.
2. "time" to hear the current time.
3. "temperature" to convert between Fahrenheit and Celsius
4. "calculator" to perform a math calculation.
5. "quit" to exit the program.
"""

# Print out the commands at the start of the program
console.print(commands)

class Jarvis:
    def __init__(self):
        self._summary = None  # Initialize _summary attribute
        self.engine = pyttsx3.init()
        self.recognizer = sr.Recognizer()

    def run(self):
        while True:
            command = self.get_command()
            if command.lower() == "quit":
                console.print("[bold cyan]Jarvis shutting down . . .\n Goodbye![/bold cyan]")
                self.say("Jarvis shutting down. Goodbye!")
                break
            elif command.lower() == "time":
                self.tell_time()
            elif command.lower() == "temperature":
                self.temperature_conversion()
            elif command.lower() == "calculator":
                self.math_calculation()
            elif command.lower() == "wikipedia":
                self.get_wikipedia()
            else:
                self.say("Invalid command. Please try again.")

    def get_command(self):
        try:
            with sr.Microphone() as source:
                console.print("\n[green]Waiting for command . . .[/green]")
                audio = self.recognizer.listen(source)
                console.print("[green]Processing . . .[/green]")
                command = self.recognizer.recognize_google(audio)
                console.print("[green]Command:[/green]", command, "\n")
                return command
        except sr.UnknownValueError:
            console.print("[bold red]Sorry, I couldn't understand the command. Please try again.[/bold red]")
            return ""
        except sr.RequestError:
            console.print("[bold red]Could not request results. Please check your internet connection.[/bold red]")
            return ""

    def get_wikipedia(self):
        """
        Search Wikipedia using voice input after the command "Wikipedia"
        """
        try:
            # Initialize speech recognition
            r = sr.Recognizer()
            with sr.Microphone() as source:
                console.print("[bold blue]Waiting for search term. . .[/bold blue]")
                audio = r.listen(source)

            try:
                # Recognize speech input for search term
                query = r.recognize_google(audio)
                # Get Wikipedia summary based on user input
                self._summary = wikipedia.summary(query, sentences=3)
                self.display_wikipedia()
            # Handle exceptions
            except sr.UnknownValueError:
                console.print("[bold red]Sorry, I could not understand the search term. Please try again.[/bold red]")

        except Exception as e:
            # Handle exceptions
            console.print("[red]Error: {}[/red]".format(e))
            console.print("[red]Please try again.[/red]")

    def display_wikipedia(self):
        """
        Display Wikipedia search results
        """
        if self._summary:
            # Display search result and say the summary
            console.print("[bold blue]\nResult >> [/bold blue]", self._summary)
            self.say(self._summary)
        else:
            console.print("[bold red]No search result to display. Please perform a Wikipedia search first.[/bold red]")

    def tell_time(self):
        """
        Tells the user the current time.
        """
        # Get the current time
        current_time = datetime.datetime.now().strftime("%I:%M %p")
        # Speak the current time
        self.say(f"The current time is {current_time}")
        # Print the current time
        console.print(f"[bold blue]Current Time >>[/bold blue] {current_time}")

    def temperature_conversion(self):
        """
        Converts temperature between Fahrenheit and Celsius.
        """
        try:
            # Initialize speech recognition
            r = sr.Recognizer()
            with sr.Microphone() as source:
                console.print("[bold blue]Enter the temperature value >> [/bold blue]")
                self.say("Enter the temperature value")
                audio = r.listen(source)
                temperature = float(r.recognize_google(audio))

                console.print("[bold blue]Enter the unit (Fahrenheit or Celsius) >> [/bold blue]")
                self.say("Fahrenheit or Celsius")
                audio = r.listen(source)
                unit = r.recognize_google(audio).lower()

                if unit == 'fahrenheit':
                    # Convert Fahrenheit to Celsius
                    converted_temperature = int(temperature - 32) * 5/9
                    console.print(f"[bold blue]Temperature in Celsius >>[/bold blue] {converted_temperature:.2f}°C")
                    self.say(f"The temperature in Celsius is {converted_temperature:.2f} degrees Celsius")
                elif unit == 'celsius':
                    # Convert Celsius to Fahrenheit
                    converted_temperature = (temperature * 9/5) + 32
                    console.print(f"[bold blue]Temperature in Fahrenheit >> [/bold blue] {converted_temperature:.2f}°F")
                    self.say(f"The temperature in Fahrenheit is {converted_temperature:.2f} degrees Fahrenheit")
                else:
                    console.print("[bold red]Invalid unit. Please enter either 'Fahrenheit' or 'Celcius'.[/bold red]")
        except Exception as e:
            console.print("[bold red]An error occurred. Please try again.[/bold red]")
            console.print("[bold red]Error: {}[/bold red]".format(e))

    def math_calculation(self):
        """
        Performs a math calculation.
        """
        # Initialize speech recognition
        r = sr.Recognizer()
        with sr.Microphone() as source:
            console.print("[bold blue]Enter a math expression to calculate >> [/bold blue]")
            self.say("What would you like to calculate")
            audio = r.listen(source)
            expression = r.recognize_google(audio)
        
        try:
            # Evaluate the expression
            result = eval(expression)
            console.print(f"[bold blue]Result >>[/bold blue] {result}")
            self.say(f"The result is {result}")
        except Exception as e:
            console.print("[bold red]Error occurred while performing calculation. Please check your expression.[/bold red]")

    def say(self, text):
        """
        Function to speak given text
        """
        self.engine.say(text)
        self.engine.runAndWait()

# Create a Jarvis program object
jarvis = Jarvis()

# Run the program
jarvis.run()