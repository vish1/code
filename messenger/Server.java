import java.net.*;
import java.io.*;

public class Server 
{
	public static void main(String argv[]) throws IOException
	{
		ServerSocket sock=null;
		Socket client=null;
		
		try
		{
			sock = new ServerSocket(5155);
			client=sock.accept();	
			
			messenger box1=new messenger("Server",client);
			box1.setSize(400,400);
			box1.setVisible(true);	
			
			while(true)		read(client,box1);								
		}
		catch(IOException ioe)
		{
			System.err.println(ioe);
		}
		finally
		{
			if(client!=null) client.close();
			if(sock!=null) sock.close();
		}
	}
	
	public static void read(Socket client,messenger box1)
	{
		InputStream in = null;
		BufferedReader br2=null;
		
		try
		{
			in=client.getInputStream();
			br2=new BufferedReader(new InputStreamReader(in));
			String line;
			if((line=br2.readLine())!=null)
			box1.addbox("Client says: \n"+line+"\n");
		}
		catch(IOException ioe)
		{
			System.err.println(ioe);
		}
		
	}
}

	