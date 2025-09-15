package config;

public class LanguageValidator {
    
    public static ValidationResult validateLanguageCode(String languageCode) {
        if (languageCode == null || languageCode.trim().isEmpty()) {
            return new ValidationResult(false, "言語コードが指定されていません");
        }
        
        LanguageCode lang = LanguageCode.fromCode(languageCode);
        if (lang == null) {
            String availableCodes = String.join(", ", LanguageCode.getAllCodes());
            return new ValidationResult(false, 
                "無効な言語コードです。利用可能な言語コード: " + availableCodes);
        }
        
        return new ValidationResult(true, lang.getDisplayName());
    }
    
    public static class ValidationResult {
        private final boolean valid;
        private final String message;
        
        public ValidationResult(boolean valid, String message) {
            this.valid = valid;
            this.message = message;
        }
        
        public boolean isValid() { return valid; }
        public String getMessage() { return message; }
    }
}