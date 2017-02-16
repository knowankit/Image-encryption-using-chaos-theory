
/**
AES encryption library.
**/
package Swing;

import java.awt.image.BufferedImage;
import java.io.ByteArrayOutputStream;
import java.io.IOException;
import java.net.MalformedURLException;
import java.net.URL;

import javax.imageio.ImageIO;

import Decoder.BASE64Encoder;
import it.sauronsoftware.base64.Base64;

import org.apache.commons.io.IOUtils;
public class TestClass {
	public static String encodeToString(BufferedImage image,String type){
		String imageString=null;
		ByteArrayOutputStream bos=new ByteArrayOutputStream();
			try {
				ImageIO.write(image,type,bos);
				byte[] imageBytes=bos.toByteArray();
				BASE64Encoder encoder=new BASE64Encoder();
				imageString =encoder.encode(imageBytes);
			} catch (IOException e)
			{
				e.printStackTrace();
			}
		return imageString;
		
		
	}
	
	public static String encodeTo(String url){
		String base64=null;
		ByteArrayOutputStream bos=new ByteArrayOutputStream();
				try {
					byte[] imageByte = IOUtils.toByteArray(new URL(url));
					 base64 =Base64.encode(imageByte).toString();
					System.out.println("Inside-> "+base64);
				} catch (IOException e) {
					e.printStackTrace();
				}
				return base64;
	}
		
		
		
	
	
	public static void main(String[] args) {
			String u="C:/Users/Ankit/Desktop/big_tiger-wide.jpeg";
			String str=encodeTo(u);
			System.out.println(str);
		
	}
}
