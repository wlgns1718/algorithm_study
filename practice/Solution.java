package gumi.algo;

import java.io.BufferedReader;
import java.io.BufferedWriter;
import java.io.InputStreamReader;
import java.io.OutputStreamWriter;
import java.util.ArrayDeque;
import java.util.StringTokenizer;

class Solution {

	public static void main(String args[]) throws Exception {
		
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));
		
		long N = Long.parseLong(br.readLine());
		sol(N);
		/*
		int n = 8;
		System.out.println(n & ~n) == n ? "1" : "0");
		*/
		
		
	}
	public static void sol(long N) {
		for(long i = 1; (1L<<i)<= N; i++) {
			if(1L<<i == N) {
				System.out.println(1);
				return;
			}
		}
		System.out.println(0);
		return;
	}

}