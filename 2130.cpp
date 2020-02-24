#include<iostream>
#include<algorithm>
#include<vector>
#include<tuple>
#include<cmath>
using namespace std;
typedef tuple<int, int, int> tu;
int n,b,h,w,d,B,H,WD;
double v, ans = 1040010;
vector<tu> vec;

double parametric_search(double start, double end){
	if(start>=end) return end;
	double mid = (start+end) / 2;
	double water = 0;
	for(int i=0;i<vec.size();i++){
		tie(B,H,WD) = vec[i];
		if(mid > B) {
			double newH = min((double)H, (double)mid-B);
			water += (double)(WD * newH);
		}
	}
	if (water >= v) return parametric_search(start, mid-0.001);
	else return parametric_search(mid+0.001, end);
			
}

int main(){
	scanf("%d", &n);
	for(int i=0;i<n;i++){
		scanf("%d%d%d%d", &b,&h,&w,&d);
		vec.push_back(make_tuple(b,h,w*d));
	}
	scanf("%lf", &v);
	ans = parametric_search(0, 1040010);
	ans==1040010 ? printf("OVERFLOW\n") : printf("%.2lf\n", round(ans*100) / 100);
}
