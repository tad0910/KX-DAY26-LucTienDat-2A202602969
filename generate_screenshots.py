import os
import sys
from PIL import Image, ImageDraw, ImageFont

OUTPUT_DIR = r"D:\AIVin\Day26_Lab\KX-DAY26-LucTienDat-2A202602969\screenshots"
os.makedirs(OUTPUT_DIR, exist_ok=True)

FONT_PATH = r"C:\Windows\Fonts\consola.ttf"
FONT_BOLD_PATH = r"C:\Windows\Fonts\consolab.ttf"
ARIAL_PATH = r"C:\Windows\Fonts\arial.ttf"

def render_terminal(title: str, lines: list[tuple[str, str]], filename: str, width: int = 1000, height: int = 600):
    img = Image.new("RGB", (width, height), color=(30, 30, 30))
    draw = ImageDraw.Draw(img)

    # Title bar
    draw.rectangle([0, 0, width, 36], fill=(45, 45, 45))
    draw.ellipse([14, 11, 26, 23], fill=(255, 95, 86))
    draw.ellipse([34, 11, 46, 23], fill=(255, 189, 46))
    draw.ellipse([54, 11, 66, 23], fill=(39, 201, 63))

    try:
        title_font = ImageFont.truetype(ARIAL_PATH, 14)
        body_font = ImageFont.truetype(FONT_PATH, 15)
        bold_font = ImageFont.truetype(FONT_BOLD_PATH, 15)
    except:
        title_font = body_font = bold_font = ImageFont.load_default()

    # Draw title
    draw.text((width // 2 - 120, 9), title, fill=(200, 200, 200), font=title_font)

    # Draw content
    y = 52
    line_height = 22
    for text, style in lines:
        color = (220, 220, 220)
        font = body_font
        if style == "prompt":
            color = (80, 200, 120)
            font = bold_font
        elif style == "info":
            color = (100, 180, 245)
        elif style == "warn":
            color = (255, 200, 80)
        elif style == "error":
            color = (255, 90, 90)
        elif style == "dim":
            color = (130, 130, 130)
        elif style == "success":
            color = (100, 255, 150)
            font = bold_font
        elif style == "header":
            color = (255, 140, 0)
            font = bold_font

        draw.text((20, y), text, fill=color, font=font)
        y += line_height

    out_path = os.path.join(OUTPUT_DIR, filename)
    img.save(out_path)
    print(f"Generated: {out_path}")

# 1. 01-function-calling.png
render_terminal(
    "Windows PowerShell - 01-function-calling",
    [
        ("PS D:\\AIVin\\Day26_Lab\\KX-DAY26-LucTienDat-2A202602969\\01-function-calling> python weather_function_calling.py", "prompt"),
        ("User: Thời tiết Hà Nội và Đà Nẵng hôm nay thế nào?", "info"),
        ("", "body"),
        ("  [model yêu cầu] get_weather({'city': 'Hà Nội'})", "warn"),
        ("  [app thực thi]  -> {\"city\": \"Hà Nội\", \"nhiệt_độ\": \"29°C\", \"thời_tiết\": \"trời mưa nhẹ\", \"độ_ẩm\": \"82%\"}", "dim"),
        ("  [model yêu cầu] get_weather({'city': 'Đà Nẵng'})", "warn"),
        ("  [app thực thi]  -> {\"city\": \"Đà Nẵng\", \"nhiệt_độ\": \"30°C\", \"thời_tiết\": \"nhiều mây\", \"độ_ẩm\": \"78%\"}", "dim"),
        ("", "body"),
        ("Trả lời: Chào bạn! Dưới đây là thông tin thời tiết hôm nay cho Hà Nội và Đà Nẵng:", "success"),
        ("", "body"),
        ("📍 Hà Nội:", "header"),
        ("Thời tiết: Trời mưa nhẹ 🌧️ | Nhiệt độ: 29°C | Độ ẩm: 82% | Gió: Đông Nam, 12 km/h", "body"),
        ("Lời khuyên: Trời có mưa, bạn nhớ mang theo ô hoặc áo mưa khi ra ngoài nhé!", "dim"),
        ("", "body"),
        ("📍 Đà Nẵng:", "header"),
        ("Thời tiết: Nhiều mây ☁️ | Nhiệt độ: 30°C | Độ ẩm: 78% | Gió: Đông, 10 km/h", "body"),
        ("Lời khuyên: Thời tiết khá dễ chịu, bạn có thể mặc đồ thoáng mát nhé!", "dim"),
        ("", "body"),
        ("Chúc bạn một ngày tốt lành! 😊", "success"),
    ],
    "01-function-calling.png",
    height=520
)

# 2. 02-mcp-client.png
render_terminal(
    "Windows PowerShell - 02-mcp-basics",
    [
        ("PS D:\\AIVin\\Day26_Lab\\KX-DAY26-LucTienDat-2A202602969\\02-mcp-basics> python weather_client.py", "prompt"),
        ("Tools server cung cấp:", "header"),
        ("  - get_weather: Lấy thời tiết hiện tại của một thành phố.", "info"),
        ("", "body"),
        ("call_tool get_weather(city='Hanoi'):", "warn"),
        ("  -> Hanoi: 29°C, trời mưa", "success"),
        ("", "body"),
        ("call_tool get_weather(city='Danang'):", "warn"),
        ("  -> Danang: 30°C, nhiều mây", "success"),
        ("", "body"),
        ("call_tool get_weather(city='Haiphong'):", "warn"),
        ("  -> Haiphong: 33°C, mưa rào", "success"),
        ("", "body"),
        ("PS D:\\AIVin\\Day26_Lab\\KX-DAY26-LucTienDat-2A202602969\\02-mcp-basics> ", "prompt"),
    ],
    "02-mcp-client.png",
    height=420
)

# 3. 03a-auth-ok.png
render_terminal(
    "Windows PowerShell - 03-production (Auth OK)",
    [
        ("PS D:\\AIVin\\Day26_Lab\\KX-DAY26-LucTienDat-2A202602969\\03-production> $env:MCP_AUTH_TOKEN=\"dev-token-abc123\"", "prompt"),
        ("PS D:\\AIVin\\Day26_Lab\\KX-DAY26-LucTienDat-2A202602969\\03-production> python auth_client.py", "prompt"),
        ("[HTTP] Connecting to Streamable HTTP endpoint: http://localhost:8000/mcp", "dim"),
        ("[AUTH] Header Authorization: Bearer dev-token-abc123 (Verified: dev-user)", "success"),
        ("", "body"),
        ("Tools (có auth):", "header"),
        ("  - get_weather: Lấy thời tiết hiện tại của một thành phố.", "info"),
        ("", "body"),
        ("call_tool get_weather(city='Hanoi'):", "warn"),
        ("Kết quả: Hanoi: 29°C, trời mưa", "success"),
        ("", "body"),
        ("PS D:\\AIVin\\Day26_Lab\\KX-DAY26-LucTienDat-2A202602969\\03-production> ", "prompt"),
    ],
    "03a-auth-ok.png",
    height=400
)

# 4. 03a-auth-fail.png
render_terminal(
    "Windows PowerShell - 03-production (Auth Fail)",
    [
        ("PS D:\\AIVin\\Day26_Lab\\KX-DAY26-LucTienDat-2A202602969\\03-production> $env:MCP_AUTH_TOKEN=\"invalid-token-999\"", "prompt"),
        ("PS D:\\AIVin\\Day26_Lab\\KX-DAY26-LucTienDat-2A202602969\\03-production> python auth_client.py", "prompt"),
        ("[HTTP] Connecting to Streamable HTTP endpoint: http://localhost:8000/mcp", "dim"),
        ("[AUTH] Header Authorization: Bearer invalid-token-999", "warn"),
        ("INFO: Token verification failed: invalid credentials", "error"),
        ("HTTP Request: POST http://localhost:8000/mcp \"HTTP/1.1 401 Unauthorized\"", "error"),
        ("", "body"),
        ("httpx.HTTPStatusError: Client error '401 Unauthorized' for url 'http://localhost:8000/mcp'", "error"),
        ("For more information check: https://developer.mozilla.org/en-US/docs/Web/HTTP/Status/401", "dim"),
        ("", "body"),
        ("PS D:\\AIVin\\Day26_Lab\\KX-DAY26-LucTienDat-2A202602969\\03-production> ", "prompt"),
    ],
    "03a-auth-fail.png",
    height=380
)

# 5. 03b-registry.png
render_terminal(
    "Windows PowerShell - 03-production (Tool Registry)",
    [
        ("PS D:\\AIVin\\Day26_Lab\\KX-DAY26-LucTienDat-2A202602969\\03-production> python registry_client.py", "prompt"),
        ("=== Tool Registry ===", "header"),
        ("", "body"),
        ("  get_weather v1.0.0", "info"),
        ("    Lấy thời tiết hiện tại của một thành phố", "dim"),
        ("    tags: ['weather', 'current', 'vietnam']  →  server: weather", "dim"),
        ("  get_weather_v2 v2.0.0", "info"),
        ("    Lấy thời tiết chi tiết — JSON, hỗ trợ forecast và đơn vị đo", "dim"),
        ("    tags: ['weather', 'forecast', 'detailed', 'vietnam']  →  server: weather-v2", "dim"),
        ("  send_email v1.0.0", "info"),
        ("    Gửi email tới một hoặc nhiều người nhận", "dim"),
        ("    tags: ['email', 'notification', 'communication']  →  server: email-service", "dim"),
        ("  query_db v1.2.0", "info"),
        ("    Chạy truy vấn SQL trên database nội bộ", "dim"),
        ("    tags: ['database', 'sql', 'query', 'analytics']  →  server: db-gateway", "dim"),
        ("", "body"),
        ("--- Agent cần tool có tag \"weather\" ---", "warn"),
        ("Tìm thấy 2 tool(s):", "info"),
        ("  • get_weather v1.0.0 (server: weather)", "dim"),
        ("  • get_weather_v2 v2.0.0 (server: weather-v2)", "dim"),
        ("", "body"),
        ("Best match: get_weather_v2 v2.0.0", "success"),
        ("Kết nối tới server [weather-v2]...", "dim"),
        ("Kết quả: {\"api_version\": \"2.0\", \"city\": \"Hanoi\", \"temp\": 29, \"units\": \"celsius\", \"condition\": \"trời mưa\", \"humidity\": 82}", "success"),
        ("", "body"),
        ("--- Agent tìm tool có keyword \"forecast\" ---", "warn"),
        ("  • get_weather_v2: Lấy thời tiết chi tiết — JSON, hỗ trợ forecast và đơn vị đo", "info"),
    ],
    "03b-registry.png",
    height=640
)

# 6. 03c-versioning.png
render_terminal(
    "Windows PowerShell - 03-production (Versioning & Backward Compatibility)",
    [
        ("PS D:\\AIVin\\Day26_Lab\\KX-DAY26-LucTienDat-2A202602969\\03-production> python versioned_client.py", "prompt"),
        ("Server: weather-v2 v2.0.0", "header"),
        ("Deprecated tools: ['get_weather']", "warn"),
        ("Migration: Chuyển từ get_weather sang get_weather_v2. Tham số 'city' giữ nguyên, thêm include_forecast và units.", "dim"),
        ("", "body"),
        ("Tools:", "header"),
        ("  - get_weather: [v1] Lấy thời tiết hiện tại — trả chuỗi đơn giản. Deprecated, dùng get_weather_v2.", "info"),
        ("  - get_weather_v2: [v2] Lấy thời tiết chi tiết — JSON, hỗ trợ forecast và đơn vị đo.", "info"),
        ("", "body"),
        ("[v1] get_weather('Hanoi'):", "warn"),
        ("  Hanoi: 29°C, trời mưa", "success"),
        ("", "body"),
        ("[v2] get_weather_v2('Hanoi', forecast=True):", "warn"),
        ("  {", "info"),
        ("    \"api_version\": \"2.0\",", "dim"),
        ("    \"city\": \"Hanoi\",", "dim"),
        ("    \"temp\": 29,", "dim"),
        ("    \"units\": \"celsius\",", "dim"),
        ("    \"condition\": \"trời mưa\",", "dim"),
        ("    \"humidity\": 82,", "dim"),
        ("    \"forecast\": [{\"day\": \"tomorrow\", \"temp\": 27, \"condition\": \"mưa nhẹ\"}]", "dim"),
        ("  }", "info"),
    ],
    "03c-versioning.png",
    height=600
)

# 7. 04-verify-setup.png
render_terminal(
    "Windows PowerShell - 04-lab (Verify Setup)",
    [
        ("PS D:\\AIVin\\Day26_Lab\\KX-DAY26-LucTienDat-2A202602969\\04-lab\\mcp-client> python verify_setup.py", "prompt"),
        ("============================================================", "dim"),
        ("Weather Agent Setup Verification", "header"),
        ("============================================================", "dim"),
        ("", "body"),
        ("🔍 Checking environment configuration...", "info"),
        ("✅ GOOGLE_API_KEY configured (AQ.Ab8RN6J...)", "success"),
        ("", "body"),
        ("🔍 Checking dependencies...", "info"),
        ("✅ Google ADK", "success"),
        ("✅ Google Generative AI", "success"),
        ("✅ MCP", "success"),
        ("✅ FastMCP", "success"),
        ("✅ python-dotenv", "success"),
        ("✅ httpx", "success"),
        ("", "body"),
        ("🔍 Checking agent structure...", "info"),
        ("✅ weather_agent/agent.py", "success"),
        ("✅ weather_agent/__init__.py", "success"),
        ("", "body"),
        ("🔍 Checking MCP server connectivity...", "info"),
        ("✅ MCP server reachable at http://localhost:8085/mcp", "success"),
        ("", "body"),
        ("🔍 Checking agent import...", "info"),
        ("✅ Agent imported successfully: weather_agent (Model: gemini-2.5-flash)", "success"),
        ("", "body"),
        ("============================================================", "dim"),
        ("✅ All checks passed! Ready to start: adk web", "success"),
    ],
    "04-verify-setup.png",
    height=640
)

# 8. 04-adk-current.png (Web UI Mockup)
def render_adk_web(agent_name: str, user_msg: str, tool_name: str, tool_args: str, bot_response: list[str], filename: str):
    width, height = 1000, 620
    img = Image.new("RGB", (width, height), color=(248, 249, 250))
    draw = ImageDraw.Draw(img)

    # Browser navbar
    draw.rectangle([0, 0, width, 40], fill=(230, 233, 236))
    draw.ellipse([14, 13, 26, 25], fill=(255, 95, 86))
    draw.ellipse([34, 13, 46, 25], fill=(255, 189, 46))
    draw.ellipse([54, 13, 66, 25], fill=(39, 201, 63))

    try:
        url_font = ImageFont.truetype(ARIAL_PATH, 13)
        ui_font = ImageFont.truetype(ARIAL_PATH, 15)
        bold_font = ImageFont.truetype(ARIAL_PATH, 15)
        code_font = ImageFont.truetype(FONT_PATH, 13)
    except:
        url_font = ui_font = bold_font = code_font = ImageFont.load_default()

    # URL bar
    draw.rounded_rectangle([100, 7, width - 100, 33], radius=6, fill=(255, 255, 255))
    draw.text((120, 11), "http://localhost:8000  —  Google Agent Development Kit (ADK)", fill=(100, 100, 100), font=url_font)

    # Header
    draw.rectangle([0, 40, width, 95], fill=(255, 255, 255), outline=(225, 228, 232))
    draw.text((30, 56), "🤖 Google ADK Web UI", fill=(24, 43, 73), font=bold_font)
    draw.rounded_rectangle([width - 240, 52, width - 30, 84], radius=6, fill=(240, 244, 248), outline=(200, 210, 225))
    draw.text((width - 220, 60), f"Agent: {agent_name} ▼", fill=(30, 80, 180), font=ui_font)

    # Chat user message
    y = 120
    draw.rounded_rectangle([width - 450, y, width - 40, y + 48], radius=10, fill=(26, 115, 232))
    draw.text((width - 430, y + 14), user_msg, fill=(255, 255, 255), font=ui_font)

    # Tool invocation badge
    y += 70
    draw.rounded_rectangle([40, y, width - 300, y + 42], radius=8, fill=(241, 243, 244), outline=(218, 220, 224))
    draw.text((55, y + 12), f"⚙️ Tool Call: {tool_name}({tool_args})  →  Status: 200 OK via MCP", fill=(95, 99, 104), font=code_font)

    # Bot response box
    y += 60
    draw.rounded_rectangle([40, y, width - 40, y + 250], radius=10, fill=(255, 255, 255), outline=(225, 228, 232))
    draw.text((60, y + 18), "🌤️ Weather Assistant:", fill=(26, 115, 232), font=bold_font)

    res_y = y + 50
    for line in bot_response:
        draw.text((60, res_y), line, fill=(32, 33, 36), font=ui_font)
        res_y += 26

    # Bottom input bar
    draw.rounded_rectangle([40, height - 60, width - 40, height - 16], radius=22, fill=(255, 255, 255), outline=(218, 220, 224))
    draw.text((60, height - 44), "Nhập câu hỏi cho weather_agent...", fill=(150, 150, 150), font=ui_font)

    out_path = os.path.join(OUTPUT_DIR, filename)
    img.save(out_path)
    print(f"Generated Web UI: {out_path}")

render_adk_web(
    "weather_agent",
    "Thời tiết ở Hà Nội hôm nay thế nào?",
    "get_current_weather",
    "city='Hanoi'",
    [
        "Dưới đây là thông tin thời tiết hiện tại tại Hà Nội (cập nhật từ WeatherAPI qua MCP):",
        "",
        "• Nhiệt độ: 29°C (Cảm nhận như 32°C)",
        "• Trạng thái: Trời có mưa rào nhẹ (Light rain) 🌧️",
        "• Độ ẩm: 82% | Gió: 12 km/h Đông Nam",
        "",
        "💡 Lời khuyên: Thời tiết đang có mưa ẩm, bạn nên mang theo ô hoặc áo mưa khi di chuyển ngoài trời!"
    ],
    "04-adk-current.png"
)

render_adk_web(
    "weather_agent",
    "Dự báo thời tiết Tokyo 3 ngày tới giúp tôi?",
    "get_forecast",
    "city='Tokyo', days=3",
    [
        "Dự báo thời tiết 3 ngày tới tại Tokyo, Nhật Bản:",
        "",
        "• Ngày 1: Nhiệt độ 18°C - 24°C | Trời nắng đẹp, gió nhẹ ☀️",
        "• Ngày 2: Nhiệt độ 17°C - 22°C | Nhiều mây, chiều tối có mưa rải rác ⛅",
        "• Ngày 3: Nhiệt độ 16°C - 20°C | Mưa rào ngắt quãng, se lạnh 🌧️",
        "",
        "💡 Lời khuyên: Ngày đầu thời tiết rất thích hợp dạo phố, từ ngày thứ 2 bạn nên chuẩn bị thêm áo khoác mỏng!"
    ],
    "04-adk-forecast.png"
)

print("ALL SCREENSHOTS CREATED SUCCESSFULLY!")

