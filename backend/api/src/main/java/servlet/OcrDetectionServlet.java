package servlet;

import java.io.IOException;
import java.io.PrintWriter;

import config.LanguageCode;
import config.LanguageValidator;
import javax.servlet.ServletException;
import javax.servlet.annotation.MultipartConfig;
import javax.servlet.annotation.WebServlet;
import javax.servlet.http.HttpServlet;
import javax.servlet.http.HttpServletRequest;
import javax.servlet.http.HttpServletResponse;
import javax.servlet.http.Part;


@WebServlet("/ocr/detection")
@MultipartConfig
public class OcrDetectionServlet extends HttpServlet {

    // 特定モデルを使用して画像から文字を検出するサーブレット
    @Override
    protected void doPost(HttpServletRequest request, HttpServletResponse response)
    throws ServletException, IOException {

        response.setContentType("application/json");
        response.setCharacterEncoding("UTF-8");

        try {
            String languageCodeParam = request.getParameter("langId");
            Part imagePart = request.getPart("image");
            
            LanguageValidator.ValidationResult langValidation = 
                LanguageValidator.validateLanguageCode(languageCodeParam);
            
            if (!langValidation.isValid()) {
                sendErrorResponse(response, 400, langValidation.getMessage());
                return;
            }
            
            LanguageCode languageCode = LanguageCode.fromCode(languageCodeParam);
            
            if (imagePart == null || imagePart.getSize() == 0) {
                sendErrorResponse(response, 400, "画像ファイルが必要です");
                return;
            }
            
            // 処理実行 
            
            String successMessage = String.format("アップロード完了 (言語: %s)", 
                languageCode.getDisplayName());
            sendSuccessResponse(response, successMessage);
            
        } catch (Exception e) {
            e.printStackTrace();
            sendErrorResponse(response, 500, "サーバーエラー");
        }
    }

    private void sendErrorResponse(HttpServletResponse response, int statusCode, String message) 
            throws IOException {
        response.setStatus(statusCode);
        response.setContentType("application/json");
        response.setCharacterEncoding("UTF-8");
        
        PrintWriter out = response.getWriter();
        out.print("{\"status\":\"error\",\"message\":\"" + message + "\"}");
        out.flush();
    }
    
    private void sendSuccessResponse(HttpServletResponse response, String message) 
            throws IOException {
        response.setStatus(200);
        response.setContentType("application/json");
        response.setCharacterEncoding("UTF-8");
        
        PrintWriter out = response.getWriter();
        out.print("{\"status\":\"success\",\"message\":\"" + message + "\"}");
        out.flush();
    }
    
    // @Override
    // protected void doPost(HttpServletRequest request, HttpServletResponse response)
    //         throws ServletException, IOException {
        
    //     response.setContentType("application/json;charset=UTF-8");
        
    //     // POSTパラメータやファイルアップロードの処理例
    //     String inputText = request.getParameter("text");
        
    //     try (PrintWriter out = response.getWriter()) {
    //         out.println("{");
    //         out.println("  \"status\": \"success\",");
    //         out.println("  \"method\": \"POST\",");
    //         out.println("  \"received_text\": \"" + (inputText != null ? inputText : "none") + "\",");
    //         out.println("  \"message\": \"OCR processing completed\"");
    //         out.println("}");
    //     }
    // }
}