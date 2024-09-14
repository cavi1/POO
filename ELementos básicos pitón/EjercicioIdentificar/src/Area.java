public class Area {
    public double calcularAreaCirculo(double radio) {
        return Math.PI * radio * radio;
    }

    public double calcularAreaCuadrado(double lado) {
        return lado * lado;
    }

    public double calcularAreaRectangulo(double ancho, double alto) {
        return ancho * alto;
    }
}
