package gumi.algo;

import java.io.BufferedReader;
import java.io.BufferedWriter;
import java.io.InputStreamReader;
import java.io.OutputStreamWriter;
import java.util.LinkedList;
import java.util.StringTokenizer;
import java.util.TooManyListenersException;

class Solution {
	
	static LinkedList<String> list = new LinkedList<>();
	static int code_length,order, x,y,cnt;
	static String temp;
	public static void main(String args[]) throws Exception {
		
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));
		
		for(int tc = 1; tc<=10; tc++) {
			code_length = Integer.parseInt(br.readLine());
			StringTokenizer st = new StringTokenizer(br.readLine());
			for(int i=0; i<code_length; i++) {
				list.add(st.nextToken());
			}
			order = Integer.parseInt(br.readLine());
			st = new StringTokenizer(br.readLine());
			while(true) {
				temp = st.nextToken();
				if(temp.equals("I")) {
					cnt++;
					continue;
				}
				x = Integer.parseInt(temp);
				y = Integer.parseInt(st.nextToken());
				for(int j=0; j<y; j++) {
					list.add(x+j,st.nextToken());
				}
				if(cnt == order) break;
			}
			bw.write("#"+tc+" ");
			for(int j =0; j<10; j++) {
				bw.write(list.get(j)+ " ");
			}
			bw.flush();
		}
	}
	

}