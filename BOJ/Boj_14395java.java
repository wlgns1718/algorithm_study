"""
 title: 4연산
 level : Gold5
 tag: bfs, graphs, graph_traversal
 date:20230215
"""

import java.io.BufferedReader;
import java.io.InputStreamReader;
import java.util.*;
public class Boj14395 {
	
	static long s,t;
	static Queue<Data> queue = new ArrayDeque<>();
	public static void main(String args[]) throws Exception {
		
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		StringTokenizer st = new StringTokenizer(br.readLine());
		s = Long.parseLong(st.nextToken());
		t = Long.parseLong(st.nextToken());
		queue.offer(new Data(s,""));
		queue.offer(new Data(1,"/"));
		if (s==t) {
			System.out.println(0);
		}
		else {
			ArrayList<String> answer = sol(queue,t);
			if (answer.isEmpty()){
				System.out.println(-1);
			}
			else {
				answer.sort((o1,o2) -> o1.length()==o2.length() ? o1.compareTo(o2) : o1.length() - o2.length());
				System.out.println(answer.get(0));
			}
		}
		
		
		
	}
	
	public static ArrayList<String> sol(Queue<Data> queue, long t) {
		ArrayList<String> answer = new ArrayList<>();
		HashSet<Long> visit = new HashSet<Long>();
		while(!queue.isEmpty()) {
			Data cur = queue.poll();
			visit.add((long)cur.val);
			if((long)cur.val + (long)cur.val == (long)t) {
				answer.add(cur.oper+"+");
			}
			else {
				if((long)cur.val*2 <= (long)t && !visit.contains((long)cur.val*2)) {
					queue.offer(new Data((long)cur.val*2,cur.oper+"+"));
				}
			}
			if((long)cur.val *(long) cur.val ==(long)t) {
				answer.add(cur.oper+"*");
			}
			else {
				if((long)cur.val*(long)cur.val <=(long)t && !visit.contains(cur.val*cur.val)) {
					queue.offer(new Data((long)cur.val*cur.val, cur.oper+"*"));
				}
			}
			if((long)cur.val-(long)cur.val == (long)t) {
				answer.add(cur.oper+"-");
			}
			else {
				if(!visit.contains((long)0)) {
					queue.offer(new Data((long)0,cur.oper+"-"));
				}
			}
			if((long)1 == (long)t) {
				answer.add(cur.oper+'/');
			}
			else {
				if(!visit.contains((long)1)) {
					queue.offer(new Data((long)1,cur.oper+"/"));
				}
			}
			
		}
		return answer; 
	}
	public static class Data{
		long val;
		String oper;
		public Data(long val, String oper) {
			super();
			this.val = val;
			this.oper = oper;
		}
		
	}

}
