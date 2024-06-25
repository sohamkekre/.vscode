#include <iostream>
using namespace std;

struct first
{
    int myNum;
    string myStr;
};

int main(){
    first myStructure;
    myStructure.myNum = 1;
    myStructure.myStr = "Hello";
    cout << myStructure.myNum << "\n";
    cout << myStructure.myStr << "\n";

    first myStructure2;
    myStructure2.myNum = 2;
    myStructure2.myStr = "Hello 2";
    cout << myStructure2.myNum << "\n";
    cout << myStructure2.myStr << "\n";
}

