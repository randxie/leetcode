class Solution {
public:
    bool isMatch(string s, string p) {
        int ptrS = 0;
        int ptrP = 0;
        if (s.length()==0 && p.length()==0){
        	return true;
        }
        else if (s.length()!=0 && p.length()==0){
        	return false;
        }
        else if (s.length()==0 && p.length()!=0){
        	return false;
        }

        return matching(s, p, ptrS, ptrP);
    }

    bool matching(string &ss, string &pp, int ptrS, int ptrP) {
        if (ptrS > (ss.length()-1) and ptrP >= (pp.length()-1))
        {
            return true;
        }
        else if (ptrS > (ss.length()-1) and ptrP < (pp.length()-1) ){
            return false;
        }
        else if (ptrS <= (ss.length()-1) and ptrP > (pp.length()-1) ){
            return false;
        }
            
        if (ss[ptrS] == pp[ptrP] or pp[ptrP]=='?'){
            return matching (ss, pp, ptrS+1, ptrP+1);
        }
        else if (pp[ptrP] == '*'){
            return (matching (ss, pp, ptrS+1, ptrP+1) || matching (ss, pp, ptrS+1, ptrP) ) ;
        }
        else{
            return false;
        }
    }
};