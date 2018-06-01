class PasoPorValor{
    public static void calculaNumero(int numero){
        int numero2 = 5;
        numero = numero2 * numero;
    }

    public static void main(String[] args){
        int numero = 10;
        PasoPorValor.calculaNumero(numero);
        System.out.println("Valor antes= " + numero);
        System.out.println("Valor despues= "+ numero);
    }
}