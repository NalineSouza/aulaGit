import java.math.BigDecimal;
import java.util.Scanner;

public class Main {
    public static void main(String[] args) {
        System.out.println("Informe dois numeros ");

        Scanner scanner = new Scanner(System.in);


        BigDecimal num =  scanner.nextBigDecimal();
        scanner.nextLine();

        BigDecimal num2 = scanner.nextBigDecimal();
        scanner.nextLine();

        System.out.println("Digite o simbolo da operaçao desejada");


        String operacao = scanner.nextLine();
        if (operacao.equals("*")) {
            BigDecimal resultado = num.multiply(num2);


            System.out.println("O resultado da operação é: "+resultado);
        }
    }
}
