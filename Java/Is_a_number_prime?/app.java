/*This was answered taking help from google, I had answer but was too slow, 
being a newbie to java, taken help */
public class Prime {

  public static boolean isPrime(long n) {
      if(n < 2) return false;
      if(n == 2 || n == 3) return true;
      if(n%2 == 0 || n%3 == 0) return false;
      long sqrtN = (long)Math.sqrt(n)+1;
      for(long i = 6L; i <= sqrtN; i += 6) {
          if(n%(i-1) == 0 || n%(i+1) == 0) return false;
      }
      return true;
  }
  
  }