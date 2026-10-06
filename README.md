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