#include <iostream>
using namespace std;

int main(){
bool ships[4][4] = {
    {0,1,0,1},
    {1,0,1,0},
    {0,1,0,1},
    {1,0,1,0}
};
int hits = 0;
int numberofturns = 0;

while (hits < 4) {
    int row,column;
    cout << "selecting cordinates\n";
    cout << "choose the row number between 0 and 3\n";
    cin >> row;
    if (row>3){
        cout << "Please choose a number less than 4\n";
        cin >> row;
    }
    cout << "choose the column number between 0 and 3\n";
    cin >> column;
    if (column>3){
        cout << "Please choose a number less than 4\n";
        cin >> column;
    }
    if (ships[row][column]){
        ships[row][column] = 0;
        hits++;
        cout << "Hit!!" << (4-hits) << "left]\n" ;
    }
    else{
        cout << "Missed\n";
    }
    numberofturns++;
}
cout<<"You have completed in " << numberofturns << " turns!";
cout << "You Won!!";
return 0;
}