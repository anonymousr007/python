# python

> 1. Yes,I build a community of coders,developers and hackers like hackathon participants and mentors too.
My organization name is bitandbytes8 [https://github.com/bitandbytes8] and it's open source.
Working of my organization teach coding and development such as web development,machine learning, deep learning, quantum computing, quantum machine learning, competitive coding, core subjects such as data structure and algorithms, database and management system, operating system, theory of computation, compiler design, object oriented programming, languages such as c++, python, java, javascript and much more etc, actually my plans are realistic if github support me so it's reality by me, and also develop large scale real projects solve real problem. 
2. Struggle faced by students proper awareness regarding programs, mentorship,what can they do or what cannot? that's the real struggle faced by students, a lot technologies in which one more scope in future market and all these problems struggles.

3. Our community get support by github to organised hackathons, challenges and workshops 

4. I had 5 years teaching experience so i want to become a teacher to taught computer science core subjects and famous technologies.


1. Beta Tester at Coursera.
2. Quantum Computing Student at The Coding School and IBM's QubitByQubit Organization.
3. IBM Quantum Computing Challenge Fall 2020 - Intermediate Badge Certified
4. ICPC IBM Quantum Computing Challenge 2021 - Intermediate 
5. Participant at QHack 2021, Quantum Machine Learning Hackathon organised by Xanadu and got Rank :: 56/390 in the world and also the perfect scorer :: 2500/2500.
6. Diploma in Quantum Computation Workshop organised by QWorld.
7. QWORLD : Research Candidate
8. CERN : TraineeHigh Energy Physics Software Foundation Hackathon
9. CERN : Quantum Computing Lectures
10. QTML 2020 : Attendee
11. QIP 2021 Attendee
12. 9200+ Connections and 9000+ Followers on Linkedin.
13. Mentee at Girlscript Summer of Code
14. Mentor at Hack with Code Warriors.
15. Mentor at TechTogether New York.
16. Mentor at Indian Road Safety Compaign and Toyota at IIT Delhi.
17. Volunteer in the Global Student Solar Ambassadors Workshop by IIT Bombay
18. Volunteer at Code Warriors
19. Technical Organizer at INNOVA DTU
20. Head of Logistics at Yuvaan DTU
21. Web Developer Co-head at INNOVA DTU
22. Public Relation Manager at Elixir DTU
23. Technical Team AND Marketing Member at Codechef DTU
24. //Codeforces #712 A
#include<bits/stdc++.h>
#define endl '\n'
typedef long long ll;
using namespace std;

#define Fast       ios_base::sync_with_stdio(false); cin.tie(NULL); cout.tie(NULL);

int main(){
    Fast
    int tc = 1; cin>>tc;
    for(int t = 0; t < tc; t++){
        string s; cin>>s;
        int n = s.length();
        bool work = false;
        for(int i = 0; i < (n+1)/2; i++){
            if(s[i] !='a'){
                work = true;
                cout<<"YES"<<endl;
                string t = s.substr(0, n-i);
                cout<<t<<'a';
                t = s.substr(n-i);
                cout<<t<<endl;
                break;
            }
            else if(s[n-i-1] != 'a'){
                work = true;
                cout<<"YES"<<endl;
                string t = s.substr(0, i+1);
                cout<<t<<'a';
                t = s.substr(i+1);
                cout<<t<<endl;
                break;
            }
        }
        if(!work)cout<<"NO"<<endl;
    }
    return 0;
}





#include<bits/stdc++.h>
#define endl '\n'
typedef long long ll;
using namespace std;

#define Fast       ios_base::sync_with_stdio(false); cin.tie(NULL); cout.tie(NULL);

int main(){
    Fast
    int tc = 1; cin>>tc;
    for(int t = 0; t < tc; t++){
        int n; string a, b; cin>>n>>a>>b;
        int pref[n+1] = {};

        for(int i = 0; i < n; i++){
            if(a[i] == '1')pref[i+1] = pref[i]+1;
            else pref[i+1] = pref[i] - 1;
        }

        //for(int i = 0; i <=n; i++)cout<<pref[i]<<' ';
        //cout<<endl;

        bool work = true;
        bool flip = false;
        for(int i = n-1; i >= 0; i--){
            if((!flip && a[i] == b[i]) || (flip && a[i] != b[i]))continue;
            else if(pref[i+1] == 0){
                flip = !flip;
            }
            else {work = false;break;}
        }

        cout<<(work?"YES":"NO")<<endl;
    }
    return 0;
}


#include<bits/stdc++.h>
using namespace std;
#define ll long long
void solve(){
 ll n;
 cin>>n;
 string str;
 cin>>str;
 string a ="",b ="";
        for(ll i=0;i<n;++i)
        {
            if(i % 2 == 0)
                a += '(';
            else
                a += ')';
        }
        ll count_open = 0,count_close = 0;
        bool flag = true;
        for(ll i=0;i<n;++i)
        {
            if(str[i] == '1')
            {
                b += a[i];
                if(a[i] == '(')
                {
                    count_open++;
                }
                else
                {
                    count_close++;
                    if(count_close > count_open)
                    {
                        flag = false;
                        break;
                    }
                }
            }
            else
            {
                if(a[i] == '(')
                {
                    b += ')';
                    count_close++;
                    if(count_close > count_open)
                    {
                        flag = false;
                        break;
                    }
                }
                else
                    b += '(',count_open++;
            }
        }
            if(!flag || (count_open != count_close))
                cout<<"NO\n";
            else
            {
                cout<<"YES\n";
                cout<<a<<"\n";
                cout<<b<<"\n";
            }
}

int main(){
  ll t;
  cin>>t;
//    t=1;
  while(t--)
  solve();
}
