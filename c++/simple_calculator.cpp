// Day 1: Simple Calculator

// Concepts implemented:
//   -> 'if/else' conditions
//   -> 'while' loop
//   -> functions


#include<iostream>

//calculator functions
int add(int num1, int num2)
{
	return num1 + num2;
}
int subtract(int num1, int num2)
{
	return num1 - num2;
}
int multiply(int num1, int num2)
{
	return num1 * num2;
}
int quotient(int num1, int num2)
{
	return num1 / num2;
}
int remainder(int num1, int num2)
{
	return num1 % num2;
}

//print functions
void menu()
{
	std::cout << "*********** MENU ***********\n\n";
	std::cout << "KEYCODE          FUNCTION\n";
	std::cout << "  0                Exit\n";
	std::cout << "  1                Add\n";
	std::cout << "  2              Subtract\n";
	std::cout << "  3              Multiply\n";
	std::cout << "  4               Divide\n";
	std::cout << "\n*****************************\n\n";
}
void exitMessage() 
{
	std::cout << "\n\nBye bye! See you next time! :)\n\n";
}


int main()
{
	int userInput = -1;
	bool isExited = false; //check if user has exited the calculator
	int num1 = -1;
	int num2 = -1;

	std::cout << "Welcome to my Simple Calculator! I got the solution to all your arithmetic needs!\n\n";

	while (!isExited)
	{
		menu(); //print menu

		do
		{
			std::cout << "Please enter the function you would like to perform: ";
			std::cin >> userInput;

		} while (userInput < 0 || userInput > 4); //make sure it's between 0 and 4

		if (userInput == 0) //Exit
		{
			isExited = true;
			continue;
		}
		else if (userInput == 1) //Addition
		{
			std::cout << "\n------ ADDITION ------\n";
			std::cout << "FORMAT: A + B\n\n";

			std::cout << "Enter A: ";
			std::cin >> num1;

			std::cout << "Enter B: ";
			std::cin >> num2;
			
			std::cout << "\n-> " << num1 << " + " << num2 << " = " << add(num1, num2);
			
			std::cout << "\n----------------------\n\n\n\n";
		}
		else if (userInput == 2) //Subtraction
		{
			std::cout << "\n------ SUBTRACTION ------\n";

			std::cout << "FORMAT: A - B\n\n";

			std::cout << "Enter A: ";
			std::cin >> num1;

			std::cout << "Enter B: ";
			std::cin >> num2;

			std::cout << "\n ->" << num1 << " - " << num2 << " = " << subtract(num1, num2);

			std::cout << "\n----------------------\n\n\n\n";
		}
		else if (userInput == 3) //Multiplication
		{
			std::cout << "\n------ MULTIPLICATION ------\n";

			std::cout << "FORMAT: A * B\n\n";

			std::cout << "Enter A: ";
			std::cin >> num1;

			std::cout << "Enter B: ";
			std::cin >> num2;

			std::cout << "\n-> " << num1 << " * " << num2 << " = " << multiply(num1, num2);

			std::cout << "\n----------------------\n\n\n\n";
		}
		else if (userInput == 4) //Division
		{
			std::cout << "\n------ DIVISION ------\n";

			std::cout << "FORMAT: A / B\n\n";

			std::cout << "Enter A: ";
			std::cin >> num1;

			std::cout << "Enter B: ";
			std::cin >> num2;

			std::cout << "\n-> " << num1 << " / " << num2 << " = " << quotient(num1, num2) << " r " << remainder(num1, num2);

			std::cout << "\n----------------------\n\n\n\n";
		}

	}
	
	exitMessage();

	return 0;
}
