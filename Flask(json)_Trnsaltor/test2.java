
import java.io.BufferedReader;

import java.io.InputStreamReader;

 
class test2{
public static void main(String a[]){
try{
 
String commandToExecute = new String("python3 text.py test_kannda.pdf kannada english");

                String s, r = null;
                Process p = Runtime.getRuntime().exec(commandToExecute);
            	BufferedReader stdInput = new BufferedReader(new 
                        InputStreamReader(p.getInputStream()));

            	BufferedReader stdError = new BufferedReader(new 
                    InputStreamReader(p.getErrorStream()));

System.out.println("Json from python\n");
            	while ((s = stdInput.readLine()) != null) {
            		System.out.println(s);
            		
}
}catch(Exception e){System.out.println(e);}
}
}
