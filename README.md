#Planetary Query System

Our Python script is designed to provide information about all of the planets in the solar system. Users can type in questions about a planet’s mass, distance from the sun, or moons, and the script will pull it out from our data base and return the relevant information.

How my Code works?

##1. Planet Class:

The script defines a Planet class that serves as a base for storing planetary data as requested from our task requerements. The class has:

    An "__init__" method that contains the planets' name, mass, distance from the sun, and moons.

    The "getter methods (get_name(), get_mass(), etc.)" allow us to access this data separately as a function.

This setup ensures that each planet has its own information, and it is available in a timely manner as needed.

##2. Our Dictionary:

Instead of creating separate objects for each planet, the script stores all planetary data. Each planet’s mass, distance from the Sun, and moons are stored as key-value pairs.

This makes it easy to look up planetary information very simply.

##3. Our "query_planet" function:

This function is responsible for analyzing a question and finding the correct response. It does this by converting the user’s input to lowercase to avoid case-sensitivity issues.

    We are also using regular expressions such as "(re.search)" to detect different ways of asking for the same information even if the person has made a minor spelling mistake or has rephrased their question.

 "How massive is Jupiter?"

 "What is the mass of Jupiter?"

  "How heavy is Jupiter?"

#All of these questions are asking the same thing. The function will return without a fail:

"The mass of Jupiter is 1.8982×10^27 kg"

The same logic applies to all other questions.

##4. Handling Pluto Separately:

Since poor Pluto is often under a heated debate, the script includes a special case. If our user asks:

 "Is Pluto a planet?"

 "Does Pluto exist in the database?"

The script responds with: "Pluto is classified as a dwarf planet" (and then displays Pluto’s details).

This ensures that Pluto’s planetary status is acknowledged with sensitivity and transparency about the problem. 

##5. The Loop "(while True)":

Our script allows the user to keep asking questions meanwhile the program will continue running until the user types "exit". Each time the user inputs a question, the returns the answer.


#Key Strengths to our methods:

    The user can inquire in different ways about the planetary data.

    The user doesn’t have to worry about precise spelling and grammar.

    Using our storage of data for all planetary information in one place, makes it easy to manipulate later and apply changes to our script below, while being able to record and backtrack any issues for troubleshooting without messing up with the entire code. 

    It is exactly the function "query_planet" that enables us to separate the code from the data and add more features later.

    Because of the "re.search" method, the script can recognize varieties of synonyms and handle them correctly.

    The "if __name__ == "__main__" statement ensures that our script will only run if we execute it, and will not initiate itself automatically if it is imported somewhere else.

#Conclusion:

##Our script contains:

    Locally stored data with the Planet class.

    The utilization of dictionaries for structured data storage.

   Expressions such as "(re.search)" for flexibility.

    A loop-based user interface for continuous interaction until ceased. 
