public class Solution {

  public int solution(int number) {
    int count=0;
      int sum=0;
      while(count<number) {
        if(count%3==0 || count%5==0) sum+=count;
        count++;
      }
      
      return sum;
  }
}