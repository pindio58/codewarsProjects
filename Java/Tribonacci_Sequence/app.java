import java.util.Arrays;
public class Xbonacci {

  public  double[] tribonacci(double[] s, int n) {
    System.out.println(Arrays.toString(s));
    System.out.println(n);    
    
      double[] ret = new double[n];
      double num=0;
      if (n==0) {
        return ret;
      } else{
       
        for(int x =0;x<Math.min(3.0,n);x++) {
          ret[x]=s[x];
          num+=s[x];
        }
        
      };
      
    if (n<3) {
      return ret;
    } else{
      ret[3]=num;
    }
      
      
      for (int x=4; x<n;x++) {
        ret[x]=ret[x-1]+ret[x-2]+ret[x-3];
      }
      ;
      return ret;
        
    }
}