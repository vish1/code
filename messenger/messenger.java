
import java.awt.event.*;
import javax.swing.*;
import java.net.*;
import java.io.*;

public class messenger extends JFrame
{	
		JLabel L1,L2,L3;
		JTextArea t1=new JTextArea(10,20);
		JTextField t2=new JTextField(10);
		JPanel contentpane;
		JButton b1;
		String name;
		Socket sock;
		
	public messenger(String t,Socket socket)
	{
		name=t;
		sock=socket;
		setTitle(t+"Messenger");
		
		JPanel contentpane=(JPanel)getContentPane();
	  	contentpane.setLayout(null);
		
		//JLabel L1=new JLabel("Welcome to The Messenger");
		JLabel L2=new JLabel("Connected to: ");
		JLabel L3=new JLabel("Type On: ");
		JButton b1=new JButton("OK");
		JButton b2=new JButton("Close");
		b1.addActionListener(new ButtonHandler());
		b2.addActionListener(new ButtonHandler());
		addWindowListener(new WindowHandler());			
		//L1.setBounds(10,10,200,20);
		//contentpane.add(L1);
		
		L2.setBounds(10,0,100,20);
		contentpane.add(L2);		
		//add the ip no.
		t1.setBounds(10,20,360,200);
		contentpane.add(t1);
		L3.setBounds(10,230,75,30);
		contentpane.add(L3);
		t2.setBounds(85,230,200,30);
		contentpane.add(t2);	
		b1.setBounds(285,230,75,30);
		contentpane.add(b1);
		b2.setBounds(10,270,360,30);
		contentpane.add(b2);
	}
		/*public static void main(String argv[])
	{
		messenger box1=new messenger("Vish");
		box1.setBounds(0,0,400,350);
		box1.setVisible(true);
	}*/
		
	public void addbox(String s)
	{
		String a;
		a=t1.getText()+s;
		t1.setText(a);
	}
	
	class ButtonHandler implements ActionListener
	{
		public void actionPerformed(ActionEvent e)
		{
			String t=e.getActionCommand();
			if(t.equals("OK"))
			{
				try
				{
					PrintWriter pout =null;	
					pout=new PrintWriter(sock.getOutputStream(),true);
					pout.println(t2.getText());
				}
				catch(IOException ioe)
				{
					System.err.println(ioe);
				}						
				String s =name+" says:\n"+t2.getText()+"\n";
				t2.setText("");
				t1.setText(t1.getText()+s);
			}
			else if(t.equals("Close"))
			{
				System.exit(0);
			}
		}
	}
	class WindowHandler extends WindowAdapter 
	{
		public void windowClosing(WindowEvent e)
		{
			try{	sock.close();}
			catch(IOException ioe)
			{}
			System.exit(0);	
		}
	}

}
