public class Nombre{
    public static String dameNombre(){
        return "Pepe";
    }

    public static void imprimeNombre (String nombre){
        System.out.println("Coche: " + nombre);
    }

    public static void main(String[] args){
        String nombre = Nombre.dameNombre();
        Nombre.imprimeNombre(nombre);
    }
}