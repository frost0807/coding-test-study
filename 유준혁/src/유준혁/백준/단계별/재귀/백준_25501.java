// https://www.acmicpc.net/problem/25501
import java.util.*;
class Main {
	static int rec = 0;
	public static int recursion(String s, int l, int r){
		rec++;
		if(l >= r) return 1;
		else if(s.charAt(l) != s.charAt(r)) return 0;
		else return recursion(s, l+1, r-1);
	}
	public static int isPalindrome(String s){
		return recursion(s, 0, s.length()-1);
	}
	public static void main (String[] args) {
		Scanner sc = new Scanner(System.in);
		int n = sc.nextInt();
		while(n-->0) {
			System.out.printf("%d %d\n", isPalindrome(sc.next()), rec + (rec = 0));
		}
	}
}