#include <iostream>

using namespace std;

int main()
{
    char continuar;

do {
  int op, om, od, precio;
  cout << "ingrese la opcion de procesador 1 (i5), 2 (i7), 3 (i9): ";
  cin >> op;
  cout << "ingrese la opcion de memoria RAM 1 (8gb), 2 (16gb), 3 (32gb): ";
  cin >> om;
  cout << "extiende Disco? 1 (si) / 0 (no)";
  cin >> od;

  switch(op){
  case 1:
      cout << "\nElegiste un i5 ";
      switch(om){
      case 1:
        precio = 800;
        cout << "con RAM de 8gb ";
        break;
      case 2:
        precio = 900;
        cout << "con RAM de 16gb ";
        break;
      default:
        precio = 1000;
        cout << "con RAM de 32gb ";
        break;
      }
      break;
  case 2:
    cout << "\nElegiste un i7 ";
    switch(om){
    case 1:
        precio = 900;
        cout << "con RAM de 8gb ";
        break;
    case 2:
        precio = 1000;
        cout << "con RAM de 16gb ";
        break;
    default:
        precio = 1400;
        cout << "con RAM de 32gb ";
        break;
      }
    break;
  default:
    cout << "\nElegiste un i9 ";
      switch(om){
      case 1:
        precio = 1200;
        cout << "con RAM de 8gb ";
        break;
      case 2:
        precio = 1400;
        cout << "con RAM de 16gb ";
        break;
      default:
        precio = 2000;
        cout << "con RAM de 32gb ";
        break;
      }
    break;
  }
  if (od == 1){
    precio+= 300;
  }

cout << "\nEl monto total a cancelar es: " << precio << endl;

  //Pregunta al usuario si quiere volver a ejecutar
  cout << "\nDesea continuar? (s/n): ";
  cin >> continuar;
} while (continuar == 's' || continuar == 'S');

return 0;
}
