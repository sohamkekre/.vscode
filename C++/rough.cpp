#include<iostream>
using namespace std;

int main(){
    int arr_size;
    cout<<"Enter the size of array: ";
    cin>>arr_size;
    int arr[arr_size];
    for (int i=0;i<arr_size;++i){
        cin>>arr[i];
    }
    for(int i : arr)
    // cout<<"position"<<i<<" of array: "<<arr[i]<<endl;
    cout << "array inputs "<<i<<endl;
}