#include <iostream>
using namespace std;

int main()
{
    char continuar;
do{
    int n, nmin = 0, posicion = 0, pmin = 0;
    cout << "INGRESE 20 NUMEROS, BUSCAREMOS EL MENOR DE ELLOS Y LA POSICION QUE FUE INGREASDO" << endl;
    for (int x = 0; x <20; x++){
        cin >> n;
        posicion++; //SUMAMOS LA POSICION DESDE EL PRIMER INGRESO PARA SABER EL ORDEN DEL INGRESO
        if (x==0){ //EL PRIMER NUMERO INGRESADO SERA CON EL QUE COMPARAREMOS LOS SIGUENTES, SOLO POR SI ACASO EL PRIMERO FUESE NEGATIVO.
            nmin = n;
            pmin = posicion; //CUANDO SEA VERDADERO ASIGNAMOS EL VALOR DE POSICION
        }if( n < nmin){
            nmin = n;
            pmin = posicion; //CUANDO SEA VERDADERO ASIGNAMOS EL VALOR DE POSICION
        }else{
        }
    }
    cout << nmin << " FUE EL NUMERO MENOR Y SU POSICION " << pmin << endl;

  //Pregunta al usuario si quiere volver a compilar el código
  cout << "\n====== Desea continuar con la prueba? ====== (s/n): ";
  cin >> continuar; cout << endl;
} while (continuar == 's' || continuar == 'S');

return 0;
}
