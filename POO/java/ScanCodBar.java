import java.util.Scanner;

public class ScanCodBar {

    public static void main(String[] args) {
        // Cria scanner
        Scanner scan = new Scanner(System.in);

        // Inicia vars
        double[] precos = {0.5, 1, 4, 7, 8};
        int[] compraQtds = {0, 0, 0, 0, 0};
        int codNum;
        int qtdNum;

        while(true) {
            // Solicita código
            System.out.print("Digite o Cod. do produto: ");
            String cod = scan.nextLine();
            
            // Para de solicitar se digitar 0
            if(cod.equals("0"))
                break;

            // Solicita quantidade do produto
            System.out.print("Digite a qtd: ");
            String qtd = scan.nextLine();

            try {
                // Converte para inteiro
                codNum = Integer.parseInt(cod);
                // Converte para inteiro
                qtdNum = Integer.parseInt(qtd);
            } catch (Exception e) {
                // Para de solicitar se ser erro
                System.out.println("Erro: Digite um número!");
                break;
            }
            
            // Para de solicitar se código inválido
            if(codNum < 0 || codNum >= 5) {
                System.out.println("Código inválido!");
                break;
            }
            
            // Adiciona produtos a compra
            compraQtds[codNum] += qtdNum;
        }
        
        // Calcula total
        double total = 0;
        for(int i = 0; i < 5; i++) {
            total += compraQtds[i] * precos[i];
        }

        System.out.println("Total: "+total);

    }
}