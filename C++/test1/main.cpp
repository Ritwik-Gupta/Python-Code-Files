#include <iostream>
using namespace std;
// Function declaration
void func(void);

int count = 10; /* Global variable */
int i=5;
main() {
   while(count--) {
      func();
   }

   return 0;
}

// Function definition
void func( void ) {
   //int i = 5; // local static variable
   i++;
   cout << "i is " << i ;
   cout << " and count is " << count <<endl;
}
