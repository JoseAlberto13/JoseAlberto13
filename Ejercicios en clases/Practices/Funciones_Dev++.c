#include <stdio.h>

float buscar_promedioAsignatura(float vector[], int tamanio);
float buscar_notasPositivasyNegativas(float vector[], int tamanio);
float buscar_promedioTodasAsignaturas(float promedio1, float promedio2, float promedio3);
float buscar_CalificacionAF(float promedio);

int main() {
    float notasFundamentosProgramacion[] = {5.2, 5.3, 7.0, 3.5, 2.6};
    int cantidad_notasFProgramacion = sizeof(notasFundamentosProgramacion)/sizeof(notasFundamentosProgramacion[0]);
    float notasMatematicas[] = {2.5, 6.5, 5.4, 2.3, 1.1, 2.5};
    int cantidad_notasMatematicas = sizeof(notasMatematicas)/sizeof(notasMatematicas[0]);
    float notasTallerComunicacionOralyEscrita[] = {2.8, 3.6, 7.0, 6.8, 2.1, 3.6};
    int cantidad_notasTallerComunicacionOralyEscrita = sizeof(notasTallerComunicacionOralyEscrita)/sizeof(notasTallerComunicacionOralyEscrita[0]);
    float promedio_AsignaturaProgramacion, promedio_AsignaturaMatematicas, promedio_AsignaturaComunicacionOralyEscrita;
    float promedio_General;
    int conteoDeNotasMenores_Mayores;
    float aprueba_o_Desaprueba;
    
    promedio_AsignaturaProgramacion = buscar_promedioAsignatura(notasFundamentosProgramacion, cantidad_notasFProgramacion);
        printf("***Fundamentos de Programacion***\nPromedio: [%.2f]\n", promedio_AsignaturaProgramacion);
     conteoDeNotasMenores_Mayores = buscar_notasPositivasyNegativas(notasFundamentosProgramacion, cantidad_notasFProgramacion);
    aprueba_o_Desaprueba = buscar_CalificacionAF(promedio_AsignaturaProgramacion);
    printf("\n");
    promedio_AsignaturaMatematicas = buscar_promedioAsignatura(notasMatematicas, cantidad_notasMatematicas);
        printf("***Matematicas***\nPromedio: [%.2f]\n", promedio_AsignaturaMatematicas);
    conteoDeNotasMenores_Mayores = buscar_notasPositivasyNegativas(notasMatematicas, cantidad_notasMatematicas);
    aprueba_o_Desaprueba = buscar_CalificacionAF(promedio_AsignaturaMatematicas);
    printf("\n");
    promedio_AsignaturaComunicacionOralyEscrita = buscar_promedioAsignatura(notasTallerComunicacionOralyEscrita, cantidad_notasTallerComunicacionOralyEscrita);
         printf("***Taller de Comunicacion Oral y Escrita***\nPromedio: [%.2f]\n", promedio_AsignaturaComunicacionOralyEscrita);
    conteoDeNotasMenores_Mayores = buscar_notasPositivasyNegativas(notasTallerComunicacionOralyEscrita, cantidad_notasTallerComunicacionOralyEscrita);
    aprueba_o_Desaprueba = buscar_CalificacionAF(promedio_AsignaturaComunicacionOralyEscrita);
    printf("\n");
    promedio_General = buscar_promedioTodasAsignaturas(promedio_AsignaturaProgramacion, promedio_AsignaturaMatematicas, promedio_AsignaturaComunicacionOralyEscrita);
    printf("El promedio general es: [%.2f]\n", promedio_General);
    
    return 0;
}

//funcion para buscar el promedio de la asignatura
float buscar_promedioAsignatura(float vector[], int tamanio) {
    float promedio = 0;
    int cant_notas = 0;
    for (int x = 0; x < tamanio; x++) {
        promedio += vector[x];
        cant_notas ++;
    }
    promedio = promedio /cant_notas;
    return promedio;
}
//funcion para buscar las notas mayores y menores a "4"
float buscar_notasPositivasyNegativas(float vector[], int tamanio) {
    float notas = 0;
    int contadorNotasMayores = 0, contadorNotasMenores = 0;
    for (int x = 0; x< tamanio; x++) {
        if (vector[x] >= 4) {
            contadorNotasMayores ++;
        } else {
            contadorNotasMenores ++;
        }
    }
    printf("Notas mayores o iguales a 4: [%d]\nNotas menores a 4: [%d]\n", contadorNotasMayores, contadorNotasMenores);
   // return 0;
}
//funcion para hacer el promedio de las tres asignaturas
float buscar_promedioTodasAsignaturas(float promedio1, float promedio2, float promedio3) {
    float promedios;
    promedios = (promedio1 + promedio2 + promedio3) / 3;
    return promedios;
}
//funcion para saber si aprueba o reprueba la asignatrua
float buscar_CalificacionAF(float promedio) {
    if (promedio >= 5) {
        printf("Asignatura Aprobada (Azul)\n");
    } else {
        printf("Asignatura Reporbada (Rojo)\n");
    }
}