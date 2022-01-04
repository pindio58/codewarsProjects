class Solution {
      public static String camelCase(String input) {
      //System.out.println(input);
      return input.replaceAll("([A-Z])", " $1"); 
    }
  }