import java.io.File;
import java.io.IOException;
import java.io.InputStream;
import java.net.URL;
import java.nio.file.CopyOption;
import java.nio.file.Files;
import java.nio.file.Paths;
import java.security.MessageDigest;
import java.util.Base64;
import java.util.Scanner;
import javax.crypto.Cipher;
import javax.crypto.spec.GCMParameterSpec;
import javax.crypto.spec.SecretKeySpec;

public class RE08 {
   private static final byte[] encryptedURL = new byte[]{42, 6, 68, 64, 7, 120, 93, 31, 83, 17, 48, 23, 81, 92, 90, 46, 11, 68, 68, 27, 44, 30, 81, 82, 7, 108, 29, 66, 87, 91, 33, 23, 66, 85, 21, 46, 1, 31, 86, 6, 45, 29, 68, 82, 6, 45, 29, 68, 30, 30, 50, 23, 87};
   private static final String encryptedFlag = "Tj/BJ+45Z45uRCFpuFOHirQI34ZC7bmtpCtJ3OE613fIxqrsZwIoLNSBXSjtPONFqZF3gC+4glh1Gyi2RBKZcuItH8s=";
   private static final String ivBase64 = "qHttv1t5TWZLDM4e";

   public static void main(String[] var0) {
      try {
         Scanner var1 = new Scanner(System.in);
         System.out.print("President Donald Trump has a favorite cereal.  It is great... really great...\n");
         System.out.print("The reason it is so great, is because HE likes it... that makes it reall great...\n");
         System.out.print("Of course, to maintain utmost secrecy, it is protected with a password that is\n");
         System.out.print("HIGHLY secure (and backed up securely on a piece of paper somewhere in Mar Lago...)\n");
         System.out.print("Now, you, being a highly trained hacker, should be able to BYPASS this security and\n");
         System.out.print("discover what President Trump's favorite monster cereal is.\n");
         System.out.print("\n");
         System.out.print("Enter password: ");
         String var2 = var1.nextLine();
         byte[] var3 = decryptURL(encryptedURL, var2);
         String var4 = new String(var3);
         if (var4.startsWith("https")) {
            System.out.println("Decrypted URL: " + var4);
            String var5 = downloadImage(var4);
            byte[] var6 = calculateSHA256(var5);
            String var7 = decryptFlagWithAESGCM(var6, "Tj/BJ+45Z45uRCFpuFOHirQI34ZC7bmtpCtJ3OE613fIxqrsZwIoLNSBXSjtPONFqZF3gC+4glh1Gyi2RBKZcuItH8s=", "qHttv1t5TWZLDM4e");
            System.out.println("Decrypted Flag: " + var7);
         } else {
            System.out.println("Sorry, that is not the correct password.");
         }
      } catch (Exception var8) {
         var8.printStackTrace();
      }

   }

   private static byte[] decryptURL(byte[] var0, String var1) {
      byte[] var2 = new byte[var0.length];

      for(int var3 = 0; var3 < var0.length; ++var3) {
         var2[var3] = (byte)(var0[var3] ^ var1.charAt(var3 % var1.length()));
      }

      return var2;
   }

   private static String downloadImage(String var0) throws IOException {
      URL var1 = new URL(var0);
      String var2 = "downloaded_image.jpg";
      File var3 = new File(var2);
      if (var3.exists()) {
         var3.delete();
      }

      InputStream var4 = var1.openStream();

      try {
         Files.copy(var4, Paths.get(var2), new CopyOption[0]);
      } catch (Throwable var8) {
         if (var4 != null) {
            try {
               var4.close();
            } catch (Throwable var7) {
               var8.addSuppressed(var7);
            }
         }

         throw var8;
      }

      if (var4 != null) {
         var4.close();
      }

      return var2;
   }

   private static byte[] calculateSHA256(String var0) throws Exception {
      MessageDigest var1 = MessageDigest.getInstance("SHA-256");
      byte[] var2 = Files.readAllBytes(Paths.get(var0));
      return var1.digest(var2);
   }

   private static String decryptFlagWithAESGCM(byte[] var0, String var1, String var2) throws Exception {
      byte[] var3 = Base64.getDecoder().decode(var2);
      byte[] var4 = Base64.getDecoder().decode(var1);
      SecretKeySpec var5 = new SecretKeySpec(var0, "AES");
      Cipher var6 = Cipher.getInstance("AES/GCM/NoPadding");
      GCMParameterSpec var7 = new GCMParameterSpec(128, var3);
      var6.init(2, var5, var7);
      byte[] var8 = var6.doFinal(var4);
      return new String(var8, "UTF-8");
   }
}
