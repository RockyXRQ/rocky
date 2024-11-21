import os
from jinja2 import Environment, FileSystemLoader, select_autoescape
import index
import time
from datetime import datetime, timezone, timedelta

TEMPLATE_DIR = "template"
INDEX_TEMPLATE_FILE_NAME = "index.html.j2"
INDEX_OUTPUT_FILE_NAME = "index.html"

try:
    os.system("cls" if os.name == "nt" else "clear")

    print("\n🔧 Build Process Initiated")
    print("━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━")
    china_timezone = timezone(timedelta(hours=8))
    current_time = datetime.now(china_timezone).strftime("%Y-%m-%d %H:%M:%S")
    print(f"⏰ Build Start Time: {current_time}\n")

    print(f"📂 Template Directory: {TEMPLATE_DIR}")
    print(f"📄 Template File: {INDEX_TEMPLATE_FILE_NAME}")
    print(f"🎯 Output Target: {INDEX_OUTPUT_FILE_NAME}")

    start_time = time.time()

    try:
        env = Environment(
            loader=FileSystemLoader(TEMPLATE_DIR),
            trim_blocks=True,
            lstrip_blocks=True,
            autoescape=select_autoescape(["html"]),
        )
        template = env.get_template(INDEX_TEMPLATE_FILE_NAME)
        print("\n🔄 Template Loading Complete ")
    except FileNotFoundError as e:
        print(f"\n❌ Error: Template file not found - {e}")
        raise
    except Exception as e:
        print(f"\n❌ Error: Failed to load template - {e}")
        raise

    try:
        print("\n📊 Rendering Content:")
        output = template.render(
            head=index.head,
            bio=index.bio,
            moments=index.moments,
            galleries=index.galleries,
        )
        print("✨ Content Rendering Successful")
    except Exception as e:
        print(f"\n❌ Error: Content rendering failed - {e}")
        raise

    try:
        with open(INDEX_OUTPUT_FILE_NAME, "w", encoding="utf-8") as f:
            f.write(output)
        print(f"\n📦 Output Generated: {INDEX_OUTPUT_FILE_NAME}")
    except IOError as e:
        print(f"\n❌ Error: Failed to write file - {e}")
        raise

    print("\n✅ Build Process Completed Successfully")
    print("━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━")

    print(f"\n⏱️  Build Time: {time.time() - start_time:.5f}s")

except Exception as e:
    print("\n❌ Build Process Failed")
    print("━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━")
    print(f"Error Type: {type(e).__name__}")
    print(f"Error Message: {str(e)}")
    exit(1)
