 import java.util.Scanner;

public class Main {
    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);
        System.out.print("Qual é seu nome: ");
        String name = scanner.nextLine();
        System.out.println("Hello " + name + "!");
        System.out.print("Qual sua idade? ");
        int idade = scanner.nextInt();
        System.out.println(name +  " tem " + idade + " anos.");
        scanner.close();

        if (idade >= 18) {
            System.out.println("É maior de idade.");
        } else {
            System.out.println("É menor de idade.");
        }

    }
}

