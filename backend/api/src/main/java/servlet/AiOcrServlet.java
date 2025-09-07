package servlet;

import java.io.IOException;
import java.io.PrintWriter;
import jakarta.servlet.ServletException;
import jakarta.servlet.annotation.WebServlet;
import jakarta.servlet.http.HttpServlet;
import jakarta.servlet.http.HttpServletRequest;
import jakarta.servlet.http.HttpServletResponse;


@WebServlet("/ocr")
public class AiOcrServlet extends HttpServlet {
    private static final long serialVersionUID = 1L;

    @Override
    protected void doGet(HttpServletRequest request, HttpServletResponse response)
            throws ServletException, IOException {
        
        response.setContentType("text/html;charset=UTF-8");
        
        try (PrintWriter out = response.getWriter()) {
            out.println("<!DOCTYPE html>");
            out.println("<html>");
            out.println("<head>");
            out.println("<title>Hello Servlet</title>");
            out.println("</head>");
            out.println("<body>");
            out.println("<h1>Hello, Servlet!</h1>");
            out.println("<p>現在時刻: " + new java.util.Date() + "</p>");
            out.println("</body>");
            out.println("</html>");
        }
    }
    
    @Override
    protected void doPost(HttpServletRequest request, HttpServletResponse response)
            throws ServletException, IOException {
        
        response.setContentType("application/json;charset=UTF-8");
        
        // POSTパラメータやファイルアップロードの処理例
        String inputText = request.getParameter("text");
        
        try (PrintWriter out = response.getWriter()) {
            out.println("{");
            out.println("  \"status\": \"success\",");
            out.println("  \"method\": \"POST\",");
            out.println("  \"received_text\": \"" + (inputText != null ? inputText : "none") + "\",");
            out.println("  \"message\": \"OCR processing completed\"");
            out.println("}");
        }
    }
}