## 项目概述
基于 RAG 与多层记忆的智能文档问答系统：实现 PDF 文档的自动解析、按标题层次的语义分块与向量化入库，结合 Qdrant 向量检索与大模型生成带引用溯源的答案，并支持 MQE、HyDE 等高级检索策略；在此基础上设计三层记忆架构——工作记忆按 TTL 管理会话上下文，情景记忆基于 SQLite 与向量库记录交互事件，语义记忆借 spaCy 实体抽取在 Neo4j 中构建知识图谱并实现"向量检索 + 图关系推理"的混合召回，使系统既能回答文档内容，也能回溯用户自身的学习轨迹；采用 Gradio 构建交互界面，涵盖文档管理、笔记记录与学习报告生成，全栈打通 Docker 容器化的 Neo4j、云端 Qdrant 与本地嵌入模型推理。
## 快速开始
### 启动 neo4j
```
colima start          # 启动虚拟机（已创建过，这次很快）
docker start neo4j    # 启动容器
```

### 安装spaCy的语言模型
```
python -m spacy download zh_core_web_sm
python -m spacy download en_core_web_sm
```