/**
GUI for the project using swing

**/

package Swing;

import java.awt.event.ActionEvent;
import java.awt.event.ActionListener;
import java.awt.event.MouseEvent;
import java.awt.event.MouseListener;
import java.io.File;
import java.io.FileInputStream;
import java.io.FileOutputStream;

import javax.crypto.Cipher;
import javax.crypto.CipherOutputStream;
import javax.crypto.spec.SecretKeySpec;
import javax.swing.JButton;
import javax.swing.JFileChooser;
import javax.swing.JFrame;
import javax.swing.JTextField;
import javax.swing.plaf.FileChooserUI;

public class BaseJFrame extends JFrame implements MouseListener,ActionListener {
	//Browsing file location menu
	JFileChooser fc=new JFileChooser();
	
	//various button to interact
	JButton browse = new JButton("Browse");
	JButton encrypt = new JButton("Encrypt");
	static private final String newline = "\n";
	JTextField tf=new JTextField();
	
	//setting size of GUI window
	public BaseJFrame() {
		Cipher cipher;
		final String pass = "password12345678";
		JButton exit = new JButton("Exit");
		
		browse.addActionListener(this);
		encrypt.setBounds(20, 20, 80, 30);
		
		//action method to response to several click events
		encrypt.addActionListener(new ActionListener() {
			
			@Override
			public void actionPerformed(ActionEvent e) {
				try {
					FileInputStream fis = new FileInputStream(tf.getText());
					FileOutputStream fos = new FileOutputStream("Encrypt.jpg");
					SecretKeySpec key = new SecretKeySpec(pass.getBytes(), "AES");
					byte[] k = pass.getBytes();
					Cipher enc = Cipher.getInstance("AES");
					enc.init(Cipher.ENCRYPT_MODE, key);
					CipherOutputStream cos = new CipherOutputStream(fos, enc);
					byte[] buffer = new byte[1024];
					int read;
					while ((read = fis.read()) != -1) {
						cos.write(buffer, 0, read);
					}
					fis.close();
					fos.flush();
					cos.close();
					System.out.println("File Encrypted successfully");
				} catch (Exception l) {
					l.printStackTrace();;
				}

				
			}
		});
		browse.setBounds(120, 20, 80, 30);
		exit.setBounds(220, 20, 80, 30);
		tf.setBounds(120,70, 180,20);
		this.setTitle("Encryption Using Chaos Theory");
		add(encrypt);
		add(browse);
		add(tf);
		add(exit);
		this.setSize(400, 400);
		setLayout(null);
		setVisible(true);
	}

	public static void main(String[] args) {
		new BaseJFrame();
	}

	@Override
	public void mouseClicked(MouseEvent e) {
		// TODO Auto-generated method stub

	}

	@Override
	public void mousePressed(MouseEvent e) {
		// TODO Auto-generated method stub

	}

	@Override
	public void actionPerformed(ActionEvent e) {
	    //Handle open button action.
	    if (e.getSource() == browse) {
	      int returnVal = fc.showOpenDialog(BaseJFrame.this);

	      if (returnVal == JFileChooser.APPROVE_OPTION) {
	        File file = fc.getSelectedFile();
	        tf.setText(file.getAbsolutePath());
	        
	        //This is where a real application would open the file.
	       // log.append("Opening: " + file.getName() + "." + newline);
	      } else {
	       // log.append("Open command cancelled by user." + newline);
	      }
	    //  log.setCaretPosition(log.getDocument().getLength());

	      //Handle save button action.
	    } 
	  }
		
	

	@Override
	public void mouseReleased(MouseEvent e) {
		// TODO Auto-generated method stub
		
	}

	@Override
	public void mouseEntered(MouseEvent e) {
		// TODO Auto-generated method stub
		
	}

	@Override
	public void mouseExited(MouseEvent e) {
		// TODO Auto-generated method stub
		
	}
}
