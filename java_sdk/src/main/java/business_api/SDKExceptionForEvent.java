
package business_api;

import java.util.Map;
import java.util.List;

public class SDKExceptionForEvent extends Exception {
    private String request_id;
    private long error_code;
    private String message;
    private String error_message;
    private Object data;

    public SDKExceptionForEvent(String request_id, long error_code, String error_message, Object data) {
        this.request_id = request_id;
        this.error_code = error_code;
        this.error_message = message;
        this.data = data;
        this.message = String.format("request_id : %s, error_code: %d, message: %s, data: %s", request_id, error_code, error_message, data);
    }

    public String getRequestId() {
        return request_id;
    }

    public long getErrorCode() {
        return error_code;
    }

    public String getMessage() {
        return message;
    }
    public Object getData() {
        return data;
    }
}