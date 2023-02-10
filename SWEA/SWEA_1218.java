/*
title: 감소하는 수
level : D4
tag: Stack
date:20230210
*/


import java.io.BufferedReader;
import java.io.BufferedWriter;
import java.io.InputStreamReader;
import java.io.OutputStreamWriter;
import java.util.Stack;
import java.util.StringTokenizer;

class Solution {
	static int N;
	static String temp;
	static String temp1;
	static boolean tri;
	static int ans;

	public static void main(String args[]) throws Exception {
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));

		for (int tc = 1; tc <= 10; tc++) {
			tri = true;
			ans = 1;
			N = Integer.parseInt(br.readLine());
			StringTokenizer st = new StringTokenizer(br.readLine());
			Stack<String> stack = new Stack<>();
			temp = st.nextToken();
			for (int i = 0; i < N; i++) {
				temp1 = Character.toString(temp.charAt(i));
				switch (temp1) {
				case "(":
					stack.add(temp1);
					break;
				case "{":
					stack.add(temp1);
					break;
				case "[":
					stack.add(temp1);
					break;
				case "<":
					stack.add(temp1);
					break;
				case ")":
					if (!stack.isEmpty()) {
						if (stack.peek().equals("(")) {
							stack.pop();
						} else {
							tri = false;
							
						}
					} else {
						tri = false;
						
					}
					break;
				case "}":
					if (!stack.isEmpty()) {
						if (stack.peek().equals("{")) {
							stack.pop();
						} else {
							tri = false;
							
						}
					} else {
						tri = false;
						
					}
					break;
				case "]":

					if (!stack.isEmpty()) {
						if (stack.peek().equals("[")) {
							stack.pop();
						} else {
							tri = false;
							
						}
					} else {
						tri = false;
						
					}
					break;
				case ">":

					if (!stack.isEmpty()) {
						if (stack.peek().equals("<")) {
							stack.pop();
						} else {
							tri = false;
							
						}
					} else {
						tri = false;
						
					}
					break;
				}
				if (!tri) {
					ans = 0;
					break;
				}

			}
			System.out.printf("#%d %d%n", tc, ans);
		}

	}

}