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

        int idade = 0;
        scanner = new Scanner(System.in);
        while (idade < 18) {
            System.out.print("Qual sua idade? ");
            idade = scanner.nextInt();
            scanner.close();    
                break;
        }
        System.out.println(name +  " tem " + idade + " anos.");

    }
    
}

