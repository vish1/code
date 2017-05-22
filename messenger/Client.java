import java.net.*;
import java.io.*;

public class Client 
{		
	public static void main(String argv[]) throws IOException
	{
		Socket sock=null;		try
		{
         sock = new Socket("127.0.0.1",5155);
			messenger box2=new messenger("Client",sock);
			box2.setSize(400,400);
			box2.setVisible(true);	
			while(true)	read(sock,box2);											
		}
		catch(IOException ioe)
		{
			System.err.println(ioe);
		}
		finally
		{
			if(sock!=null) sock.close();
		}
	}
			
	public static void read(Socket sock,messenger box2)
	{
		InputStream in = null;
		BufferedReader br2=null;		
		try
		{
			in=sock.getInputStream();
			br2=new BufferedReader(new InputStreamReader(in));
			String line;
			if((line=br2.readLine())!=null)
			box2.addbox("Server says: \n"+line+"\n");
		}
		catch(IOException ioe)
		{
			System.err.println(ioe);
		}		
	}
}

	
