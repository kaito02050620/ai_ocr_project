package config;

public enum LanguageCode {
    JAPANESE("ja", "日本語"),
    ENGLISH("en", "English"),
    KOREAN("ko", "한국어"),
    CHINESE_SIMPLIFIED("zh-cn", "简体中文"),
    CHINESE_TRADITIONAL("zh-tw", "繁體中文"),
    SPANISH("es", "Español"),
    FRENCH("fr", "Français"),
    GERMAN("de", "Deutsch"),
    ITALIAN("it", "Italiano"),
    PORTUGUESE("pt", "Português");
    
    private final String code;
    private final String displayName;
    
    LanguageCode(String code, String displayName) {
        this.code = code;
        this.displayName = displayName;
    }
    
    public String getCode() {
        return code;
    }
    
    public String getDisplayName() {
        return displayName;
    }
    
    public static LanguageCode fromCode(String code) {
        if (code == null || code.trim().isEmpty()) {
            return null;
        }
        
        for (LanguageCode lang : LanguageCode.values()) {
            if (lang.code.equalsIgnoreCase(code.trim())) {
                return lang;
            }
        }
        return null;
    }
    
    public static boolean isValidCode(String code) {
        return fromCode(code) != null;
    }
    
    public static String[] getAllCodes() {
        LanguageCode[] values = LanguageCode.values();
        String[] codes = new String[values.length];
        for (int i = 0; i < values.length; i++) {
            codes[i] = values[i].code;
        }
        return codes;
    }
    
    @Override
    public String toString() {
        return code;
    }
}