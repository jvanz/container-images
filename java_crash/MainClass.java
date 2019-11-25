
import java.nio.*;

public class MainClass {
	public static void main(String[] args) {
		try {
		 System.out.println("Capacity: " + args[0] + "mb");
		 int capacity = Integer.parseInt(args[0]);
		 ByteBuffer[] buffers = new ByteBuffer[capacity];
		 for (int i = 0; i < capacity; i++){
			 buffers[i] = ByteBuffer.allocate(1048576);
			 Thread.sleep(500);
			 System.out.println("Memory: " + (i*1048576)/(1024*1024) + "mb");
		 }
		int wait_minutes = Integer.parseInt(args[1]);
		Thread.sleep(wait_minutes*60*1000);
		} catch (Exception e) {
			System.out.println(e);
		}

	}
}
