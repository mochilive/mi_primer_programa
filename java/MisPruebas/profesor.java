public class profesor{
    static int numProfesores = 0;

    static void incrementaNumProfesores(){
        numProfesores++;
    }
    static void imprimeTotalProfesores(){
        System.out.println("Numero total de profesores " + numProfesores);
    }

    public static void main(String[] args){

        profesor.incrementaNumProfesores();
        profesor.imprimeTotalProfesores();
    }
}