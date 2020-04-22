import java.util.Scanner;

class Fibo {
    public static void main(String[] args) {

        Scanner input = new Scanner(System.in);
        int number;

        System.out.print("Enter an integer: ");

        if (input.hasNextInt()) {
            number = input.nextInt();
            if (number < 2000) {
                printFibonacci(number);
            } else {
                System.out.println("Please enter a valid number");
            }
        } else {
            System.out.println("Please enter a number");
        }
    }

    private static void printFibonacci(int number) {

        int previousNumber = 0;
        int nextNumber = 1;

        System.out.print(number+"th term of the Fibonacci Series is: ");

        for (int i = 1; i <= number; ++i)
        {

            if (i == number){
                System.out.println(previousNumber);
            }

            int sum = previousNumber + nextNumber;
            previousNumber = nextNumber;
            nextNumber = sum;
        }
    }
}