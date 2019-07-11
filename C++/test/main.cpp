#include <iostream>
#include <typeinfo>
using namespace std;
typedef int number;
int main()
{
    /*
    cout << "\nSize of char:"<< sizeof(char);
    cout << "\nSize of int:"<< sizeof(int);
    cout << "\nSize of short int:"<< sizeof(short int);
    cout << "\nSize of long int:"<< sizeof(long int);
    cout << "\nSize of float:"<< sizeof(float);
    cout << "\nSize of double:"<< sizeof(double);
    */

    number a,b;
    cin>>a>>b;
    int n=a+b;
    cout<<n<<endl;
    cout<<typeid(n).name();
    return 0;
}
