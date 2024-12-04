#include <fstream>
#include <iostream>
#include <string>
#include <vector>
#include <algorithm>
using namespace std;
int main(){
	std::ifstream infile("input.txt");

	std::string line;

	int a;
	int b;
	vector<int> aa;
	vector<int> bb;
	while (infile >> a >>b){
		aa.emplace_back(a);
		bb.emplace_back(b);
	}
	sort(aa.begin(), aa.end());
	sort(bb.begin(), bb.end());

	int ret = 0;
	for (int i = 0; i < aa.size(); i++){
		int aux = aa[i] - bb[i];
		ret += (aux < 0) ? -aux : aux;
	}
	int final = 0;
	for (int i = 0; i < aa.size(); i++){
		int aux = 0;
		for (int j= 0; j < bb.size(); j++){
			if (aa[i] == bb[j]){
				aux++;
			}
		}
		final += aa[i] * aux;
	}
	cout<< final;
}
