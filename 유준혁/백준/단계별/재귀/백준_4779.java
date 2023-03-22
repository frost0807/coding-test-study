import java.util.*;
class Main {
	public static void main (String[] args) {
		Scanner sc = new Scanner(System.in);
		String[] arr = new String[13];
		arr[0] = "";
		StringBuilder sb = new StringBuilder("-"), out = new StringBuilder();
		for(int i = 0; i < 13; i++) {
			arr[i] = sb.toString();
			sb.append(" ".repeat(sb.length()) + sb.toString());
		}
		while(sc.hasNextInt()) out.append(arr[sc.nextInt()] + "\n");
		System.out.print(out);
	}
}