//importamos libreria Scanner
import java.util.Scanner;

class IntroduccionJava1{

    public static void main(String[] args){
        //creamos objeto Scanner
        Scanner sc = new Scanner(System.in);
        //creamos variable de tipo entero
        int opc;
        //tienes que elegir entre 1 - for o 2 - while (tienes que elegir con numeros)
        System.out.print("Que quieres usar: FOR(1)/WHILE(2) ? ");
        opc = sc.nextInt();

        //si el numero seleccionado es 1 se ejecutara el primer if
        if (opc == 1) {
            //para saber que se nos ejecuta "FOR"
            System.out.println("Usamos FOR");
            //ejecutamos el ciclo for
            for(int i = 0; i < 10; i++){
                System.out.println(i);
            }
        }
        //si el numero seleccionado es 2 se ejecutara el segundo if
        if (opc == 2) {
            //delaramos variable int i con valor 0
            int i = 0;
            //para saber que se nos ejecuto el "WHILE"
            System.out.println("Usamos WHILE");
            //ejecutamos el ciclo while
            while (i < 10) {
                System.out.println(i++);
            }
        }
    }
}

// tenia problemas usando String para selecionar entre WHILE o FOR asi que utilize int que si que me funciono