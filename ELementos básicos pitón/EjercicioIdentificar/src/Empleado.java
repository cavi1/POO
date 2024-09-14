public class Empleado {
    private String nombre;
    private Integer horasTrabajadas;
    private Double valorHora;
    
    public Empleado(String nombre, Integer horasTrabajadas, Double valorHora) {
        this.nombre = nombre;
        this.horasTrabajadas = horasTrabajadas;
        this.valorHora = valorHora;
    }

    public Double calcularSueldo(){
        return horasTrabajadas * this.valorHora;
    } 

    public void guardarDB(){
        //logica de guardado en BD 
        System.out.println("\"INSERT INTO empleados (nombre, horas_trabajadas, valor_hora) VALUES (" + this.nombre + ", "+this.horasTrabajadas + ", "+this.valorHora + ")\";");
    }

}
