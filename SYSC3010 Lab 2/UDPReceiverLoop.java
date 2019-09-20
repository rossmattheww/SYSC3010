import java.net.* ;

public class UDPReceiverLoop {

	private final static int PACKETSIZE=100;

	public static void main( String args[] )
	{
		//Make a counter to count the packets recieved/sent
		int i = 1;

		//check the arguemets
		if( args.length != 1 )
		{
			System.out.println( "Usage: UDPReceiver port" ) ;
			return;
		}
		try
		{
			//Convert the arguement to ensure that it s valid
			int port = Integer.parseInt( args[0] );

			//Construct the socket
			DatagramSocket socket = new DatagramSocket( port );

			System.out.println("Receiving on port: " + port);

			for( ;; )
			{
				//Receiving packet 
				DatagramPacket packet = new DatagramPacket( new byte[PACKETSIZE], PACKETSIZE );
				socket.receive( packet ) ;
				System.out.println( packet.getAddress() + " " + packet.getPort() + ": " + new String(packet.getData()).trim());
				
				//sending back new packet
				String message = new String(packet.getData());
				message = "ACK: " + message; 

				byte [] data = message.getBytes();
				DatagramPacket senderPacket = new DatagramPacket( data, data.length, packet.getAddress(), packet.getPort());

				socket.send(senderPacket);
			}
		}
		catch( Exception e )
		{
			System.out.println( e );
		}
	}
}
