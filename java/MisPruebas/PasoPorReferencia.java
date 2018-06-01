class PasoPorReferencia{
    static void modificaVector(int[] numeros){
        for(int i = 0; i < numeros.length; i++){
            numeros[i] = 0;
        }
    }

    static void rellenaVector(int[] numeros){
        for(int i = 0; i < numeros.length; i++){
            numeros[i] = 4;
        }
    }

    static void imprimeVector(int[] numeros){
        for(int i = 0; i < numeros.length; i++){
            System.out.println("" + numeros[i]);
        }
    }

    public static void main(String[] args){
        int[] numero = new int[10];
        PasoPorReferencia.rellenaVector(numero);
        System.out.println("Valor antes");
        PasoPorReferencia.imprimeVector(numero);
        System.out.println("Valor despues");
        PasoPorReferencia.modificaVector(numero);
        PasoPorReferencia.imprimeVector(numero);

    }
}