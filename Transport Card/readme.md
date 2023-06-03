# Transport Card Problem - Python Technical Test
You are tasked with developing a fare card system that functions similarly to Madrid card system but with certain limitations. By the end of the test, you should be able to demonstrate a user loading a card with 50.00 EUR, undertaking specific trips, and then checking the remaining balance.

Here is the sequence of trips the user should take, along with the corresponding fares:

Travel from "Retiro" to "Atocha" via the metro.
Take the 27 bus from "Atocha" to "Puerto Chico".
Travel from "Atocha" to "Callao" via the metro.

### Operational details:

When the user enters the station through the entry barrier, their transport card will be charged the maximum fare.

Upon exiting the station through the exit barrier, the actual fare will be calculated and the maximum fare transaction will be replaced with the real transaction. If the user fails to swipe out, they will be charged the maximum fare.

All bus journeys will incur the same price.

The system should prioritize the customer's benefit in cases where multiple fares are possible for a given journey. For example, the fare from "Retiro" to "Atocha" is 2.50 EUR.

For this test, please utilize the following data:

Stations and Zones Table:

|   Station    |   Zone(s)  |
|--------------|------------|
|   Retiro     |     1      |
|    Atocha    |    1, 2    |
|   Barajas    |     3      |
|   Callao     |     2      |

Fares Table:

|             Journey                |   Fare   |
|------------------------------------|----------|
|     Anywhere in Zone 1             | 2.50 EUR |
| Any one zone outside zone 1        | 2.00 EUR |
| Any two zones including zone 1     | 3.00 EUR |
| Any two zones excluding zone 1     | 2.25 EUR |
|        Any three zones             | 3.20 EUR |
|         Any bus journey            | 1.80 EUR |

The maximum possible fare is therefore 3.20 EUR.


### Evaluation Criteria:
You will be evaluated based on the following points:

Compliance with Operational Requirements: Your solution should adhere to the specified operational requirements, including the fare calculation, and maximum fare charging.

Functionality and Requirement Fulfillment: Your solution should be fully functional and meet all the stated requirements. It should demonstrate the ability to load a card with 50 EUR, perform the designated trips, and display the remaining balance accurately.

Testing Methods and Coverage: Your testing approach should be comprehensive, covering different scenarios and edge cases. Thoroughly test your solution to ensure its correctness and reliability.

Design, Approach, and Elegance: Your solution's design and approach should be well-thought-out. Aim for an elegant solution that is efficient, maintainable, and extensible.

Please keep these evaluation criteria in mind as you develop and present your solution.