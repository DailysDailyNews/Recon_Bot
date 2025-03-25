import java.net.*;

public class ClienrDebugger {
  public static void main(String[] args) {
    try {
      InetAddress localHost = InetAddress.getLocalHost();

System.out.println("Debugging 
Client: "+
localHost.getHostName();
    } catch (Exception e) {
        e.printStackTrace();
    }
  }
"
