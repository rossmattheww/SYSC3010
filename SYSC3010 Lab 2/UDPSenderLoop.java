import java.net.*;
import java.util.Scanner;

public class UDPSender {
	private final static int PACKETSIZE = 100 ;

	public static void main(String[] args) 
   {
	      // Check the arguments
	      if( args.length != 3 )
	      {
	         System.out.println( "usage: java UDPSender host port" ) ;
	         return ;
	      }
	      DatagramSocket socket = null ;
	      try
	      {
	         // Convert the arguments first, to ensure that they are valid
	         InetAddress host = InetAddress.getByName( args[0] ) ;
	         int port         = Integer.parseInt( args[1] ) ;
	         int n			  = Integer.parseInt( args[2] ) ;
	         socket = new DatagramSocket() ;
			
	         Scanner in;
	         in = new Scanner (System.in);
	         String message = null;
	         while (true)
	         {
	        		 System.out.println("Enter text to be sent, ENTER to quit ");
	        		 message = in.nextLine();
	        		 if (message.length()==0) break;
	        		 for(int i = 0; i < n; i++){
						//Sending packet to receiver
						String s = message + i;
						byte [] data = s.getBytes() ;
						DatagramPacket packet = new DatagramPacket( data, data.length, host, port ) ;
						socket.send( packet ) ;
						
						//Receiving packet back from receiver
						DatagramPacket packetR = new DatagramPacket( new byte[PACKETSIZE], PACKETSIZE ) ;
						socket.receive( packetR ) ;
					    System.out.println( packetR.getAddress() + " " + packetR.getPort() + ": " + new String(packetR.getData()).trim() ) ;
						
					 }
	         } 
	         System.out.println ("Closing down");
	      }
	      catch( Exception e )
	      {
	         System.out.println( e ) ;
	      }
	      finally
	      {
	         if( socket != null )
	            socket.close() ;
      }
   }
}

