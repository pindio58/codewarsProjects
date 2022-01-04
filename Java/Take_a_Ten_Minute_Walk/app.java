import java.util.HashMap;
import java.util.Map;

public class TenMinWalk {
  public static boolean isValid(char[] walk) {
      if(walk.length!=10) return false;
      //System.out.println(walk);
      Map<Character, Integer> dictionary = new HashMap<Character, Integer>();
     
      for (char ch: walk) {
       if (!dictionary.containsKey(ch)) {
         dictionary.put(ch, 0);
       } else{
         dictionary.put(ch, dictionary.get(ch)+1);
       };
       
     }
     
//      System.out.println(dictionary.keySet().toArray()[0]);
      
    if (dictionary.size()==1  || dictionary.size()==3) return false;
      
    if (dictionary.size()==2) {
      if (dictionary.get(dictionary.keySet().toArray()[0]) != dictionary.get(dictionary.keySet().toArray()[1])) return false;
    }
    
    
    if ((dictionary.get('n')!=dictionary.get('s'))||((dictionary.get('e')!=dictionary.get('w')))) return false;
    
    return true;
  }
}