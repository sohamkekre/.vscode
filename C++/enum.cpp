#include <iostream>
using namespace std;

enum level{
low = 10,
medium,
high
};
int main(){
    enum level myVar = high;
    cout << myVar;
}