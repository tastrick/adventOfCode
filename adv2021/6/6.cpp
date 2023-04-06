#include <vector>
//#include<string>
#include <iostream>
using namespace std;

int main(){
    vector<int> v{3,4,3,1,2};
    int s = 0;
    int j = 0;
    int i = 0;
    cout<<s<<endl;
    while(i <80){
        j = 0;
        s = v.size();
        //cout<<"test loop 1"<<endl;
        while(j<s){
            //cout<<"test loop 2"<<endl;
            if (v[j]==0){
                v.push_back(8);
                v[j] = 6;
            }else{
                v[j]-=1;
            }
            j++;
        }
        i++;
    }
    cout<<v.size()<<endl;
}
