# OpenClaw Skills

OpenClaw 技能集合，包含图片理解与分析技能。

## 技能列表

### 1. siliconflow-qwen-vision
使用 SiliconFlow 的 Qwen2.5-VL 模型进行图片理解与分析。

**功能：**
- 图片内容描述
- 物体识别
- 场景分析
- 图片问答

**使用方法：**
```bash
cd siliconflow-qwen-vision
python scripts/analyze_image.py -i image.jpg -p "描述图片"
```

### 2. minimax-mcp-vision
使用 MiniMax Coding Plan MCP 进行图片理解与分析。

**功能：**
- 图片内容描述
- 物体识别
- 场景分析
- 图片问答

**使用方法：**
```bash
cd minimax-mcp-vision
source .venv/bin/activate
python scripts/analyze_image.py -i image.jpg -p "描述图片"
```

**环境变量：**
- `MINIMAX_API_KEY`: MiniMax Coding Plan API Key

## License

MIT
