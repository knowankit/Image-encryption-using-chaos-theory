/**
This class is about the fetching of the pixels from the image and storing them in a 2d array which could be further passed to encryption
module.In encryption module each pixel is encrypted using AES(Advanced Encryption Standard), the encrypted pixel are stored in a text file.
Decryption module fetch the encrypted pixel from the text file and decrypts it and generates the image.

**/

package Swing;

import java.awt.Color;
import java.awt.image.BufferedImage;
import java.io.BufferedReader;
import java.io.File;
import java.io.FileNotFoundException;
import java.io.FileReader;
import java.io.IOException;
import java.io.PrintWriter;
import java.io.UnsupportedEncodingException;
import java.security.InvalidAlgorithmParameterException;
import java.security.InvalidKeyException;
import java.security.Key;
import java.security.NoSuchAlgorithmException;
import java.security.spec.AlgorithmParameterSpec;

import javax.crypto.BadPaddingException;
import javax.crypto.Cipher;
import javax.crypto.IllegalBlockSizeException;
import javax.crypto.NoSuchPaddingException;
import javax.crypto.spec.IvParameterSpec;
import javax.crypto.spec.SecretKeySpec;
import javax.imageio.ImageIO;

import Decoder.BASE64Decoder;
import Decoder.BASE64Encoder;

public class RgbProject {
	Cipher cipher;
	//Key for encrypting the image
	final static String strPassword = "password12345678";

	public RgbProject() {
		try {
			//Fetching of the image file which is to be encrypted
			BufferedImage image = ImageIO.read(new File("C:/Users/Ankit/Desktop/logo.jpg"));
			
			//calling function to get the pixel values in RGB format
			marchThroughImage(image);
			
		} catch (IOException e) {
			 e.printStackTrace();
			System.err.println("Unable to read Image");
		}
	}

	
	/********************************************************************************************/
	// Method 1 to fetch the value of pixels and image is passed as an argument.
	
	private void marchThroughImage(BufferedImage image) {
		//Declaring 2d array of the image height and width
		String[][] pxel = new String[image.getHeight()][image.getWidth()];
		
		//fetching image height and width of the passed image.This will act as x and y axis of the image
		int h = image.getHeight();
		int w = image.getWidth();
		for (int i = 0; i < h; i++) {
			for (int j = 0; j < w; j++) {
				//Each pixel value is getting stored in different variables.
				int pixel = image.getRGB(j, i);
				int alpha = (pixel >> 24) & 0xff;
				int red = (pixel >> 16) & 0xff;
				int green = (pixel >> 8) & 0xff;
				int blue = (pixel) & 0xff;
				
				//Integer value is getting stored in string format separated by comma.
				String temp = alpha + "," + red + "," + green + "," + blue;

				/* System.out.println("RGB values->" + alpha + " " + red + " " +
				 green + " " + blue);*/
				
				
				//Finally the string value is stored in the 2d array.
				pxel[i][j] = temp;

			}
		}
		
		/*calling the pxelEncrypt module to encrypt the fetched pixel and return value is stored in rpxel(2d array),
		this also stores the encrypted pixel in the given location */
		String[][] rpxel = pxelEncrypt(pxel, image.getHeight(), image.getWidth());
		
		System.out.println("Encrypted Successfully");
		
		/* Here DecryptUtil module is to decrypt the image pixels*/
		String[][] enc=DecryptUtil(rpxel,image.getHeight(),image.getWidth());
		
		//This module is called to fetch the pixel from the text file.
		 rpxel=pxelGet();
		
		//This module is used to generate the new image form the decrypted pixel.
		 putPixel(rpxel, image.getHeight(), image.getWidth());
	}

	// Image Decrytpion Method

	/********************************************************************************************/
	void pxelGet() {
		try {
			//fetching the text file
			BufferedReader br = new BufferedReader(new FileReader("C:/Users/Ankit/Desktop/textOutput.txt"));
			String arr = br.readLine();
			String[] enc = arr.split("~");
			System.out.println("After->" + enc.length);
			String[][] enc2 = new String[100][100];
			int k = 0;
			out: for (int i = 0; i < 100; i++) {
				for (int j = 0; j < 100; j++) {
					if (k == 9503)
						break out;
					//Storing each pixel in this 2d array
					enc2[i][j] = enc[k];
					k++;
					System.out.println(enc2[i][j]);
				}
			}
			//pxelDecrypt(enc2);

		} catch (IOException e) {
			System.err.println("Image not found in the provided location");
		}
	}

	String[][] pxelDecrypt(String[][] dpxel,int height,int width) {

		return null;
	}

	// Image Encryption Method

	/********************************************************************************************/

	String[][] pxelEncrypt(String[][] pxel, int height, int width) {
		SecretKeySpec key = new SecretKeySpec(strPassword.getBytes(), "AES");
		AlgorithmParameterSpec paramSpec = new IvParameterSpec(strPassword.getBytes());
		String[][] epxel = new String[height][width];
		String totalString = "";
		for (int i = 0; i < height; i++) {
			for (int j = 0; j < width; j++) {

				try {
					Cipher cipher = Cipher.getInstance("AES/CBC/PKCS5Padding");
					try {
						cipher.init(Cipher.ENCRYPT_MODE, (Key) key, paramSpec);
					} catch (InvalidKeyException e1) {
						e1.printStackTrace();
					} catch (InvalidAlgorithmParameterException e1) {
						e1.printStackTrace();
					}

					// encrypt data
					byte[] ecrypted;
					try {
						ecrypted = cipher.doFinal(pxel[i][j].getBytes());
						String output = new BASE64Encoder().encode(ecrypted);
						String output2 = new BASE64Encoder().encode(ecrypted);
						
						//Each pixel is separated by this symbol "~" to distinguish from different pixel. 
						totalString += output + "~";
						epxel[i][j] = output2;

						// System.out.println("Encripted string: " + output);
					} catch (IllegalBlockSizeException e) {
						e.printStackTrace();
					} catch (BadPaddingException e) {
						e.printStackTrace();
					}

					// encode data using standard encoder

				} catch (NoSuchAlgorithmException e) {
					e.printStackTrace();
				} catch (NoSuchPaddingException e) {
					e.printStackTrace();
				}
			}
		}
		
		
		try {
			//New text file is created 
			PrintWriter pw = new PrintWriter("C:/Users/Ankit/Desktop/textOutput.txt", "UTF-8");

			String[] sp = totalString.split("~");
			System.out.println("Before->" + sp.length);
			
			//Pixels are getting inserted in to the newly created txt file
			pw.write(totalString);
			
			System.out.println("File Saved On Desktop");
			BufferedReader br = new BufferedReader(new FileReader("C:/Users/Ankit/Desktop/textOutput.txt"));
			String arr;
			try {
				arr = br.readLine();
				String[] enc = arr.split("~");
				System.out.println("After->" + enc.length);
			} catch (IOException e) {
				e.printStackTrace();
			}

		} catch (FileNotFoundException | UnsupportedEncodingException e) {
			e.printStackTrace();
			System.err.println("Unable to write");
		}
		return epxel;

	}

	// Image creation Method AFTER decryption

	/********************************************************************************************/

	void putPixel(String[][] epxel, int height, int width) {
		BufferedImage img = null;
		System.out.println("Inside Putpixel");
		try {
			img = ImageIO.read(new File("C:/Users/Ankit/Desktop/google.jpg"));
		} catch (IOException e) {
			e.printStackTrace();
		}
		for (int i = 0; i < height; i++) {
			for (int j = 0; j < width; j++) {
				String[] arr = new String[4];
				
				//separating the pixel by comma(,)
				arr = epxel[i][j].split(",");
				int alpha=Integer.parseInt(arr[0]);
				int red=Integer.parseInt(arr[1]);
				int green=Integer.parseInt(arr[2]);
				int blue=Integer.parseInt(arr[3]);
				int full = Integer.parseInt(epxel[i][j]);

				Color mycolor = new Color(full);
				int rgb = mycolor.getRGB();
				img.setRGB(i, j, rgb);

			}
			File outfile = new File("C:/Users/Ankit/Desktop/saved.jpg");
			try {
				ImageIO.write(img, "jpg", outfile);
			} catch (IOException e1) {
				e1.printStackTrace();
			}
		}
	}

	
	
	/*****************************************************************************************************/
	//Main method for execution
	public static void main(String[] args) {
		new RgbProject();

	}

	
	/*****************************************************************************************************/
	//Decrypting Method
	
	//encryted pixels are passed as an argument in the form of 2d array.
	
	public String[][] DecryptUtil(String[][] enc,int height,int width) {

		try {
			Cipher cipher;
			final String strPassword = "password12345678";

			SecretKeySpec key = new SecretKeySpec(strPassword.getBytes(), "AES");

			AlgorithmParameterSpec paramSpec = new IvParameterSpec(strPassword.getBytes());
			
			//Padding is done in case the key size is less the 128bit
			Cipher cipher1 = Cipher.getInstance("AES/CBC/PKCS5Padding");

			cipher1.init(Cipher.DECRYPT_MODE, key, paramSpec);
			for (int i = 0; i < height; i++) {
				for (int j = 0; j < width; j++) {
					byte[] output;

					output = new BASE64Decoder().decodeBuffer(enc[i][j]);
					byte[] decrypted = cipher1.doFinal(output);
					String dec = new String(decrypted);
					enc[i][j] = dec;
					
					//Finally the decrypted pixels are printed.
					System.out.println(enc[i][j] + " ");
					
					
				}
				putpixel(enc,height,width)
			}
		} catch (IOException | InvalidKeyException | InvalidAlgorithmParameterException | NoSuchAlgorithmException
				| NoSuchPaddingException | IllegalBlockSizeException | BadPaddingException e) {
			e.printStackTrace();
		}
		return enc;

	}

	// System.out.println("Original string: " + new String(input));

	// System.out.println("Decrypted string: " + new String(decrypted));
	// String ep = new String(decrypted);
	// System.out.println(ep);

}
