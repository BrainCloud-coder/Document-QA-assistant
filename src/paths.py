"""路径与运行环境配置。

必须在导入 gradio / hello_agents 之前先导入本模块：HF_HOME 和
GRADIO_TEMP_DIR 这两个变量是被那些库在导入时读成模块常量的，
导入之后再设置就不生效了。
"""

import os
from pathlib import Path

from dotenv import load_dotenv

# 项目根目录（study/reproduceQ&A_Assistant），用 __file__ 定位，与工作目录无关
PROJECT_DIR = Path(__file__).resolve().parents[1]
# 所有运行期生成的文件统一放这里
FILES_DIR = PROJECT_DIR / "files"

MEMORY_DIR = FILES_DIR / "memory_data"             # 记忆系统的 SQLite 库
KNOWLEDGE_BASE_DIR = FILES_DIR / "knowledge_base"  # RAG 知识库
REPORTS_DIR = FILES_DIR / "reports"                # 学习报告 JSON
HF_CACHE_DIR = FILES_DIR / "hf_cache"              # HuggingFace 模型缓存
GRADIO_TMP_DIR = FILES_DIR / "gradio_tmp"          # Gradio 上传的临时文件

for _d in (MEMORY_DIR, KNOWLEDGE_BASE_DIR, REPORTS_DIR, HF_CACHE_DIR, GRADIO_TMP_DIR):
    _d.mkdir(parents=True, exist_ok=True)

load_dotenv(PROJECT_DIR / ".env", override=True)

# 用 setdefault 让 .env 或 shell 里显式设置的值优先
os.environ.setdefault("HF_HOME", str(HF_CACHE_DIR))
os.environ.setdefault("GRADIO_TEMP_DIR", str(GRADIO_TMP_DIR))
