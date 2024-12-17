#include <iostream>
using namespace std;

int main()
{
    char continuar;
do{
    //DEFINIMOS LAS VARIABLES PARA IDENTIFICAR CUAL DE LOS 10 NUMEROS INGRESADOS ES EL MAYOR Y SU POSICION
    int n, maxN=0, posicion=0, pmax = 0;
    cout << "Ingrese 10 numeros: " << endl;
    //FOR PARA LA PETICION DE LOS NUMEROS DESEADOS
    for (int x = 0; x < 10; x++){
        cin >> n;
    //EVALUAMOS Y ASIGNAMOS VALORES CORRESPONDIENTES A LAS VARIABLES
        if (n > maxN){
            maxN = n; //CAMBIAMOS EL VALOR PARA TENER SIEMPRE EL MAYOR
            posicion ++;//AUMENTAMOS EL VALOR DE LA POSICION YA SEA TRUE O FALSE
            pmax = posicion;//ASIGNAMOS EL VALOR DE LA POSICON AL MOMENTO QUE SE CUMPLA LA CONDICION
        }else{
            posicion ++;//SIMPLEMENTE AUMENTAMOS EL VALOR DE LA POSICION YA SEA TRUE O FALSE
        }
    }
    cout << maxN <<" Es el mayor ingresado de " << pmax << endl;

  //Pregunta al usuario si quiere volver a compilar el código
  cout << "\n====== Desea continuar con la prueba? ====== (s/n): ";
  cin >> continuar; cout << endl;
} while (continuar == 's' || continuar == 'S');

return 0;
}
