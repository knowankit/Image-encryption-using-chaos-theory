package Encrpytion;

import java.io.File;
import java.io.FileInputStream;
import java.io.FileOutputStream;

import javax.crypto.Cipher;
import javax.crypto.CipherOutputStream;
import javax.crypto.spec.SecretKeySpec;

public class Encrypt {
	Cipher cipher;
	final static String pass = "password12345678";

	public static void main(String[] args) {
		try {
			FileInputStream fis = new FileInputStream(new File("C:/User/Ankit/Desktop/maxresdefault"));
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
		} catch (Exception e) {
			e.printStackTrace();;
		}
	}
}
